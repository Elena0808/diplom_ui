import os
from selene import have
from selene.support.shared import browser
from litres.models.pages.home_page import HomePage
import time


class LoginPage(HomePage):
    def __init__(self):
        return

    def click_login(self):
        browser.element('[href="/pages/login/"]').click()
        return self

    def login_by_email(self, email):
        browser.element('[class*="ButtonV1-module__button__orange"]').click()
        browser.element('[class*="AuthorizationPopup-module__input"]').type(email)
        browser.element('[class*=ButtonV1-module__button__orange]').click()
        time.sleep(4)
        return self

    def login_by_phone(self):
        browser.element('[class*="ButtonV1-module__button__lightgray"]').click()
        return self

    def sent_password(self, password):
        browser.element('input[type="password"]').type(password)
        time.sleep(5)
        browser.element('[class*="ButtonV1-module__button__orange"]').click()
        return self

    def close_popup(self):
        browser.element('[class*="AuthorizationPopup-module__closeIcon"]').click()
        return self

    def check_successes_auth(self):
        browser.element('[class="Profile-module__name"]').should(have.text(os.getenv('LOGIN')))
        return self

    def check_open_windows_registration(self):
        browser.element('//*[@id="__next"]/div[1]/header/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/form/div[1]')\
            .should(have.text('Адрес свободен для регистрации'))
        return self

    def check_error_auth(self):
        browser.element('[class="AuthorizationPopup-module__error"]')\
            .should(have.text('Неверное сочетание логина и пароля'))
        return self
