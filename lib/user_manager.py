import boto3
from werkzeug.utils import secure_filename
import os
import uuid
from lib.location_manager import LocationManager
from model import db, User
from werkzeug.security import generate_password_hash, check_password_hash
import datetime


class UserManager:
    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def add_user(username, email, password, first_name='', last_name='', bio='', country=''):
        new_user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password),
            first_name=first_name,
            last_name=last_name,
            bio=bio,
            country=country,  # Set country field
            create_date=datetime.datetime.now(),
            last_login_date=datetime.datetime.now(),
            status='Active'
        )
        db.session.add(new_user)
        try:
            db.session.commit()
            return new_user
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def update_user_with_location(user_id, user_data):
        user = User.query.get(user_id)
        if not user:
            return None

        # Update user details
        immutable_fields = {'id', 'username', 'password_hash', 'create_date'}
        for key, value in user_data.items():
            if key in immutable_fields:
                continue  # Skip updating immutable fields
            if hasattr(user, key):
                setattr(user, key, value)

        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False

    @staticmethod
    def check_password(user_id, password):
        user = User.query.get(user_id)
        if user and check_password_hash(user.password_hash, password):
            return True
        return False

    @staticmethod
    def get_all_users():
        return User.query.all()
    
    

    @staticmethod
    def update_password(user_id, new_password):
        user = User.query.get(user_id)
        if not user:
            return False  # User not found

        user.password_hash = generate_password_hash(new_password)
        db.session.commit()
        return True

    @staticmethod
    def upload_to_s3(file, bucket_name):
        # Ensure boto3 is installed and configured correctly
        s3_client = boto3.client('s3')

        # Generate a unique file name
        filename = secure_filename(file.filename)
        unique_filename = str(uuid.uuid4()) + "_" + filename

        try:
            # Upload file to S3
            s3_client.upload_fileobj(
                file,
                bucket_name,
                unique_filename,
                ExtraArgs={'ACL': 'public-read'}  # Make the file publicly readable
            )

            # Construct the file URL
            file_url = f"https://{bucket_name}.s3.amazonaws.com/{unique_filename}"
            return file_url

        except Exception as e:
            print("Something went wrong: ", e)
            return None