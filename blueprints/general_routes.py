from flask import Blueprint, current_app, flash, redirect, request, render_template, session, url_for
from sqlalchemy import func
from data import home_page_content, about_page_content, user_dashboard_page_content
from lib.service_manager import ServiceManager
from lib.donation_manager import DonationManager
from extensions import db
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from lib.user_manager import UserManager


# Import models
from model import User, Service, Booking, Donation, Charity, Location, Payment

from utils import process_contact_form, is_user_admin

general_blueprint = Blueprint('general_blueprint', __name__)


@general_blueprint.route('/')
def home():
    return render_template(
        'index.html',
        metadata=home_page_content['meta'],
        hero=home_page_content['hero'],
        problem_solution=home_page_content['problem_solution_section'],
        benefits=home_page_content['benefits_section'],
        social_proof=home_page_content["social_proof_section"],
        features=home_page_content["features_section"],
        faq=home_page_content["faq_section"],
        footer=home_page_content['footer']
        )

@general_blueprint.route('/about')
def about():
    return render_template(
        'about.html',
        metadata=about_page_content['meta'],
        content=about_page_content['content'],
        footer=about_page_content['footer']
    )

@general_blueprint.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Process the contact form data (e.g., send an email, store in database)
        process_contact_form(name, email, message)
        
        return render_template('contact_thankyou.html', name=name, metadata=about_page_content['meta'],
        footer=about_page_content['footer'])

    return render_template(
        'contact.html',
        metadata=about_page_content['meta'],
        footer=about_page_content['footer']
    )

@general_blueprint.route('/services')
def services():
    all_services = ServiceManager.list_all_services()
    return render_template(
        'services.html', 
        metadata=home_page_content['meta'],
        services=all_services,
        footer=about_page_content['footer']
    )

@general_blueprint.route('/user_dashboard')
def user_dashboard():
    user_id = session.get('user_id')
    if not user_id:
        # Redirect to login if user is not logged in
        return redirect(url_for('user_blueprint.login'))

    user_bookings = Booking.query.filter_by(user_id=user_id).all()
    user_donations = Donation.query.filter_by(user_id=user_id).all()
    user_payments = Payment.query.filter_by(user_id=user_id).all()  # Fetch user payments

    user_dashboard_data = {
        'bookings': user_bookings,
        'donations': user_donations,
        'payments': user_payments  # Include payments in the data
    }

    return render_template(
        'user_dashboard.html',
        data=user_dashboard_data,
        metadata=user_dashboard_page_content["meta"], 
        footer=user_dashboard_page_content["footer"]
    )

@general_blueprint.route('/admin_dashboard')
def admin_dashboard():
    if not is_user_admin():
        return "Access denied", 403

    # User-Related Metrics
    user_count = User.query.count()
    users_by_role = db.session.query(User.user_role, func.count(User.id)).group_by(User.user_role).all()
    latest_signups = User.query.order_by(User.create_date.desc()).limit(10).all()

    # Service Metrics
    service_count = Service.query.count()
    services_by_type = db.session.query(Service.service_type, func.count(Service.id)).group_by(Service.service_type).all()
    # Assuming Booking has a relationship with Service as 'service'
    popular_services = db.session.query(Service.name, func.count(Booking.id)).join(Booking).group_by(Service.name).order_by(func.count(Booking.id).desc()).limit(10)

    # Booking Metrics
    booking_count = Booking.query.count()
    monthly_bookings = db.session.query(func.extract('month', Booking.booking_date), func.count(Booking.id)).group_by(func.extract('month', Booking.booking_date)).all()
    bookings_by_status = db.session.query(Booking.status, func.count(Booking.id)).group_by(Booking.status).all()

    # Donation Metrics
    total_donations = Donation.query.with_entities(func.sum(Donation.amount)).scalar()
    donation_count = Donation.query.count()
    avg_donation_amount = db.session.query(func.avg(Donation.amount)).scalar()

    # Location-Based Metrics
    # Assuming Service and Charity have a relationship with Location as 'location'
    services_by_location = db.session.query(Location.city, func.count(Service.id)).join(Service).group_by(Location.city).all()

    # Financial Metrics
    total_payments = db.session.query(func.sum(Payment.amount)).scalar()
    payment_count = Payment.query.count()

    
    formatted_latest_signups = [
        {
            'name': f"{user.first_name} {user.last_name}",
            'signup_date': user.create_date.strftime('%Y-%m-%d'),
            'profile_image': user.profile_image_url,  # Add this if you want to display profile pictures
            'country': user.country
        }
        for user in latest_signups
    ]


    # Set a default value for display when no data is available
    default_display_value = "N/A"

    # Format monetary values as strings
    formatted_total_donations = "${:,.2f}".format(total_donations) if total_donations is not None else default_display_value
    formatted_avg_donation_amount = "${:,.2f}".format(avg_donation_amount)  if avg_donation_amount is not None else default_display_value 
    formatted_users_by_role = {role: count for role, count in users_by_role}
    formatted_services_by_type = {service_type: count for service_type, count in services_by_type}
    popular_services_query = db.session.query(Service.name, func.count(Booking.id)).join(Booking).group_by(Service.name).order_by(func.count(Booking.id).desc()).limit(10)
    popular_services = {service: count for service, count in popular_services_query.all()}
    formatted_bookings_by_status = {status: count for status, count in bookings_by_status}
    month_names = {
        1: "January", 2: "February", 3: "March",
        4: "April", 5: "May", 6: "June",
        7: "July", 8: "August", 9: "September",
        10: "October", 11: "November", 12: "December"
    }
    formatted_monthly_bookings = {month_names.get(month, "Unknown Month"): count for month, count in monthly_bookings}



    admin_dashboard_data = {
        'user_count': user_count,
        'users_by_role': formatted_users_by_role,
        'latest_signups': latest_signups,
        'service_count': service_count,
        'services_by_type': formatted_services_by_type,
        'popular_services': popular_services,
        'booking_count': booking_count,
        'monthly_bookings': formatted_monthly_bookings,
        'bookings_by_status': formatted_bookings_by_status,
        'total_donations': formatted_total_donations,
        'donation_count': donation_count,
        'avg_donation_amount': formatted_avg_donation_amount,
        'services_by_location': services_by_location,
        'total_payments': total_payments,
        'payment_count': payment_count
    }
    print(admin_dashboard_data)

    return render_template('admin_dashboard.html', data=admin_dashboard_data, metadata=user_dashboard_page_content["meta"], 
        footer=user_dashboard_page_content["footer"])

@general_blueprint.route('/confirm/<token>')
def confirm_email(token):
    try:
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        email = serializer.loads(
            token,
            salt=current_app.config['SECURITY_PASSWORD_SALT'],
            max_age=3600
        )
    except SignatureExpired:
        flash('The confirmation link has expired.', 'error')
        return redirect(url_for('user_blueprint.login'))

    user = UserManager.get_user_by_email(email)
    if user and not user.confirmed:
        UserManager.update_user(user.id, confirmed=True)  # Correctly pass user ID and confirmed field
        flash('Your email has been confirmed.', 'success')
    else:
        flash('Invalid or already confirmed token.', 'error')

    return redirect(url_for('user_blueprint.login'))
