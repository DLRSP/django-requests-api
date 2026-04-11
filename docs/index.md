# django-requests-api

Small Django app: a `requests.Session` wrapper with a fixed base URL, plus helpers for language codes and query strings. Use it when several views talk to the same HTTP API and you want connection reuse and predictable URL joining.

---

## Requirements

- Python 3.8 or newer
- Django 4.2 or newer (see the package metadata for the exact matrix)

We test against current patch releases of supported Python and Django versions.

## Installation

```shell
pip install django-requests-api
```

Add the app to `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    # ...
    "requests_api",
    # ...
)
```

## Basic usage

```python
from requests_api import RequestsApi

client = RequestsApi("https://api.publicapis.org")
r = client.get("/entries")
print(r.json())

github = RequestsApi(
    "https://api.github.com",
    headers={"Authorization": "token abcdef"},
)
r = github.get("/user", headers={"Accept": "application/json"})
print(r.text)
```

Relative paths are joined to `base_url` with a single slash. Paths that already start with `http://` or `https://` are left as-is. The library depends on the **requests** package.

## Helpers

`RequestsApi` is defined in `requests_api.requests_api`. Shared utilities live in `requests_api.helpers` and are re-exported from the top-level package:

```python
from requests_api import (
    copy_get_params_with_overrides,
    normalize_api_language,
    requests_api_for_base,
)

lang = normalize_api_language(
    request.LANGUAGE_CODE,
    allowed=("it", "en"),
    fallback="en",
)
params = copy_get_params_with_overrides(request, lang=lang)
client = requests_api_for_base("https://www.example.com")
r = client.get("api/resource", params=params, timeout=30)
```

`requests_api_for_base` returns one client per distinct base URL inside the process, up to a configurable limit (see [Configuration](tutorial/configuration.md)).

## Configuration

Optional settings (cache size for `requests_api_for_base`, optional default timeout helper) are read through `requests_api.conf`: Django settings `REQUESTS_API_*`, then `APP_CONFIG["requests_api"]`, then `requests_api.defaults`. Details: [Configuration](tutorial/configuration.md).

## Example project

The [DLRSP/example](https://github.com/DLRSP/example) repo has a **`django-requests-api`** branch with a runnable demo. Clone steps: [Example project](tutorial/example.md).

There is also a [Heroku demo](https://django-requests-api.herokuapp.com/) (if still deployed).

## Contributing

Clone the repo, run the test suite, open a PR: [Contributing](community/contributing.md).

## References

Links to **requests**, Django settings, other packages that ship this client, and an [HTTP status code cheat sheet](community/http-status-codes.md): [References](community/references.md).

## Security

Do not open security issues in public trackers. Email [dlrsp.issue@gmail.com](mailto:dlrsp.issue@gmail.com) with a description; maintainers will coordinate a fix before public disclosure.

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
