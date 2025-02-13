
from flask import Flask
import os
from .routes.home import home
from .routes.register import register
from .routes.login import login
from .routes.transactions import transactions
from .routes.settings import settings
from .routes.dashboard import dashboard

def createApp():
    app = Flask(__name__)
    app.register_blueprint(home)
    app.register_blueprint(dashboard)
    app.register_blueprint(register)
    app.register_blueprint(login)
    app.register_blueprint(transactions)
    app.register_blueprint(settings)
    app.secret_key = os.environ.get('SECRET_KEY')
    return app
