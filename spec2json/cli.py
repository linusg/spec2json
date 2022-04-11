from __future__ import annotations

import json

import click
import httpx

from spec2json.exceptions import InvalidSpecContentTypeError, UnknownSpecFormatError
from spec2json.numbering import number_and_flatten_algorithm_steps
from spec2json.parsers import get_parser_class
from spec2json.utils import get_html, get_soup


@click.command(
    help=(
        "Extract section metadata and algorithm steps from specification HTML "
        "documents as JSON. Supported formats are Bikeshed (various Web specs), "
        "Ecmarkup (ECMAScript), and Wattsi (HTML standard)."
    ),
)
@click.option(
    "--numbered",
    is_flag=True,
    default=False,
    help="Turn nested algorithm steps into numbered, flattened steps.",
)
@click.option(
    "--url-format",
    help="Python format string to make a URL from each given spec name.",
)
@click.argument(
    "specs",
    nargs=-1,
)
def main(numbered: bool, url_format: str | None, specs: list[str]) -> None:
    if not url_format:
        urls = specs
    else:
        urls = [url_format.format(spec) for spec in specs]
    data = {}
    for i, url in enumerate(urls):
        click.echo(f"Spec {i+1}/{len(urls)}: {url}", err=True)

        click.echo("-> Downloading", err=True)
        try:
            html = get_html(url)
        except (
            httpx.RequestError,
            httpx.HTTPStatusError,
            InvalidSpecContentTypeError,
        ) as e:
            raise click.ClickException(str(e))

        click.echo("-> Parsing HTML", err=True)
        soup = get_soup(html)

        click.echo("-> Determining suitable spec parser", err=True)
        try:
            parser_class = get_parser_class(soup)
        except UnknownSpecFormatError as e:
            raise click.ClickException(str(e))

        click.echo(f"-> Parsing spec sections using {parser_class.__name__}", err=True)
        parser = parser_class(url, soup)
        try:
            sections = parser.parse_sections()
        except NotImplementedError as e:
            raise click.ClickException(str(e))

        click.echo("-> Numbering and flattening algorithm steps", err=True)
        if numbered:
            for section in sections:
                section.algorithm_steps = number_and_flatten_algorithm_steps(
                    section.algorithm_steps, parser.numbering_style_for_level
                )

        click.echo(f"-> Done, parsed {len(sections)} sections", err=True)
        data[url] = [vars(section) for section in sections]

    click.echo(json.dumps(data))
