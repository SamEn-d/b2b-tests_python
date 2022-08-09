import os
import time

import allure
from allure_commons.types import Severity
from selene.support.shared import browser

from renlife_b2b_test.controls import browser_params
from renlife_b2b_test.controls import login
from renlife_b2b_test.controls import investor
from renlife_b2b_test.controls.program_selection import program_selection
from renlife_b2b_test.controls import policy_calculate_ui
from renlife_b2b_test.controls.policy_calculate_ui import FillPersonalData, policy_results, PolicyUpdateInfo
from renlife_b2b_test.controls.verification_ds import Verification_DS, PFCheck
# from renlife_b2b_test.path_to_directory import path_to_download_resources
# from dotenv import load_dotenv

login_b2b = os.getenv('LOGIN_b2b2')
password_b2b = os.getenv('PASSWORD_b2b2')

def test_pass(setup_browser):
    browser = setup_browser
    browser.open('https://b2b.cloud-test.renlife.com/')
    ...

'''
Нужно сделать
Подвязать внешний браузер - жопа
Шаги для алюра - просто
Зафигачить всё это в jenkins - просто
'''

@allure.title("Б2Б2 УБРИР Инвестор 4.1. (3 года) создание ДС и скачивание файлов")
def test_partner_ubrir_b2b(setup_browser):
    # Given
    browser = setup_browser
    allure.dynamic.tag('B2B2')
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.label('owner', 'Sam')
    allure.dynamic.description('Заполнение ДС и проверка скачивания файла')
    # path_to_download_resources()
    browser.open('https://b2b.cloud-test.renlife.com/')
    browser.driver.set_window_size(width=1920, height=1080)
    # browser_params.browser_params_1920()
    login.ubrir(login_b2b, password_b2b)

    # When
    program_selection('Инвестор 4.1. (3 года)')

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
    with allure.step(f'Вносим данные о застрахованном'):
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
     # .insurance_rules()
     .memo_client()
     )
    # time.sleep(5)