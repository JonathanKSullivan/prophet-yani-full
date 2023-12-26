from flask import Blueprint, redirect, request, render_template, session, url_for
from sqlalchemy import func
from data import home_page_content, about_page_content, user_dashboard_page_content
from lib.service_manager import ServiceManager
from lib.donation_manager import DonationManager

# Import models
from models import User, Service, Booking, Donation, Charity, Location, Payment

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
    # User-specific data for the dashboard
    # Example: user's bookings, donations, etc.
    user_id = session.get('user_id')
    if not user_id:
        # Redirect to login if user is not logged in
        return redirect(url_for('user_blueprint.login'))

    user_bookings = Booking.query.filter_by(user_id=user_id).all()
    user_donations = Donation.query.filter_by(user_id=user_id).all()

    user_dashboard_data = {
        'bookings': user_bookings,
        'donations': user_donations
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

    # Admin-specific data for the dashboard
    user_count = User.query.count()
    service_count = Service.query.count()
    booking_count = Booking.query.count()
    total_donations = Donation.query.with_entities(func.sum(Donation.amount)).scalar()

    admin_dashboard_data = {
        'user_count': user_count,
        'service_count': service_count,
        'booking_count': booking_count,
        'total_donations': total_donations
    }

    return render_template('admin_dashboard.html', data=admin_dashboard_data, metadata=user_dashboard_page_content["meta"], 
        footer=user_dashboard_page_content["footer"])