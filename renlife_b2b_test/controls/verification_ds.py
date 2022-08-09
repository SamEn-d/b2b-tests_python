import time

import allure
from selene import be, have
from selene.support.shared import browser
import shutil
import os
import glob
from renlife_b2b_test.path_to_directory import filename


dirpath = os.path.join(filename(), 'tmp')

# def presence_file():
#     os.mkdir(filename() + "/tmp")
#     time_spleep = 0
#     while time_spleep < 15:
#         if len(os.listdir(dirpath)) > 0:
#             assert len(os.listdir(dirpath)) > 0
#             shutil.rmtree(dirpath)
#             break
#         else:
#             # проверяем, есть ли файл в папке tmp
#             time_spleep += 1
#             time.sleep(1)



def presence_and_delete_file():
    time_spleep = 0
    while time_spleep < 15:
        if len(os.listdir(dirpath)) > 0:
            time.sleep(1)
            break
        else:
            time_spleep += 1
            time.sleep(1)
    assert len(os.listdir(dirpath)) > 0
    files = os.listdir(dirpath)
    for f in files:
        with allure.step(f'Скачался файл {f}'):
            print(f)
        os.remove(dirpath + '/' + f)


class Verification_DS():
    @staticmethod
    def check():
        # browser.element('h2.contract__title').with_(timeout=30).should(have.text('Заявления по договору'))
        browser.element('.inner-wrapper > .el-loading-mask').with_(timeout=30).should(be.hidden)
        browser.element('h2.contract__title').with_(timeout=30).should(have.text('Заявления по договору'))
        time.sleep(3)

class PFCheck():
    def __init__(self, css_class: str = None):
        # self.css_class = browser.all('.contract__info-block-buttons .el-dropdown-selfdefine').should(have.text('Напечатать'))
        self.css_class = browser.all('.contract__info-block_right  .contract-actions__btn')[1].hover()
        #[0]#[1].hover()


    def application_VS(self):
        with allure.step(f'Проверка на скачивание ПФ Приложение - выкупные суммы'):
            self.css_class.hover()
            browser.all('.el-dropdown-menu__item').element_by(have.text('Приложение - выкупные суммы')).click()
            presence_and_delete_file()
            return self


    def notification(self):
        with allure.step(f'Проверка на скачивание ПФ Уведомление'):
            self.css_class.hover()
            browser.all('.el-dropdown-menu__item').element_by(have.text('Уведомление')).click()
            presence_and_delete_file()
            return self


    def anketa_specialnih_znaniy(self):
        with allure.step(f'Проверка на скачивание ПФ Анкета специальных знаний ИСЖ'):
            self.css_class.hover()
            browser.all('.el-dropdown-menu__item').element_by(have.text('Анкета специальных знаний ИСЖ')).click()
            presence_and_delete_file()
            return self


    def memo(self):
        with allure.step(f'Проверка на скачивание ПФ Памятка'):
            self.css_class.hover()
            browser.all('.el-dropdown-menu__item').element_by(have.text('Памятка')).click()
            presence_and_delete_file()
            return self


    def policy(self):
        with allure.step(f'Проверка на скачивание ПФ Полис'):
            self.css_class.hover()
            browser.all('.el-dropdown-menu__item').element_by(have.text('Полис')).click()
            presence_and_delete_file()
            return self


    def insurance_rules(self):
        with allure.step(f'Проверка на скачивание ПФ Правила страхования'):
            self.css_class.hover()
            browser.all('.el-dropdown-menu__item').element_by(have.text('Правила страхования')).click()
            presence_and_delete_file()
            return self


    def memo_client(self):
        with allure.step(f'Проверка на скачивание ПФ Памятка для клиента'):
            self.css_class.hover()
            browser.all('.el-dropdown-menu__item').element_by(have.text('Памятка для клиента')).click()
            presence_and_delete_file()
            return self
