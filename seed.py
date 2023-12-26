from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
from app import app, db  # Replace with your actual Flask app init file
from models import User, Service, Booking, Donation, Charity, Location, Payment
from werkzeug.security import generate_password_hash
from datetime import datetime

def add_users():
    yani = User(
        username='Prophet Yani',
        email='prophetyani@gmail.com',
        password_hash=generate_password_hash('password123'),  # Use a secure hash for real scenarios
        first_name='Yani',
        last_name='White',
        bio='Administrator of the website',
        create_date=datetime.now(),
        last_login_date=datetime.now(),
        user_role='admin',
        status='active'
    )
    jonathan = User(
        username='Tech Guy',
        email='jonathan.k.sullivan@gmail.com',
        password_hash=generate_password_hash('password123'),  # Use a secure hash for real scenarios
        first_name='Jonathan',
        last_name='Sullivan',
        bio='Administrator of the website',
        create_date=datetime.now(),
        last_login_date=datetime.now(),
        user_role='admin',
        status='active'
    )
    test_user = User(
        username='test',
        email='test@example.com',
        password_hash=generate_password_hash('testpassword'),  # Use a secure hash for real scenarios
        first_name='John',
        last_name='Doe',
        profile_image_url='http://example.com/user1.jpg',
        bio='Regular user of the website',  # Example bio
        create_date=datetime.now(),
        last_login_date=datetime.now(),
        user_role='user',
        status='active'
    )
    db.session.add_all([yani, jonathan, test_user])
    db.session.commit()  # Don't forget to commit the changes

def add_services():
    service1 = Service(
        name='Customized Spiritual Consultations',
        description='Personalized one-on-one sessions tailored to your unique spiritual journey, offering specific insights and guidance. Aimed at achieving lasting inner peace, heightened self-awareness, and a clearer life path.',
        duration=30,
        price=20.00,
        image_url='images/consultations.webp',
        type='Spiritual Guidance',
        donation_percentage=10.00
    )
    db.session.add(service1)

def add_bookings():
    pass
    db.session.add(booking1)

def add_donations():
    pass
    db.session.add(donation1)

def add_charities():
    pass

def add_locations():
    pass

def add_payments():
    pass

def seed_database():
    with app.app_context():
        db.create_all()  # Create tables if they don't exist

        add_users()
        add_services()

        db.session.commit()  # Commit all changes

if __name__ == '__main__':
    seed_database()
