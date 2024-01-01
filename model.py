# model.py
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    profile_image_url = db.Column(db.String(255))
    bio = db.Column(db.String(500))
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_login_date = db.Column(db.DateTime)
    user_role = db.Column(db.String(50))
    status = db.Column(db.String(50))
    country = db.Column(db.String(100))
    confirmed = db.Column(db.Boolean, default=False)

    # Relationships
    bookings = db.relationship('Booking', backref='user', lazy=True)
    donations = db.relationship('Donation', backref='user', lazy=True)
    payments = db.relationship('Payment', backref='user', lazy=True)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    duration = db.Column(db.Integer)
    price = db.Column(db.Numeric(10, 2))
    image_url = db.Column(db.String(255))
    service_type = db.Column(db.String(50))
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    donation_percentage = db.Column(db.Numeric(5, 2))

    # Relationships
    bookings = db.relationship('Booking', backref='service', lazy=True)
    donations = db.relationship('Donation', backref='service', lazy=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)
    appointment_date = db.Column(db.DateTime)
    appointment_end = db.Column(db.DateTime)
    status = db.Column(db.String(50))

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    amount = db.Column(db.Numeric(10, 2))
    charity_id = db.Column(db.Integer, db.ForeignKey('charity.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    donation_date = db.Column(db.DateTime, default=datetime.utcnow)
    donation_type = db.Column(db.String(50))

class Charity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))

    # Relationships
    donations = db.relationship('Donation', backref='charity', lazy=True)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.String(20))
    location_type = db.Column(db.String(50))

    # Relationships
    services = db.relationship('Service', backref='location', lazy=True)
    charities = db.relationship('Charity', backref='location', lazy=True)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    amount = db.Column(db.Numeric(10, 2))
    transaction_id = db.Column(db.String(100))
    payment_method = db.Column(db.String(50))
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)

class AvailabilityRule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day_of_week = db.Column(db.Integer)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    priority = db.Column(db.Integer, default=0)
    is_recurring = db.Column(db.Boolean, default=True)

    # Relationships
    exclusion_dates = db.relationship('ExclusionDate', backref='availability_rule', lazy=True)

class ExclusionDate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    availability_rule_id = db.Column(db.Integer, db.ForeignKey('availability_rule.id'))
    date = db.Column(db.Date, nullable=False)

class GlobalExclusionDate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message
