from datetime import datetime
import os
from flask import Blueprint, flash, jsonify, redirect, render_template, request, session, url_for
import stripe
from lib.charity_manager import CharityManager
from lib.donation_manager import DonationManager

donations_blueprint = Blueprint('donations_blueprint', __name__)

# Set Stripe API key from environment variable
stripe.api_key = os.environ.get('STRIPE_TEST_SECRET_KEY')

# Helper function to create Stripe charge
def create_stripe_charge(stripe_token, amount, description):
    return stripe.Charge.create(
        amount=int(amount * 100),  # Convert to cents
        currency='usd',
        description=description,
        source=stripe_token
    )

# Helper function to add donation record
def add_donation_record(user_id, donation_amount, charity_id, donation_type):
    DonationManager.add_donation(
        user_id=user_id, 
        amount=donation_amount, 
        charity_id=charity_id, 
        service_id=None,  # Assuming no service for both routes
        donation_date=datetime.now(), 
        donation_type=donation_type
    )

@donations_blueprint.route('/donations/organization', methods=['GET', 'POST'])
def organization_donations():
    if request.method == 'POST':
        print(request.form)
        print(request)
        try:
            stripe_token = request.form['stripeToken']
            donation_amount = float(request.form['donation-amount'])
            charge = create_stripe_charge(stripe_token, donation_amount, 'Organization Donation')
            user_id = session.get('user_id', None)
            add_donation_record(user_id, donation_amount, None, 'Organization')
            flash('Donation successful. Thank you for your support!', 'success')
        except stripe.error.StripeError as e:
            flash(f'An error occurred: {str(e)}', 'error')
        return redirect(url_for('donations_blueprint.organization_donations'))

    return render_template('organization_donations.html', metadata={}, footer={})

@donations_blueprint.route('/donations/charities', methods=['GET', 'POST'])
def charity_donations():
    if request.method == 'POST':
        print(request.form)
        print(request)
        try:
            stripe_token = request.form.get('stripeToken')
            donation_amount = float(request.form.get('amount'))
            charity_id = request.form.get('charityId')
            
            user_id = session.get('user_id', None)
            charge = create_stripe_charge(stripe_token, donation_amount, f'Donation to Charity ID {charity_id}')
            add_donation_record(user_id, donation_amount, charity_id, 'Charity')

            flash('Donation successful. Thank you for your support!', 'success')
        except stripe.error.StripeError as e:
            flash(f'An error occurred during the donation process: {str(e)}', 'error')

    all_charities = CharityManager.list_all_charities()
    return render_template('charity_donations.html', charities=all_charities, metadata={}, footer={})
