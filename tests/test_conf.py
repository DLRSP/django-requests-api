"""Tests for requests_api.conf (APP_CONFIG and top-level settings)."""

from django.test import SimpleTestCase, override_settings

from requests_api.conf import (
    get_requests_api_cached_clients_maxsize,
    get_requests_api_default_request_timeout,
)


class RequestsApiConfTests(SimpleTestCase):
    def test_cached_clients_maxsize_default(self):
        self.assertEqual(get_requests_api_cached_clients_maxsize(), 8)

    @override_settings(
        APP_CONFIG={"requests_api": {"CACHED_CLIENTS_MAXSIZE": 3}}
    )
    def test_cached_clients_maxsize_from_app_config(self):
        self.assertEqual(get_requests_api_cached_clients_maxsize(), 3)

    @override_settings(
        REQUESTS_API_CACHED_CLIENTS_MAXSIZE=7,
        APP_CONFIG={"requests_api": {"CACHED_CLIENTS_MAXSIZE": 3}},
    )
    def test_cached_clients_maxsize_top_level_over_app_config(self):
        self.assertEqual(get_requests_api_cached_clients_maxsize(), 7)

    def test_default_request_timeout_none_by_default(self):
        self.assertIsNone(get_requests_api_default_request_timeout())

    @override_settings(
        APP_CONFIG={"requests_api": {"DEFAULT_REQUEST_TIMEOUT": 42.5}}
    )
    def test_default_request_timeout_from_app_config(self):
        self.assertEqual(get_requests_api_default_request_timeout(), 42.5)

    @override_settings(
        REQUESTS_API_DEFAULT_REQUEST_TIMEOUT=15.0,
        APP_CONFIG={"requests_api": {"DEFAULT_REQUEST_TIMEOUT": 99.0}},
    )
    def test_default_request_timeout_top_level_over_app_config(self):
        self.assertEqual(get_requests_api_default_request_timeout(), 15.0)

    @override_settings(REQUESTS_API_DEFAULT_REQUEST_TIMEOUT=None)
    def test_default_request_timeout_explicit_none(self):
        self.assertIsNone(get_requests_api_default_request_timeout())
