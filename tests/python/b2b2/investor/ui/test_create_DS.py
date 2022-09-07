import os
import allure
from renlife_b2b_test.controls import policy_calculate_ui
from renlife_b2b_test.controls.policy_calculate_ui import FillPersonalData, policy_results, PolicyUpdateInfo
from renlife_b2b_test.controls.verification_ds import Verification_DS, PFCheck
from renlife_b2b_test.ui.investor import fill_form_investor

login_b2b = os.getenv('LOGIN_b2b2')
password_b2b = os.getenv('PASSWORD_b2b2')
url = os.getenv('URL_FRONT')
program_name = 'Инвестор 4.1. (3 года)'

@allure.parent_suite('Создание ДС')
@allure.suite('Создание ДС и проверка файлов')
@allure.title(f"Б2Б2 УБРИР {program_name} создание ДС и скачивание файлов")
def test_partner_ubrir_b2b(setup_browser):
    # Given
    browser = setup_browser
    fill_form_investor.precondition(setup_browser, program_name)
    policy_calculate_ui.UI()

    FillPersonalData().submit()
    policy_results()

    (PolicyUpdateInfo()
        .check()
        .passport_adress()
        .passport()
        .phone()
        .mail()
        .adress()
        .addresses_match()
        .arrange_DS()
     )

    Verification_DS.check()
    (PFCheck()
     .application_VS()
     .notification()
     .anketa_specialnih_znaniy()
     .memo()
     .policy()
     .memo_client()
     )
