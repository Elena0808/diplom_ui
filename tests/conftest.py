import pytest
from selene.support.shared import browser
import os


@pytest.fixture(scope='function', autouse=True)
def driver_managment():
    browser.config.base_url = 'https://www.litres.ru'
    browser.config.window_height, browser.config.window_width = 1000, 1300
    browser.config.timeout = float(os.getenv('selene.timeout', '7'))
    browser.config.hold_browser_open = True

    yield
    browser.quit()

