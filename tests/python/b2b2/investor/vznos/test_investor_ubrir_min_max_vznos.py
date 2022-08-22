import os
import time

import allure
from allure_commons.types import Severity
from selene import be
from selene.support.shared import browser

from conftest import setup_browser
from renlife_b2b_test.controls import login, investor
from renlife_b2b_test.controls.policy_calculate_ui import FillPersonalData
from renlife_b2b_test.controls.program_selection import program_selection
from renlife_b2b_test import minimal_fee, attach

login_b2b = os.getenv('LOGIN_b2b2')
password_b2b = os.getenv('PASSWORD_b2b2')
url = os.getenv('URL_FRONT')

min_vznos = 30000
average_vznos = 1500000
max_vznos = 50000000


def precondition():
    # Given
    allure.dynamic.tag('B2B2')
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.label('owner', 'Sam')
    allure.dynamic.description('Заполнение ДС и проверка скачивания файлов ПФ')
    # path_to_download_resources()
    browser.open(url)
    browser.driver.set_window_size(width=1920, height=1080)
    # browser_params.browser_params_1920()
    login.ubrir(login_b2b, password_b2b)

    # When
    time.sleep(2)
    browser.element('.el-button.kit-el-button.el-button--info').with_(timeout=5).should(be.visible).click()
    # browser.element('.inner-wrapper > .el-loading-mask').with_(timeout=30).should(be.hidden)
    # browser.element('.el-button.kit-el-button.el-button--info').click()
    program_selection('Инвестор 4.1. (3 года)')

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
     )

#min vznos
@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка минимального взноса')
@allure.title(f"Проверка минимального взноса {min_vznos}-0.01")
def test_partner_ubrir_b2b_min_minus001():
    precondition()
    minimal_fee.vznos_minus_001(min_vznos)
    postcondition()

@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка минимального взноса')
@allure.title(f"Проверка минимального взноса {min_vznos}")
def test_partner_ubrir_b2b_min():
    precondition()
    minimal_fee.vznos(min_vznos)
    postcondition()

@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка минимального взноса')
@allure.title(f"Проверка минимального взноса {min_vznos}+0.01")
def test_partner_ubrir_b2b_min_plus001():
    precondition()
    minimal_fee.vznos_plus_001(min_vznos)
    postcondition()


#max vznos
@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка максимального взноса')
@allure.title(f"Проверка максимального взноса {max_vznos}-0.01")
def test_partner_ubrir_b2b_max_minus001():
    precondition()
    minimal_fee.vznos_max_minus_001(max_vznos)
    postcondition()

@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка максимального взноса')
@allure.title(f"Проверка максимального взноса {max_vznos}")
def test_partner_ubrir_b2b_max():
    precondition()
    minimal_fee.vznos_max(max_vznos)
    postcondition()

@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка максимального взноса')
@allure.title(f"Проверка максимального взноса {max_vznos}+0.01")
def test_partner_ubrir_b2b_max_plus001():
    precondition()
    minimal_fee.vznos_max_plus_001(max_vznos)
    postcondition()



@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка среднее \ граничное значение взноса')
@allure.title(f"Проверка взноса {average_vznos} без программы")
def test_partner_ubrir_b2b_avg_no_program():
    precondition()
    minimal_fee.vznos_avg_no_program(average_vznos)
    postcondition()

@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка среднее \ граничное значение взноса')
@allure.title(f"Проверка взноса {average_vznos} с программой")
def test_partner_ubrir_b2b_avg_program():
    precondition()
    minimal_fee.vznos_avg_program(average_vznos)
    postcondition()

@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка среднее \ граничное значение взноса')
@allure.title(f"Проверка максимального взноса {average_vznos}+0.01 с программой")
def test_partner_ubrir_b2b_avg_program_plus001():
    precondition()
    minimal_fee.vznos_avg_program_plus001(average_vznos)
    postcondition()

@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка среднее \ граничное значение взноса')
@allure.title(f"Проверка максимального взноса {average_vznos}+0.01 без программы")
def test_partner_ubrir_b2b_avg_no_program_plus001():
    precondition()
    minimal_fee.vznos_avg_no_program_plus001(average_vznos)
    postcondition()

#флаки тесты при копейке
@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка среднее \ граничное значение взноса')
@allure.title(f"Проверка максимального взноса {average_vznos}-1 без программы")
def test_partner_ubrir_b2b_avg_no_program_minus001():
    precondition()
    minimal_fee.vznos_avg_no_program_minus001(average_vznos)
    postcondition()

@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка среднее \ граничное значение взноса')
@allure.title(f"Проверка максимального взноса {average_vznos}-1 c программы")
def test_partner_ubrir_b2b_avg_c_program_minus001():
    precondition()
    minimal_fee.vznos_avg_program_minus001(average_vznos)
    postcondition()


def postcondition():
    time.sleep(1)
    attach.add_screenshot(browser)
    browser.quit()


