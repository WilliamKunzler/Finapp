from flask import Blueprint, jsonify, render_template, request, url_for
from app.database.db import db  

register = Blueprint('register', __name__, url_prefix='/register')


@register.route('/')
def register_handler():
    return render_template('register.html')


@register.route('/addAccount', methods = ['POST'])
def registerUser():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    verify = db.query('SELECT COUNT(*) AS user_exists FROM usuarios WHERE email = %s',email, ) 

    if verify[0]['user_exists'] == 0:
        db.query('INSERT INTO usuarios VALUES (%s, %s, %s, %s)','default', email, username, password)
        # print(f"Usuário: {username}, Email: {email}, Senha: {password}")
        return jsonify({"status": "success", "message": "Usuário registrado com sucesso"}), 200

    else:
        return jsonify({"status": "error", "message": "Usuário já existe"}), 400


    

