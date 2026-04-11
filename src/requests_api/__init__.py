"""
See PEP 386 (https://peps.python.org/pep-0386/)
"""

from .helpers import (
    copy_get_params_with_overrides,
    normalize_api_language,
    requests_api_for_base,
)
from .requests_api import RequestsApi

__version__ = "0.6.1"
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
