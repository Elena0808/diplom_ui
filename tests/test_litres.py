import pytest
from litres.models import app
import os
import allure
from allure_commons.types import Severity
from dotenv import load_dotenv
from litres.models.data import data_home_page, data_rmd_search, data_my_books
from litres.models.data.data_genre import Formats, Language


@pytest.mark.skip('Тест перегружает систему')
@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Elena0808')
@allure.description('Проверка авторизации')
@allure.feature('Проверка авторизации с валидными данными (os.getenv("EMAIL")')
@allure.link('https://www.litres.ru')
def test_authorization_valid_data():
    load_dotenv()
    app.login_page.open_page() \
        .click_login() \
        .login_by_email(os.getenv('EMAIL')) \
        .sent_password(os.getenv('PASSWORD')) \
        .check_successes_auth()


@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Elena0808')
@allure.description('Проверка авторизации')
@allure.feature('Проверка отображния окна регистрации при вводе email, который отсутствует в системе')
@allure.link('https://www.litres.ru')
def test_auth_with_not_exist_email():
    app.login_page.open_page() \
        .click_login() \
        .login_by_email('ed23iufdeflwkjf.kwef@test.test') \
        .check_open_windows_registration()


@pytest.mark.skip('Тест перегружает систему')
@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Elena0808')
@allure.description('Проверка авторизации')
@allure.feature('Проверка авторизации с не валидным паролем')
@allure.link('https://www.litres.ru')
def test_auth_not_valid_password():
    app.login_page.open_page() \
        .click_login() \
        .login_by_email(os.getenv('EMAIL')) \
        .sent_password('12345678') \
        .check_error_auth()


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Elena0808')
@allure.description('Проверка поиска книг')
@allure.feature('Проверка поиска отсутствующей книги')
@allure.link('https://www.litres.ru')
def test_error_search_book():
    app.home_page.open_page(). \
        search_book(data_home_page.not_valid_name_book) \
        .check_error_search_book()


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Elena0808')
@allure.description('Проверка поиска книг')
@allure.feature('Проверка поиска существующей книги')
@allure.link('https://www.litres.ru')
def test_valid_search_book():
    app.home_page.open_page() \
        .search_book(data_home_page.valid_name_book) \
        .check_valid_search_book(data_home_page.valid_name_book)


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Elena0808')
@allure.description('Проверка поиска книг')
@allure.feature(f'Проверка поиска поиска книг по заданным параметрам: {Language.English} и {Formats.Text}')
@allure.link('https://www.litres.ru')
def test_search_with_language_and_format():
    app.home_page.open_page() \
        .open_genres(data_home_page.easy_reading)
    app.genre_page \
        .set_format([Formats.Text]) \
        .set_language([Language.English]) \
        .check_set_format() \
        .check_set_language()


@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Elena0808')
@allure.description('Добавление в корзину')
@allure.feature('Проверка добавления книги в корзину неавторизоваттым пользователем')
@allure.link('https://www.litres.ru')
def test_add_book_in_basket():
    load_dotenv()
    app.login_page.open_page()
    app.my_books.clean_basket()
    app.home_page.open_page() \
        .search_book(data_home_page.book_to_read)
    app.rmd_search_page.open_search_book(data_rmd_search.href_read_book)
    app.book_page.add_in_basket() \
        .close_popap() \
        .open_my_books()
    app.my_books.open_new_basket()
    app.book_page.check_add_in_basket()


@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Elena0808')
@allure.description('Списки')
@allure.feature(f'Создание нового списка с наименованием {data_my_books.name}')
@allure.link('https://www.litres.ru')
def test_creating_new_folder_list():
    load_dotenv()
    app.login_page.open_page() \
        .click_login() \
        .login_by_email(os.getenv('EMAIL2')) \
        .sent_password(os.getenv('PASSWORD2')) \
        .open_my_books()
    app.my_books \
        .open_my_folders_list() \
        .create_new_folder(data_my_books.name)\
        .check_create_new_folder(data_my_books.name)


def test_error_open_pats_book_without_auth():
    app.home_page.open_page() \
        .search_book(data_home_page.book_to_read)
    app.rmd_search_page.open_search_book(data_rmd_search.href_read_book)
    app.book_page.open_read_part()
