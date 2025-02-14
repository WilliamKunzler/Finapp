import base64
import io
from flask import Blueprint, redirect, render_template, session, url_for

from app.database.db import db

home = Blueprint('home', __name__)


def loadNavbar(rota):
    if 'user' in session:
        email = session['user']['email']
        userid = db.query('SELECT UserID from usuarios WHERE email = %s', email)
        infoUser = db.query('SELECT  c.first_name, c.last_name, c.image  FROM details_users c INNER JOIN usuarios t ON c.UserID = t.UserID WHERE t.UserID = %s', userid[0]['UserID'])
        img_io = io.BytesIO(infoUser[0]['image'])
        img_io.seek(0)
        infoUser[0]['image'] = base64.b64encode(img_io.read()).decode('utf-8')

    if (infoUser[0]['last_name'] == None):
        name = infoUser[0]['first_name']
    
    else:
        name = infoUser[0]['first_name'] + ' ' + infoUser[0]['last_name']
    image = infoUser[0]['image']

    return render_template('index.html', title = rota, nome = name, image = image)


@home.route('/')
def home_handler():
    return redirect(url_for('login.login_handler'))

