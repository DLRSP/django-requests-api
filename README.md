# django-requests-api [![PyPi license](https://img.shields.io/pypi/l/django-requests-api.svg)](https://pypi.python.org/pypi/django-requests-api)

[![PyPi status](https://img.shields.io/pypi/status/django-requests-api.svg)](https://pypi.python.org/pypi/django-requests-api)
[![PyPi version](https://img.shields.io/pypi/v/django-requests-api.svg)](https://pypi.python.org/pypi/django-requests-api)
[![PyPi python version](https://img.shields.io/pypi/pyversions/django-requests-api.svg)](https://pypi.python.org/pypi/django-requests-api)
[![PyPi downloads](https://img.shields.io/pypi/dm/django-requests-api.svg)](https://pypi.python.org/pypi/django-requests-api)
[![PyPi downloads](https://img.shields.io/pypi/dw/django-requests-api.svg)](https://pypi.python.org/pypi/django-requests-api)
[![PyPi downloads](https://img.shields.io/pypi/dd/django-requests-api.svg)](https://pypi.python.org/pypi/django-requests-api)

## GitHub ![GitHub release](https://img.shields.io/github/tag/DLRSP/django-requests-api.svg) ![GitHub release](https://img.shields.io/github/release/DLRSP/django-requests-api.svg)

## Test [![codecov.io](https://codecov.io/github/DLRSP/django-requests-api/coverage.svg?branch=master)](https://codecov.io/github/DLRSP/django-requests-api?branch=master) [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/DLRSP/django-requests-api/master.svg)](https://results.pre-commit.ci/latest/github/DLRSP/django-requests-api/master) [![gitthub.com](https://github.com/DLRSP/django-requests-api/actions/workflows/ci.yml/badge.svg)](https://github.com/DLRSP/django-requests-api/actions/workflows/ci.yml)

## Check Demo Project
* Browser the demo app on-line on [Heroku](https://django-requests-api.herokuapp.com/)
* Check the demo repo on [GitHub](https://github.com/DLRSP/example/tree/django-requests-api)

## Requirements
-   Python 3.8+ supported.
-   Django 3.2+ supported.

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

## Run Example Project

```shell
git clone --depth=50 --branch=django-requests-api https://github.com/DLRSP/example.git DLRSP/example
cd DLRSP/example
python manage.py runserver
```

Now browser the app @ http://127.0.0.1:8000
