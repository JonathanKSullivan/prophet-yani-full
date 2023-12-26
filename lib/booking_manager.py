from models import db, Booking
from datetime import datetime

class BookingManager:

    @staticmethod
    def count_past_bookings():
        try:
            now = datetime.utcnow()
            past_bookings_count = Booking.query.filter(Booking.appointment_end < now).count()
            return past_bookings_count
        except Exception as e:
            print("Error counting past bookings:", e)
            return -1
        
    @staticmethod
    def add_booking(user_id, service_id, appointment_date, appointment_end):
        new_booking = Booking(
            user_id=user_id,
            service_id=service_id,
            booking_date=datetime.now(),
            appointment_date=appointment_date,
            appointment_end=appointment_end,  # Include appointment_end in the booking
            status='Booked'
        )
        db.session.add(new_booking)
        try:
            db.session.commit()
            return new_booking
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_booking_by_id(booking_id):
        return Booking.query.get(booking_id)

    @staticmethod
    def update_booking(booking_id, **kwargs):
        booking = Booking.query.get(booking_id)
        if not booking:
            return None
        for key, value in kwargs.items():
            if hasattr(booking, key):
                setattr(booking, key, value)
        db.session.commit()
        return booking

    @staticmethod
    def delete_booking(booking_id):
        booking = Booking.query.get(booking_id)
        if booking:
            db.session.delete(booking)
            db.session.commit()
            return True
        return False

    @staticmethod
    def list_all_bookings():
        return Booking.query.all()
