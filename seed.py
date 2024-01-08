# seed.py
from datetime import datetime
import time
from werkzeug.security import generate_password_hash
from app import app, db  # Replace with your actual Flask app init file
from model import AvailabilityRule, Location, User, Service, Charity

def add_users():
    """
    Creates and adds predefined users to the database.
    """
    users = [
        User(
            username='Prophet Yani',
            email='prophetyani@gmail.com',
            password_hash=generate_password_hash('password123'),
            first_name='Yani',
            last_name='White',
            bio='Administrator of the website',
            create_date=datetime.now(),
            last_login_date=datetime.now(),
            user_role='admin',
            status='active',
            country='United States',
            confirmed=True
        ),
        User(
            username='Tech Guy',
            email='jonathan.k.sullivan@gmail.com',
            password_hash=generate_password_hash('password123'),
            first_name='Jonathan',
            last_name='Sullivan',
            bio='Administrator of the website',
            create_date=datetime.now(),
            last_login_date=datetime.now(),
            user_role='admin',
            status='active',
            country='United States',
            confirmed=True
        )
    ]
    db.session.add_all(users)

def add_services():
    """
    Creates and adds predefined services to the database.
    """
    service = Service(
        name='Customized Spiritual Consultations',
        description='Personalized one-on-one sessions tailored to your unique spiritual journey...',
        duration=15,
        price=25.00,
        image_url='images/consultations.webp',
        service_type='Spiritual Guidance',
        donation_percentage=10.00
    )
    db.session.add(service)

def add_charities():
    """
    Creates and adds predefined charities to the database.
    """
    charities = [
        Charity(
            name='Doctors Without Borders',
            description='An international medical humanitarian organization...',
            image_url='images/doctors_without_borders.svg'
        ),
        Charity(
            name='Room to Read',
            description='Focused on improving literacy and gender equality in education...',
            image_url='images/room_to_read.png'
        ),
        Charity(
            name='The Nature Conservancy',
            description='A global environmental non-profit working to protect the lands...',
            image_url='images/nature_conservancy.webp'
        )
    ]
    db.session.add_all(charities)

def add_availability():
    """
    Adds predefined availability rule to the database for 24/7 availability.
    """
    availability_rule = AvailabilityRule(
        day_of_week=0,  # None for all days
        start_time=time(0, 0),  # 24-hour format for midnight
        end_time=time(23, 59),  # 24-hour format for end of day
        priority=0,  # You can set this based on your priorities
        is_recurring=True
    )
    db.session.add(availability_rule)

def add_locations():
    """
    Creates and adds predefined locations to the database.
    """
    locations = [
        Location(
            address='123 Main St',
            city='Cityville',
            state='Stateville',
            country='Countryland',
            zip_code='12345',
            location_type='Business'
        ),
        Location(
            address='456 Oak Ave',
            city='Townsville',
            state='Stateland',
            country='Countryland',
            zip_code='67890',
            location_type='Residence'
        )
        # Add more locations as needed
    ]
    db.session.add_all(locations)

def seed_database():
    """
    Drops existing tables, recreates them, and seeds the database with initial data.
    """
    try:
        with app.app_context():
            db.drop_all()
            print("Tables dropped successfully.")
    except Exception as e:
        print(f"Error dropping tables: {e}")

    try:
        with app.app_context():
            db.create_all()
            print("Tables created successfully.")
            add_users()
            # add_services()
            # add_charities()
            # add_availability()
            # add_locations()
            db.session.commit()
            print("Database seeded successfully.")
    except Exception as e:
        db.session.rollback()
        print(f"Error seeding database: {e}")

if __name__ == '__main__':
    seed_database()
    # print("DB Already Seeded.")