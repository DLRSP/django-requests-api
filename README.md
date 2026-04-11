# django-requests-api [![PyPi license](https://img.shields.io/pypi/l/django-requests-api.svg)](https://pypi.python.org/pypi/django-requests-api)

[![PyPi status](https://img.shields.io/pypi/status/django-requests-api.svg)](https://pypi.python.org/pypi/django-requests-api)
[![PyPi version](https://img.shields.io/pypi/v/django-requests-api.svg)](https://pypi.python.org/pypi/django-requests-api)
[![PyPi python version](https://img.shields.io/pypi/pyversions/django-requests-api.svg)](https://pypi.python.org/pypi/django-requests-api)
[![PyPi downloads](https://img.shields.io/pypi/dm/django-requests-api.svg)](https://pypi.python.org/pypi/django-requests-api)
[![PyPi downloads](https://img.shields.io/pypi/dw/django-requests-api.svg)](https://pypi.python.org/pypi/django-requests-api)
[![PyPi downloads](https://img.shields.io/pypi/dd/django-requests-api.svg)](https://pypi.python.org/pypi/django-requests-api)

## GitHub ![GitHub release](https://img.shields.io/github/tag/DLRSP/django-requests-api.svg) ![GitHub release](https://img.shields.io/github/release/DLRSP/django-requests-api.svg)

## Test [![codecov.io](https://codecov.io/github/DLRSP/django-requests-api/coverage.svg?branch=master)](https://codecov.io/github/DLRSP/django-requests-api?branch=master) [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/DLRSP/django-requests-api/master.svg)](https://results.pre-commit.ci/latest/github/DLRSP/django-requests-api/master) [![gitthub.com](https://github.com/DLRSP/django-requests-api/actions/workflows/ci.yaml/badge.svg)](https://github.com/DLRSP/django-requests-api/actions/workflows/ci.yaml)

## Check Demo Project
* Browser the demo app on-line on [Heroku](https://django-requests-api.herokuapp.com/)
* Check the demo repo on [GitHub](https://github.com/DLRSP/example/tree/django-requests-api)

## Requirements
-   Python 3.8+ supported.
-   Django 4.2+ supported.

## Setup
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

Paths are joined to `base_url` with a single slash (with or without leading/trailing slashes on either part). If the path is already an absolute URL (`http://` or `https://`), it is used as-is. The package declares a dependency on **requests** (see `install_requires`).

### Reusable helpers

`RequestsApi` lives in `requests_api.requests_api`; the utilities are in `requests_api.helpers`. All are re-exported from the package root so you can still use `from requests_api import …`.

```python
from requests_api import (
    copy_get_params_with_overrides,
    normalize_api_language,
    requests_api_for_base,
)

# Map Django language to an API that only supports a subset of codes
lang = normalize_api_language(
    request.LANGUAGE_CODE,
    allowed=("it", "en"),
    fallback="en",
)

# Outbound GET: keep the browser query string but force lang=
params = copy_get_params_with_overrides(request, lang=lang)

# One shared Session / connection pool per base URL in the process
client = requests_api_for_base("https://www.example.com")
r = client.get("api/resource", params=params, timeout=30)
```

## Run Example Project

```shell
git clone --depth=50 --branch=django-requests-api https://github.com/DLRSP/example.git DLRSP/example
cd DLRSP/example
python manage.py runserver
```

Now browser the app @ http://127.0.0.1:8000
