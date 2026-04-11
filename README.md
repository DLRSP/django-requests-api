# django-requests-api [![PyPi license](https://img.shields.io/pypi/l/django-requests-api.svg)](https://pypi.python.org/pypi/django-requests-api)

[![PyPi status](https://img.shields.io/pypi/status/django-requests-api.svg)](https://pypi.python.org/pypi/django-requests-api)
[![PyPi version](https://img.shields.io/pypi/v/django-requests-api.svg)](https://pypi.python.org/pypi/django-requests-api)
[![PyPi python version](https://img.shields.io/pypi/pyversions/django-requests-api.svg)](https://pypi.python.org/pypi/django-requests-api)
[![codecov.io](https://codecov.io/github/DLRSP/django-requests-api/coverage.svg?branch=master)](https://codecov.io/github/DLRSP/django-requests-api?branch=master)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/DLRSP/django-requests-api/master.svg)](https://results.pre-commit.ci/latest/github/DLRSP/django-requests-api/master)
[![CI](https://github.com/DLRSP/django-requests-api/actions/workflows/ci.yaml/badge.svg)](https://github.com/DLRSP/django-requests-api/actions/workflows/ci.yaml)

## Demo

- [Heroku demo](https://django-requests-api.herokuapp.com/) (if still online)
- [Example branch](https://github.com/DLRSP/example/tree/django-requests-api) on DLRSP/example

## Requirements

- Python 3.8+
- Django 4.2+ (see package classifiers for the full matrix)

## Install

```shell
pip install django-requests-api
```

```python
INSTALLED_APPS = (
    # ...
    "requests_api",
    # ...
)
```

## Usage

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

Paths are joined to `base_url` with a single slash. Absolute URLs (`http://` / `https://`) are passed through unchanged. The package depends on **requests** (`install_requires`).

### Helpers

Implementation: `requests_api.requests_api` and `requests_api.helpers`; public imports from the package root:

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

### Configuration (`APP_CONFIG` / `REQUESTS_API_*`)

Read via **`requests_api.conf`**: Django settings first, then **`APP_CONFIG["requests_api"]`**, then defaults.

| `APP_CONFIG["requests_api"]` | Django setting | Notes |
|------------------------------|----------------|--------|
| `CACHED_CLIENTS_MAXSIZE` | `REQUESTS_API_CACHED_CLIENTS_MAXSIZE` | Cap for `requests_api_for_base` (default `8`). `0` or below turns caching off. |
| `DEFAULT_REQUEST_TIMEOUT` | `REQUESTS_API_DEFAULT_REQUEST_TIMEOUT` | Optional seconds; default `None`. Not applied automatically—call `get_requests_api_default_request_timeout()` and pass `timeout=` yourself if you want a shared value. |

```python
from requests_api import get_requests_api_default_request_timeout

timeout = get_requests_api_default_request_timeout()
client = requests_api_for_base("https://api.example.com")
r = client.get("v1/x", timeout=timeout if timeout is not None else 30)
```

In tests, call **`clear_requests_api_client_cache()`** when you change cache settings. Full write-up: `docs/tutorial/configuration.md` (MkDocs: *Tutorials → Configuration*).

## Run the example locally

```shell
git clone --depth=50 --branch=django-requests-api https://github.com/DLRSP/example.git example-requests-api
cd example-requests-api
python manage.py runserver
```

Then open http://127.0.0.1:8000 (install dependencies from that repo’s `requirements/` first).

## Docs

MkDocs sources live under `docs/`. See [Contributing](docs/community/contributing.md) for `mkdocs serve`.

- [References & ecosystem](docs/community/references.md)
- [HTTP status codes (quick reference)](docs/community/http-status-codes.md)

## Used in

Public GitHub projects that reference **django-requests-api** / `requests_api` (weekly sync via [`.github/used-in.yaml`](.github/used-in.yaml) and [`update-used-in`](https://github.com/DLRSP/workflows/blob/main/.github/workflows/update-used-in.yaml)):

<!-- used-in:auto-start -->
- ![GitHub stars](https://img.shields.io/github/stars/DLRSP/django-iubenda?label=%E2%AD%90&style=flat-square) [django-iubenda](https://github.com/DLRSP/django-iubenda#readme) — Django application for privacy and cookies policy managed by Iubenda.
<!-- used-in:auto-end -->

Missing a project? Open a PR or run the workflow manually in your fork.

## License

MIT — see [LICENSE](LICENSE).
