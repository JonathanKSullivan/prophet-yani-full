from sqlalchemy import func
from model import db, Location

class LocationManager:
    @staticmethod
    def count_locations_by_country():
        try:
            country_counts = (db.session.query(Location.country, func.count(Location.id))
                                      .group_by(Location.country)
                                      .all())
            return len(country_counts)
        except Exception as e:
            print("Error counting locations by country:", e)
            return -1

    @staticmethod
    def add_location(address, city, state, country, zip_code, location_type):
        new_location = Location(
            address=address,
            city=city,
            state=state,
            country=country,
            zip_code=zip_code,
            location_type=location_type
        )
        db.session.add(new_location)
        try:
            db.session.commit()
            return new_location
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_location_by_id(location_id):
        return Location.query.get(location_id)

    @staticmethod
    def update_location(location_id, **kwargs):
        location = Location.query.get(location_id)
        if not location:
            return None
        for key, value in kwargs.items():
            if hasattr(location, key):
                setattr(location, key, value)
        db.session.commit()
        return location

    @staticmethod
    def delete_location(location_id):
        location = Location.query.get(location_id)
        if location:
            db.session.delete(location)
            db.session.commit()
            return True
        return False

    @staticmethod
    def list_all_locations():
        return Location.query.all()
