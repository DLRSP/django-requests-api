"""
Resolved requests_api configuration (lazy reads from ``django.conf.settings``).

Priority for each value:

1. Top-level Django setting (e.g. ``REQUESTS_API_CACHED_CLIENTS_MAXSIZE``), if defined.
2. Partial override inside ``settings.APP_CONFIG["requests_api"]`` (merged onto
   :mod:`requests_api.defaults`).
3. Package defaults from :mod:`requests_api.defaults`.

Example::

    APP_CONFIG = {
        "requests_api": {
            "CACHED_CLIENTS_MAXSIZE": 16,
            "DEFAULT_REQUEST_TIMEOUT": 30.0,
        },
    }

    REQUESTS_API_CACHED_CLIENTS_MAXSIZE = 4  # overrides APP_CONFIG for this key only
"""

from __future__ import annotations

from typing import Any

from django.conf import settings

from . import defaults

_UNSET = object()


def _app_config_requests_api() -> dict[str, Any]:
    cfg = getattr(settings, "APP_CONFIG", None) or {}
    block = cfg.get("requests_api")
    return dict(block) if isinstance(block, dict) else {}


def get_requests_api_cached_clients_maxsize() -> int:
    """
    Max number of distinct base URLs cached by :func:`requests_api.helpers.requests_api_for_base`.

    If ``0`` or negative, caching is disabled (each call returns a new client).
    """
    v = getattr(settings, "REQUESTS_API_CACHED_CLIENTS_MAXSIZE", _UNSET)
    if v is not _UNSET and v is not None:
        return int(v)
    nested = _app_config_requests_api().get("CACHED_CLIENTS_MAXSIZE")
    if nested is not None:
        return int(nested)
    return int(defaults.CACHED_CLIENTS_MAXSIZE)


def get_requests_api_default_request_timeout() -> float | None:
    """
    Optional default timeout in seconds for HTTP calls.

    ``None`` means no default is applied by this package; callers still pass
    ``timeout=`` to :class:`requests_api.requests_api.RequestsApi` methods when needed.
    """
    v = getattr(settings, "REQUESTS_API_DEFAULT_REQUEST_TIMEOUT", _UNSET)
    if v is not _UNSET:
        if v is None:
            return None
        return float(v)
    nested = _app_config_requests_api().get("DEFAULT_REQUEST_TIMEOUT")
    if nested is not None:
        return float(nested)
    d = defaults.DEFAULT_REQUEST_TIMEOUT
    return float(d) if d is not None else None
