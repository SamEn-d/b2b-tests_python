import os.path

import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def filename():
    from pathlib import Path
    return (
        Path(os.path.abspath(__file__))
        .parent
        .parent
        .joinpath('resources')
        # .joinpath('koren.txt')
        .absolute()
        .__str__()
    )


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