from flask import Blueprint, jsonify, render_template, request, session
from app.database.db import db
import looker_sdk
import os
import json
from looker_sdk import models40
config_path = os.path.join(os.path.dirname(__file__), '../../looker.ini')
sdk = looker_sdk.init40(config_path)

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

    if verify[0]['user_exists'] == 1:
        username = {"email": email, "password": password, "id": None}
        session["user"] = username

        user = db.query('SELECT UserID,nome FROM usuarios WHERE email = %s', email)

        temp = None
        if (user[0]["UserID"] == 1):
            temp = "13"
        else:
            temp = "9"

        sso_embed_params = {
            # "target_url": "https://clusterdesign.cloud.looker.com/embed/extensions/cl_ecommerce_demo_extension_v2::demo_v3/",
            # "target_url": "https://clusterdesign.cloud.looker.com/embed/extensions/cl_ecommerce_demo_extension_v2::demo_v3/",
            "session_length": 300,
            "force_logout_login": False,
            "external_user_id": str(user[0]["UserID"]),
            "first_name": user[0]["nome"],
            # "permissions": ["access_data", "see_looks", "see_dashboards", "manage_models"],
            # "models": ["looker_ecommerce_sandbox", "cl_ecommerce_extension_demo_v2", "unico_poc"],
            "group_ids": [temp],
            # "user_attributes": {}
        }

        response = sdk.acquire_embed_cookieless_session(models40.EmbedCookielessSessionAcquire(**sso_embed_params))

        print(sso_embed_params)
        # response = sdk.create_sso_embed_url(models40.EmbedSsoParams(**sso_embed_params))
        print(response)

        # return jsonify({"status": "success", "message": "Login bem sucedido", "embed_url": response.url}), 200
        return jsonify({"status": "success", "message": "Login bem sucedido", "authentication_token": response.authentication_token}), 200
    
    else:
        return jsonify({"status": "error", "message": "Email e/ou senha incorretos"}), 400






# teste = {
#             "session_length": 300,
#             "force_logout_login": false,
#             "external_user_id": "1",
#             "first_name": "teste",
#             "group_ids": ["13"],
#         }