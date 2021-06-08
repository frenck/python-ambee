# Python: Ambee API Client

[![GitHub Release][releases-shield]][releases]
[![Python Versions][python-versions-shield]][pypi]
![Project Stage][project-stage-shield]
![Project Maintenance][maintenance-shield]
[![License][license-shield]](LICENSE.md)

[![Build Status][build-shield]][build]
[![Code Coverage][codecov-shield]][codecov]
[![Code Quality][code-quality-shield]][code-quality]
[![Deepcode.ai][deepcode-shield]][deepcode]

[![Sponsor Frenck via GitHub Sponsors][github-sponsors-shield]][github-sponsors]

[![Support Frenck on Patreon][patreon-shield]][patreon]

Asynchronous Python client for the Ambee API.

## About

This is a simple asynchronous Python client library for the Ambee API.

Ambee fuses the power of thousands of on-ground sensor data and hundreds of
remote imagery from satellites. Their state-of-the-art AI and ML techniques with
proprietary models analyze environmental factors such as air quality, soil,
micro weather, pollen, and more to help millions worldwide say safe and protect
themselves.

Get a free API key for 100 requests a day (or paid if you want more) here:

<https://api-dashboard.getambee.com/#/signup>

## Installation

```bash
pip install ambee
```

## Usage

```python
import asyncio

from ambee import Ambee


async def main():
    """Show example on getting Ambee data."""
    async with Ambee(api_key="example_api_key", latitude=12, longitude=77) as client:
        air_quality = await client.air_quality()
        print(air_quality)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

## Changelog & Releases

This repository keeps a change log using [GitHub's releases][releases]
functionality.

Releases are based on [Semantic Versioning][semver], and use the format
of `MAJOR.MINOR.PATCH`. In a nutshell, the version will be incremented
based on the following:

- `MAJOR`: Incompatible or major changes.
- `MINOR`: Backwards-compatible new features and enhancements.
- `PATCH`: Backwards-compatible bugfixes and package updates.

## Contributing

This is an active open-source project. We are always open to people who want to
use the code or contribute to it.

We've set up a separate document for our
[contribution guidelines](CONTRIBUTING.md).

Thank you for being involved! :heart_eyes:

## Setting up development environment

This Python project is fully managed using the [Poetry][poetry] dependency
manager. But also relies on the use of NodeJS for certain checks during
development.

You need at least:

- Python 3.7+
- [Poetry][poetry-install]
- NodeJS 12+ (including NPM)

To install all packages, including all development requirements:

```bash
npm install
poetry install
```

As this repository uses the [pre-commit][pre-commit] framework, all changes
are linted and tested with each commit. You can run all checks and tests
manually, using the following command:

```bash
poetry run pre-commit run --all-files
```

To run just the Python tests:

```bash
poetry run pytest
```

## Authors & contributors

The original setup of this repository is by [Franck Nijhof][frenck].

For a full list of all authors and contributors,
check [the contributor's page][contributors].

## License

MIT License

Copyright (c) 2021 Franck Nijhof

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[build-shield]: https://github.com/frenck/python-ambee/actions/workflows/tests.yaml/badge.svg
[build]: https://github.com/frenck/python-ambee/actions/workflows/tests.yaml
[code-quality-shield]: https://img.shields.io/lgtm/grade/python/g/frenck/python-ambee.svg?logo=lgtm&logoWidth=18
[code-quality]: https://lgtm.com/projects/g/frenck/python-ambee/context:python
[codecov-shield]: https://codecov.io/gh/frenck/python-ambee/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/frenck/python-ambee
[contributors]: https://github.com/frenck/python-ambee/graphs/contributors
[deepcode-shield]: https://www.deepcode.ai/api/gh/badge?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGF0Zm9ybTEiOiJnaCIsIm93bmVyMSI6ImZyZW5jayIsInJlcG8xIjoicHl0aG9uLWVsZ2F0byIsImluY2x1ZGVMaW50IjpmYWxzZSwiYXV0aG9ySWQiOjI4MDU1LCJpYXQiOjE2MTUxODgzODh9.hJsD6PTw8K8bnTmHUzroQi7XkXRi46bdt-oMqx2zXj0
[deepcode]: https://www.deepcode.ai/app/gh/frenck/python-ambee/_/dashboard?utm_content=gh%2Ffrenck%2Fpython-ambee
[frenck]: https://github.com/frenck
[github-sponsors-shield]: https://frenck.dev/wp-content/uploads/2019/12/github_sponsor.png
[github-sponsors]: https://github.com/sponsors/frenck
[license-shield]: https://img.shields.io/github/license/frenck/python-ambee.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2021.svg
[patreon-shield]: https://frenck.dev/wp-content/uploads/2019/12/patreon.png
[patreon]: https://www.patreon.com/frenck
[poetry-install]: https://python-poetry.org/docs/#installation
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com/
[project-stage-shield]: https://img.shields.io/badge/project%20stage-experimental-yellow.svg
[pypi]: https://pypi.org/project/ambee/
[python-versions-shield]: https://img.shields.io/pypi/pyversions/ambee
[releases-shield]: https://img.shields.io/github/release/frenck/python-ambee.svg
[releases]: https://github.com/frenck/python-ambee/releases
[semver]: http://semver.org/spec/v2.0.0.html
