from flask import Blueprint, redirect, render_template, request, url_for
from lib.donation_manager import DonationManager

from lib.charity_manager import CharityManager


charity_blueprint = Blueprint('charity_blueprint', __name__)

@charity_blueprint.route('/charities')
def charities():
    all_charities = CharityManager.list_all_charities()
    return render_template('charities.html', charities=all_charities)
