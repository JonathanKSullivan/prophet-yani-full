from cgi import FieldStorage
from email import message
from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from werkzeug.datastructures import FileStorage 
from lib.availability_manager import AvailabilityManager
from lib.charity_manager import CharityManager
from lib.contact_message_manager import ContactMessageManager
from lib.donation_manager import DonationManager
from lib.location_manager import LocationManager
from lib.payment_manager import PaymentManager
from lib.user_manager import UserManager
from lib.service_manager import ServiceManager
from lib.booking_manager import BookingManager
from utils import send_email


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
                'bio': user.bio,
                'create_date': user.create_date.strftime('%Y-%m-%d %H:%M:%S'),
                'last_login_date': user.last_login_date.strftime('%Y-%m-%d %H:%M:%S'),
                'user_role': user.user_role,
                'status': user.status,
                'country': user.country,
                'confirmed': user.confirmed,
                'profile_image_url': user.profile_image_url,
                # Add other fields as necessary
            }
            user_data.append(user_info)
        return {'users': user_data}
    
    def put(self, user_id):
        parser = reqparse.RequestParser()
        # Define the expected fields for updating a user
        parser.add_argument('username')
        parser.add_argument('email')
        parser.add_argument('password')  # Note: Handle password updates securely in production
        parser.add_argument('first_name')
        parser.add_argument('last_name')
        parser.add_argument('bio')
        parser.add_argument('country')
        parser.add_argument('profileImage', type=FileStorage, location='files')

        args = parser.parse_args()

        print(args)


        # Check if a file is present in the request
        if args['profileImage']:
            file = args['profileImage']
            # Handle the image upload (use your preferred method)
            file_url = UserManager.upload_to_s3(file, 'prophet-yani-assests', 'profile_images')
            # Update the user's profile_image_url with the new URL
            args['profile_image_url'] = file_url

        # Update the user using the UserManager class
        updated_user = UserManager.update_user(user_id, args)

        if updated_user:
            return {'message': 'User updated successfully'}, 200
        else:
            return {'message': 'User not found'}, 404

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
                'service_type': service.service_type,
                'donation_percentage': str(service.donation_percentage),
                'image_url': service.image_url
                # Add other fields as necessary
            }
            service_data.append(service_info)
        return {'services': service_data}
    
    def put(self, service_id):
        parser = reqparse.RequestParser()
        # Define the expected fields for updating a service
        parser.add_argument('name')
        parser.add_argument('description')
        parser.add_argument('duration', type=int)
        parser.add_argument('price', type=float)
        parser.add_argument('service_type')
        parser.add_argument('donation_percentage', type=float)
        parser.add_argument('image', type=FileStorage, location='files')

        args = parser.parse_args()

        # Extract the image file from the request
        image_file = args['image']
        if image_file:
            # Handle the image file as needed (e.g., save to server or cloud storage)
            print("add code here")

        # Update the service using the ServiceManager class
        updated_service = ServiceManager.update_service(service_id, **args)

        if updated_service:
            return {'message': 'Service updated successfully'}, 200
        else:
            return {'message': 'Error updating service'}, 500

    def post(self):
        parser = reqparse.RequestParser()
        # Define the expected fields for adding a new service
        parser.add_argument('name', required=True)
        parser.add_argument('description')
        parser.add_argument('duration', type=int)
        parser.add_argument('price', type=float)
        parser.add_argument('service_type')
        parser.add_argument('donation_percentage', type=float)
        parser.add_argument('image', type=FileStorage, location='files')

        args = parser.parse_args()

        # Extract the image file from the request
        image_file = args['image']
        if image_file:
            # Handle the image file as needed (e.g., save to server or cloud storage)
            print("complete")

        # Add the new service using the ServiceManager class
        new_service = ServiceManager.add_service(**args)

        if new_service:
            return {'message': 'Service added successfully'}, 201
        else:
            return {'message': 'Error adding service'}, 500
        
    def delete(self, service_id):
        # Delete the service using the ServiceManager class
        deleted = ServiceManager.delete_service(service_id)

        if deleted:
            return {'message': 'Service deleted successfully'}, 200
        else:
            return {'message': 'Error deleting service'}, 500

