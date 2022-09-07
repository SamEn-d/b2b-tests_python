from renlife_b2b_test.api.PF_print import print_file, print_zapros
import allure

@allure.parent_suite('API проверка печати')
@allure.suite('API проверка печати')
@allure.title(f"API проверка печати полиса")
def test_print_policy():
    policy = print_file('POLICY')
    response = print_zapros(policy)
    assert response['method'] == 'b2b_get_policy_report_uuid'

@allure.parent_suite('API проверка печати')
@allure.suite('API проверка печати')
@allure.title(f"API проверка печати Выкупные суммы")
def test_print_vs():
    policy = print_file('APPLICATION_REFUNDABLE_AMOUNTS')
    response = print_zapros(policy)
    assert response['method'] == 'b2b_get_policy_report_uuid'

@allure.parent_suite('API проверка печати')
@allure.suite('API проверка печати')
@allure.title(f"API проверка печати Уведомление")
def test_print_yvedomlenie():
    policy = print_file('CONFIRM_POLICY')
    response = print_zapros(policy)
    assert response['method'] == 'b2b_get_policy_report_uuid'

@allure.parent_suite('API проверка печати')
@allure.suite('API проверка печати')
@allure.title(f"API проверка печати Анкета специальных знаний ИСЖ")
def test_print_anketa_isj():
    policy = print_file('KNOWLEDGE_ISZH_QUEST')
    response = print_zapros(policy)
    assert response['method'] == 'b2b_get_policy_report_uuid'

@allure.parent_suite('API проверка печати')
@allure.suite('API проверка печати')
@allure.title(f"API проверка печати Памятка")
def test_print_memo():
    policy = print_file('MEMO')
    response = print_zapros(policy)
    assert response['method'] == 'b2b_get_policy_report_uuid'

@allure.parent_suite('API проверка печати')
@allure.suite('API проверка печати')
@allure.title(f"API проверка печати Памятка для клиента")
def test_print_klient_memo():
    policy = print_file('REMINDER')
    response = print_zapros(policy)
    assert response['method'] == 'b2b_get_policy_report_uuid'
