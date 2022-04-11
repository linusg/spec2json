from __future__ import annotations

from abc import ABC, abstractmethod

from bs4 import BeautifulSoup

from spec2json.numbering import NumberingStyle
from spec2json.spec import Section

__all__ = ["BaseParser"]


class BaseParser(ABC):
    def __init__(self, spec_url: str, soup: BeautifulSoup) -> None:
        self.spec_url = spec_url
        self.soup = soup

    @staticmethod
    @abstractmethod
    def numbering_style_for_level(level: int) -> NumberingStyle:
        ...

    @abstractmethod
    def parse_sections(self) -> list[Section]:
        ...
