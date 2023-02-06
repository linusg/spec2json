import pytest

from spec2json.numbering import int_to_alpha, int_to_roman


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
