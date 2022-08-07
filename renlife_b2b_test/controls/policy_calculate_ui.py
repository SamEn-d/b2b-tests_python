from selene import have, command, be
from selene.support.shared import browser


def UI(sum: int = 100000):
    browser.element('.calculate-contract__row [name="base_sum"]').set(sum)

class FillPersonalData():
    def gender(self, gender):
        browser.element('.collapsable-info-block__content [name="gender__0"]').click()
        browser.all('.el-select-dropdown__item').element_by(have.text(gender)).click()
        return self
        # def famale(self):
        #     'Женский'
        # def male(self):
        #     'Мужской'
        # # lambda male: male if male else famale
        # browser.all('.el-select-dropdown__item').element_by(have.text(famale or male)).click()

    def birth_date(self, date: int = '11102000'):
        browser.element('.el-date-editor [name="birth_date__0"]').set(date).press_enter()
        return self

    def surname(self,surname: str = 'Фамилия'):
        browser.element('[name="surname__0"]').set(surname)
        return self

    def name(self,name: str = 'Имя'):
        browser.element('[name="name__0"]').set(name)
        return self

    def midname(self,midname: str = 'Отчество'):
        browser.element('[name="midname__0"]').set(midname)
        return self

    def submit(self):
        browser.element('.calculate-contract__btn-wrapper .kit-el-button').perform(command.js.click)

def policy_results():
    browser.element('.edit-contract__title-text').with_(timeout=30).should(have.text('Результат расчета'))
    browser.all('.calculate-contract__btn-wrapper .kit-el-button').element_by(have.text('Оформить')).perform(command.js.click)

class PolicyUpdateInfo():
    def check(self):
        browser.element('h1').should(have.text('Договор')).with_(timeout=10).should(be.visible)
        return self

    def passport_adress(self, adress: str = 'Адрес'):
        browser.element('.collapsable-info-block .common-data__item_widest .el-input__inner').set(adress)
        return self

    def passport(self, series: int = '1234', number: int = '123456', date: int = '12112020', kod: int = '011028', issued: str = '011028'):
        browser.element('.el-form-item.series .el-input__inner').type(series)
        browser.element('.number-field .el-input__inner').type(number)
        browser.element('.document .date-picker .el-input__inner').type(date).press_enter()
        browser.element('.document [popperclass="document__suggestion-wrapper"]').type(kod).press_enter()
        browser.element('.document .department input').type(issued).press_enter()
        return self
    def phone(self,phone: int = '9625550123'):
        browser.element('.contact-info .phone-input .el-input-group__append .el-input__inner').type(phone).press_enter()
        return self

    def mail(self,mail: str = 'w@wth.su'):
        browser.all('.contact-info .contact-info__item')[1].element('.el-input__inner').type(mail)
        return self

    def adress(self, adress, zip):
        browser.element('.address .address__wrapper .address__item_fluid input').type(adress)
        browser.element('.el-form-item.address__item.address__item_small input').type(zip)
        return self
        # browser.element('[x-placement="bottom-start"] .el-autocomplete-suggestion__wrap.el-scrollbar__wrap').should(
        #     be.visible).click()
        # # browser.element('[x-placement="top-start"] .el-autocomplete-suggestion__wrap.el-scrollbar__wrap').should(be.visible).click()

    def addresses_match(self):
        browser.element('.address .el-checkbox').click()
        return self

    def arrange_DS(self):
        browser.all('.nav-btn-list .kit-el-button').element_by(have.text('Сохранить')).click()