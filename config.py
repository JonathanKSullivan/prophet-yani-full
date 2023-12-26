# config.py
import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_random_secret_key'
    
    # Configure Flask-Mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'SullivanSoftwareSolutions@gmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'omib pebi rwua mrsk')
    MAIL_DEFAULT_SENDER = 'jonathan.k.sullivan@gmail.com'

    # Twitter API Credentials
    TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY', 'YOUR_CONSUMER_KEY')
    TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET', 'YOUR_CONSUMER_SECRET')
    TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN', 'YOUR_ACCESS_TOKEN')
    TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET', 'YOUR_ACCESS_TOKEN_SECRET')

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prophet_yani_dev.db'
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///prophet_yani.db')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    DEBUG = False
