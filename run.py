from app import createApp
# import looker_sdk
# import os
# from looker_sdk import models40
# config_path = os.path.join(os.path.dirname(__file__), 'looker.ini')
# sdk = looker_sdk.init40(config_path)
app = createApp()
app.secret_key = "socios"
# response = sdk.search_users(email="kauan.toldo@clusterdesign.io")
# Definição da requisição para criar o Embed SSO URL
# sso_embed_params = {
#     "target_url": "https://clusterdesign.cloud.looker.com/embed/extensions/cl_ecommerce_demo_extension_v2::demo_v3/",
#     "session_length": 300,
#     "external_user_id": "1",
#     "first_name": "Fulano",
#     "last_name": "Tal",
#     "group_ids": ["13"]
# }



# Cria a URL de SSO Embed
# response = sdk.create_sso_embed_url(sso_embed_params)
# print(response)
if __name__ == '__main__':
    app.run(debug=True)