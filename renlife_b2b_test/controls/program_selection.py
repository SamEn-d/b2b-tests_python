from selene import have, be
from selene.support.shared import browser


def program_selection(name):
    browser.all('.product-list__title').element_by(have.exact_text(name)).with_(timeout=10).should(be.visible).click()
