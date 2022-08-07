from selene.support.shared import browser


def ubrir(login, password):
    browser.element('.el-input__inner[name="username"]').type(login)
    browser.element('.el-input__inner[name="password"]').type(password)
    browser.element('.el-button--info').click()