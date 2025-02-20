from flask import Blueprint, jsonify, render_template

from app.database.db import db
from app.routes.home import loadNavbar

transactions = Blueprint('transactions', __name__, url_prefix='/transactions')

@transactions.route('/')
def transactions_handler():

    return loadNavbar('transactions')



@transactions.route('/loadTransactions')
def loadTransactions():
    dados = db.query('SELECT * from saida')
    return jsonify({"status": "success", "data": dados}), 200