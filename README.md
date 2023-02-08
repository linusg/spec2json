# spec2json

> Extract section metadata and algorithm steps from specification HTML documents
> as JSON.

[![PyPI](https://img.shields.io/pypi/v/spec2json)](https://pypi.org/project/spec2json/)
![Python Version](https://img.shields.io/pypi/pyversions/spec2json)
[![License: MIT](https://img.shields.io/github/license/linusg/spec2json?color=d63e97)](https://github.com/linusg/spec2json/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/imports-isort-1674b1?labelColor=ef8336)](https://pycqa.github.io/isort/)

## Installation

Install from PyPI:

```console
pip3 install spec2json
```

## Usage

See `spec2json --help`.

Example:

```console
spec2json --numbered https://tc39.es/ecma262/ https://tc39.es/ecma402/ > ecmascript.json
```

## Supported formats

- [Bikeshed](https://tabatkins.github.io/bikeshed/) (various Web specs),
- [Ecmarkup](https://tc39.es/ecmarkup/) (ECMAScript)
- [Wattsi](https://github.com/whatwg/wattsi) (HTML standard)
