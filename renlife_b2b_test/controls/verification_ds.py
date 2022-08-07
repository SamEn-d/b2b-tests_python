import time
from selene import be, have
from selene.support.shared import browser
import os
import shutil
from renlife_b2b_test.path_to_directory import filename

def delete_file():
    time.sleep(15)
    dirpath = os.path.join(filename(), 'tmp')
    assert len(os.listdir(dirpath)) > 0
    shutil.rmtree(dirpath)

class Verification_DS():
    @staticmethod
    def check():
        browser.element('h2.contract__title').with_(timeout=30).should(have.text('Заявления по договору'))
        time.sleep(3)

class PFCheck():
    def __init__(self, css_class: str = None):
            self.css_class = browser.all('.contract__info-block-buttons .el-dropdown-selfdefine')[1].hover()

    def application_VS(self):
        self.css_class.hover()
        browser.all('.el-dropdown-menu__item').element_by(have.text('Приложение - выкупные суммы')).click()
        delete_file()
        return self

    def notification(self):
        self.css_class.hover()
        browser.all('.el-dropdown-menu__item').element_by(have.text('Уведомление')).click()
        delete_file()
        return self

    def anketa_specialnih_znaniy(self):
        self.css_class.hover()
        browser.all('.el-dropdown-menu__item').element_by(have.text('Анкета специальных знаний ИСЖ')).click()
        delete_file()
        return self

    def memo(self):
        self.css_class.hover()
        browser.all('.el-dropdown-menu__item').element_by(have.text('Памятка')).click()
        delete_file()
        return self

    def policy(self):
        self.css_class.hover()
        browser.all('.el-dropdown-menu__item').element_by(have.text('Полис')).click()
        delete_file()
        return self

    def insurance_rules(self):
        self.css_class.hover()
        browser.all('.el-dropdown-menu__item').element_by(have.text('Правила страхования')).click()
        delete_file()
        return self

    def memo_client(self):
        self.css_class.hover()
        browser.all('.el-dropdown-menu__item').element_by(have.text('Памятка для клиента')).click()
        delete_file()
        return self
