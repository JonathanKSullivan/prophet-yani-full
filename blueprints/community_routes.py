from flask import Blueprint, render_template

# Define the Community Blueprint
community_blueprint = Blueprint('community_blueprint', __name__)

@community_blueprint.route('/')
def community():
    # This route will display a "Coming Soon" page for the community section
    return render_template('community_coming_soon.html',
                           metadata={},
                           footer={}
                           )