import pytest
from litres.models import app
import os
import allure
from allure_commons.types import Severity
from dotenv import load_dotenv
from litres.models.data import data_home_page, data_rmd_search, data_my_books
from litres.models.data.data_genre import Formats, Language


@pytest.mark.skip('Тест вызывает капчу при пакетном запуске')
@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Elena0808')
@allure.description('Проверка авторизации')
@allure.feature(f'Проверка авторизации с валидными данными {os.getenv("EMAIL")} и валидным паролем')
@allure.link('https://www.litres.ru')
def test_authorization_valid_data():
    with allure.step('Открываем главную страницу ЛитРеса'):
        load_dotenv()
    with allure.step('Открываем форму авторизации и вводим валидные логин и пароль'):
        app.login_page.open_page() \
            .click_login() \
            .login_by_email(os.getenv('EMAIL')) \
            .sent_password(os.getenv('PASSWORD'))
    with allure.step('Проверяем успешность авторизации'):
        app.login_page.check_successes_auth()


@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Elena0808')
@allure.description('Проверка авторизации')
@allure.feature('Проверка отображния окна регистрации при вводе email, который отсутствует в системе')
@allure.link('https://www.litres.ru')
def test_auth_with_not_exist_email():
    with allure.step('Открываем главную страницу ЛитРеса и форму авторизации'):
        app.login_page.open_page() \
            .click_login()
    with allure.step('Вводим емейл который отсутствует в системе'):
        app.login_page.login_by_email('ed23iufdeflwkjf.kwef@test.test')
    with allure.step('Проверяем, что появилось сообщение о предложении регистрации'):
        app.login_page.check_open_windows_registration()


@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Elena0808')
@allure.description('Проверка авторизации')
@allure.feature('Проверка авторизации с не валидным паролем')
@allure.link('https://www.litres.ru')
def test_auth_not_valid_password():
    with allure.step(
            'Открываем главную страницу и вводим в форму авторизации валидный логин и не валидный пароль'):
        app.login_page.open_page() \
            .click_login() \
            .login_by_email(os.getenv('EMAIL')) \
            .sent_password('12345678')
    with allure.step('Проверяем получение ошибки авторизации'):
        app.login_page.check_error_auth()


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Elena0808')
@allure.description('Проверка поиска книг')
@allure.feature('Проверка поиска отсутствующей книги')
@allure.link('https://www.litres.ru')
def test_error_search_book():
    with allure.step('Открываем главную страницу ЛитРеса и вводим в строку поиска несуществующее наименование книги'):
        app.home_page.open_page(). \
            search_book(data_home_page.not_valid_name_book)
    with allure.step('Проверяем получение пустого поиска'):
        app.home_page.check_error_search_book()


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Elena0808')
@allure.description('Проверка поиска книг')
@allure.feature('Проверка поиска существующей книги')
@allure.link('https://www.litres.ru')
def test_valid_search_book():
    with allure.step(
            f'Открываем главную страницу и вводим в строку поска наименование книги: {data_home_page.valid_name_book}'):
        app.home_page.open_page() \
            .search_book(data_home_page.valid_name_book)
    with allure.step('Проверяем результат поиска'):
        app.home_page.check_valid_search_book(data_home_page.valid_name_book)


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Elena0808')
@allure.description('Проверка поиска книг')
@allure.feature('Проверка поиска книг по заданным параметрам: English и Текст')
@allure.link('https://www.litres.ru')
def test_search_with_language_and_format():
    with allure.step('Открываем главную страницу и переходим в Жанры, выбираем "Легкое чтение"'):
        app.home_page.open_page() \
            .open_genres(data_home_page.easy_reading)
    with allure.step(f'В фильтрах проставляем {Formats.Text} и {Language.English}'):
        app.genre_page \
            .set_format([Formats.Text]) \
            .set_language([Language.English])
    with allure.step('Проверяем, что фильтры проставлены и книги отфильтрованы'):
        app.genre_page.check_set_format().check_set_language()


@pytest.mark.skip('отрабатывает локально')
@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Elena0808')
@allure.description('Добавление в корзину')
@allure.feature('Проверка добавления книги в корзину неавторизованным пользователем')
@allure.link('https://www.litres.ru')
def test_add_book_in_basket():
    with allure.step('Открываем главную страницу ЛитРеса'):
        load_dotenv()
    with allure.step(
            f'Переходим на главную страницу и вводим в поиске наименование книги {data_home_page.book_to_read}'):
        app.home_page.open_page() \
            .search_book(data_home_page.book_to_read)
    with allure.step('Открываем найденную книгу'):
        app.rmd_search_page.open_serch_book_valid()
    with allure.step('Добавляем книгу в корзину'):
        app.book_page.add_in_basket() \
            .close_popap() \
            .open_my_books()
    with allure.step('Проверяем, что книга добавлена в корзину'):
        app.my_books.open_new_basket()
        app.book_page.check_add_in_basket()


@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Elena0808')
@allure.description('Списки')
@allure.feature(f'Создание нового списка с наименованием {data_my_books.name}')
@allure.link('https://www.litres.ru')
def test_creating_new_folder_list():
    with allure.step('Открываем главную страницу ЛитРеса'):
        load_dotenv()
    with allure.step('Авторизуемся и открываем страницу "Мои книги'):
        app.login_page.open_page() \
            .click_login() \
            .login_by_email(os.getenv('EMAIL2')) \
            .sent_password(os.getenv('PASSWORD2')) \
            .open_my_books()
    with allure.step('Создаем новый список книг'):
        app.my_books \
            .open_my_folders_list() \
            .create_new_folder(data_my_books.name)
    with allure.step('Проверяем, что новый список создан'):
        app.my_books.check_create_new_folder(data_my_books.name)


def test_error_open_pats_book_without_auth():
    with allure.step(
            f'Открываем главную страницу и вводим в поисковую строку название книги {data_home_page.book_to_read}'):
        app.home_page.open_page() \
            .search_book(data_home_page.book_to_read)
    with allure.step('Открываем найденную книгу'):
        app.rmd_search_page.open_search_book(data_rmd_search.href_read_book)
    with allure.step('Открываем фрагмент книги на чтение'):
        app.book_page.open_read_part()
