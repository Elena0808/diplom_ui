from selene.support.shared import browser
from litres.models.pages.home_page import HomePage


class RmdSearchPage(HomePage):
    def __int__(self):
        return

    #локально отрабатывает, а selenoid падает на этом методе c InvalidSessionIdException
    def open_search_book(self, href_read_book):
        browser.element(f'[href="{href_read_book}"]').click()
        return self

    def open_serch_book_valid(self):
        browser.element('[href="/maks-fray/prostye-volshebnye-veschi/"]').click()
        return self
