# References

## Core stack

- **[requests](https://requests.readthedocs.io/en/latest/)** — HTTP library used under the hood.
- **[Django settings](https://docs.djangoproject.com/en/stable/topics/settings/)** — where `APP_CONFIG` and `REQUESTS_API_*` live.
- **[HTTP status codes](http-status-codes.md)** — short reference when handling `response.status_code`.

## Other Django / Python packages

Any project can depend on **django-requests-api**; you only need `requests_api` in `INSTALLED_APPS` and a normal install from PyPI or VCS.

### Known open-source consumers (GitHub)

These repositories under **[github.com/DLRSP](https://github.com/DLRSP)** are discovered with GitHub code search. Queries and exclusions live in **[`.github/used-in.yaml`](https://github.com/DLRSP/django-requests-api/blob/main/.github/used-in.yaml)**. The table between the HTML markers is **refreshed automatically** by the reusable [`update-used-in`](https://github.com/DLRSP/workflows/blob/main/.github/workflows/update-used-in.yaml) workflow (weekly on this repository).

<!-- used-in:auto-table-start -->
| Repository | Role |
|------------|------|
| [django-iubenda](https://github.com/DLRSP/django-iubenda) | Django application for privacy and cookies policy managed by Iubenda. |
<!-- used-in:auto-table-end -->

The **[example](https://github.com/DLRSP/example)** repo is the shared demo workspace; use the branch named after the package you are trying. It may not appear in the table until the search index picks up matching files.

If a public consumer is missing, extend the markers in `README.md` / `references.md` only when you change the manual text around them—otherwise wait for the next scheduled sync or open a PR that updates the generated block.

Private sites and forks are expected to use **django-requests-api** as well; they are not listed here.