class BookingListResource(Resource):
    def get(self):
        bookings = BookingManager.list_all_bookings()
        booking_data = []
        for booking in bookings:
            booking_info = {
                'id': booking.id,
                'user': booking.user.first_name + ' ' + booking.user.last_name,
                'service': booking.service.name,
                'booking_date': booking.booking_date.isoformat(),
                'appointment_date': booking.appointment_date.isoformat(),
                'appointment_end': booking.appointment_end.isoformat(),
                'status': booking.status,
                # Add other fields as necessary
            }
            booking_data.append(booking_info)
        return {'bookings': booking_data}
    
    def put(self, booking_id):
        # Confirm the booking using the BookingManager class
        confirmed_booking = BookingManager.confirm_booking(booking_id)

        if confirmed_booking:
            return {'message': 'Booking confirmed successfully'}, 200
        else:
            return {'message': 'Error confirming booking'}, 500

class DonationListResource(Resource):
    def get(self):
        donations = DonationManager.list_all_donations()
        donation_data = []
        for donation in donations:
            donation_info = {
                'id': donation.id,
                'user': donation.user.first_name + ' ' + donation.user.last_name,
                'amount': str(donation.amount),  # Convert to string if it's a Decimal type
                'charity': donation.charity.name,
                'service': donation.service.name,
                'donation_date': donation.donation_date.isoformat(),
                'type': donation.donation_type,
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
                'image_url': charity.image_url,
                'donations_count': '3',
                # Add other fields as necessary
            }
            charity_data.append(charity_info)
        return {'charities': charity_data}
    
    def post(self):
        parser = reqparse.RequestParser()
        # Define the expected fields for adding a new charity
        parser.add_argument('name', required=True)
        parser.add_argument('description')
        parser.add_argument('image_url')
        # Add other fields as necessary

        args = parser.parse_args()

        # Add the new charity using the CharityManager class
        new_charity = CharityManager.add_charity(**args)

        if new_charity:
            return {'message': 'Charity added successfully'}, 201
        else:
            return {'message': 'Error adding charity'}, 500

    def put(self, charity_id):
        parser = reqparse.RequestParser()
        # Define the expected fields for updating a charity
        parser.add_argument('name')
        parser.add_argument('description')
        parser.add_argument('image_url')
        # Add other fields as necessary

        args = parser.parse_args()

        # Update the charity using the CharityManager class
        updated_charity = CharityManager.update_charity(charity_id, **args)

        if updated_charity:
            return {'message': 'Charity updated successfully'}, 200
        else:
            return {'message': 'Error updating charity'}, 500

    def delete(self, charity_id):
        # Delete the charity using the CharityManager class
        deleted = CharityManager.delete_charity(charity_id)

        if deleted:
            return {'message': 'Charity deleted successfully'}, 200
        else:
            return {'message': 'Error deleting charity'}, 500

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
                'zip_code': location.zip_code,
                'location_type': location.location_type,
                # Add other fields as necessary
            }
            location_data.append(location_info)
        return {'locations': location_data}

    def post(self):
        parser = reqparse.RequestParser()
        # Define the expected fields for adding a new location
        parser.add_argument('address', required=True)
        parser.add_argument('city', required=True)
        parser.add_argument('state', required=True)
        parser.add_argument('country', required=True)
        parser.add_argument('zip_code')
        parser.add_argument('location_type', required=True)
        # Add other fields as necessary

        args = parser.parse_args()

        # Add the new location using the LocationManager class
        new_location = LocationManager.add_location(**args)

        if new_location:
            return {'message': 'Location added successfully'}, 201
        else:
            return {'message': 'Error adding location'}, 500

    def put(self, location_id):
        parser = reqparse.RequestParser()
        # Define the expected fields for updating a location
        parser.add_argument('address')
        parser.add_argument('city')
        parser.add_argument('state')
        parser.add_argument('country')
        parser.add_argument('zip_code')
        parser.add_argument('location_type')
        # Add other fields as necessary

        args = parser.parse_args()

        # Update the location using the LocationManager class
        updated_location = LocationManager.update_location(location_id, **args)

        if updated_location:
            return {'message': 'Location updated successfully'}, 200
        else:
            return {'message': 'Error updating location'}, 500

    def delete(self, location_id):
        # Delete the location using the LocationManager class
        deleted = LocationManager.delete_location(location_id)

        if deleted:
            return {'message': 'Location deleted successfully'}, 200
        else:
            return {'message': 'Error deleting location'}, 500

