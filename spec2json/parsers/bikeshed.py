from __future__ import annotations

from spec2json.numbering import NumberingStyle
from spec2json.parsers.base import BaseParser
from spec2json.spec import Section

__all__ = ["BikeshedParser"]


class BikeshedParser(BaseParser):
    @staticmethod
    def numbering_style_for_level(_: int) -> NumberingStyle:
        return NumberingStyle.DECIMAL

    def parse_sections(self) -> list[Section]:
        raise NotImplementedError("The Bikeshed spec parser is not implemented yet.")
