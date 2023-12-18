from models import db, Payment
from datetime import datetime

class PaymentManager:
    @staticmethod
    def add_payment(user_id, amount, transaction_id, payment_method, payment_date=None):
        new_payment = Payment(
            user_id=user_id,
            amount=amount,
            transaction_id=transaction_id,
            payment_method=payment_method,
            payment_date=payment_date or datetime.now()
        )
        db.session.add(new_payment)
        try:
            db.session.commit()
            return new_payment
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_payment_by_id(payment_id):
        return Payment.query.get(payment_id)

    @staticmethod
    def update_payment(payment_id, **kwargs):
        payment = Payment.query.get(payment_id)
        if not payment:
            return None
        for key, value in kwargs.items():
            if hasattr(payment, key):
                setattr(payment, key, value)
        db.session.commit()
        return payment

    @staticmethod
    def delete_payment(payment_id):
        payment = Payment.query.get(payment_id)
        if payment:
            db.session.delete(payment)
            db.session.commit()
            return True
        return False

    @staticmethod
    def list_all_payments():
        return Payment.query.all()
