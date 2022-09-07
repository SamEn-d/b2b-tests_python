import datetime
import os
import json
import allure
import requests

from renlife_b2b_test.api.age import print_api_age, AssertAge
from renlife_b2b_test.api.policy_calculate_api import policy_calculate_zapros_api
from renlife_b2b_test.api.token import api_token

min_vozrast = int(os.getenv('MIN_VOZRAST_UBRIR'))
max_vozrast = int(os.getenv('MAX_VOZRAST_UBRIR'))

url = os.getenv('URL_API')


def zaros_policy_calculate_age(birth_date):
    policy_calculate_age = policy_calculate_zapros_api(dtp_risk=0,
                                                        breef='INVESTOR_LUMP_4.1_BASE3_113_TM_CB_UBRIR',
                                                        birth_date=birth_date, ag_contract_num=91061,
                                                        base_sum=100000, bso_series=487,
                                                        payment_terms='Единовременно',
                                                        policy_period_brief='3_YEARS',
                                                        product_brief='INVESTOR_LUMP_4.1_BASE3_113_TM_CB',
                                                        calc_only='YES', save_policy='NO')
    return policy_calculate_age


min_age_api = json.loads(zaros_policy_calculate_age(print_api_age(y=min_vozrast, d=0)))
min_age_minus_1d_api = json.loads(zaros_policy_calculate_age(print_api_age(y=min_vozrast, d=-1)))
min_age_plus_1d_api = json.loads(zaros_policy_calculate_age(print_api_age(y=min_vozrast, d=+1)))

max_age_api = json.loads(zaros_policy_calculate_age(print_api_age(y=max_vozrast + 1, d=0)))
max_age_minus_1d_api = json.loads(zaros_policy_calculate_age(print_api_age(y=max_vozrast + 1, d=-1)))
max_age_plus_1d_api = json.loads(zaros_policy_calculate_age(print_api_age(y=max_vozrast + 1, d=+1)))


''' Min age '''
@allure.parent_suite('API проверка возраста')
@allure.suite('API проверка минимального возраста')
@allure.title(f"API проверка минимального возраста {min_vozrast}")
def test_policy_calculate_min_age():
    with allure.step(f'Проверка минимального возраста {min_vozrast}'):
        assertion = json.loads(policy_calculate_age(min_age_api))
        assert AssertAge().passed(assertion) == AssertAge().min_age(min_vozrast)

@allure.parent_suite('API проверка возраста')
@allure.suite('API проверка минимального возраста')
@allure.title(f"API проверка минимального возраста {min_vozrast} -1 день")
def test_policy_calculate_min_age_minus_1d_age():
    with allure.step(f'Проверка минимального возраста {min_vozrast} -1 день'):
        assertion = json.loads(policy_calculate_age(min_age_minus_1d_api))
        assert AssertAge().passed(assertion) == AssertAge().min_age_minus_1d(min_vozrast)


@allure.parent_suite('API проверка возраста')
@allure.suite('API проверка минимального возраста')
@allure.title(f"API проверка минимального возраста {min_vozrast} +1 день")
def test_policy_calculate_min_age_plus_1d_age():
    with allure.step(f'Проверка минимального возраста {min_vozrast} +1 день'):
        assertion = json.loads(policy_calculate_age(min_age_plus_1d_api))
        assert AssertAge().error(assertion)

''' Max age '''
@allure.parent_suite('API проверка возраста')
@allure.suite('API проверка максимального возраста')
@allure.title(f"API проверка максимального возраста {max_vozrast}")
def test_policy_calculate_max_age():
    with allure.step(f'Проверка максимального возраста {max_vozrast}'):
        assertion = json.loads(policy_calculate_age(max_age_api))
        assert AssertAge().passed(assertion) == AssertAge().max_age(max_vozrast)

@allure.parent_suite('API проверка возраста')
@allure.suite('API проверка максимального возраста')
@allure.title(f"API проверка максимального возраста {max_vozrast} -1 день")
def test_policy_calculate_max_age_minus_1d_age():
    with allure.step(f'Проверка максимального возраста {max_vozrast}-1 день'):
        assertion = json.loads(policy_calculate_age(max_age_minus_1d_api))
        assert AssertAge().error(assertion)

@allure.parent_suite('API проверка возраста')
@allure.suite('API проверка максимального возраста')
@allure.title(f"API проверка максимального возраста {max_vozrast} +1 день")
def test_policy_calculate_max_age_plus_1d_age():
    with allure.step(f'Проверка максимального возраста {max_vozrast}+1 день'):
        assertion = json.loads(policy_calculate_age(max_age_plus_1d_api))
        assert AssertAge().passed(assertion) == AssertAge().max_age_plus_1d(max_vozrast)

def policy_calculate_age(zapros_age):
    headers_token = {"Authorization": api_token()}
    request = requests.post(url, json=zapros_age, headers=headers_token)
    return request.text

