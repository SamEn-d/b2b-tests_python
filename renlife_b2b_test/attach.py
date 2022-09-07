import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    allure.attach(body=browser.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')

def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')

def add_pagesource(browser):
    allure.attach(browser.driver.page_source, 'page_source', AttachmentType.HTML, '.html')
