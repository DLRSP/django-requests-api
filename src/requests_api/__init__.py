"""
See PEP 386 (https://peps.python.org/pep-0386/)
"""

from .conf import (
    get_requests_api_cached_clients_maxsize,
    get_requests_api_default_request_timeout,
)
from .helpers import (
    clear_requests_api_client_cache,
    copy_get_params_with_overrides,
    normalize_api_language,
    requests_api_for_base,
)
from .requests_api import RequestsApi

__all__ = [
    "RequestsApi",
    "clear_requests_api_client_cache",
    "copy_get_params_with_overrides",
    "get_requests_api_cached_clients_maxsize",
    "get_requests_api_default_request_timeout",
    "normalize_api_language",
    "requests_api_for_base",
]

__version__ = "0.8.2"
__version_info__ = tuple(int(i) if i.isdigit() else i for i in __version__.split("."))
__license__ = "MIT"
__title__ = "requests_api"

__author__ = "DLRSP"
__copyright__ = "Copyright 2010-present DLRSP"

# Version synonym
VERSION = __version_info__

# Header encoding (see RFC5987)
HTTP_HEADER_ENCODING = "iso-8859-1"

# Default datetime input and output formats
ISO_8601 = "iso-860-1"
