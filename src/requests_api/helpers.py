"""Module-level helpers for language/query params and shared HTTP clients."""

from __future__ import annotations

from collections.abc import Collection
from functools import lru_cache

from django.http import HttpRequest

from .requests_api import RequestsApi


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


@lru_cache(maxsize=8)
def requests_api_for_base(base_url: str) -> RequestsApi:
    """
    Return a cached :class:`RequestsApi` for *base_url*.

    One session per distinct *base_url* in the process, so TCP connections can
    be reused.
    """
    return RequestsApi(base_url)
