from flask import Blueprint, request
from lib.service_manager import ServiceManager

service_blueprint = Blueprint('service_blueprint', __name__)

@service_blueprint.route('/services')
def services():
    all_services = ServiceManager.list_all_services()
    return render_template('services.html', services=all_services)

@service_blueprint.route('/service/add', methods=['GET', 'POST'])
def add_service():
    if request.method == 'POST':
        # Extract data from form
        name = request.form['name']
        description = request.form['description']
        duration = request.form['duration']
        price = request.form['price']
        image_url = request.form['image_url']
        service_type = request.form['service_type']
        location_id = request.form.get('location_id')
        donation_percentage = request.form.get('donation_percentage', 0)

        # Add service to database
        new_service = ServiceManager.add_service(name, description, duration, price, image_url, service_type, location_id, donation_percentage)
        return redirect(url_for('view_service', service_id=new_service.id))
    
    return render_template('add_service.html')

@service_blueprint.route('/service/edit/<int:service_id>', methods=['GET', 'POST'])
def edit_service(service_id):
    service = ServiceManager.get_service_by_id(service_id)
    if not service:
        return "Service not found", 404

    if request.method == 'POST':
        # Update service details
        updated_fields = {key: request.form[key] for key in request.form}
        ServiceManager.update_service(service_id, **updated_fields)
        return redirect(url_for('view_service', service_id=service_id))

    return render_template('edit_service.html', service=service)

@service_blueprint.route('/service/delete/<int:service_id>', methods=['POST'])
def delete_service(service_id):
    success = ServiceManager.delete_service(service_id)
    if success:
        return redirect(url_for('list_services'))
    else:
        return "Error deleting service", 500

@service_blueprint.route('/service/<int:service_id>')
def view_service(service_id):
    service = ServiceManager.get_service_by_id(service_id)
    if not service:
        return "Service not found", 404

    return render_template('view_service.html', service=service)
