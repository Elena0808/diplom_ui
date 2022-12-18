import time

from selene import have
from selene.support.shared import browser
from litres.models.pages.home_page import HomePage


class MyBooks(HomePage):
    def __int__(self):
        return

    def open_page_my_books(self):
        browser.open('/pages/my_books_all/')
        return self

    def open_my_books_all(self):
        browser.element('[href="/pages/my_books_all/"]').click()
        return self

    def open_my_books_fresh(self):
        browser.element('[href="/pages/my_books_fresh/"]').click()
        return self

    def open_my_views(self):
        browser.element('[href="/pages/my_views/"]').click()
        return self

    def open_new_liked(self):
        browser.element('[href="/pages/new_liked/"]').click()
        return self

    def open_new_basket(self):
        browser.element('[href="/pages/new_basket/"]').click()
        return self

    def clean_basket(self):
        browser.open('/pages/new_basket/')
        element = browser.all('[class*="btn_link"]')
        if len(element) > 0:
            element[0].click()
        return self

    def open_my_folders_list(self):
        browser.element('[href="/pages/my_folders_list/"]').click()
        return self

    def create_new_folder(self, name):
        browser.element('[class="my_folders__new"]').click()
        browser.element('[id="editCaption"]').type(name)
        browser.element('[id="editCaptionYesButton"]').click()
        time.sleep(3)
        return self

    def check_create_new_folder(self, name):
        browser.element('[id="folderCaptionWrap"]').should(have.text(name))
        return self
