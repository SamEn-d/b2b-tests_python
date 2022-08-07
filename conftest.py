import os
import pytest
from selenium import webdriver
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

# from python_demoqa import attach

DEFAULT_BROWSER_VERSION = "104.0"

def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='104.0'
    )

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "104.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }
    options.capabilities.update(selenoid_capabilities)

    # login = os.getenv('LOGIN')
    # password = os.getenv('PASSWORD')
    selenoid_browser = os.getenv('BROWSER')
    # command_executor = f"http://{login}:{password}@185.221.152.138:4444/wd/hub",
    driver = webdriver.Remote(
        command_executor=f"http://{selenoid_browser}:4444/wd/hub",
        options=options
    )
    browser.config.driver = driver
    # browser = Browser(Config(driver))

    yield browser
    # attach.add_pagesource(browser)
    # attach.add_screenshot(browser)
    # attach.add_logs(browser)
    # attach.add_video(browser)
    browser.quit()