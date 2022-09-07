import os

import allure
import requests

# from tests.python.b2b2.investor.api.test_api_vznos import auth_url, body, header_token_type

login_b2b = os.getenv('LOGIN_b2b2')
password_b2b = os.getenv('PASSWORD_b2b2')
auth_url = os.getenv('URL_TOKEN')
url = os.getenv('URL_API')
client_id = 'b2b-frontend'
body = 'grant_type=password' + '&client_id=' + client_id + '&username=' + login_b2b + '&password=' + password_b2b;
header_token_type = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}

@allure.parent_suite('API Проверка получения токена')
@allure.suite('API получения токена')
@allure.title(f"API получения токена")
def test_api_token():
    token_request = requests.post(auth_url, data=body, headers=header_token_type)
    token_request_json = token_request.json()
    access_token = token_request_json['access_token']
    return access_token

# policy_calculate_zapros = policy_calculate_zapros_api(
#     breef='INVESTOR_LUMP_4.1_BASE3_113_TM_CB_UBRIR',
#     b2b_user_uuid = 'e4bf4d87-c500-424f-bed6-ca2355dab7a1',
#     birth_date='2000-10-10',
#     ag_contract_num= 91061,
#     base_sum= 30000,
#     bso_series = 487,
#     payment_terms= 'Единовременно',
#     policy_period_brief= '3_YEARS',
#     product_brief= 'INVESTOR_LUMP_4.1_BASE3_113_TM_CB',
# )
# policy_calculate_json = json.loads(policy_calculate_zapros)