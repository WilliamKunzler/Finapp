
from flask import Blueprint, render_template, session, url_for

from app.routes.home import loadNavbar


dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard.route('/')
def dashboard_handler():
    return loadNavbar('dashboard')