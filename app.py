from flask import Flask
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

from extensions import db

app = Flask(__name__)

# Configure the SQLAlchemy part
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prophet_yani.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_random_secret_key'  # Replace with your secret key

# Initialize the database with the Flask app
db.init_app(app)

# Function to initialize the database
def initialize_database():
    with app.app_context():
        # Import models here. This ensures they are known to SQLAlchemy
        from models import User, Service, Booking, Donation, Charity, Location, Payment
        # Create tables
        db.create_all()

# Call the initialize function
initialize_database()

# Register blueprints
app.register_blueprint(booking_blueprint, url_prefix='/booking')
app.register_blueprint(charity_blueprint, url_prefix='/charity')
app.register_blueprint(donation_blueprint, url_prefix='/donation')
app.register_blueprint(general_blueprint)
app.register_blueprint(location_blueprint, url_prefix='/location')
app.register_blueprint(payment_blueprint, url_prefix='/payment')
app.register_blueprint(service_blueprint, url_prefix='/service')
app.register_blueprint(user_blueprint, url_prefix='/user')

# The following is not necessary if using `flask run`
# if __name__ == '__main__':
#     app.run(debug=True)
