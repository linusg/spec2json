from __future__ import annotations

from dataclasses import dataclass
from typing import TypeAlias, Union

__all__ = ["NestedAlgorithmSteps", "Section"]


NestedAlgorithmSteps: TypeAlias = list[Union[str, "NestedAlgorithmSteps"]]  # type: ignore


@dataclass
class Section:
    url: str
    id: str
    number: str
    title: str
    algorithm_steps: NestedAlgorithmSteps
