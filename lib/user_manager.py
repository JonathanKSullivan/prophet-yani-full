from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
import datetime


class UserManager:
    @staticmethod
    def add_user(username, email, password, first_name='', last_name='', bio=''):
        new_user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password),
            first_name=first_name,
            last_name=last_name,
            bio=bio,  # Add bio field
            create_date=datetime.datetime.now(),
            last_login_date=datetime.datetime.now(),  # Assuming this is a new field
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
    def update_user(user_id, **kwargs):
        user = User.query.get(user_id)
        if not user:
            return None

        immutable_fields = {'id', 'username', 'password_hash', 'create_date'}
        for key, value in kwargs.items():
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
