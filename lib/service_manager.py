from models import db, Service

class ServiceManager:
    @staticmethod
    def add_service(name, description, duration, price, image_url, service_type, location_id=None, donation_percentage=0):
        new_service = Service(
            name=name,
            description=description,
            duration=duration,
            price=price,
            image_url=image_url,
            type=service_type,
            location_id=location_id,
            donation_percentage=donation_percentage
        )
        db.session.add(new_service)
        try:
            db.session.commit()
            return new_service
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_service_by_id(service_id):
        return Service.query.get(service_id)

    @staticmethod
    def update_service(service_id, **kwargs):
        service = Service.query.get(service_id)
        if not service:
            return None
        for key, value in kwargs.items():
            if hasattr(service, key):
                setattr(service, key, value)
        db.session.commit()
        return service

    @staticmethod
    def delete_service(service_id):
        service = Service.query.get(service_id)
        if service:
            db.session.delete(service)
            db.session.commit()
            return True
        return False

    @staticmethod
    def list_all_services():
        return Service.query.all()
    
    @staticmethod
    def list_all_services():
        return Service.query.all()
