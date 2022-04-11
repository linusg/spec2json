from __future__ import annotations

from enum import Enum, auto
from typing import Callable

from spec2json.spec import NestedAlgorithmSteps

__all__ = ["NumberingStyle", "number_and_flatten_algorithm_steps"]


def int_to_alpha(number: int) -> str:
    result = []
    while number > 0:
        letter = chr(ord("a") + (number - 1 % 26))
        number -= 26
        result.append(letter)
    return "".join(result)


def int_to_roman(number: int) -> str:
    result = []
    roman_numerals = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    for arabic, roman in roman_numerals:
        factor, number = divmod(number, arabic)
        result.append(roman * factor)
        if number == 0:
            break
    return "".join(result).lower()


class NumberingStyle(Enum):
    DECIMAL = auto()
    ALPHA = auto()
    ROMAN = auto()


NUMBERING_FUNCTIONS = {
    NumberingStyle.DECIMAL: lambda x: str(x),
    NumberingStyle.ALPHA: int_to_alpha,
    NumberingStyle.ROMAN: int_to_roman,
}


def number_and_flatten_algorithm_steps(
    algorithm_steps: NestedAlgorithmSteps,
    numbering_style_for_level: Callable[[int], NumberingStyle],
    level: int = 0,
) -> list[str]:
    processed_steps = []
    i = 0
    for step in algorithm_steps:
        if isinstance(step, list):
            processed_steps.extend(
                number_and_flatten_algorithm_steps(
                    step, numbering_style_for_level, level + 1
                )
            )
            continue
        i += 1
        numbering_function = NUMBERING_FUNCTIONS[numbering_style_for_level(level)]
        processed_steps.append(f"{numbering_function(i)}. {step}")
    return processed_steps
