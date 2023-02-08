import pytest

from spec2json.numbering import NumberingStyle
from spec2json.parsers import EcmarkupParser
from spec2json.utils import get_soup

from tests.fixtures.ecmarkup import (
    ECMA262_MATH_OBJECT_HTML,
    ECMA262_MATH_OBJECT_SECTIONS,
    TEMPORAL_CALENDAR_DATE_TO_ISO_HTML,
    TEMPORAL_CALENDAR_DATE_TO_ISO_SECTIONS,
    TEMPORAL_TO_LOCALTIME_HTML,
    TEMPORAL_TO_LOCALTIME_SECTIONS,
)


@pytest.fixture
def ecmarkup_parser(request):
    soup = get_soup(request.param)
    return EcmarkupParser("https://tc39.es/ecma262/", soup)


@pytest.mark.parametrize(
    "level,expected",
    [
        (0, NumberingStyle.DECIMAL),
        (1, NumberingStyle.ALPHA),
        (2, NumberingStyle.ROMAN),
        (3, NumberingStyle.DECIMAL),
        (4, NumberingStyle.ALPHA),
        (5, NumberingStyle.ROMAN),
        (6, NumberingStyle.DECIMAL),
    ],
)
def test_ecmarkup_parser__numbering_style_for_level(level, expected):
    assert EcmarkupParser.numbering_style_for_level(level) == expected


@pytest.mark.parametrize(
    "ecmarkup_parser,expected",
    [
        ("", []),
        (ECMA262_MATH_OBJECT_HTML, ECMA262_MATH_OBJECT_SECTIONS),
        (TEMPORAL_CALENDAR_DATE_TO_ISO_HTML, TEMPORAL_CALENDAR_DATE_TO_ISO_SECTIONS),
        (TEMPORAL_TO_LOCALTIME_HTML, TEMPORAL_TO_LOCALTIME_SECTIONS),
    ],
    indirect=["ecmarkup_parser"],
)
def test_ecmarkup_parser__parse_sections(ecmarkup_parser, expected):
    assert ecmarkup_parser.parse_sections() == expected
