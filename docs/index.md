Django's application to provide simple and shared requests client.

---

## Requirements

These packages are required:

-   Python 3.8+ supported.
-   Django 3.2+ supported.

We **highly recommend** and only officially support the latest patch release of each Python and Django series.


## Installation

1. Install from **pip**:
```shell
pip install django-requests-api
```

2. Modify `settings.py` by adding the app to `INSTALLED_APPS`:
```python
INSTALLED_APPS = (
    # ...
    "requests_api",
    # ...
)
```

## Usage

```shell
from requests_api import RequestsApi

client = RequestsApi("https://api.publicapis.org")
r = client.get("/entries")
print(r.json())

github = RequestsApi("https://api.github.com", headers={"Authorization": "token abcdef"})
r = github.get("/user", headers={"Accept": "application/json"})
print(r.text)
```

## Example

Let's take a look at a quick example of using this project to build a simple App with **custom error pages**.

* Check the demo repo on [GitHub][github-demo]

## Quickstart

Can't wait to get started? The [quickstart guide][quickstart] is the fastest way to get up and running and building a **demo App**.

## Customize

Do you want custom solutions? The [customize][customize] section is an overview of which part are easy to design.
If you find how to personalize different scenarios or behaviors, a [pull request][pull-request] is welcome!

## Development

See the [Contribution guidelines][contributing] for information on how to clone  the repository, run the test suite and contribute changes back to django-requests-api.

## Security

If you believe you’ve found something in this project which has security implications, please **do not raise the issue in a public forum**.

Send a description of the issue via email to [dlrsp.issue@gmail.com][security-mail].  The project maintainers will then work with you to resolve any issues where required, prior to any public disclosure.

## License

MIT License

Copyright (c) 2010-present DLRSP (https://dlrsp.org) and other contributors.

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

[index]: .
[github-demo]: https://github.com/DLRSP/example/tree/django-requests-api
[python-requests]: http://docs.python-requests.org/en/master/api/
[requests-api]: https://gist.github.com/stefansundin/96b655f1512d1ce9d570e008dbe122d3

[quickstart]: tutorial/example.md

[contributing]: community/contributing.md
[pull-request]: community/contributing.png#pull-request

[security-mail]: mailto:dlrsp.issue@gmail.com
