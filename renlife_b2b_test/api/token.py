import os

import requests


login_b2b = os.getenv('LOGIN_b2b2')
password_b2b = os.getenv('PASSWORD_b2b2')
auth_url = os.getenv('URL_TOKEN')
client_id = os.getenv('CLIENT_ID')

body = 'grant_type=password' + '&client_id=' + client_id + '&username=' + login_b2b + '&password=' + password_b2b;
header_token_type = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}

def api_token():
    token_request = requests.post(auth_url, data=body, headers=header_token_type)
    token_request_json = token_request.json()
    access_token = token_request_json['access_token']
    return access_token
