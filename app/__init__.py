
from flask import Flask
import os
from .routes.home import home



def createApp():
    app = Flask(__name__)
    app.register_blueprint(home)
    app.secret_key = os.environ.get('SECRET_KEY')
    return app
