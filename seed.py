from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
from app import app, db  # Replace with your actual Flask app init file
from models import AvailabilityRule, ExclusionDate, User, Service, Booking, Donation, Charity, Location, Payment
from werkzeug.security import generate_password_hash
from datetime import datetime

def add_users():
    yani = User(
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
    )
    jonathan = User(
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
    test_user = User(
        username='test',
        email='test@example.com',
        password_hash=generate_password_hash('testpassword'),
        first_name='John',
        last_name='Doe',
        profile_image_url='http://example.com/user1.jpg',
        bio='Regular user of the website',
        create_date=datetime.now(),
        last_login_date=datetime.now(),
        user_role='user',
        status='active',
        country='United States',
        confirmed=True
    )
    db.session.add_all([yani, jonathan, test_user])
    db.session.commit()

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
    # Assuming service1 is the ID of an existing service
    service1 = Service.query.filter_by(name='Customized Spiritual Consultations').first()

    # Fetch the Tech Guy user
    tech_guy = User.query.filter_by(username='Tech Guy').first()

    if service1 and tech_guy:
        booking1 = Booking(
            user_id=tech_guy.id,
            service_id=service1.id,
            booking_date=datetime.now(),
            appointment_date=datetime.now() + timedelta(days=7),
            appointment_end=datetime.now() + timedelta(days=7, hours=1),  # 1 hour after the appointment starts
            status='confirmed'
        )
        db.session.add(booking1)
        db.session.commit()

def add_donations():
    # Assuming charity1 is the ID of an existing charity
    charity1 = Charity.query.filter_by(name='Doctors Without Borders').first()

    # Fetch the Tech Guy user
    tech_guy = User.query.filter_by(username='Tech Guy').first()

    if charity1 and tech_guy:
        donation1 = Donation(
            user_id=tech_guy.id,
            amount=50.00,  # Example amount
            charity_id=charity1.id,
            donation_date=datetime.now(),
            type='One-time'  # Example donation type
        )
        db.session.add(donation1)
        db.session.commit()

def add_charities():
    charity1 = Charity(
        name='Doctors Without Borders',
        description='An international medical humanitarian organization providing aid in nearly 70 countries to people whose survival is threatened by violence, neglect, or catastrophe.',
        image_url='images/doctors_without_borders.svg'
    )

    charity2 = Charity(
        name='Room to Read',
        description='Focused on improving literacy and gender equality in education in low-income countries, Room to Read seeks to transform the lives of millions of children in developing countries by focusing on literacy and gender equality in education.',
        image_url='images/room_to_read.png'
    )

    charity3 = Charity(
        name='The Nature Conservancy',
        description='A global environmental non-profit working to protect the lands and waters on which all life depends, emphasizing harmony with nature and promoting a sense of global responsibility and care for the environment.',
        image_url='images/nature_conservancy.webp'
    )

    db.session.add_all([charity1, charity2, charity3])
    db.session.commit()  # Don't forget to commit the changes

def add_locations():
    locations = [
        Location(address='123 Main Street', city='City1', state='State1', country='United States', zip_code='12345', location_type='Country'),
        Location(address='456 Second Street', city='City2', state='State2', country='United States', zip_code='23456', location_type='Country'),
        Location(address='789 Third Street', city='City3', state='State3', country='United States', zip_code='34567', location_type='Country')
        # Add more locations as needed
    ]
    db.session.add_all(locations)
    db.session.commit()
    return [location.id for location in locations]

def add_weekly_availability_rules():
    for day in range(1, 6):  # Monday (1) to Friday (5)
        availability_rule = AvailabilityRule(
            day_of_week=day,
            start_time=datetime.strptime("09:00:00", "%H:%M:%S").time(),
            end_time=datetime.strptime("17:00:00", "%H:%M:%S").time(),
            priority=1,
            is_recurring=True
        )
        db.session.add(availability_rule)
    db.session.commit()

def add_us_holidays_exclusion():
    # Common US Holidays
    holidays = [
        "2023-01-01",  # New Year's Day
        "2023-07-04",  # Independence Day
        "2023-11-11",  # Veterans Day
        "2023-11-23",  # Thanksgiving Day
        "2023-12-25",  # Christmas Day
    ]

    for holiday in holidays:
        exclusion_date = ExclusionDate(
            date=datetime.strptime(holiday, "%Y-%m-%d").date()
        )
        db.session.add(exclusion_date)
    db.session.commit()

def add_payments():
    pass

def seed_database():
    with app.app_context():
        db.create_all()  # Create tables if they don't exist

        location_ids = add_locations()
        add_users()
        add_services()
        add_charities()
        add_bookings()
        add_donations()
        add_weekly_availability_rules()
        add_us_holidays_exclusion()
        add_payments()  # Call this if you have implemented it

        db.session.commit() 

if __name__ == '__main__':
    seed_database()

