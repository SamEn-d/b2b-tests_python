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
from renlife_b2b_test.ui.investor import fill_form_investor
login_b2b = os.getenv('LOGIN_b2b2')
password_b2b = os.getenv('PASSWORD_b2b2')
url = os.getenv('URL_FRONT')

min_vznos = 30000
average_vznos = 1500000
max_vznos = 50000000
program_name = 'Инвестор 4.1. (3 года)'


#min vznos
@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка минимального взноса')
@allure.title(f"Проверка минимального взноса {min_vznos}-0.01")
def test_partner_ubrir_b2b_min_minus001():
    fill_form_investor.precondition(setup_browser,program_name)
    minimal_fee.vznos_minus_001(min_vznos)
    fill_form_investor.postcondition()

@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка минимального взноса')
@allure.title(f"Проверка минимального взноса {min_vznos}")
def test_partner_ubrir_b2b_min():
    fill_form_investor.precondition(setup_browser,program_name)
    minimal_fee.vznos(min_vznos)
    fill_form_investor.postcondition()

@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка минимального взноса')
@allure.title(f"Проверка минимального взноса {min_vznos}+0.01")
def test_partner_ubrir_b2b_min_plus001():
    fill_form_investor.precondition(setup_browser,program_name)
    minimal_fee.vznos_plus_001(min_vznos)
    fill_form_investor.postcondition()


#max vznos
@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка максимального взноса')
@allure.title(f"Проверка максимального взноса {max_vznos}-0.01")
def test_partner_ubrir_b2b_max_minus001():
    fill_form_investor.precondition(setup_browser,program_name)
    minimal_fee.vznos_max_minus_001(max_vznos)
    fill_form_investor.postcondition()

@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка максимального взноса')
@allure.title(f"Проверка максимального взноса {max_vznos}")
def test_partner_ubrir_b2b_max():
    fill_form_investor.precondition(setup_browser,program_name)
    minimal_fee.vznos_max(max_vznos)
    fill_form_investor.postcondition()

@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка максимального взноса')
@allure.title(f"Проверка максимального взноса {max_vznos}+0.01")
def test_partner_ubrir_b2b_max_plus001():
    fill_form_investor.precondition(setup_browser,program_name)
    minimal_fee.vznos_max_plus_001(max_vznos)
    fill_form_investor.postcondition()



@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка среднее \ граничное значение взноса')
@allure.title(f"Проверка взноса {average_vznos} без программы")
def test_partner_ubrir_b2b_avg_no_program():
    fill_form_investor.precondition(setup_browser,program_name)
    minimal_fee.vznos_avg_no_program(average_vznos)
    fill_form_investor.postcondition()

@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка среднее \ граничное значение взноса')
@allure.title(f"Проверка взноса {average_vznos} с программой")
def test_partner_ubrir_b2b_avg_program():
    fill_form_investor.precondition(setup_browser,program_name)
    minimal_fee.vznos_avg_program(average_vznos)
    fill_form_investor.postcondition()

@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка среднее \ граничное значение взноса')
@allure.title(f"Проверка взноса {average_vznos}+0.01 с программой")
def test_partner_ubrir_b2b_avg_program_plus001():
    fill_form_investor.precondition(setup_browser,program_name)
    minimal_fee.vznos_avg_program_plus001(average_vznos)
    fill_form_investor.postcondition()

@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка среднее \ граничное значение взноса')
@allure.title(f"Проверка взноса {average_vznos}+0.01 без программы")
def test_partner_ubrir_b2b_avg_no_program_plus001():
    fill_form_investor.precondition(setup_browser,program_name)
    minimal_fee.vznos_avg_no_program_plus001(average_vznos)
    fill_form_investor.postcondition()

#флаки тесты при копейке
@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка среднее \ граничное значение взноса')
@allure.title(f"Проверка взноса {average_vznos}-1 без программы")
def test_partner_ubrir_b2b_avg_no_program_minus001():
    fill_form_investor.precondition(setup_browser,program_name)
    minimal_fee.vznos_avg_no_program_minus001(average_vznos)
    fill_form_investor.postcondition()

@allure.parent_suite('Проверка взноса')
@allure.suite('Проверка среднее \ граничное значение взноса')
@allure.title(f"Проверка взноса {average_vznos}-1 c программы")
def test_partner_ubrir_b2b_avg_c_program_minus001():
    fill_form_investor.precondition(setup_browser,program_name)
    minimal_fee.vznos_avg_program_minus001(average_vznos)
    fill_form_investor.postcondition()



