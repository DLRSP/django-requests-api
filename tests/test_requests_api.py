"""Unit Tests for the module"""
import logging

from django.test import TestCase
from requests_api import RequestsApi

LOGGER = logging.getLogger(name="django-requests-api")


class ErrorsTestCase(TestCase):
    """Test Case for django-requests-api"""

    def setUp(self):
        """Set up common assets for tests"""
        LOGGER.debug("Tests setUp")

    def tearDown(self):
        """Remove Test Data"""
        LOGGER.debug("Tests tearDown")

    def test_init_client(self):
        """Test the initialization of client"""
        LOGGER.debug("Test the initialization of client")
        api_client = RequestsApi("https://fakeapiurl.com")
        self.assertIsInstance(api_client, RequestsApi)

    def test_init_client_without_parameters(self):
        """Test the initialization of client without parameters"""
        LOGGER.debug("Test the initialization of client without parameters")
        self.assertRaises(TypeError, lambda: RequestsApi())

