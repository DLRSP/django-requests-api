"""Module-level helpers for language/query params and shared HTTP clients."""

from __future__ import annotations

from collections import OrderedDict
from collections.abc import Collection
from threading import Lock

from django.http import HttpRequest

from . import conf
from .requests_api import RequestsApi

_client_cache: OrderedDict[str, RequestsApi] = OrderedDict()
_client_cache_lock = Lock()


def clear_requests_api_client_cache() -> None:
    """Drop cached clients from :func:`requests_api_for_base` (e.g. in tests)."""
    with _client_cache_lock:
        _client_cache.clear()


def normalize_api_language(
    language_code: str | None,
    *,
    allowed: Collection[str],
    fallback: str,
) -> str:
    """
    Map a BCP-47-like *language_code* to a value allowed by a remote API.

    Uses the primary subtag (segment before the first ``-``). If it is not in
    *allowed* (compared case-insensitively), returns *fallback*.
    """
    allowed_set = frozenset(str(x).strip().lower() for x in allowed if str(x).strip())
    fb = str(fallback).strip().lower() or "en"
    primary = (language_code or fb).strip().lower().split("-", 1)[0]
    if primary in allowed_set:
        return primary
    return fb


def copy_get_params_with_overrides(request: HttpRequest, **overrides: str):
    """
    ``request.GET.copy()`` with string keys in *overrides* replacing or adding
    query parameters (typical pattern: force ``lang=`` for a third-party API).
    """
    q = request.GET.copy()
    for key, value in overrides.items():
        q[key] = value
    return q


def requests_api_for_base(base_url: str) -> RequestsApi:
    """
    Return a cached :class:`RequestsApi` for *base_url*.

    One session per distinct *base_url* in the process (up to
    :func:`requests_api.conf.get_requests_api_cached_clients_maxsize`), so TCP
    connections can be reused. Configure via ``REQUESTS_API_CACHED_CLIENTS_MAXSIZE``
    or ``APP_CONFIG["requests_api"]["CACHED_CLIENTS_MAXSIZE"]``. If the max size
    is ``0`` or negative, caching is disabled and a new client is returned each time.
    """
    base = base_url.rstrip("/")
    maxsize = conf.get_requests_api_cached_clients_maxsize()
    if maxsize <= 0:
        return RequestsApi(base)

    with _client_cache_lock:
        if base in _client_cache:
            _client_cache.move_to_end(base)
            return _client_cache[base]
        client = RequestsApi(base)
        _client_cache[base] = client
        _client_cache.move_to_end(base)
        while len(_client_cache) > maxsize:
            _client_cache.popitem(last=False)
        return client
