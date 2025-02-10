from flask import Blueprint, render_template

transactions = Blueprint('transactions', __name__, url_prefix='/transactions')

@transactions.route('/')
def transactions_handler():
    return render_template('transactions.html')