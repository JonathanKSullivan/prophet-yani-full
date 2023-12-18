
from flask import Blueprint, redirect, request, render_template, session, flash, url_for
# from flask import Flask, request

from lib.user_manager import UserManager

from data import home_page_content, about_page_content, login_page_content, register_page_content, profile_page_content

from werkzeug.security import generate_password_hash

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        # Process the registration form
        data = request.form
        new_user = UserManager.add_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', '')
        )
        # Redirect to a different page, like login, after successful registration
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
        if user and UserManager.check_password(user.id, password):
            session['user_id'] = user.id  # User is logged in
            return redirect(url_for('user_blueprint.profile'))
        else:
            flash('Invalid username or password')
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
        return redirect(url_for('login'))

    user = UserManager.get_user_by_id(user_id)
    if request.method == 'POST':
        # Update user details here
        user = UserManager.update_user(user_id, **request.form)
    return render_template(
        'profile.html', 
        metadata=profile_page_content["meta"],
        footer=profile_page_content["footer"],
        user=user)

@user_blueprint.route('/change_password', methods=['GET', 'POST'])
def change_password():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('user_blueprint.login'))

    if request.method == 'POST':
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        if UserManager.check_password(user_id, old_password):
            UserManager.update_user(user_id, password_hash=generate_password_hash(new_password))
            flash('Password successfully changed')
            return redirect(url_for('user_blueprint.profile'))
        else:
            flash('Incorrect old password')

    return render_template('change_password.html')

@user_blueprint.route('/password_reset', methods=['GET', 'POST'])
def password_reset():
    if request.method == 'POST':
        email = request.form['email']
        user = UserManager.get_user_by_email(email)
        if user:
            # Send password reset email here
            flash('Password reset email sent')
        else:
            flash('Email not found')
    return render_template('password_reset.html')
