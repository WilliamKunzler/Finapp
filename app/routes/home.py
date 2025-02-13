from flask import Blueprint, redirect, render_template, url_for

home = Blueprint('home', __name__)


@home.route('/')
def home_handler():
    return redirect(url_for('login.login_handler'))

