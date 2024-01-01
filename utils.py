# utils.py

import os
from flask import current_app, render_template, session
from model import ContactMessage, User
from flask_mail import Message
from extensions import mail, db
from itsdangerous import URLSafeTimedSerializer

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=current_app.config['SECURITY_PASSWORD_SALT'])

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

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=current_app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)

def send_username_recovery_email(email, username):
    # Define email subject
    subject = "Username Recovery"

    # Render email template
    html = render_template('email/username_recovery.html', username=username)

    # Send email
    msg = Message(
        subject,
        recipients=[email],
        html=html,
        sender=current_app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)