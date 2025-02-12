from flask import Blueprint, jsonify, render_template, request

from app.database import db

login = Blueprint('login', __name__, url_prefix='/login')

@login.route('/')
def login_handler():
    return render_template('login.html')

@login.route('/entrance', methods = ['POST'])
def entranceDashboard():
    pass

    
