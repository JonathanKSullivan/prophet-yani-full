# seed.py
from datetime import datetime
from werkzeug.security import generate_password_hash
from app import app, db  # Replace with your actual Flask app init file
from model import User, Service, Charity

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
        duration=30,
        price=20.00,
        image_url='images/consultations.webp',
        type='Spiritual Guidance',
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

def seed_database():
    """
    Seeds the database with initial data.
    """
    with app.app_context():
        db.create_all()
        try:
            add_users()
            add_services()
            add_charities()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error seeding database: {e}")

if __name__ == '__main__':
    seed_database()
