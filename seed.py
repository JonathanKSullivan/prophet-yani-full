# seed.py
from datetime import datetime, time
from werkzeug.security import generate_password_hash
from app import app, db  # Replace with your actual Flask app init file
from model import AvailabilityRule, ExclusionDate, Location, User, Service, Charity

def add_users():
    """
    Creates and adds predefined users to the database.
    """
    users = [
        User(
            username='Prophet Yani'.lower(),
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
            username='Tech Guy'.lower(),
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
    Adds predefined availability rules to the database for each day of the week.
    """
    for day in range(7):  # Days are typically represented from 0 to 6 (Monday to Sunday)
        start_time = time(0, 0)  # 24-hour format for midnight
        end_time = time(23, 59)  # 24-hour format for end o

        availability_rule = AvailabilityRule(
            day_of_week=day,
            start_time=start_time,
            end_time=end_time,
            priority=0,
            is_recurring=True
        )

        # Add exclusion dates if needed
        exclusion_dates = [
            ExclusionDate(date=datetime(2024, 1, 15, 0, 0)),
            ExclusionDate(date=datetime(2024, 2, 1, 0, 0)),
            # Add more exclusion dates as needed
        ]

        availability_rule.exclusion_dates.extend(exclusion_dates)

        # Save the availability rule to the database
        db.session.add(availability_rule)

    try:
        # Commit changes to the database
        db.session.commit()
        print("Availability rules added successfully.")
    except Exception as e:
        # Rollback changes in case of an error
        db.session.rollback()
        print(f"Error adding availability rules: {e}")

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
    # try:
    #     with app.app_context():
    #         AvailabilityRule.__table__.drop()
    #         ExclusionDate.__table__.drop()
    #         Location.__table__.drop()
    #         User.__table__.drop()
    #         Service.__table__.drop()
    #         Charity.__table__.drop()
    #         db.drop_all()
    #         print("Tables dropped successfully.")
            
    # except Exception as e:
    #     db.session.rollback()
    #     print(f"Error seeding database: {e}")
    try:
        with app.app_context():
            db.create_all()
            print("Tables created successfully.")
            add_users()
            add_services()
            add_charities()
            add_availability()
            # add_locations()
            db.session.commit()
            print("Database seeded successfully.")
    except Exception as e:
        db.session.rollback()
        print(f"Error seeding database: {e}")

if __name__ == '__main__':
    # app.app_context().push()
    # seed_database()
    print("DB Already Seeded.")