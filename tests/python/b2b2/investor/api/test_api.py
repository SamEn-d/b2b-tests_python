import os
import datetime
import allure
import requests
import json
from renlife_b2b_test.api.policy_calculate_api import policy_calculate_zapros_api
from renlife_b2b_test.api.policy_update_info_api import policy_update_info_api
from allure_commons.types import AttachmentType
from renlife_b2b_test.jwt_decode import jwt_decode
from renlife_b2b_test.policy_calculate_data import create_data_policy_calculate, read_data_create_data_policy_calculate

login_b2b = os.getenv('LOGIN_b2b2')
password_b2b = os.getenv('PASSWORD_b2b2')
auth_url = 'https://auth.cloud-test.renlife.com/auth/realms/test/protocol/openid-connect/token'
client_id = 'b2b-frontend'
body = 'grant_type=password' + '&client_id=' + client_id + '&username=' + login_b2b + '&password=' + password_b2b;
header_token_type = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}

min_vznos = 30000
avg_vznos = 1500000
max_vznos = 50000000

min_vozrast = 18
max_vozrast = 85

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
    start_date= '2022-08-15'
)
policy_calculate_json = json.loads(policy_calculate_zapros)

@allure.parent_suite('API Проверка получения токена')
@allure.suite('API получения токена')
@allure.title(f"API получения токена")
def test_api_token():
    token_request = requests.post(auth_url, data=body, headers=header_token_type)
    token_request_json = json.loads(token_request.text)
    access_token = token_request_json['access_token']
    return access_token

@allure.parent_suite('API Создание ДС')
@allure.suite('API Создание ДС')
@allure.title(f"API policy_calculate + policy_update_info")
def test_policy_calculate_api():
    test_api_token_session = test_api_token()
    headers_token = {"Authorization": test_api_token_session}
    uuid = jwt_decode(test_api_token_session)
    with allure.step(f'Создаём договор'):
        r = requests.post('https://gateway.cloud-test.renlife.com/api/v1/b2b/rpc', json=(policy_calculate_json), headers=headers_token)
        # print(r.text)
        policy_calculate = json.loads(r.text)
        ids = policy_calculate['result']['policy']['ids']
        with allure.step(f'Создался договор ID: {ids}'):
            policy_header_id = policy_calculate['result']['policy']['policy_header_id']
            asset_id = policy_calculate['result']['insured'][0]['asset_id']
        create_data_policy_calculate(ids=ids, policy_header_id=policy_header_id, uuid=uuid)

    with allure.step(f'Обновляем персональные данные в ДС: {ids}'):
        policy_update_info = policy_update_info_api(birth_date='2000-10-10', ids=ids, policy_header_id=policy_header_id, asset_id=asset_id)
        r_policy_update_info = requests.post(
            'https://gateway.cloud-test.renlife.com/api/v1/b2b/rpc',
            json=(policy_update_info),
            headers=headers_token)
        assertion = json.loads(r_policy_update_info.text)
    assert assertion['result']['insured'][0]['asset_id'] == asset_id
    return {'policy_header_id': policy_header_id, 'ids': ids, 'uuid': uuid}




''' _________ VZNOS ________'''
def vznos_policy_calculate_zapros_api(base_summa, dtp_risk_15kk):
    vznos_policy_calculate_zapros_api = policy_calculate_zapros_api(dtp_risk=dtp_risk_15kk,
                                                                    breef='INVESTOR_LUMP_4.1_BASE3_113_TM_CB_UBRIR',
                                                                    birth_date='2000-10-10', ag_contract_num=91061,
                                                                    base_sum=base_summa, bso_series=487,
                                                                    payment_terms='Единовременно',
                                                                    policy_period_brief='3_YEARS',
                                                                    product_brief='INVESTOR_LUMP_4.1_BASE3_113_TM_CB',
                                                                    start_date='2022-08-15',
                                                                    calc_only='YES', save_policy='NO')
    return vznos_policy_calculate_zapros_api

