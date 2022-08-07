import os
import time
from renlife_b2b_test.controls import browser_params
from renlife_b2b_test.controls import login
from renlife_b2b_test.controls import investor
from renlife_b2b_test.controls.program_selection import program_selection
from renlife_b2b_test.controls import policy_calculate_ui
from renlife_b2b_test.controls.policy_calculate_ui import FillPersonalData, policy_results, PolicyUpdateInfo
from renlife_b2b_test.controls.verification_ds import Verification_DS, PFCheck
from renlife_b2b_test.path_to_directory import path_to_download_resources
from dotenv import load_dotenv

login_b2b = os.getenv('LOGIN_b2b2')
password_b2b = os.getenv('PASSWORD_b2b2')

def test_partner_ubrir_b2b():
    # Given
    # browser = setup_browser
    path_to_download_resources()
    browser_params.browser_params_1920()
    login.ubrir(login_b2b, password_b2b)

    # When
    program_selection('Инвестор 4.1 (3 года) 105')

    policy_calculate_ui.UI(100000)

    investor.investor_question(0)
    investor.investor_question(1)
    investor.investor_question(2)
    investor.investor_question(3)
    investor.investor_question(4)

    (FillPersonalData()
     .gender('Мужской')
     .birth_date(12102000)
     .surname('Фамилияя')
     .midname('Отчествоо')
     .name('Имяя')
     .submit()
     )

    policy_results()

    (PolicyUpdateInfo()
        .check()
        .passport_adress('Адрес чего-то там')
        .passport('1235', '123456', '12112020', '011028', 'Кто выдал')
        .phone('9615550123')
        .mail('w@wth.su')
        .adress('г. Москва, Дербеневская набережная д. 7, стр. 22, кв. 10', '123100')
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
     .insurance_rules()
     .memo_client()
     )
    # time.sleep(5)