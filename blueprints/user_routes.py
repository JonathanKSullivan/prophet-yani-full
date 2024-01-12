import uuid
from flask import current_app
from flask import Blueprint, redirect, request, render_template, session, flash, url_for
from werkzeug.utils import secure_filename

from itsdangerous import SignatureExpired, URLSafeTimedSerializer
from lib.location_manager import LocationManager
# from flask import Flask, request

from lib.user_manager import UserManager

from data import home_page_content, about_page_content, login_page_content, register_page_content, profile_page_content

from werkzeug.security import generate_password_hash

from utils import send_email, send_username_recovery_email

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        # Process the registration form
        data = request.form
        email = data['email']

        # Check if a user with this email already exists
        existing_user = UserManager.get_user_by_email(email)
        if existing_user:
            flash('An account with this email already exists.', 'error')
            return redirect(url_for('user_blueprint.register_user'))

        # Continue with the user creation process
        country_code = data.get('country')
        new_user = UserManager.add_user(
            username=data['username'],
            email=email,
            password=data['password'],
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', ''),
            country=country_code
        )

        # Generate a token for email confirmation
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        token = serializer.dumps(new_user.email, salt=current_app.config['SECURITY_PASSWORD_SALT'])

        # Construct the confirm URL
        confirm_url = url_for('general_blueprint.confirm_email', token=token, _external=True)

        # Send the confirmation email
        html = render_template('email/activate.html', confirm_url=confirm_url)
        send_email(new_user.email, 'Confirm Your Email', html)

        flash('A confirmation email has been sent to your email address.', 'info')
        return redirect(url_for('user_blueprint.login'))

    # Display the registration form for GET request
    return render_template(
        'register.html', 
        metadata=register_page_content["meta"], 
        footer=register_page_content["footer"]
    )

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = UserManager.get_user_by_username(username)

        if user:
            if not user.confirmed:
                flash('Please confirm your email address before logging in.', 'warning')
                return redirect(url_for('user_blueprint.login'))

            if UserManager.check_password(user.id, password):
                session['user_id'] = user.id  # User is logged in
                return redirect(url_for('user_blueprint.profile'))
            else:
                flash('Invalid username or password', 'error')
        else:
            flash('Invalid username or password', 'error')

    return render_template(
        'login.html',
        metadata=login_page_content["meta"], 
        footer=login_page_content["footer"]
    )

@user_blueprint.route('/logout')
def logout():
    session.pop('user_id', None)  # User is logged out
    return redirect(url_for('user_blueprint.login'))

@user_blueprint.route('/profile', methods=['GET', 'POST'])
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('user_blueprint.login'))

    user = UserManager.get_user_by_id(user_id)
    if request.method == 'POST':
        user_data = {
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'bio': request.form.get('bio'),
            'country': request.form.get('country'),
        }

        # Handle profile image upload
        profile_image = request.files.get('profile_image')
        if profile_image:
            folder_name = 'profile_images/'  # Specify the folder name
            bucket_name = 'prophet-yani-assests'  # Replace with your actual bucket name

            # Generate a unique file name
            filename = secure_filename(profile_image.filename)
            unique_filename = str(uuid.uuid4()) + "_" + filename

            # Combine folder name and unique filename to create the S3 object key
            s3_object_key = folder_name + unique_filename

            image_url = UserManager.upload_to_s3(profile_image, bucket_name, s3_object_key)
            if image_url:
                # Update user with new profile image URL
                user_data['profile_image_url'] = image_url
                # Update user in the database
                UserManager.update_user(user_id, user_data)


        # Check and update password if new_password field is provided
        new_password = request.form.get('new_password')
        if new_password:
            UserManager.update_password(user_id, new_password)
            flash('Your password has been updated.', 'success')

        # Refresh user data after updates
        user = UserManager.get_user_by_id(user_id)

        flash('Profile updated successfully.', 'success')

    return render_template(
        'profile.html', 
        metadata=profile_page_content["meta"],
        footer=profile_page_content["footer"],
        user=user
    )

@user_blueprint.route('/password_reset', methods=['GET', 'POST'])
def password_reset():
    if request.method == 'POST':
        email = request.form['email']
        user = UserManager.get_user_by_email(email)
        if user:
            # Generate a token for password reset
            serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
            token = serializer.dumps(email, salt=current_app.config['SECURITY_PASSWORD_SALT'])

            # Construct the password reset URL
            reset_url = url_for('user_blueprint.reset_password_token', token=token, _external=True)

            # Send the password reset email
            html = render_template('email/reset_password.html', reset_url=reset_url)
            send_email(email, 'Password Reset Request', html)

            flash('A password reset email has been sent.', 'info')
        else:
            flash('Email not found', 'error')

    return render_template('password_reset.html',
                           metadata=profile_page_content["meta"],
                            footer=profile_page_content["footer"]
                            )

@user_blueprint.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password_token(token):
    try:
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        email = serializer.loads(
            token,
            salt=current_app.config['SECURITY_PASSWORD_SALT'],
            max_age=3600
        )
    except SignatureExpired:
        flash('The password reset link has expired.', 'error')
        return redirect(url_for('user_blueprint.password_reset'))

    user = UserManager.get_user_by_email(email)
    if user is None:
        flash('Invalid password reset token.', 'error')
        return redirect(url_for('user_blueprint.login'))

    if request.method == 'POST':
        new_password = request.form['password']
        # Ensure password hashing
        hashed_password = generate_password_hash(new_password)
        UserManager.update_password(user.id, new_password)
        flash('Your password has been updated.', 'success')
        return redirect(url_for('user_blueprint.login'))

    return render_template('reset_password_with_token.html', token=token)

@user_blueprint.route('/recover_username', methods=['GET', 'POST'])
def recover_username():
    if request.method == 'POST':
        email = request.form['email']
        user = UserManager.get_user_by_email(email)
        if user:
            # Send an email with the username
            send_username_recovery_email(user.email, user.username)
            flash('A recovery email with your username has been sent.', 'info')
        else:
            flash('No account found with that email.', 'error')
    return render_template('recover_username.html',
                           metadata=profile_page_content["meta"],
                           footer=profile_page_content["footer"])
