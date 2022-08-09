import os
import pytest
from selenium import webdriver
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

import os.path
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# from python_demoqa import attach
# from renlife_b2b_test.path_to_directory import path_to_download_resources
from renlife_b2b_test import attach
from renlife_b2b_test.path_to_directory import filename

DEFAULT_BROWSER_VERSION = "104.0"

def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='104.0'
    )

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

def path_to_download_resources():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": os.path.join(filename(), 'tmp'),
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.config.driver = driver
    browser.config.hold_browser_open = True

@pytest.fixture(scope='function')
def setup_browser(request):
    # options = webdriver.ChromeOptions()
    # prefs = {
    #     "download.default_directory": os.path.join(filename(), 'tmp'),
    #     "download.prompt_for_download": False
    # }
    # options.add_experimental_option("prefs", prefs)
    #
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # browser.config.driver = driver
    # browser.config.hold_browser_open = True
    path_to_download_resources()
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "104.0",
        "selenoid:options": {
            "enableVNC": False,
            "enableVideo": False
        }
    }
    options.capabilities.update(selenoid_capabilities)

    # login = os.getenv('LOGIN')
    # password = os.getenv('PASSWORD')
    selenoid_browser = os.getenv('BROWSER')
    #command_executor = f"https://user1:1234@selenoid.autotests.cloud/wd/hub",

    # driver = webdriver.Remote(
    #     command_executor=f"http://{selenoid_browser}:4444/wd/hub",
    #     options=options
    # )
    # browser.config.driver = driver

    yield browser
    # attach.add_pagesource(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    # attach.add_video(browser)
    browser.quit()
    ...