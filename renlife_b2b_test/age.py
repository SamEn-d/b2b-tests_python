import datetime
import time

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


# def birth_date_element():
#     browser.element('.collapsable-info-block__content [name="birth_date__0"')
# import datetime
#
# date = datetime.date.today()
# def my_date():
#     year = date.year
#     month = date.month
#     day = date.day
#
# def age_18(age):
#     year_age = date.year - age
#     print(z)
#     #date.day, date.month, date.year-age
#
# age_18(18)


def age_minimal(age):
    year_age = date.year - age
    my_date = date.day, month, year_age
    #browser.element('.el-date-editor [name="birth_date__0"]').set(date).press_enter()
    browser.element('.collapsable-info-block__content [name="birth_date__0"').set(my_date).press_enter()
    FillPersonalData().submit()
    passed_vibor()
    time.sleep(1)

def age_18_minus_1_day(age):
    year_age = date.year - age
    day_age = date.day - 1
    my_date = day_age, month, year_age
    #browser.element('.el-date-editor [name="birth_date__0"]').set(date).press_enter()
    browser.element('.collapsable-info-block__content [name="birth_date__0"').set(my_date).press_enter()
    FillPersonalData().submit()
    passed_vibor()
    time.sleep(1)

def age_18_plus_1_day(age):
    year_age = date.year - age
    day_age = date.day + 1
    my_date = day_age, month, year_age
    #browser.element('.el-date-editor [name="birth_date__0"]').set(date).press_enter()
    browser.element('.collapsable-info-block__content [name="birth_date__0"').set(my_date).press_enter()
    FillPersonalData().submit()
    error_vibor()
    time.sleep(1)