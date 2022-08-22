import os

from selene.support.shared import browser

url = os.getenv('URL_FRONT')

def browser_params_1920():
    browser.open(url)
    browser.driver.set_window_size(width=1920, height=1080)
