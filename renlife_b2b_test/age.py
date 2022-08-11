import datetime
import time

import allure
from selene.support.shared import browser

from renlife_b2b_test.controls.policy_calculate_ui import FillPersonalData
from renlife_b2b_test.minimal_fee import passed_vibor, error_vibor

date = datetime.date.today()
year = date.year
month = date.month
if month < 10:
    month = str(0) + str(month)

day = date.day
if day < 10:
    day = str(0) + str(day)


def age_minimal(age):
    year_age = date.year - age
    my_date = day, month, year_age
    with allure.step(f'Минимальный возраст {my_date}'):
        #browser.element('.el-date-editor [name="birth_date__0"]').set(date).press_enter()
        browser.element('.collapsable-info-block__content [name="birth_date__0"').set(my_date).press_enter()
        FillPersonalData().submit()
        passed_vibor()
        time.sleep(1)

def age_18_minus_1_day(age):
    year_age = date.year - age
    day_age = day - 1
    my_date = day_age, month, year_age
    with allure.step(f'Минимальный возраст - 1 день {my_date}'):
        #browser.element('.el-date-editor [name="birth_date__0"]').set(date).press_enter()
        browser.element('.collapsable-info-block__content [name="birth_date__0"').set(my_date).press_enter()
        FillPersonalData().submit()
        passed_vibor()
        time.sleep(1)

def age_18_plus_1_day(age):
    year_age = date.year - age
    day_age = day + 1
    my_date = day_age, month, year_age
    with allure.step(f'Минимальный возраст + 1 день {my_date}'):
        #browser.element('.el-date-editor [name="birth_date__0"]').set(date).press_enter()
        browser.element('.collapsable-info-block__content [name="birth_date__0"').set(my_date).press_enter()
        FillPersonalData().submit()
        error_vibor()
        time.sleep(1)

def age_max(age):
    year_age = date.year - age - 1
    day_age = day
    my_date = day_age, month, year_age
    with allure.step(f'Максимальный возраст {my_date}'):
        browser.element('.collapsable-info-block__content [name="birth_date__0"').set(my_date).press_enter()
        FillPersonalData().submit()
        error_vibor()
        time.sleep(1)

def age_max_plus_1(age):
    year_age = date.year - age - 1
    day_age = day + 1
    my_date = day_age, month, year_age
    with allure.step(f'Максимальный возраст + 1 день {my_date}'):
        browser.element('.collapsable-info-block__content [name="birth_date__0"').set(my_date).press_enter()
        FillPersonalData().submit()
        passed_vibor()
        time.sleep(1)

def age_max_minus_1(age):
    year_age = date.year - age - 1
    day_age = day - 1
    my_date = day_age, month, year_age
    with allure.step(f'Максимальный возраст - 1 день {my_date}'):
        browser.element('.collapsable-info-block__content [name="birth_date__0"').set(my_date).press_enter()
        FillPersonalData().submit()
        error_vibor()
        time.sleep(1)
