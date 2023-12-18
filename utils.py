# utils.py

from flask import session
from models import User

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
    return user is not None and user.is_admin

    # If there's no 'is_admin' attribute, you might check the user's role:
    # return user is not None and user.role == 'admin'

def process_contact_form(name, email, message):
    """
    Process the contact form data. This can include sending an email,
    storing the data in a database, or any other required action.

    Args:
    - name (str): The name of the person who filled out the contact form.
    - email (str): The email address of the person.
    - message (str): The message from the contact form.
    """

    # Example: Print the data (In a real app, you might send an email or store it in a database)
    print(f"Received message from {name} ({email}): {message}")

    # Implement the required actions here. For example:
    # - Send an email notification to yourself or a support team.
    # - Store the contact form data in a database for future reference.
    # - Any other necessary processing.

    # Make sure to handle exceptions and errors appropriately.
