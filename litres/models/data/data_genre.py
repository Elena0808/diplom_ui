from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Formats(Enum):
    Text = 'text_book'
    Audio = 'audiobook'


class Language(Enum):
    English = 'en'
    Belarusian = 'be'
    Spanish = 'es'
    Lithuanian = 'lt'
    German = 'de'
    Polish = 'pl'
    Russian = 'ru'
    Ukrainian = 'uk'
    Finnish = 'fi'
    French = 'fr'

