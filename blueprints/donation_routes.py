from flask import Blueprint, redirect, render_template, request, url_for
from lib.donation_manager import DonationManager

donation_blueprint = Blueprint('donations_blueprint', __name__)

@donation_blueprint.route('/donations')
def donations():
    all_donations = DonationManager.list_all_donations()
    return render_template('donations.html', donations=all_donations)
