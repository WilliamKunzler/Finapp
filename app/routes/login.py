from flask import Blueprint, jsonify, render_template, request
from app.database.db import db

login = Blueprint('login', __name__, url_prefix='/login')

@login.route('/')
def login_handler():
    return render_template('login.html')

@login.route('/entrance', methods = ['POST'])
def entranceDashboard():
    data = request.get_json()
    password = data.get("password")
    email = data.get("email")

    verify = db.query('SELECT COUNT(*) AS user_exists FROM usuarios WHERE email = %s AND senha = %s',email, password) 

    print(verify)

    if verify[0]['user_exists'] == 1:
        return jsonify({"status": "success", "message": "Login bem sucedido"}), 200
    else:
        return jsonify({"status": "error", "message": "Email e/ou senha incorretos"}), 400



    