def policy_calculate_vznos(zapros_summa):
    headers_token = {"Authorization": test_api_token()}
    r = requests.post(
        'https://gateway.cloud-test.renlife.com/api/v1/b2b/rpc',
        json=(zapros_summa),
        headers=headers_token)
    allure.attach(r.text, 'page_source', AttachmentType.HTML, '.html')
    print(r.text)
    return r.text

min_vznos_api = json.loads(vznos_policy_calculate_zapros_api(min_vznos, dtp_risk_15kk=0))
min_vznos_api_minus_001 = json.loads(vznos_policy_calculate_zapros_api(min_vznos-0.01, dtp_risk_15kk=0))
min_vznos_api_plus_001 = json.loads(vznos_policy_calculate_zapros_api(min_vznos+0.01, dtp_risk_15kk=0))

max_vznos_api = json.loads(vznos_policy_calculate_zapros_api(max_vznos, dtp_risk_15kk=1))
max_vznos_api_minus_001 = json.loads(vznos_policy_calculate_zapros_api(max_vznos-0.01, dtp_risk_15kk=1))
max_vznos_api_plus_001 = json.loads(vznos_policy_calculate_zapros_api(max_vznos+0.01, dtp_risk_15kk=1))


avg_vznos_api = json.loads(vznos_policy_calculate_zapros_api(avg_vznos, dtp_risk_15kk=0))
avg_vznos_api_minus_1_risk_off = json.loads(vznos_policy_calculate_zapros_api(avg_vznos-1, dtp_risk_15kk=0))
avg_vznos_api_plus_1_risk_off = json.loads(vznos_policy_calculate_zapros_api(avg_vznos+1, dtp_risk_15kk=0))

avg_vznos_api_risk_on = json.loads(vznos_policy_calculate_zapros_api(avg_vznos, dtp_risk_15kk=1))
avg_vznos_api_minus_1_risk_on = json.loads(vznos_policy_calculate_zapros_api(avg_vznos-1, dtp_risk_15kk=1))
avg_vznos_api_plus_1_risk_on = json.loads(vznos_policy_calculate_zapros_api(avg_vznos+1, dtp_risk_15kk=1))

''' MIN VZNOS '''
@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка минимального взноса')
@allure.title(f"API проверка мнимального взноса {min_vznos}")
def test_policy_calculate_min_vznos():
    with allure.step(f'Проверка минимального взноса {min_vznos}'):
        # policy_calculate_vznos(min_vznos_api)
        assertion = json.loads(policy_calculate_vznos(min_vznos_api))
        assert assertion['result']['insured'][0]['fee'] == min_vznos

@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка минимального взноса')
@allure.title(f"API проверка мнимального взноса {min_vznos} минус 1 копейка")
def test_policy_calculate_min_vznos_api_minus_001():
    with allure.step(f'Проверка минимального взноса {min_vznos}-0.01'):
        # policy_calculate_vznos(min_vznos_api_minus_001)
        assertion = json.loads(policy_calculate_vznos(min_vznos_api_minus_001))
        assert assertion['error']['data']['status'] == 'ERROR'

@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка минимального взноса')
@allure.title(f"API проверка мнимального взноса {min_vznos} плюс 1 копейка")
def test_policy_calculate_min_vznos_api_plus_001():
    with allure.step(f'Проверка минимального взноса {min_vznos}+0.01'):
        # policy_calculate_vznos(min_vznos_api_plus_001)
        assertion = json.loads(policy_calculate_vznos(min_vznos_api_plus_001))
        assert assertion['result']['insured'][0]['fee'] == min_vznos+0.01

''' MAX VZNOS '''
@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка максимального взноса')
@allure.title(f"API проверка максимального взноса {min_vznos}")
def test_policy_calculate_max_vznos():
    with allure.step(f'Проверка максимального взноса {max_vznos}'):
        # policy_calculate_vznos(max_vznos_api)
        assertion = json.loads(policy_calculate_vznos(max_vznos_api))
        assert assertion['result']['insured'][0]['fee'] == max_vznos

