from selene.support.shared import browser


def browser_params_1920():
    browser.open('https://b2b.cloud-test.renlife.com/')
    browser.driver.set_window_size(width=1920, height=1080)
