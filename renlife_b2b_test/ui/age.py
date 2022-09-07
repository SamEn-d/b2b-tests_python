import datetime
import time

import allure
from selene.support.shared import browser

from renlife_b2b_test.controls.policy_calculate_ui import FillPersonalData
from renlife_b2b_test.minimal_fee import message_error, message_passed

date = datetime.date.today()
year = date.year
month = date.month
if month < 10:
    month = str(0) + str(month)

def new_day(plus_minus_day: int = 0):
    day = date.day
    day = day + plus_minus_day
    if day < 10:
        day = str(0) + str(day)
    return day

def print_full_date(age:int=None, day:int = 0, ):
    year_age = date.year - age
    day_age = new_day(day)
    full_date_ui = day_age, month, year_age
    return full_date_ui


def birth_date_set(my_date):
    return browser.element('.collapsable-info-block__content [name="birth_date__0"').set(my_date).press_enter()

def submit_passed():
    FillPersonalData().submit()
    message_passed()
    time.sleep(1)

def submit_error():
    FillPersonalData().submit()
    message_error()
    time.sleep(1)

def age_minimal(age):
    my_date = print_full_date(age=age, day=0)
    with allure.step(f'Минимальный возраст {my_date}'):
        birth_date_set(my_date)
        submit_passed()

def age_18_minus_1_day(age):
    my_date = print_full_date(age=age, day=-1)
    with allure.step(f'Минимальный возраст - 1 день {my_date}'):
        birth_date_set(my_date)
        submit_passed()

def age_18_plus_1_day(age):
    my_date = print_full_date(age=age, day=1)
    with allure.step(f'Минимальный возраст + 1 день {my_date}'):
        birth_date_set(my_date)
        submit_error()

def age_max(age):
    my_date = print_full_date(age=age + 1, day=0)
    with allure.step(f'Максимальный возраст {my_date}'):
        birth_date_set(my_date)
        submit_error()

def age_max_plus_1(age):
    my_date = print_full_date(age=age + 1, day=1)
    with allure.step(f'Максимальный возраст + 1 день {my_date}'):
        birth_date_set(my_date)
        submit_passed()

def age_max_minus_1(age):
    my_date = print_full_date(age=age + 1, day=-1)
    with allure.step(f'Максимальный возраст - 1 день {my_date}'):
        birth_date_set(my_date)
        submit_error()
