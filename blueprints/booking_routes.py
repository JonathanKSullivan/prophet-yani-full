from flask import Blueprint, jsonify, redirect, render_template, request, session, url_for
from lib.booking_manager import BookingManager
from models import Service
from datetime import datetime
from data import confirm_booking_page_content

booking_blueprint = Blueprint('booking_blueprint', __name__)

@booking_blueprint.route('/book_service/<int:service_id>', methods=['GET', 'POST'])
def book_service(service_id):
    service = Service.query.get_or_404(service_id)

    if request.method == 'POST':
        user_id = session.get('user_id')
        # process the booking form
        booking_date = request.form.get('booking_date')
        appointment_date_str = request.form.get('appointment_date')
        appointment_end_str = request.form.get('appointment_end')  # Get end time from the form

        appointment_date = datetime.strptime(appointment_date_str, '%Y-%m-%d %H:%M') if appointment_date_str else None
        appointment_end = datetime.strptime(appointment_end_str, '%Y-%m-%d %H:%M') if appointment_end_str else None

        # Now pass these datetime objects to your booking manager
        BookingManager.add_booking(user_id, service_id, appointment_date, appointment_end)
        return redirect(url_for('general_blueprint.user_dashboard'))

    return render_template('book_service.html', service=service)

@booking_blueprint.route('/confirm_booking', methods=['GET'])
def confirm_booking():
    service_id = request.args.get('service_id')
    start_time = request.args.get('start')
    end_time = request.args.get('end')
    
    # Fetch additional details as needed, e.g., service details
    service = Service.query.get_or_404(service_id)

    return render_template(
        'confirm_booking.html', 
        service=service, 
        start_time=start_time, 
        end_time=end_time, 
        metadata=confirm_booking_page_content["meta"],
        footer=confirm_booking_page_content["footer"],

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