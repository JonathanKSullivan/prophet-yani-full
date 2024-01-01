from model import db, Payment
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
    def get_payments_by_user(user_id):
        return Payment.query.filter_by(user_id=user_id).all()

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

    @staticmethod
    def summarize_payments(user_id=None):
        query = Payment.query
        if user_id:
            query = query.filter_by(user_id=user_id)
        total_amount = query.with_entities(db.func.sum(Payment.amount)).scalar()
        return total_amount

    @staticmethod
    def filter_payments(start_date=None, end_date=None, min_amount=None, max_amount=None):
        query = Payment.query
        if start_date:
            query = query.filter(Payment.payment_date >= start_date)
        if end_date:
            query = query.filter(Payment.payment_date <= end_date)
        if min_amount:
            query = query.filter(Payment.amount >= min_amount)
        if max_amount:
            query = query.filter(Payment.amount <= max_amount)
        return query.all()
