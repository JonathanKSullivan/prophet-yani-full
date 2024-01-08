import os
from flask import Blueprint, flash, jsonify, redirect, render_template, request, session, url_for
from lib.booking_manager import BookingManager
from lib.charity_manager import CharityManager
from lib.donation_manager import DonationManager
from lib.payment_manager import PaymentManager
from model import Charity, Service
from datetime import datetime
from data import confirm_booking_page_content
import stripe
from dateutil import parser


# Set Stripe API key from environment variable
stripe.api_key = os.environ.get('STRIPE_TEST_SECRET_KEY')

booking_blueprint = Blueprint('booking_blueprint', __name__)

@booking_blueprint.route('/book_service/<int:service_id>', methods=['POST'])
def book_service(service_id):
    service = Service.query.get_or_404(service_id)

    if request.method == 'POST':
        user_id = session.get('user_id')
        # Validate user_id and handle non-logged-in users as needed

        # Retrieve form data
        charity_id = request.form.get('charity_id', type=int)  # Retrieve selected charity ID
        cardholder_name = request.form.get('cardholder_name')
        stripe_token = request.form.get('stripeToken')

        # Booking dates (replace with your logic to get these dates)
        appointment_date_str = request.form.get('start_time')
        appointment_end_str = request.form.get('end_time')
        appointment_date = parser.parse(appointment_date_str) if appointment_date_str else None
        appointment_end = parser.parse(appointment_end_str) if appointment_end_str else None


        # Calculate donation amount
        payment_amount = service.price
        donation_amount = payment_amount * (service.donation_percentage / 100)

        try:
            # Create a charge: this will charge the user's card
            charge = stripe.Charge.create(
                amount=int(payment_amount * 100),  # Amount in cents
                currency='usd',
                description=f'Service charge for {service.name}',
                source=stripe_token
            )

            # Add the booking
            booking = BookingManager.add_booking(user_id, service_id, appointment_date, appointment_end)

            # Record the payment
            payment = PaymentManager.add_payment(user_id, payment_amount, charge.id, 'Credit Card')

            # Record the donation if a charity is selected and donation amount is more than 0
            if charity_id and donation_amount > 0:
                DonationManager.add_donation(user_id, donation_amount, charity_id, service_id, datetime.now(), 'Booking')

            flash('Booking and payment successful.', 'success')
            return redirect(url_for('general_blueprint.user_dashboard'))

        except stripe.error.StripeError as e:
            
            # Handle Stripe errors (e.g., card declined)
            flash(str(e), 'error')
            
            # Redirect back to confirm_booking with necessary parameters
            start_time = request.form.get('start_time')
            end_time = request.form.get('end_time')

            return redirect(
                url_for('booking_blueprint.confirm_booking', 
                        service_id=service_id, 
                        start=start_time, 
                        end=end_time))

@booking_blueprint.route('/confirm_booking', methods=['GET'])
def confirm_booking():
    service_id = request.args.get('service_id')
    start_time = request.args.get('start')
    end_time = request.args.get('end')
    
    # Fetch additional details as needed, e.g., service details
    service = Service.query.get_or_404(service_id)

    # Use CharityManager to fetch all charities
    charities = CharityManager.list_all_charities()


    return render_template(
        'confirm_booking.html', 
        service=service,
        charities=charities,
        start_time=start_time,
        end_time=end_time,
        metadata=confirm_booking_page_content["meta"],
        footer=confirm_booking_page_content["footer"]
        )

@booking_blueprint.route('/api/bookings')
def get_bookings():
    bookings = BookingManager.list_all_bookings()  # Assuming this returns all bookings
    booking_data = [
        {
            'title': f"Booked: {booking.service.name}",  # Example title
            'start': booking.appointment_date.isoformat(),  # Convert to ISO format
            'end': booking.appointment_end.isoformat()  # Convert to ISO format
        } for booking in bookings
    ]
    return jsonify(booking_data)