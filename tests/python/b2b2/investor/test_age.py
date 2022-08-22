import allure

from renlife_b2b_test import age
from renlife_b2b_test.controls import policy_calculate_ui
from renlife_b2b_test.controls.policy_calculate_ui import FillPersonalData
from tests.python.b2b2.investor.vznos.test_investor_ubrir_min_max_vznos import precondition, postcondition
from conftest import setup_browser

min_vozrast = 18
max_vozrast = 85

#min_vozrast
def precondition_sum():
    precondition()
    policy_calculate_ui.UI(100000)

@allure.parent_suite('Проверка возраста')
@allure.suite('Проверка минимального возраста')
@allure.title(f"Проверка минимального возраста {min_vozrast}")
def test_age_minimal():
    precondition_sum()
    age.age_minimal(min_vozrast)
    postcondition()

@allure.parent_suite('Проверка возраста')
@allure.suite('Проверка минимального возраста')
@allure.title(f"Проверка минимального возраста {min_vozrast} -1 день")
def test_age_minimal_minus_1():
    precondition_sum()
    age.age_18_minus_1_day(min_vozrast)
    postcondition()

@allure.parent_suite('Проверка возраста')
@allure.suite('Проверка минимального возраста')
@allure.title(f"Проверка минимального возраста {min_vozrast} +1 день")
def test_age_minimal_plus_1():
    precondition_sum()
    age.age_18_plus_1_day(min_vozrast)
    postcondition()


#max_vozrast
@allure.parent_suite('Проверка возраста')
@allure.suite('Проверка максимального возраста')
@allure.title(f"Проверка максимального возраста {max_vozrast}")
def test_max_age():
    precondition_sum()
    age.age_max(max_vozrast)
    postcondition()

@allure.parent_suite('Проверка возраста')
@allure.suite('Проверка максимального возраста')
@allure.title(f"Проверка максимального возраста {max_vozrast} +1 день")
def test_max_age_plus_1():
    precondition_sum()
    age.age_max_plus_1(max_vozrast)
    postcondition()

@allure.parent_suite('Проверка возраста')
@allure.suite('Проверка максимального возраста')
@allure.title(f"Проверка максимального возраста {max_vozrast} -1 день")
def test_max_age_minus_1():
    precondition_sum()
    age.age_max_minus_1(max_vozrast)
    postcondition()

