"""Tests for normalize_api_language, copy_get_params_with_overrides, requests_api_for_base."""

from django.test import RequestFactory, SimpleTestCase

from requests_api import (
    RequestsApi,
    copy_get_params_with_overrides,
    normalize_api_language,
    requests_api_for_base,
)


class NormalizeApiLanguageTests(SimpleTestCase):
    def test_primary_subtag(self):
        self.assertEqual(
            normalize_api_language(
                "it-it",
                allowed=frozenset({"it", "en"}),
                fallback="en",
            ),
            "it",
        )

    def test_fallback_when_not_allowed(self):
        self.assertEqual(
            normalize_api_language(
                "zh-hans",
                allowed=frozenset({"it", "en"}),
                fallback="en",
            ),
            "en",
        )

    def test_none_uses_fallback(self):
        self.assertEqual(
            normalize_api_language(
                None,
                allowed=frozenset({"de"}),
                fallback="de",
            ),
            "de",
        )


class CachedClientTests(SimpleTestCase):
    def test_same_instance_same_base(self):
        a = requests_api_for_base("https://example.com")
        b = requests_api_for_base("https://example.com")
        self.assertIs(a, b)
        self.assertIsInstance(a, RequestsApi)

    def test_different_base_different_instance(self):
        a = requests_api_for_base("https://a.example.com")
        b = requests_api_for_base("https://b.example.com")
        self.assertIsNot(a, b)


class CopyGetParamsTests(SimpleTestCase):
    def test_overrides_lang(self):
        rf = RequestFactory()
        request = rf.get("/x/", {"lang": "zh-hans", "foo": "bar"})
        request.LANGUAGE_CODE = "it"
        q = copy_get_params_with_overrides(request, lang="en")
        self.assertEqual(q["lang"], "en")
        self.assertEqual(q["foo"], "bar")
