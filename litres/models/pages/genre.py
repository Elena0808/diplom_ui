from typing import Tuple
from selene.support.shared import browser
from selene import have
from litres.models.controls.checkbox import select_checkbox
from litres.models.data.data_genre import Formats, Language
from litres.models.pages.home_page import HomePage


class GenrePage(HomePage):
    def __init__(self):
        return

    def set_format(self, formats: Tuple[Formats]):
        for format in formats:
            select_checkbox(f'[for="art_types-{format.value}"]')
        return self

    def set_language(self, languages: Tuple[Language]):
        for language in languages:
            select_checkbox(f'[for="languages-{language.value}"]')
        return self

    def check_set_format(self):
        browser.all('[class="Chips__left_zb6Ix Chips__isClosable_LsZtD"]')[0].should(have.text('Текст'))
        return self

    def check_set_language(self):
        browser.all('[class="Chips__left_zb6Ix Chips__isClosable_LsZtD"]')[1].should(have.text('Английский'))
        return self
