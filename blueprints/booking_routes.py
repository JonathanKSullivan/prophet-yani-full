from flask import Blueprint, redirect, render_template, request, url_for
from lib.booking_manager import BookingManager

booking_blueprint = Blueprint('booking_blueprint', __name__)

@booking_blueprint.route('/book_service/<int:service_id>', methods=['GET', 'POST'])
def book_service(service_id):
    service = Service.query.get_or_404(service_id)

    if request.method == 'POST':
        user_id = request.form['user_id']
        # process the booking form
        booking_date = request.form.get('booking_date')
        # create and save the new booking
        BookingManager.add_booking(user_id, service_id, booking_date)
        return redirect(url_for('user_blueprint.user_dashboard'))

    return render_template('book_service.html', service=service)

[]