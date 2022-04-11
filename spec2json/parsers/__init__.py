from __future__ import annotations

from typing import TypeAlias, cast

from bs4 import BeautifulSoup, Tag

from spec2json.exceptions import UnknownSpecFormatError
from spec2json.parsers.bikeshed import BikeshedParser
from spec2json.parsers.ecmarkup import EcmarkupParser
from spec2json.parsers.wattsi import WattsiParser

__all__ = [
    "BikeshedParser",
    "EcmarkupParser",
    "Parser",
    "WattsiParser",
    "get_parser_class",
]

Parser: TypeAlias = BikeshedParser | EcmarkupParser | WattsiParser


def get_parser_class(soup: BeautifulSoup) -> type[Parser]:
    """Find a suitable parser for the given spec soup."""
    meta_tag = cast(Tag | None, soup.find("meta", {"name": "generator"}))
    if meta_tag and "Bikeshed" in meta_tag["content"]:
        return BikeshedParser
    if soup.find("emu-clause"):
        return EcmarkupParser
    if soup.find("html", {"lang": "en-US-x-hixie"}):
        return WattsiParser
    raise UnknownSpecFormatError("Cannot get parser for unknown spec format")
