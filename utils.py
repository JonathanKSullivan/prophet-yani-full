# utils.py

import os
from flask import session
from models import ContactMessage, User
from flask_mail import Message
from extensions import mail, db

def is_user_admin():
    """
    Checks if the current user is an admin.

    Returns:
    - bool: True if the user is an admin, False otherwise.
    """
    user_id = session.get('user_id')
    if not user_id:
        return False

    # Assuming the User model has an 'is_admin' attribute or similar
    user = User.query.get(user_id)
    return user is not None and user.user_role == "admin"

    # If there's no 'is_admin' attribute, you might check the user's role:
    # return user is not None and user.role == 'admin'

def process_contact_form(name, email, message):
    # Save message to database
    new_message = ContactMessage(name=name, email=email, message=message)
    db.session.add(new_message)
    db.session.commit()

    # Send email
    msg = Message("New Contact Form Submission",
                  sender=os.environ.get('MAIL_USERNAME', 'SullivanSoftwareSolutions@gmail.com'),
                  recipients=["prophetyani@gmail.com"])
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    mail.send(msg)