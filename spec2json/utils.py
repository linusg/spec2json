from __future__ import annotations

from typing import cast

import httpx
from bs4 import BeautifulSoup, Tag

from spec2json.exceptions import InvalidSpecContentTypeError, UnknownSpecFormatError
from spec2json.parsers import BikeshedParser, EcmarkupParser, Parser

__all__ = ["get_html", "get_soup", "get_parser_class"]


def get_html(url: str) -> str:
    """Download HTML from the given URL."""
    response = httpx.get(url)
    response.raise_for_status()
    if (content_type := response.headers["Content-Type"]).split(";")[0] != "text/html":
        raise InvalidSpecContentTypeError(
            f"Expected spec content type to be 'text/html', got '{content_type}'"
        )
    return response.text


def get_soup(html: str) -> BeautifulSoup:
    """Parse the given HTML string."""
    return BeautifulSoup(html, features="html5lib")
