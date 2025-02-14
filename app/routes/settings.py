import base64
from flask import Blueprint, jsonify, render_template, request, session
from PIL import Image
from io import BytesIO
import io
from app.database.db import db

settings = Blueprint('settings', __name__, url_prefix='/settings')

@settings.route('/')
def settings_handler():
    return render_template('index.html', title="settings")


@settings.route('/loadDetails', methods=['GET'])
def loadDetails_handler():
    if "user" in session:
        email = session['user']['email']
        userid = db.query('SELECT UserID from usuarios WHERE email = %s', email)
        user_data = session.get("user", {})  # Obtém os dados do usuário na sessão
        user_data["id"] = userid[0]["UserID"]  # Atualiza o ID
        session["user"] = user_data
        infoUser = db.query('SELECT c.userID, c.first_name, t.email, c.last_name, c.date_birth, c.mobile_number, c.image, t.senha FROM details_users c INNER JOIN usuarios t ON c.UserID = t.UserID WHERE t.UserID = %s', userid[0]['UserID'])
        img_io = io.BytesIO(infoUser[0]['image'])
        img_io.seek(0)
        infoUser[0]['image'] = base64.b64encode(img_io.read()).decode('utf-8')
        print(infoUser)
        for i in infoUser[0]:
            if infoUser[0][i] == None:
                infoUser[0][i] = ''
    return jsonify({"status": "success", "data": infoUser}), 200




@settings.route('/update', methods=["POST"])
def update_handler():
    try:

        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        date_birth = request.form.get('date_birth')
        mobile_number = request.form.get('mobile_number')
        senha = request.form.get('senha')
        image = request.files.get('image')
        if not image:
            db.query("UPDATE details_users SET first_name = %s, last_name = %s, date_birth = %s, mobile_number = %s WHERE userID = %s", first_name, last_name, date_birth, mobile_number, session["user"]["id"])
        else:
            image_blob = process_image(image)
            db.query("UPDATE details_users SET first_name = %s, last_name = %s, date_birth = %s, mobile_number = %s, image = %s WHERE userID = %s", first_name, last_name, date_birth, mobile_number, image_blob, session["user"]["id"])
        
        db.query("UPDATE usuarios SET email = %s, senha = %s WHERE UserID = %s", email, senha, session["user"]["id"])
        
    
        return jsonify({"message": "Dados atualizados com sucesso!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def process_image(image, max_size=(800, 800), quality=70):
    img = Image.open(image)
    
    # Converte para RGB caso seja PNG ou outro formato com transparência
    img = img.convert("RGB")

    # Redimensiona a imagem mantendo a proporção
    img.thumbnail(max_size)

    # Salva a imagem em um buffer
    img_io = io.BytesIO()
    img.save(img_io, format="JPEG", quality=quality)  # Ajusta a qualidade para reduzir o tamanho
    img_io.seek(0)
    
    return img_io.read()  # Retorna a imagem como blob