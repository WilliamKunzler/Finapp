from flask import Blueprint, render_template

login = Blueprint('login', __name__)

@login.route('/login')
def login_handler():
    return render_template('login.html')