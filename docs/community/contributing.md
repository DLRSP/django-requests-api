# Contributing

## Issues and discussions

- **Bug reports and feature ideas:** [GitHub issues](https://github.com/DLRSP/django-requests-api/issues).
- **Usage questions:** [GitHub discussions](https://github.com/DLRSP/django-requests-api/discussions) if enabled, otherwise open an issue and label it as support.

Please search existing issues first and mention the package version, Python, and Django you use.

## Development setup

Fork [django-requests-api](https://github.com/DLRSP/django-requests-api), clone your fork, then:

```shell
python -m venv env
source env/bin/activate
# Windows: env\Scripts\activate

pip install -r requirements/py312-django42.txt
# Or another requirements/*.txt line that matches your environment.

pre-commit install
```

Style checks run via **pre-commit** on CI; keep changes PEP 8–friendly.

## Tests

From the repository root:

```shell
python runtests.py
python runtests.py -q
python runtests.py tests.test_conf
```

With **pytest** directly (uses `tests.settings` from `pyproject.toml`):

```shell
pytest tests/
```

## Documentation

Docs are Markdown under `docs/`. Build locally:

```shell
pip install mkdocs mkdocs-material
mkdocs serve
```

Write in clear English; short paragraphs beat long essays.

## Pull requests

Open a PR from a branch (not `main`/`master`). Run the test suite before you push. If you add behavior, add or extend tests.

## Code of conduct

Stay polite and professional. For broader norms, see the [Django code of conduct](https://www.djangoproject.com/conduct/).
