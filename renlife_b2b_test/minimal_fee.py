import allure
from selene import by, be
from selene.support.shared import browser

from renlife_b2b_test.controls.policy_calculate_ui import FillPersonalData

'''
Необходимо, чтобы мы введя только 30 000 получали 3 проверки
'''

# min_vznos = 30000
#
# class minimal(min_vznos):
#     def __init__(self, summa: int = 100000):
#         with allure.step(f'Вводим ссумму взноса'):
#             self.summa = browser.element('.calculate-contract__row [name="base_sum"]').set(summa)
#             self.sum = summa
#
#     def minimal_vznos_minus_001(self):
#         print(self.summa-0.01)
#         print(min_vznos-0.01)
#         browser.element('.calculate-contract__row [name="base_sum"]').set(self.summa -0.01)
#         browser.element('.el-message--error').should(be.visible)
#
#     def minimal_vznos(self, summa):
#         print(min_vznos)
#         browser.element('.calculate-contract__row [name="base_sum"]').set(self.summa)
#
#     def minimal_vznos_plus_001(self, summa):
#         print(min_vznos + 0.01)
#         browser.element('.calculate-contract__row [name="base_sum"]').set(self.summa + 0.01)
#
# def test_test():
#     print(minimal().minimal_vznos_minus_001())



# def vznos(min_vznos):
#     min_vznos

#написать переменную, которую будут менять для мин макс авг


def vznos_minus_001(min_vznos):
    with allure.step(f'Вводим ссумму взноса минус 1 копейка'):
        browser.element('.calculate-contract__row [name="base_sum"]').set(min_vznos-0.01)
        FillPersonalData().submit()
        browser.element('.el-message--error').with_(timeout=10).should(be.visible)


def vznos(min_vznos):
    with allure.step(f'Вводим ссумму взноса'):
        browser.element('.calculate-contract__row [name="base_sum"]').set(min_vznos)
        FillPersonalData().submit()
        browser.element('.risks.calculate-contract__group').with_(timeout=10).should(be.visible)

def vznos_plus_001(min_vznos):
    with allure.step(f'Вводим ссумму взноса плюс 1 копейка'):
        browser.element('.calculate-contract__row [name="base_sum"]').set(min_vznos + 0.01)
        FillPersonalData().submit()
        browser.element('.risks.calculate-contract__group').with_(timeout=10).should(be.visible)

def vznos_max_minus_001(min_vznos):
    vibor_programmy(2)
    vznos(min_vznos-0.01)

def vznos_max(min_vznos):
    vibor_programmy(2)
    vznos(min_vznos)

def vznos_max_plus_001(min_vznos):
    with allure.step(f'Вводим ссумму взноса'):
        vibor_programmy(2)
        browser.element('.calculate-contract__row [name="base_sum"]').set(min_vznos + 0.01)
        FillPersonalData().submit()
        browser.element('.el-message--error').with_(timeout=10).should(be.visible)

def vibor_programmy(number):
    browser.all('.collapsable-info-block__content .program')[2].element('.el-form-item__content').click()

def error_vibor():
    browser.element('.el-message--error').with_(timeout=10).should(be.visible)

def passed_vibor():
    browser.element('.risks.calculate-contract__group').with_(timeout=10).should(be.visible)

#avg vznos
def vznos_avg_no_program(avg_vznos):
    with allure.step(f'Вводим ссумму взноса'):
        browser.element('.calculate-contract__row [name="base_sum"]').set(avg_vznos)
        FillPersonalData().submit()
        error_vibor()

def vznos_avg_program(min_vznos):
    with allure.step(f'Вводим ссумму взноса'):
        vibor_programmy(2)
        browser.element('.calculate-contract__row [name="base_sum"]').set(min_vznos)
        FillPersonalData().submit()
        passed_vibor()

def vznos_avg_program_plus001(min_vznos):
    with allure.step(f'Вводим ссумму взноса'):
        vibor_programmy(2)
        browser.element('.calculate-contract__row [name="base_sum"]').set(min_vznos + 0.01)
        FillPersonalData().submit()
        passed_vibor()

def vznos_avg_no_program_plus001(avg_vznos):
    with allure.step(f'Вводим ссумму взноса'):
        browser.element('.calculate-contract__row [name="base_sum"]').set(avg_vznos + 0.01)
        FillPersonalData().submit()
        error_vibor()


#average_vznos
#Ввести 1 500 000 и выбрать галочку - всё хорошо
#Ввести 1 500 000 и НЕ выбрать галочку - ошибка

#Ввести 1 500 000.01 и НЕ выбрать галочку - ошибка
#Ввести 1 500 000.01 и выбрать галочку - всё хорошо

#Ввести 1 499 999.99 и НЕ выбрать галочку - всё хорошо
#Ввести 1 499 999.99 и выбрать галочку - ошибка
def vznos_avg_no_program_minus001(avg_vznos):
    with allure.step(f'Вводим ссумму взноса'):
        browser.element('.calculate-contract__row [name="base_sum"]').set(avg_vznos - 1)
        FillPersonalData().submit()
        passed_vibor()

def vznos_avg_program_minus001(min_vznos):
    with allure.step(f'Вводим ссумму взноса'):
        vibor_programmy(2)
        browser.element('.calculate-contract__row [name="base_sum"]').set(min_vznos - 1)
        FillPersonalData().submit()
        error_vibor()
