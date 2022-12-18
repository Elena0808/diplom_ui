import pytest
from dotenv import load_dotenv
from selene import Browser, Config
from selenium import webdriver
from selene.support.shared import browser
import os
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function', autouse=False)
def driver_managment():
    browser.config.base_url = 'https://www.litres.ru'
    browser.config.window_height, browser.config.window_width = 1000, 1300
    browser.config.timeout = float(os.getenv('selene.timeout', '12'))
    browser.config.hold_browser_open = True

    yield
    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def driver_managment_remote():
    load_dotenv()
    browser.config.base_url = 'https://www.litres.ru'
    browser.config.window_height = 1500
    browser.config.window_width = 1800
    browser.config.timeout = float(os.getenv('selene.timeout', '15'))
    login_selenoid = os.getenv('LOGIN_SELENOID')
    password_selenoid = os.getenv('PASSWORD_SELENOID')
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": '100.0',
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f"https://{login_selenoid}:{password_selenoid}@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver
