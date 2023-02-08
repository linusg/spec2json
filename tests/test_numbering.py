import pytest

from spec2json.numbering import (
    int_to_alpha,
    int_to_roman,
    number_and_flatten_algorithm_steps,
)
from spec2json.parsers import EcmarkupParser

from tests.fixtures.ecmarkup import TEMPORAL_TO_LOCALTIME_SECTIONS


@pytest.mark.parametrize(
    "number,expected",
    [
        (1, "a"),
        (2, "b"),
        (3, "c"),
        (26, "z"),
        (27, "aa"),
        (28, "ab"),
        (52, "az"),
        (53, "ba"),
        (702, "zz"),
        (703, "aaa"),
    ],
)
def test_int_to_alpha(number, expected):
    assert int_to_alpha(number) == expected


@pytest.mark.parametrize(
    "number,expected",
    [
        (1, "i"),
        (2, "ii"),
        (3, "iii"),
        (4, "iv"),
        (5, "v"),
        (6, "vi"),
        (9, "ix"),
        (10, "x"),
        (1666, "mdclxvi"),
    ],
)
def test_int_to_roman(number, expected):
    assert int_to_roman(number) == expected


def test_number_and_flatten_algorithm_steps():
    section = TEMPORAL_TO_LOCALTIME_SECTIONS[0]
    assert number_and_flatten_algorithm_steps(
        section.algorithm_steps, EcmarkupParser.numbering_style_for_level
    ) == [
        "1. Assert: Type(t) is BigInt.",
        '2. If calendar is "gregory", then',
        "a. Let timeZoneOffset be GetNamedTimeZoneOffsetNanoseconds(timeZone, t).",
        "b. Let tz be ℝ(t) + timeZoneOffset.",
        "c. Return a record with fields calculated from tz according to Table 18.",
        "3. Else,",
        "a. Return a record with the fields of Column 1 of Table 18 calculated from ℝ(t) for the given calendar and timeZone. The calculations should use best available information about the specified calendar and timeZone, including current and historical information about time zone offsets from UTC and daylight saving time rules. Given the same values of t, calendar, and timeZone, the result must be the same for the lifetime of the surrounding agent.",
    ]