@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка максимального взноса')
@allure.title(f"API проверка максимального взноса {min_vznos} -1 копейка")
def test_policy_calculate_max_vznos_api_minus_001():
    with allure.step(f'Проверка максимального взноса {max_vznos}-0.01'):
        # policy_calculate_vznos(max_vznos_api_minus_001)
        assertion = json.loads(policy_calculate_vznos(max_vznos_api_minus_001))
        assert assertion['result']['insured'][0]['fee'] == max_vznos-0.01

@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка максимального взноса')
@allure.title(f"API проверка максимального взноса {min_vznos} +1 копейка")
def test_policy_calculate_max_vznos_api_plus_001():
    with allure.step(f'Проверка максимального взноса {max_vznos}+0.01'):
        # policy_calculate_vznos(max_vznos_api_plus_001)
        assertion = json.loads(policy_calculate_vznos(max_vznos_api_plus_001))
        assert assertion['error']['data']['status'] == 'ERROR'

''' AVG VZNOS '''
@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка среднего взноса')
@allure.title(f"API проверка среднего взноса {avg_vznos} без риска")
def test_policy_calculate_avg_vznos():
    with allure.step(f'Проверка среднего взноса БЕЗ риска {avg_vznos}'):
        # policy_calculate_vznos(avg_vznos_api)
        assertion = json.loads(policy_calculate_vznos(avg_vznos_api))
        assert assertion['error']['data']['status'] == 'ERROR'

@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка среднего взноса')
@allure.title(f"API проверка среднего взноса {avg_vznos} -1 без риска")
def test_policy_calculate_avg_vznos_api_minus_1_risk_off():
    with allure.step(f'Проверка среднего взноса БЕЗ риска {avg_vznos}-1'):
        # policy_calculate_vznos(avg_vznos_api_minus_1_risk_off)
        assertion = json.loads(policy_calculate_vznos(avg_vznos_api_minus_1_risk_off))
        assert assertion['result']['insured'][0]['fee'] == avg_vznos - 1

@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка среднего взноса')
@allure.title(f"API проверка среднего взноса {avg_vznos} +1 без риска")
def test_policy_calculate_avg_vznos_api_plus_1_risk_off():
    with allure.step(f'Проверка среднего взноса БЕЗ риска {avg_vznos}+1'):
        # policy_calculate_vznos(avg_vznos_api_plus_1_risk_off)
        assertion = json.loads(policy_calculate_vznos(avg_vznos_api_plus_1_risk_off))
        assert assertion['error']['data']['status'] == 'ERROR'

@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка среднего взноса')
@allure.title(f"API проверка среднего взноса {avg_vznos} с риском")
def test_policy_calculate_avg_vznos_api_risk_on():
    with allure.step(f'Проверка среднего взноса C риском {avg_vznos}'):
        # policy_calculate_vznos(avg_vznos_api_risk_on)
        assertion = json.loads(policy_calculate_vznos(avg_vznos_api_risk_on))
        assert assertion['result']['insured'][0]['fee'] == avg_vznos

@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка среднего взноса')
@allure.title(f"API проверка среднего взноса {avg_vznos} -1 с риском")
def test_policy_calculate_avg_vznos_api_minus_1_risk_on():
    with allure.step(f'Проверка среднего взноса C риском {avg_vznos}-1'):
        # policy_calculate_vznos(avg_vznos_api_minus_1_risk_on)
        assertion = json.loads(policy_calculate_vznos(avg_vznos_api_minus_1_risk_on))
        assert assertion['error']['data']['status'] == 'ERROR'

@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка среднего взноса')
@allure.title(f"API проверка среднего взноса {avg_vznos} +1 с риском")
def test_policy_calculate_avg_vznos_api_plus_1_risk_on():
    with allure.step(f'Проверка среднего взноса C риском {avg_vznos}+1'):
        policy_calculate_vznos(avg_vznos_api_plus_1_risk_on)
        assertion = json.loads(policy_calculate_vznos(avg_vznos_api_plus_1_risk_on))
        assert assertion['result']['insured'][0]['fee'] == avg_vznos + 1

