# Configuration

Optional behavior is controlled through **`requests_api.conf`**. Resolution order matches other DLRSP Django apps (for example **django-iubenda**, **copyai**):

1. Top-level Django settings whose names start with **`REQUESTS_API_`** (when set).
2. **`settings.APP_CONFIG["requests_api"]`** — a dict of short keys (see table).
3. Defaults in **`requests_api.defaults`**.

```python
from requests_api import (
    get_requests_api_cached_clients_maxsize,
    get_requests_api_default_request_timeout,
)
```

## Keys under `APP_CONFIG["requests_api"]`

| Key | Django setting | Meaning |
|-----|----------------|---------|
| `CACHED_CLIENTS_MAXSIZE` | `REQUESTS_API_CACHED_CLIENTS_MAXSIZE` | Upper bound on how many different base URLs `requests_api_for_base` keeps in memory. Default `8`. If `0` or negative, no caching: every call builds a new `RequestsApi`. |
| `DEFAULT_REQUEST_TIMEOUT` | `REQUESTS_API_DEFAULT_REQUEST_TIMEOUT` | Seconds, or omit. Default is `None`. The package does **not** add `timeout=` to HTTP calls by itself; use `get_requests_api_default_request_timeout()` when you want one place to read a project-wide default and pass it into `get` / `post` / etc. |

## `settings.py` example

```python
APP_CONFIG = {
    "requests_api": {
        "CACHED_CLIENTS_MAXSIZE": 16,
        "DEFAULT_REQUEST_TIMEOUT": 30.0,
    },
}

REQUESTS_API_CACHED_CLIENTS_MAXSIZE = 4  # wins over APP_CONFIG for this key only
```

## Tests

If you toggle cache-related settings between tests, call **`clear_requests_api_client_cache()`** (exported from `requests_api`) so the next `requests_api_for_base` call does not see stale instances.

## Further reading

- [Home](../index.md) — install and API overview.
- [Example project](example.md) — clone and run the demo branch.
