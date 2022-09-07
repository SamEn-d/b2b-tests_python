import json
import os
import allure
import requests

from renlife_b2b_test.api.policy_calculate_api import policy_calculate_zapros_api
from renlife_b2b_test.jwt_decode import jwt_decode
from renlife_b2b_test.api.token import api_token
from renlife_b2b_test.api.policy_update_info_api import policy_update_info_api
from renlife_b2b_test.policy_calculate_data import create_data_policy_calculate

min_vznos = os.getenv('MIN_VZNOS_UBRIR')
avg_vznos = os.getenv('AVG_VZNOS_UBRIR')
max_vznos = os.getenv('MAX_VZNOS_UBRIR')

min_vozrast = os.getenv('MIN_VOZRAST_UBRIR')
max_vozrast = os.getenv('MAX_VOZRAST_UBRIR')

url = os.getenv('URL_API')

policy_calculate_zapros = policy_calculate_zapros_api(
    breef='INVESTOR_LUMP_4.1_BASE3_113_TM_CB_UBRIR',
    b2b_user_uuid = 'e4bf4d87-c500-424f-bed6-ca2355dab7a1',
    birth_date='2000-10-10',
    ag_contract_num= 91061,
    base_sum= 30000,
    bso_series = 487,
    payment_terms= 'Единовременно',
    policy_period_brief= '3_YEARS',
    product_brief= 'INVESTOR_LUMP_4.1_BASE3_113_TM_CB',
)
policy_calculate_json = json.loads(policy_calculate_zapros)

@allure.parent_suite('API Создание ДС')
@allure.suite('API Создание ДС')
@allure.title(f"API policy_calculate + policy_update_info")
def test_policy_calculate_api():
    test_api_token_session = api_token()
    headers_token = {"Authorization": test_api_token_session}
    uuid = jwt_decode(test_api_token_session)
    with allure.step(f'Создаём договор'):
        response = requests.post(url, json=policy_calculate_json, headers=headers_token)
        policy_calculate = response.json()
        ids = policy_calculate['result']['policy']['ids']
        with allure.step(f'Создался договор ID: {ids}'):
            policy_header_id = policy_calculate['result']['policy']['policy_header_id']
            asset_id = policy_calculate['result']['insured'][0]['asset_id']

    with allure.step(f'Создаём файл с данными договора договор ID: {ids}'):
        create_data_policy_calculate(ids=ids, policy_header_id=policy_header_id, uuid=uuid)

    with allure.step(f'Обновляем персональные данные в ДС: {ids}'):
        policy_update_info = policy_update_info_api( ids=ids, policy_header_id=policy_header_id, asset_id=asset_id)
        r_policy_update_info = requests.post(url,
            json=policy_update_info,
            headers=headers_token)
        assertion = r_policy_update_info.json()
    assert assertion['result']['insured'][0]['asset_id'] == asset_id