''' __________ AGE __________ '''
date = datetime.date.today()
year = date.year
month = date.month
if month < 10:
    month = str(0) + str(month)

day = date.day
if day < 10:
    day = str(0) + str(day)

def api_age(y:int = 0, d:int = 0):
    age = str(year-y) + '-' + str(month) + '-' + str(day+d)
    # print(age)
    return age



def zaros_policy_calculate_age(birth_date):
    policy_calculate_age = policy_calculate_zapros_api(dtp_risk=0,
                                                                    breef='INVESTOR_LUMP_4.1_BASE3_113_TM_CB_UBRIR',
                                                                    birth_date=birth_date, ag_contract_num=91061,
                                                                    base_sum=100000, bso_series=487,
                                                                    payment_terms='Единовременно',
                                                                    policy_period_brief='3_YEARS',
                                                                    product_brief='INVESTOR_LUMP_4.1_BASE3_113_TM_CB',
                                                                    start_date='2022-08-15',
                                                                    calc_only='YES', save_policy='NO')
    return policy_calculate_age



def policy_calculate_age(zapros_age):
    headers_token = {"Authorization": test_api_token()}
    r = requests.post(
        'https://gateway.cloud-test.renlife.com/api/v1/b2b/rpc',
        json=zapros_age,
        headers=headers_token)
    print(r.text)
    return r.text


min_age_api = json.loads(zaros_policy_calculate_age(api_age(y=min_vozrast, d=0)))
min_age_minus_1d_api = json.loads(zaros_policy_calculate_age(api_age(y=min_vozrast, d=-1)))
min_age_plus_1d_api = json.loads(zaros_policy_calculate_age(api_age(y=min_vozrast, d=+1)))



''' Min age '''
@allure.parent_suite('API проверка возраста')
@allure.suite('API проверка минимального возраста')
@allure.title(f"API проверка минимального возраста {min_vozrast}")
def test_policy_calculate_min_age():
    with allure.step(f'Проверка минимального возраста {min_vozrast}'):
        assertion = json.loads(policy_calculate_age(min_age_api))
        assert assertion['result']['insured'][0]['person_info']['birth_date'] == api_age(y=min_vozrast, d=0) + 'T00:00:00'

@allure.parent_suite('API проверка возраста')
@allure.suite('API проверка минимального возраста')
@allure.title(f"API проверка минимального возраста {min_vozrast} -1 день")
def test_policy_calculate_min_age_minus_1d_age():
    with allure.step(f'Проверка минимального возраста {min_vozrast} -1 день'):
        assertion = json.loads(policy_calculate_age(min_age_minus_1d_api))
        assert assertion['result']['insured'][0]['person_info']['birth_date'] == api_age(y=min_vozrast, d=-1) + 'T00:00:00'


@allure.parent_suite('API проверка возраста')
@allure.suite('API проверка минимального возраста')
@allure.title(f"API проверка минимального возраста {min_vozrast} +1 день")
def test_policy_calculate_min_age_plus_1d_age():
    with allure.step(f'Проверка минимального возраста {min_vozrast} +1 день'):
        assertion = json.loads(policy_calculate_age(min_age_plus_1d_api))
        assert assertion['error']['data']['status'] == 'ERROR'

max_age_api = json.loads(zaros_policy_calculate_age(api_age(y=max_vozrast + 1, d=0)))
max_age_minus_1d_api = json.loads(zaros_policy_calculate_age(api_age(y=max_vozrast + 1, d=-1)))
max_age_plus_1d_api = json.loads(zaros_policy_calculate_age(api_age(y=max_vozrast + 1, d=+1)))
''' Max age '''
@allure.parent_suite('API проверка возраста')
@allure.suite('API проверка максимального возраста')
@allure.title(f"API проверка максимального возраста {max_vozrast}")
def test_policy_calculate_max_age():
    with allure.step(f'Проверка максимального возраста {max_vozrast}'):
        assertion = json.loads(policy_calculate_age(max_age_api))
        assert assertion['result']['insured'][0]['person_info']['birth_date'] == api_age(y=max_vozrast + 1, d=0) + 'T00:00:00'

