import allure
from selene import have, be
from selene.support.shared import browser


def program_selection(name):
    with allure.step(f'Выбираем программу страхования'):
        browser.all('.product-list__title').with_(timeout=10).element_by(have.exact_text(name)).should(be.visible).click()
