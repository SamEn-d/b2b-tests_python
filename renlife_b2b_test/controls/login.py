import allure
from selene.support.shared import browser


def login_form(login, password):
    with allure.step(f'Авторизация в Б2Б2'):
        browser.element('.el-input__inner[name="username"]').type(login)
        browser.element('.el-input__inner[name="password"]').type(password)
        browser.element('.el-button--info').click()