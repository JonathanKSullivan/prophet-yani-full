from datetime import datetime
from werkzeug.security import generate_password_hash
from app import app, db  # Replace with your actual Flask app init file
from models import User, Service, Booking, Donation, Charity, Location, Payment

def add_users():
    admin_user = User(
        username='admin',
        email='admin@example.com',
        password_hash=generate_password_hash('admin123'),  # Use a secure hash for real scenarios
        first_name='Admin',
        last_name='User',
        profile_image_url='http://example.com/admin.jpg',
        create_date=datetime.now(),
        last_login_date=datetime.now(),
        user_role='admin',
        status='active'
    )
    user1 = User(
        username='user1',
        email='user1@example.com',
        password_hash=generate_password_hash('password1'),  # Use a secure hash for real scenarios
        first_name='John',
        last_name='Doe',
        profile_image_url='http://example.com/user1.jpg',
        create_date=datetime.now(),
        last_login_date=datetime.now(),
        user_role='user',
        status='active'
    )
    db.session.add_all([admin_user, user1])

def add_services():
    service1 = Service(
        name='Service 1',
        description='Description for Service 1',
        duration=60,
        price=100.00,
        image_url='http://example.com/service1.jpg',
        type='Type1',
        donation_percentage=10.00
    )
    db.session.add(service1)

def add_bookings():
    booking1 = Booking(
        user_id=1,  # Assuming user with id 1 exists
        service_id=1,  # Assuming service with id 1 exists
        booking_date=datetime.now(),
        appointment_date=datetime.now(),
        status='confirmed'
    )
    db.session.add(booking1)

def add_donations():
    donation1 = Donation(
        user_id=1,  # Assuming user with id 1 exists
        amount=50.00,
        charity_id=1,  # Assuming charity with id 1 exists
        service_id=1,  # Assuming service with id 1 exists
        donation_date=datetime.now(),
        type='One-time'
    )
    db.session.add(donation1)

def add_charities():
    charity1 = Charity(
        name='Charity 1',
        description='Description for Charity 1',
        image_url='http://example.com/charity1.jpg'
    )
    db.session.add(charity1)

def add_locations():
    location1 = Location(
        address='123 Main St',
        city='City',
        state='State',
        country='Country',
        zip_code='12345',
        location_type='Type1'
    )
    db.session.add(location1)

def add_payments():
    payment1 = Payment(
        user_id=1,  # Assuming user with id 1 exists
        amount=100.00,
        transaction_id='txn123',
        payment_method='Credit Card',
        payment_date=datetime.now()
    )
    db.session.add(payment1)

def seed_database():
    with app.app_context():
        db.create_all()  # Create tables if they don't exist

        add_users()
        add_services()
        add_bookings()
        add_donations()
        add_charities()
        add_locations()
        add_payments()

        db.session.commit()  # Commit all changes

if __name__ == '__main__':
    seed_database()
