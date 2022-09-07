import os
import time

import allure
from selene import be
from selene.support.shared import browser

from renlife_b2b_test import attach
from renlife_b2b_test.controls import login, investor
from renlife_b2b_test.controls.browser_params import browser_params_1920
from renlife_b2b_test.controls.policy_calculate_ui import FillPersonalData
from renlife_b2b_test.controls.program_selection import program_selection

login_b2b = os.getenv('LOGIN_b2b2')
password_b2b = os.getenv('PASSWORD_b2b2')
url = os.getenv('URL_FRONT')


def precondition(setup_browser,program_name: str = None):
    # Given
    # browser = setup_browser
    browser_params_1920()
    login.login_form(login_b2b, password_b2b)

    # When
    time.sleep(2)
    browser.element('.el-button.kit-el-button.el-button--info').with_(timeout=5).should(be.visible).click()
    program_selection(program_name)

    investor.investor_question_all()

    (FillPersonalData()
     .gender()
     .birth_date()
     .surname()
     .midname()
     .name()
     )

def postcondition():
    time.sleep(1)
    attach.add_screenshot(browser)
    browser.quit()
