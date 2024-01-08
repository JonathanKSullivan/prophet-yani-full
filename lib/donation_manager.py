from sqlalchemy import func
from model import db, Donation

class DonationManager:
    @staticmethod
    def calculate_total_donations():
        try:
            total = db.session.query(func.sum(Donation.amount)).scalar()
            return total if total is not None else 0
        except Exception as e:
            print("Error calculating total donations:", e)
            return -1
        
    @staticmethod
    def add_donation(user_id, amount, charity_id, service_id, donation_date, donation_type):
        new_donation = Donation(
            user_id=user_id,
            amount=amount,
            charity_id=charity_id,
            service_id=service_id,
            donation_date=donation_date,
            donation_type=donation_type
        )
        db.session.add(new_donation)
        try:
            db.session.commit()
            return new_donation
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_donation_by_id(donation_id):
        return Donation.query.get(donation_id)

    @staticmethod
    def update_donation(donation_id, **kwargs):
        donation = Donation.query.get(donation_id)
        if not donation:
            return None
        for key, value in kwargs.items():
            if hasattr(donation, key):
                setattr(donation, key, value)
        db.session.commit()
        return donation

    @staticmethod
    def delete_donation(donation_id):
        donation = Donation.query.get(donation_id)
        if donation:
            db.session.delete(donation)
            db.session.commit()
            return True
        return False

    @staticmethod
    def list_all_donations():
        return Donation.query.all()
