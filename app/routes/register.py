from flask import Blueprint, jsonify, render_template, request

register = Blueprint('register', __name__, url_prefix='/register')


@register.route('/')
def register_handler():
    return render_template('register.html')


@register.route('/addAccount', methods = ['POST'])
def registerUser():
    data = request.get_json()

    # if not data:
    #     return jsonify({"status": "error", "message": "Nenhum dado recebido"}), 400

    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    print(f"Usuário: {username}, Email: {email}, Senha: {password}")

    return jsonify({"status": "success", "message": "Usuário registrado com sucesso"}), 200

