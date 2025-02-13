from flask import Blueprint, redirect, render_template, url_for


dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard.route('/')
def dashboard_handler():
    return render_template('index.html', title="dashboard")