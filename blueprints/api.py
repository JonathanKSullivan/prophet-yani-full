from flask import Blueprint
from flask_restful import Api, Resource
from lib.availability_manager import AvailabilityManager
from lib.charity_manager import CharityManager
from lib.contact_manager import ContactMessageManager
from lib.donation_manager import DonationManager
from lib.location_manager import LocationManager
from lib.payment_manager import PaymentManager
from lib.user_manager import UserManager
from lib.service_manager import ServiceManager
from lib.booking_manager import BookingManager


api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

class UserListResource(Resource):
    def get(self):
        users = UserManager.get_all_users()
        user_data = []
        for user in users:
            user_info = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'password_hash': user.password_hash,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'profile_image_url': user.profile_image_url,
                'bio': user.bio,
                'create_date': user.create_date.strftime('%Y-%m-%d %H:%M:%S'),
                'last_login_date': user.last_login_date.strftime('%Y-%m-%d %H:%M:%S'),
                'user_role': user.user_role,
                'status': user.status,
                'country': user.country,
                'confirmed': user.confirmed
                # Add other fields as necessary
            }
            user_data.append(user_info)
        return {'users': user_data}

class ServiceListResource(Resource):
    def get(self):
        services = ServiceManager.list_all_services()
        service_data = []
        for service in services:
            service_info = {
                'id': service.id,
                'name': service.name,
                'description': service.description,
                'duration': service.duration,
                'price': str(service.price),  # Convert to string if it's a Decimal type
                # Add other fields as necessary
            }
            service_data.append(service_info)
        return {'services': service_data}

class BookingListResource(Resource):
    def get(self):
        bookings = BookingManager.list_all_bookings()
        booking_data = []
        for booking in bookings:
            booking_info = {
                'id': booking.id,
                'user_id': booking.user_id,
                'service_id': booking.service_id,
                'booking_date': booking.booking_date.isoformat(),
                'appointment_date': booking.appointment_date.isoformat(),
                'appointment_end': booking.appointment_end.isoformat(),
                'status': booking.status,
                # Add other fields as necessary
            }
            booking_data.append(booking_info)
        return {'bookings': booking_data}

class DonationListResource(Resource):
    def get(self):
        donations = DonationManager.list_all_donations()
        donation_data = []
        for donation in donations:
            donation_info = {
                'id': donation.id,
                'user_id': donation.user_id,
                'amount': str(donation.amount),  # Convert to string if it's a Decimal type
                'charity_id': donation.charity_id,
                'service_id': donation.service_id,
                'donation_date': donation.donation_date.isoformat(),
                'type': donation.type,
                # Add other fields as necessary
            }
            donation_data.append(donation_info)
        return {'donations': donation_data}

class CharityListResource(Resource):
    def get(self):
        charities = CharityManager.list_all_charities()
        charity_data = []
        for charity in charities:
            charity_info = {
                'id': charity.id,
                'name': charity.name,
                'description': charity.description,
                # Add other fields as necessary
            }
            charity_data.append(charity_info)
        return {'charities': charity_data}

class LocationListResource(Resource):
    def get(self):
        locations = LocationManager.list_all_locations()
        location_data = []
        for location in locations:
            location_info = {
                'id': location.id,
                'address': location.address,
                'city': location.city,
                'state': location.state,
                'country': location.country,
                # Add other fields as necessary
            }
            location_data.append(location_info)
        return {'locations': location_data}

class PaymentListResource(Resource):
    def get(self):
        payments = PaymentManager.list_all_payments()
        payment_data = []
        for payment in payments:
            payment_info = {
                'id': payment.id,
                'user_id': payment.user_id,
                'amount': str(payment.amount),
                'transaction_id': payment.transaction_id,
                # Add other fields as necessary
            }
            payment_data.append(payment_info)
        return {'payments': payment_data}

class AvailabilityListResource(Resource):
    def get(self):
        # Fetch availability rules and their specific exclusion dates
        availability_rules = AvailabilityManager.list_all_availability_rules()
        availability_data = []
        for rule in availability_rules:
            exclusions = rule.exclusion_dates
            exclusion_dates = [exclusion.date.isoformat() for exclusion in exclusions]

            rule_info = {
                'id': rule.id,
                'day_of_week': rule.day_of_week,
                'start_time': rule.start_time.isoformat(),
                'end_time': rule.end_time.isoformat(),
                'priority': rule.priority,
                'is_recurring': rule.is_recurring,
                'exclusion_dates': exclusion_dates
            }
            availability_data.append(rule_info)

        # Fetch global exclusion dates
        global_exclusions = AvailabilityManager.list_all_global_exclusions()
        global_exclusion_dates = [exclusion.date.isoformat() for exclusion in global_exclusions]

        return {
            'availability_rules': availability_data,
            'global_exclusion_dates': global_exclusion_dates
        }
class ContactMessageListResource(Resource):
    def get(self):
        messages = ContactMessageManager.list_all_messages()
        message_data = []
        for message in messages:
            message_info = {
                'id': message.id,
                'name': message.name,
                'email': message.email,
                'message': message.message,
                'created_at': message.created_at.isoformat(),
                # Add other fields as necessary
            }
            message_data.append(message_info)
        return {'contact_messages': message_data}


# Add resources to the API
api.add_resource(UserListResource, '/users')
api.add_resource(ServiceListResource, '/services')
api.add_resource(BookingListResource, '/bookings')
api.add_resource(DonationListResource, '/donations')
api.add_resource(CharityListResource, '/charities')
api.add_resource(LocationListResource, '/locations')
api.add_resource(PaymentListResource, '/payments')
api.add_resource(AvailabilityListResource, '/availabilities')
api.add_resource(ContactMessageListResource, '/contact_messages')