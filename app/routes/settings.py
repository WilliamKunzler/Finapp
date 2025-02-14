from flask import Blueprint, jsonify, render_template, request, session

from app.database.db import db

settings = Blueprint('settings', __name__, url_prefix='/settings')

@settings.route('/')
def settings_handler():
    if "user" in session:
        email = session['user']['email']
        userid = db.query('SELECT UserID from usuarios WHERE email = %s', email)
        user_data = session.get("user", {})  # Obtém os dados do usuário na sessão
        user_data["id"] = userid[0]["UserID"]  # Atualiza o ID
        session["user"] = user_data
        infoUser = db.query('SELECT c.userID, c.first_name, t.email, c.last_name, c.date_birth, c.mobile_number, c.image, t.senha FROM details_users c INNER JOIN usuarios t ON c.UserID = t.UserID WHERE t.UserID = %s', userid[0]['UserID'])
        for i in infoUser[0]:
            if infoUser[0][i] == None:
                infoUser[0][i] = ''
        print (infoUser)
    return render_template('index.html', title="settings", infoUser=infoUser)

@settings.route('/update', methods=["POST"])
def update_handler():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    date_birth = data.get('date_birth')
    mobile_number = data.get('mobile_number')
    password = data.get("senha")
    email = data.get("email")
    db.query("UPDATE usuarios SET email = %s, senha = %s WHERE UserID = %s", email, password, session["user"]["id"])
    db.query("UPDATE details_users SET first_name = %s, last_name = %s, date_birth = %s, mobile_number = %s WHERE userID = %s", first_name, last_name, date_birth, mobile_number, session["user"]["id"])
    return jsonify({"status": "success", "message": "Atualização bem sucedida"}), 200