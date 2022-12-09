import time
from selene import have
from selene.support.shared import browser


class HomePage:
    def __init__(self):
        return

    def open_page(self):
        browser.open('/')
        time.sleep(6)
        return self

    def search_book(self, text):
        browser.element('[name="q"]').type(text).click()
        browser.element('[type="submit"]').click()
        return self

    def open_genres(self, href):
        browser.element('[href="/pages/new_genres/"]').click()
        browser.element(f'[href="{href}"]').click()
        return self

    def open_tab_new(self):
        browser.element('[id="newbooks"]').click()
        return self

    def open_tab_popular(self):
        browser.element('[data-goal="popbooks"]').click()
        return self

    def open_tab_audiobook(self):
        browser.element('[data-goal="audiobooks"]').click()
        return self

    def open_what_to_read(self):
        browser.element('[data-goal="whattoreadbooks"]').click()
        return self

    def open_selection_tab(self):
        browser.element('[href="/podborki/"]').click()
        return self

    def open_self_publishing_tab(self):
        browser.element('[href="/selfpublishing/"]').click()
        return self

    def open_promo_code_tab(self):
        browser.element('[id="promocode"]').click()
        return self

    def open_my_books(self):
        browser.element('[class="MyBooks-modules__myBooksLink"]').click()
        return self

    def check_error_search_book(self):
        browser.element('[class="SearchTitle-module__title__empty_horcZ"]').should(have.text('Ничего не найдено'))
        browser.element('[class="SearchTitle-module__subtitle__empty_3-hJs"]') \
            .should(have.text('Попробуйте изменить запрос'))
        browser.element('[class="SearchResultEmpty-module__interesting_title_3Yrfz"]') \
            .should(have.text('Возможно, вас заинтересует'))
        return self

    def check_valid_search_book(self, text):
        browser.element('[class="SearchTitle-module__title_YEbWG"]').should(have.text(text))
        browser.element('[alt="Приключения Шерлока Холмса: Собака Баскервилей / The Hound of the Baskervilles"]')
        return self
