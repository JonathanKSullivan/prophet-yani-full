import os
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from data import home_page_content, about_page_content

from blueprints.booking_routes import booking_blueprint
from blueprints.charity_routes import charity_blueprint
from blueprints.donation_routes import donation_blueprint
from blueprints.general_routes import general_blueprint
from blueprints.location_routes import location_blueprint
from blueprints.payment_routes import payment_blueprint
from blueprints.service_routes import service_blueprint
from blueprints.user_routes import user_blueprint
from blueprints.api import api_blueprint

from extensions import db, mail
from config import DevelopmentConfig, ProductionConfig
from flask import g

# Import models here. This ensures they are known to SQLAlchemy
from model import User, Service, Booking, Donation, Charity, Location, Payment
from utils import is_user_admin

# Create and configure app
app = Flask(__name__)
env = os.environ.get('FLASK_ENV', 'development')

@app.template_filter('currency')
def currency_filter(value):
    return "${:,.2f}".format(value)


if env == 'production':
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

# Initialize the database with the Flask app
db.init_app(app)
mail.init_app(app)

# Function to initialize the database
def initialize_database():
    with app.app_context():
        # Create tables
        db.create_all()

# Call the initialize function
initialize_database()


@app.context_processor
def inject_user():
    user = None
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
    return dict(user=user)

@app.context_processor
def inject_admin_check():
    return dict(is_user_admin=is_user_admin)

# Register blueprints
app.register_blueprint(booking_blueprint, url_prefix='/booking')
app.register_blueprint(charity_blueprint, url_prefix='/charity')
app.register_blueprint(donation_blueprint, url_prefix='/donation')
app.register_blueprint(general_blueprint)
app.register_blueprint(location_blueprint, url_prefix='/location')
app.register_blueprint(payment_blueprint, url_prefix='/payment')
app.register_blueprint(service_blueprint, url_prefix='/service')
app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(api_blueprint, url_prefix='/api')

# The following is not necessary if using `flask run`
if __name__ == "__main__":
    app.run()
