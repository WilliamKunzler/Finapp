from flask import Blueprint, render_template

register = Blueprint('register', __name__)

@register.route('/register')
def register_handler():
    return render_template('register.html')