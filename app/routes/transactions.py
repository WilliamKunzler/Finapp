from flask import Blueprint, render_template

from app.routes.home import loadNavbar

transactions = Blueprint('transactions', __name__, url_prefix='/transactions')

@transactions.route('/')
def transactions_handler():
    return loadNavbar('transactions')