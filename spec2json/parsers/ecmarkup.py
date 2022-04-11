from __future__ import annotations

from typing import Iterable, cast

from bs4 import Tag

from spec2json.numbering import NumberingStyle
from spec2json.parsers.base import BaseParser
from spec2json.spec import NestedAlgorithmSteps, Section

__all__ = ["EcmarkupParser"]


def join_and_normalize_strings(parts: Iterable[str]) -> str:
    s = "".join(parts).strip()
    # Non-breaking space gets turned into a regular one when copying
    # from the spec, so we do the same here.
    s = s.replace("\xa0", " ")
    # Collapse whitespace
    s = s.replace("\n", " ")
    while "  " in s:
        s = s.replace("  ", " ")
    return s


def parse_emu_alg_entry(li_tag: Tag) -> str:
    """Parse a <li> tag from an <emu-alg> <ol> tag."""
    for sup_tag in li_tag.find_all("sup"):
        sup_tag.replace_with(f"^{join_and_normalize_strings(sup_tag.strings)}")
    return join_and_normalize_strings(li_tag.strings)


def parse_emu_alg_list(ol_tag: Tag) -> NestedAlgorithmSteps:
    """Recursively parse <ol> tags from an <emu-alg> tag."""
    li_tags = ol_tag.find_all("li", recursive=False)
    steps: NestedAlgorithmSteps = []
    for li_tag in li_tags:
        if nested_ol_tag := li_tag.find("ol", recursive=False):
            nested_ol_tag.extract()
        steps.append(parse_emu_alg_entry(li_tag))
        if nested_ol_tag:
            steps.append(parse_emu_alg_list(nested_ol_tag))
    return steps


def parse_emu_alg(emu_alg_tag: Tag) -> NestedAlgorithmSteps:
    """Parse algorithm steps from an <emu-alg> tag."""
    ol_tag = cast(Tag, emu_alg_tag.find("ol", recursive=False))
    return parse_emu_alg_list(ol_tag)


def parse_emu_clause(spec_url: str, emu_clause_tag: Tag) -> Section:
    """Parse metadata and algorithm steps from an <emu-clause> tag."""
    h1_tag = cast(Tag, emu_clause_tag.find("h1", recursive=False))
    emu_alg_tag = cast(Tag | None, emu_clause_tag.find("emu-alg", recursive=False))
    id_ = cast(str, emu_clause_tag["id"])
    number, *title_strings = list(h1_tag.strings)
    title = join_and_normalize_strings(title_strings)
    algorithm_steps = parse_emu_alg(emu_alg_tag) if emu_alg_tag else []
    return Section(
        url=f"{spec_url}#{id_}",
        id=id_,
        number=number,
        title=title,
        algorithm_steps=algorithm_steps,
    )


class EcmarkupParser(BaseParser):
    @staticmethod
    def numbering_style_for_level(level: int) -> NumberingStyle:
        return [
            NumberingStyle.DECIMAL,
            NumberingStyle.ALPHA,
            NumberingStyle.ROMAN,
        ][level % 3]

    def parse_sections(self) -> list[Section]:
        """Extract and parse all <emu-clause> tags from the spec."""
        emu_clause_tags = self.soup.find_all("emu-clause")
        return [
            parse_emu_clause(self.spec_url, emu_clause)
            for emu_clause in emu_clause_tags
        ]
