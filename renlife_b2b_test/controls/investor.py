from selene.support.shared import browser


def investor_question(number: int = None):
    browser.all('.program')[number].element('.el-radio-button:nth-child(2)').click()

def investor_question_all():
    browser.all('.program')[0].element('.el-radio-button:nth-child(2)').click()
    browser.all('.program')[1].element('.el-radio-button:nth-child(2)').click()
    browser.all('.program')[2].element('.el-radio-button:nth-child(2)').click()
    browser.all('.program')[3].element('.el-radio-button:nth-child(2)').click()
    browser.all('.program')[4].element('.el-radio-button:nth-child(2)').click()
