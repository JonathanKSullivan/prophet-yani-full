from flask import Blueprint, redirect, render_template, request, url_for
from lib.location_manager import LocationManager

location_blueprint = Blueprint('location_blueprint', __name__)

@location_blueprint.route('/locations')
def locations():
    all_locations = LocationManager.list_all_locations()
    return render_template('locations.html', locations=all_locations)
