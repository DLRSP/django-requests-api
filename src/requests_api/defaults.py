"""
Default values for the requests_api app.

Runtime resolution (Django ``settings`` + optional ``APP_CONFIG['requests_api']``) is in
:mod:`requests_api.conf`. Projects do not need to import this module from ``settings.py``.
"""

from __future__ import annotations

# Maximum distinct base URLs kept by :func:`requests_api.helpers.requests_api_for_base`.
CACHED_CLIENTS_MAXSIZE = 8

# Optional default HTTP timeout (seconds) for outbound calls. ``None`` means the library
# does not inject a timeout; pass ``timeout=`` explicitly or use
# :func:`requests_api.conf.get_requests_api_default_request_timeout` in your code.
DEFAULT_REQUEST_TIMEOUT: float | None = None
