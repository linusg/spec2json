import pytest

from spec2json.numbering import NumberingStyle
from spec2json.parsers import BikeshedParser


@pytest.mark.parametrize(
    "level,expected",
    [
        (0, NumberingStyle.DECIMAL),
        (1, NumberingStyle.DECIMAL),
        (2, NumberingStyle.DECIMAL),
        (3, NumberingStyle.DECIMAL),
        (4, NumberingStyle.DECIMAL),
        (5, NumberingStyle.DECIMAL),
        (6, NumberingStyle.DECIMAL),
    ],
)
def test_bikeshed_parser__numbering_style_for_level(level, expected):
    assert BikeshedParser.numbering_style_for_level(level) == expected
