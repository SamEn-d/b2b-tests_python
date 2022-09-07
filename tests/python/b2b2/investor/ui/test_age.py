import allure

from renlife_b2b_test.ui import age
from renlife_b2b_test.controls import policy_calculate_ui
# from tests.python.b2b2.investor.ui.test_investor_ubrir_min_max_vznos import precondition, postcondition
from renlife_b2b_test.ui.investor import fill_form_investor
from conftest import setup_browser

min_vozrast = 18
max_vozrast = 85
program_name = 'Инвестор 4.1. (3 года)'

#min_vozrast
def precondition_sum():
    fill_form_investor.precondition(setup_browser,program_name)
    policy_calculate_ui.UI(100000)

@allure.parent_suite('Проверка возраста')
@allure.suite('Проверка минимального возраста')
@allure.title(f"Проверка минимального возраста {min_vozrast}")
def test_age_minimal():
    precondition_sum()
    age.age_minimal(min_vozrast)
    fill_form_investor.postcondition()

@allure.parent_suite('Проверка возраста')
@allure.suite('Проверка минимального возраста')
@allure.title(f"Проверка минимального возраста {min_vozrast} -1 день")
def test_age_minimal_minus_1():
    precondition_sum()
    age.age_18_minus_1_day(min_vozrast)
    fill_form_investor.postcondition()

@allure.parent_suite('Проверка возраста')
@allure.suite('Проверка минимального возраста')
@allure.title(f"Проверка минимального возраста {min_vozrast} +1 день")
def test_age_minimal_plus_1():
    precondition_sum()
    age.age_18_plus_1_day(min_vozrast)
    fill_form_investor.postcondition()


#max_vozrast
@allure.parent_suite('Проверка возраста')
@allure.suite('Проверка максимального возраста')
@allure.title(f"Проверка максимального возраста {max_vozrast}")
def test_max_age():
    precondition_sum()
    age.age_max(max_vozrast)
    fill_form_investor.postcondition()

@allure.parent_suite('Проверка возраста')
@allure.suite('Проверка максимального возраста')
@allure.title(f"Проверка максимального возраста {max_vozrast} +1 день")
def test_max_age_plus_1():
    precondition_sum()
    age.age_max_plus_1(max_vozrast)
    fill_form_investor.postcondition()

@allure.parent_suite('Проверка возраста')
@allure.suite('Проверка максимального возраста')
@allure.title(f"Проверка максимального возраста {max_vozrast} -1 день")
def test_max_age_minus_1():
    precondition_sum()
    age.age_max_minus_1(max_vozrast)
    fill_form_investor.postcondition()

