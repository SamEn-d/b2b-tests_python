import os
import requests
from renlife_b2b_test.policy_calculate_data import read_data_create_data_policy_calculate
from renlife_b2b_test.api.token import api_token

login_b2b = os.getenv('LOGIN_b2b2')
password_b2b = os.getenv('PASSWORD_b2b2')
auth_url = os.getenv('URL_TOKEN')
url = os.getenv('URL_API')
client_id = 'b2b-frontend'
body = 'grant_type=password' + '&client_id=' + client_id + '&username=' + login_b2b + '&password=' + password_b2b;
header_token_type = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}


def print_zapros(print_zapros):
    test_api_token_session = api_token()
    headers_token = {"Authorization": test_api_token_session}
    request = requests.post(url, json=print_zapros, headers=headers_token)
    return request.json()
    # return r.json json.loads(r.text)

def print_file(doc_brief):
    read_data = read_data_create_data_policy_calculate()
    policy = {
        "method": "b2b_get_policy_report_uuid",
        "params": {
            "doc_brief": doc_brief,
            "ids": read_data['ids'],
            "policy_header_id": read_data['policy_header_id'],
            "user_uuid": read_data['uuid']
        }
    }
    return policy