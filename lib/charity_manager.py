from models import db, Charity

class CharityManager:
    @staticmethod
    def add_charity(name, description, image_url, location_id):
        new_charity = Charity(
            name=name,
            description=description,
            image_url=image_url,
            location_id=location_id
        )
        db.session.add(new_charity)
        try:
            db.session.commit()
            return new_charity
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_charity_by_id(charity_id):
        return Charity.query.get(charity_id)

    @staticmethod
    def update_charity(charity_id, **kwargs):
        charity = Charity.query.get(charity_id)
        if not charity:
            return None
        for key, value in kwargs.items():
            if hasattr(charity, key):
                setattr(charity, key, value)
        db.session.commit()
        return charity

    @staticmethod
    def delete_charity(charity_id):
        charity = Charity.query.get(charity_id)
        if charity:
            db.session.delete(charity)
            db.session.commit()
            return True
        return False

    @staticmethod
    def list_all_charities():
        return Charity.query.all()
