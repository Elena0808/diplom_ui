from selene.support.shared import browser
from litres.models.pages.home_page import HomePage


class RmdSearchPage(HomePage):
    def __int__(self):
        return

    def open_search_book(self, href_read_book):
        browser.element(f'[href="{href_read_book}"]').click()
        return self
