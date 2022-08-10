import os
import time

import allure
from allure_commons.types import Severity
from selene.support.shared import browser

from conftest import setup_browser
from renlife_b2b_test.controls import login, investor
from renlife_b2b_test.controls.policy_calculate_ui import FillPersonalData
from renlife_b2b_test.controls.program_selection import program_selection
from renlife_b2b_test import minimal_fee, attach

login_b2b = os.getenv('LOGIN_b2b2')
password_b2b = os.getenv('PASSWORD_b2b2')

min_vznos = 30000
average_vznos = 1500000
max_vznos = 50000000


def precondition():
    # Given
    # browser = setup_browser
    allure.dynamic.tag('B2B2')
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.label('owner', 'Sam')
    allure.dynamic.description('Заполнение ДС и проверка скачивания файлов ПФ')
    # path_to_download_resources()
    browser.open('https://b2b.cloud-test.renlife.com/')
    browser.driver.set_window_size(width=1920, height=1080)
    # browser_params.browser_params_1920()
    login.ubrir(login_b2b, password_b2b)

    # When
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
@allure.title(f"Проверка минимального взноса {min_vznos}-0.01")
def test_partner_ubrir_b2b_min_minus001():
    precondition()
    minimal_fee.vznos_minus_001(min_vznos)
    postcondition()

@allure.title(f"Проверка минимального взноса {min_vznos}")
def test_partner_ubrir_b2b_min():
    precondition()
    minimal_fee.vznos(min_vznos)
    postcondition()

@allure.title(f"Проверка минимального взноса {min_vznos}+0.01")
def test_partner_ubrir_b2b_min_plus001():
    precondition()
    minimal_fee.vznos_plus_001(min_vznos)
    postcondition()


#max vznos
@allure.title(f"Проверка максимального взноса {max_vznos}-0.01")
def test_partner_ubrir_b2b_max_minus001():
    precondition()
    minimal_fee.vznos_max_minus_001(max_vznos)
    postcondition()

@allure.title(f"Проверка максимального взноса {max_vznos}")
def test_partner_ubrir_b2b_max():
    precondition()
    minimal_fee.vznos_max(max_vznos)
    postcondition()

@allure.title(f"Проверка максимального взноса {max_vznos}+0.01")
def test_partner_ubrir_b2b_max_plus001():
    precondition()
    minimal_fee.vznos_max_plus_001(max_vznos)
    postcondition()


#average_vznos
#Ввести 1 500 000 и выбрать галочку - всё хорошо
#Ввести 1 500 000 и НЕ выбрать галочку - ошибка
#Ввести 1 499 999.99 и НЕ выбрать галочку - всё хорошо
#Ввести 1 499 999.99 и выбрать галочку - ошибка
#Ввести 1 500 000.01 и выбрать галочку - всё хорошо
#Ввести 1 500 000.01 и НЕ выбрать галочку - ошибка
@allure.title(f"Проверка максимального взноса {average_vznos} без программы")
def test_partner_ubrir_b2b_avg_no_program():
    precondition()
    minimal_fee.vznos_avg_no_program(average_vznos)
    postcondition()

@allure.title(f"Проверка максимального взноса {average_vznos} с программой")
def test_partner_ubrir_b2b_avg_program():
    precondition()
    minimal_fee.vznos_avg_program(average_vznos)
    postcondition()

@allure.title(f"Проверка максимального взноса {average_vznos}+0.01 с программой")
def test_partner_ubrir_b2b_avg_program_plus001():
    precondition()
    minimal_fee.vznos_avg_program_plus001(average_vznos)
    postcondition()

@allure.title(f"Проверка максимального взноса {average_vznos}+0.01 без программы")
def test_partner_ubrir_b2b_avg_no_program_plus001():
    precondition()
    minimal_fee.vznos_avg_no_program_plus001(average_vznos)
    postcondition()

#флаки тесты при копейке
@allure.title(f"Проверка максимального взноса {average_vznos}-1 без программы")
def test_partner_ubrir_b2b_avg_no_program_minus001():
    precondition()
    minimal_fee.vznos_avg_no_program_minus001(average_vznos)
    postcondition()

@allure.title(f"Проверка максимального взноса {average_vznos}-1 c программы")
def test_partner_ubrir_b2b_avg_no_program_minus001():
    precondition()
    minimal_fee.vznos_avg_program_minus001(average_vznos)
    postcondition()


def postcondition():
    time.sleep(1)
    attach.add_screenshot(browser)
    browser.quit()
    '''
    Написать так, чтобы была проверка про при взносе до 30 000 выходила ошибка автоматически отнимая 1 копейку
    '''

