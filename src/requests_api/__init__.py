import django
from .requests_api import RequestsApi

__version__ = "0.3.2"
__license__ = "MIT"
__title__ = "requests_api"

__author__ = "DLRSP"
__copyright__ = "Copyright 2010-present DLRSP"

# Version synonym
VERSION = __version__

# Header encoding (see RFC5987)
HTTP_HEADER_ENCODING = "iso-8859-1"

# Default datetime input and output formats
ISO_8601 = "iso-8601"

if django.VERSION < (3, 2):
    default_app_config = "requests_api.apps.RequestsApiConfig"

