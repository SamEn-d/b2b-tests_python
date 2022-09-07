import allure
from selene import by, be
from selene.support.shared import browser

from renlife_b2b_test.controls.policy_calculate_ui import FillPersonalData

def vznos_minus_001(min_vznos):
    with allure.step(f'Вводим ссумму взноса минус 1 копейка'):
        base_sum_set(min_vznos, -0.01)
        message_error()

def vznos(min_vznos):
    with allure.step(f'Вводим ссумму взноса'):
        base_sum_set(min_vznos)
        message_passed()

def vznos_plus_001(min_vznos):
    with allure.step(f'Вводим ссумму взноса плюс 1 копейка'):
        base_sum_set(min_vznos, 0.01)
        message_passed()


def vznos_max_minus_001(max_vznos):
    with allure.step(f'Вводим ссумму взноса {max_vznos}'):
        vibor_programmy(2)
        base_sum_set(max_vznos, -0.01)
        message_passed()


def vznos_max(max_vznos):
    with allure.step(f'Вводим ссумму взноса {max_vznos}'):
        vibor_programmy(2)
        base_sum_set(max_vznos)
        message_passed()

def vznos_max_plus_001(max_vznos):
    with allure.step(f'Вводим ссумму взноса {max_vznos}'):
        vibor_programmy(2)
        base_sum_set(max_vznos, 0.01)
        message_error()

#avg vznos
def vznos_avg_no_program(avg_vznos):
    with allure.step(f'Вводим ссумму взноса {avg_vznos}'):
        base_sum_set(avg_vznos)
        message_error()

def vznos_avg_program(avg_vznos):
    with allure.step(f'Вводим ссумму взноса {avg_vznos}'):
        vibor_programmy(2)
        base_sum_set(avg_vznos)
        message_passed()

def vznos_avg_program_plus001(avg_vznos):
    with allure.step(f'Вводим ссумму взноса {avg_vznos}'):
        vibor_programmy(2)
        base_sum_set(avg_vznos, 0.01)
        message_passed()

def vznos_avg_no_program_plus001(avg_vznos):
    with allure.step(f'Вводим ссумму взноса {avg_vznos}'):
        base_sum_set(avg_vznos, 0.01)
        message_error()

def vznos_avg_no_program_minus001(avg_vznos):
    with allure.step(f'Вводим ссумму взноса {avg_vznos}'):
        base_sum_set(avg_vznos, -1)
        message_passed()

def vznos_avg_program_minus001(avg_vznos):
    with allure.step(f'Вводим ссумму взноса {avg_vznos}'):
        vibor_programmy(2)
        base_sum_set(avg_vznos, -1)
        message_error()

def vibor_programmy(number):
    with allure.step(f'Выбор программы от 1,5 млн.'):
        browser.all('.collapsable-info-block__content .program')[number].element('.el-form-item__content').click()

def base_sum_set(vznos: int = None,operation:float = 0):
    return browser.element('.calculate-contract__row [name="base_sum"]').set(vznos + operation)

def message_error():
    FillPersonalData().submit()
    with allure.step(f'Всплывающее окно ошибки'):
        browser.element('.el-message--error').with_(timeout=10).should(be.visible)

def message_passed():
    FillPersonalData().submit()
    with allure.step(f'Результат рсчёта ДС'):
        browser.element('.risks.calculate-contract__group').with_(timeout=10).should(be.visible)