@allure.parent_suite('API проверка возраста')
@allure.suite('API проверка максимального возраста')
@allure.title(f"API проверка максимального возраста {max_vozrast} -1 день")
def test_policy_calculate_max_age_minus_1d_age():
    with allure.step(f'Проверка максимального возраста {max_vozrast}-1 день'):
        assertion = json.loads(policy_calculate_age(max_age_minus_1d_api))
        assert assertion['error']['data']['status'] == 'ERROR'

@allure.parent_suite('API проверка возраста')
@allure.suite('API проверка максимального возраста')
@allure.title(f"API проверка максимального возраста {max_vozrast} +1 день")
def test_policy_calculate_max_age_plus_1d_age():
    with allure.step(f'Проверка максимального возраста {max_vozrast}+1 день'):
        assertion = json.loads(policy_calculate_age(max_age_plus_1d_api))
        assert assertion['result']['insured'][0]['person_info']['birth_date'] == api_age(y=max_vozrast + 1, d=+1) + 'T00:00:00'

''' __________ Доступные ПФ для печати___________'''
def print_zapros(print_zapros):
    test_api_token_session = test_api_token()
    headers_token = {"Authorization": test_api_token_session}
    uuid = jwt_decode(test_api_token_session)
    r = requests.post('https://gateway.cloud-test.renlife.com/api/v1/b2b/rpc', json=(print_zapros),
                      headers=headers_token)
    return json.loads(r.text)

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

@allure.parent_suite('API проверка печати')
@allure.suite('API проверка печати')
@allure.title(f"API проверка печати полиса")
def test_print_policy():
    read_data = read_data_create_data_policy_calculate()
    policy = print_file('POLICY')
    response = print_zapros(policy)
    assert response['method'] == 'b2b_get_policy_report_uuid'

@allure.parent_suite('API проверка печати')
@allure.suite('API проверка печати')
@allure.title(f"API проверка печати Выкупные суммы")
def test_print_vs():
    read_data = read_data_create_data_policy_calculate()
    policy = print_file('APPLICATION_REFUNDABLE_AMOUNTS')
    response = print_zapros(policy)
    assert response['method'] == 'b2b_get_policy_report_uuid'

@allure.parent_suite('API проверка печати')
@allure.suite('API проверка печати')
@allure.title(f"API проверка печати Уведомление")
def test_print_yvedomlenie():
    read_data = read_data_create_data_policy_calculate()
    policy = print_file('CONFIRM_POLICY')
    response = print_zapros(policy)
    assert response['method'] == 'b2b_get_policy_report_uuid'

@allure.parent_suite('API проверка печати')
@allure.suite('API проверка печати')
@allure.title(f"API проверка печати Анкета специальных знаний ИСЖ")
def test_print_anketa_isj():
    read_data = read_data_create_data_policy_calculate()
    policy = print_file('KNOWLEDGE_ISZH_QUEST')
    response = print_zapros(policy)
    assert response['method'] == 'b2b_get_policy_report_uuid'

@allure.parent_suite('API проверка печати')
@allure.suite('API проверка печати')
@allure.title(f"API проверка печати Памятка")
def test_print_memo():
    read_data = read_data_create_data_policy_calculate()
    policy = print_file('MEMO')
    response = print_zapros(policy)
    assert response['method'] == 'b2b_get_policy_report_uuid'

@allure.parent_suite('API проверка печати')
@allure.suite('API проверка печати')
@allure.title(f"API проверка печати Памятка для клиента")
def test_print_klient_memo():
    read_data = read_data_create_data_policy_calculate()
    policy = print_file('REMINDER')
    response = print_zapros(policy)
    assert response['method'] == 'b2b_get_policy_report_uuid'

