# model.py
from flask_sqlalchemy import SQLAlchemy
from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    profile_image_url = db.Column(db.String(255))
    create_date = db.Column(db.DateTime)
    last_login_date = db.Column(db.DateTime)
    user_role = db.Column(db.String(50))
    status = db.Column(db.String(50))
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
    type = db.Column(db.String(50))
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    donation_percentage = db.Column(db.Numeric(5, 2))
    bookings = db.relationship('Booking', backref='service', lazy=True)
    donations = db.relationship('Donation', backref='service', lazy=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    booking_date = db.Column(db.DateTime)
    appointment_date = db.Column(db.DateTime)
    status = db.Column(db.String(50))

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    amount = db.Column(db.Numeric(10, 2))
    charity_id = db.Column(db.Integer, db.ForeignKey('charity.id'), nullable=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    donation_date = db.Column(db.DateTime)
    type = db.Column(db.String(50))

class Charity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    donations = db.relationship('Donation', backref='charity', lazy=True)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100))
    zip_code = db.Column(db.String(20))
    location_type = db.Column(db.String(50))
    services = db.relationship('Service', backref='location', lazy=True)
    charities = db.relationship('Charity', backref='location', lazy=True)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    amount = db.Column(db.Numeric(10, 2))
    transaction_id = db.Column(db.String(100))
    payment_method = db.Column(db.String(50))
    payment_date = db.Column(db.DateTime)
