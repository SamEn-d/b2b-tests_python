import os

import allure
import requests
import json
from renlife_b2b_test.api.policy_calculate_api import policy_calculate_zapros_api
from allure_commons.types import AttachmentType

from renlife_b2b_test.api.token import api_token
from renlife_b2b_test.api.vznos import assert_vznos_passed, asser_vznos_error

url = os.getenv('URL_API')

min_vznos = float(os.getenv('MIN_VZNOS_UBRIR'))
avg_vznos = float(os.getenv('AVG_VZNOS_UBRIR'))
max_vznos = float(os.getenv('MAX_VZNOS_UBRIR'))



''' _________ VZNOS ________'''
def vznos_policy_calculate_zapros_api(base_summa, dtp_risk_15kk):
    vznos_policy_calculate_zapros_api = policy_calculate_zapros_api(dtp_risk=dtp_risk_15kk,
                                                                    breef='INVESTOR_LUMP_4.1_BASE3_113_TM_CB_UBRIR',
                                                                    birth_date='2000-10-10', ag_contract_num=91061,
                                                                    base_sum=base_summa, bso_series=487,
                                                                    payment_terms='Единовременно',
                                                                    policy_period_brief='3_YEARS',
                                                                    product_brief='INVESTOR_LUMP_4.1_BASE3_113_TM_CB',
                                                                    calc_only='YES', save_policy='NO')
    return vznos_policy_calculate_zapros_api

def policy_calculate_vznos(zapros_summa):
    headers_token = {"Authorization": api_token()}
    r = requests.post(url,
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
        assertion = json.loads(policy_calculate_vznos(min_vznos_api))
        assert assert_vznos_passed(assertion) == min_vznos

@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка минимального взноса')
@allure.title(f"API проверка мнимального взноса {min_vznos} минус 1 копейка")
def test_policy_calculate_min_vznos_api_minus_001():
    with allure.step(f'Проверка минимального взноса {min_vznos}-0.01'):
        assertion = json.loads(policy_calculate_vznos(min_vznos_api_minus_001))
        assert asser_vznos_error(assertion)

@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка минимального взноса')
@allure.title(f"API проверка мнимального взноса {min_vznos} плюс 1 копейка")
def test_policy_calculate_min_vznos_api_plus_001():
    with allure.step(f'Проверка минимального взноса {min_vznos}+0.01'):
        assertion = json.loads(policy_calculate_vznos(min_vznos_api_plus_001))
        assert assert_vznos_passed(assertion) == min_vznos+0.01

''' MAX VZNOS '''
@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка максимального взноса')
@allure.title(f"API проверка максимального взноса {min_vznos}")
def test_policy_calculate_max_vznos():
    with allure.step(f'Проверка максимального взноса {max_vznos}'):
        assertion = json.loads(policy_calculate_vznos(max_vznos_api))
        assert assert_vznos_passed(assertion) == max_vznos

@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка максимального взноса')
@allure.title(f"API проверка максимального взноса {min_vznos} -1 копейка")
def test_policy_calculate_max_vznos_api_minus_001():
    with allure.step(f'Проверка максимального взноса {max_vznos}-0.01'):
        assertion = json.loads(policy_calculate_vznos(max_vznos_api_minus_001))
        assert assert_vznos_passed(assertion) == max_vznos-0.01

@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка максимального взноса')
@allure.title(f"API проверка максимального взноса {min_vznos} +1 копейка")
def test_policy_calculate_max_vznos_api_plus_001():
    with allure.step(f'Проверка максимального взноса {max_vznos}+0.01'):
        assertion = json.loads(policy_calculate_vznos(max_vznos_api_plus_001))
        assert asser_vznos_error(assertion)

''' AVG VZNOS '''
@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка среднего взноса')
@allure.title(f"API проверка среднего взноса {avg_vznos} без риска")
def test_policy_calculate_avg_vznos():
    with allure.step(f'Проверка среднего взноса БЕЗ риска {avg_vznos}'):
        assertion = json.loads(policy_calculate_vznos(avg_vznos_api))
        assert asser_vznos_error(assertion)

@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка среднего взноса')
@allure.title(f"API проверка среднего взноса {avg_vznos} -1 без риска")
def test_policy_calculate_avg_vznos_api_minus_1_risk_off():
    with allure.step(f'Проверка среднего взноса БЕЗ риска {avg_vznos}-1'):
        assertion = json.loads(policy_calculate_vznos(avg_vznos_api_minus_1_risk_off))
        assert assert_vznos_passed(assertion) == avg_vznos - 1

@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка среднего взноса')
@allure.title(f"API проверка среднего взноса {avg_vznos} +1 без риска")
def test_policy_calculate_avg_vznos_api_plus_1_risk_off():
    with allure.step(f'Проверка среднего взноса БЕЗ риска {avg_vznos}+1'):
        assertion = json.loads(policy_calculate_vznos(avg_vznos_api_plus_1_risk_off))
        assert asser_vznos_error(assertion)

@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка среднего взноса')
@allure.title(f"API проверка среднего взноса {avg_vznos} с риском")
def test_policy_calculate_avg_vznos_api_risk_on():
    with allure.step(f'Проверка среднего взноса C риском {avg_vznos}'):
        assertion = json.loads(policy_calculate_vznos(avg_vznos_api_risk_on))
        assert assert_vznos_passed(assertion) == avg_vznos

@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка среднего взноса')
@allure.title(f"API проверка среднего взноса {avg_vznos} -1 с риском")
def test_policy_calculate_avg_vznos_api_minus_1_risk_on():
    with allure.step(f'Проверка среднего взноса C риском {avg_vznos}-1'):
        assertion = json.loads(policy_calculate_vznos(avg_vznos_api_minus_1_risk_on))
        assert asser_vznos_error(assertion)

@allure.parent_suite('API проверка взноса')
@allure.suite('API проверка среднего взноса')
@allure.title(f"API проверка среднего взноса {avg_vznos} +1 с риском")
def test_policy_calculate_avg_vznos_api_plus_1_risk_on():
    with allure.step(f'Проверка среднего взноса C риском {avg_vznos}+1'):
        policy_calculate_vznos(avg_vznos_api_plus_1_risk_on)
        assertion = json.loads(policy_calculate_vznos(avg_vznos_api_plus_1_risk_on))
        assert assert_vznos_passed(assertion) == avg_vznos + 1


