from flask import Blueprint, request, render_template
from lib.payment_manager import PaymentManager

payment_blueprint = Blueprint('payment_blueprint', __name__)

@payment_blueprint.route('/payments')
def payments():
    all_payments = PaymentManager.list_all_payments()
    return render_template('payments.html', payments=all_payments)