class PaymentListResource(Resource):
    def get(self):
        payments = PaymentManager.list_all_payments()
        payment_data = []
        for payment in payments:
            payment_info = {
                'id': payment.id,
                'user': payment.user.first_name + ' ' + payment.user.last_name,
                'amount': str(payment.amount),
                'transaction_id': payment.transaction_id,
                'payment_method': payment.payment_method,
                'payment_date': payment.payment_date.isoformat(),
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
            print(rule_info)
            availability_data.append(rule_info)

        
        return {
            'availability_rules': availability_data,
        }
    
    def post(self):
        # Logic to add a new availability rule
        data = request.get_json()
        new_rule = AvailabilityManager.add_availability_rule(
            data['day_of_week'],
            data['start_time'],
            data['end_time'],
            data.get('priority', 0),
            data.get('is_recurring', True)
        )
        if new_rule:
            return {'message': 'New rule added successfully'}, 201
        else:
            return {'error': 'Failed to add a new rule'}, 500
        
    def delete(self, rule_id):
        # Logic to delete the availability rule
        success = AvailabilityManager.delete_availability_rule(rule_id)
        if success:
            return {'message': 'Rule deleted successfully'}, 200
        else:
            return {'error': 'Rule not found'}, 404

class ExclusionDateResource(Resource):
    def delete(self, rule_id, date):
        # Logic to remove the exclusion date
        success = AvailabilityManager.remove_exclusion_date(rule_id, date)
        if success:
            return {'message': 'Exclusion date removed successfully'}, 200
        else:
            return {'error': 'Exclusion date not found'}, 404

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

class ContactMessageResource(Resource):
    def get(self, message_id):
        message = ContactMessageManager.get_message_by_id(message_id)
        if message:
            message_info = {
                'id': message.id,
                'name': message.name,
                'email': message.email,
                'message': message.message,
                'created_at': message.created_at.isoformat(),
            }
            return {'contact_message': message_info}
        else:
            return {'error': 'Message not found'}, 404

    def post(self, message_id):
        # Endpoint to send replies to messages
        # Extract necessary information from the request
        data = request.get_json()
        reply_message = data.get('reply_message')

        print('data')
        print(data)

        # Assume you have a function to send emails
        send_email(to=data['email'], subject="Reply to Your Message", template=reply_message)

        return {'message': 'Reply sent successfully'}

    def delete(self, message_id):
        # Endpoint to delete messages
        success = ContactMessageManager.delete_message(message_id)
        if success:
            return {'message': 'Message deleted successfully'}
        else:
            return {'error': 'Message not found'}, 404


# Add resources to the API
api.add_resource(UserListResource, '/users', '/users/<int:user_id>')
api.add_resource(ServiceListResource, '/services')
api.add_resource(BookingListResource, '/bookings')
api.add_resource(DonationListResource, '/donations')
api.add_resource(CharityListResource, '/charities')
api.add_resource(LocationListResource, '/locations')
api.add_resource(PaymentListResource, '/payments')
api.add_resource(AvailabilityListResource, '/availabilities')
api.add_resource(ContactMessageListResource, '/contact_messages')
api.add_resource(ContactMessageResource, '/contact_messages/<int:message_id>')
