from selene.support.shared import browser
from selene import have
from litres.models.pages.home_page import HomePage


class BookPage(HomePage):
    def __int__(self):
        return

    def add_in_basket(self):
        browser.element('[data-action="addbasket"]').click()
        return self

    def add_in_favorite(self):
        browser.element('[data-action="addfavorite"]').click()
        return self

    def mark_read(self):
        browser.element('[class="mark_as_read-btn"]').click()
        return self

    def open_read_part(self):
        browser.element('[data-clicktag-id="read_part"]').click()
        return self

    def close_popap(self):
        browser.all('[class="close"]')[-1].click()
        return self

    def check_add_in_basket(self):
        browser.element('[class="firstString"]').should(have.text('Простые'))
        browser.element('[class="secondString"]').should(have.text('волшебные вещи'))
        return self
