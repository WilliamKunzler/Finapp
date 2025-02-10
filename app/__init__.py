
from flask import Flask
import os
from .routes.home import home
from .routes.register import register
from .routes.login import login

def createApp():
    app = Flask(__name__)
    app.register_blueprint(home)
    app.register_blueprint(register)
    app.register_blueprint(login)
    app.secret_key = os.environ.get('SECRET_KEY')
    return app
