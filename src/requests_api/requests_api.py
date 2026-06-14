from __future__ import annotations

from http.cookiejar import Cookie

import requests


class RequestsApi:
    """Thin ``requests.Session`` wrapper with a configurable base URL."""

    def __init__(self, base_url: str | bytes, src_addr: str = "", **kwargs):
        self.base_url = base_url
        self.session = requests.Session()
        if src_addr:
            self.session = self.set_src_addr(src_addr)
        for arg in kwargs:
            if isinstance(kwargs[arg], dict):
                kwargs[arg] = self.__deep_merge(
                    getattr(self.session, arg), kwargs[arg]
                )
            setattr(self.session, arg, kwargs[arg])

    @staticmethod
    def join_base_url(base_url: str | bytes, url: str | bytes) -> str:
        """
        Join *base_url* and *url* with exactly one ``/`` between them.

        If *url* is already absolute (``http://`` or ``https://``), *url* is returned
        unchanged so callers can bypass the base when needed.
        """
        b = (
            base_url.decode("utf-8")
            if isinstance(base_url, bytes)
            else str(base_url)
        )
        u = url.decode("utf-8") if isinstance(url, bytes) else str(url)
        u = u.strip()
        if u.startswith(("http://", "https://")):
            return u
        return b.rstrip("/") + "/" + u.lstrip("/")

    def set_src_addr(self, src_addr: str) -> requests.Session:
        """
        Set bind to the specified local address rather than auto-selecting it
        """
        for prefix in ("http://", "https://"):
            self.session.get_adapter(prefix).init_poolmanager(
                connections=requests.adapters.DEFAULT_POOLSIZE,
                maxsize=requests.adapters.DEFAULT_POOLSIZE,
                # Tuple of (address, port). Port 0 means auto-selection.
                source_address=(src_addr, 0),
            )
        return self.session

    def request(
        self, method: str | bytes, url: str | bytes, **kwargs
    ) -> requests.Response:
        full_url = self.join_base_url(self.base_url, url)
        return self.session.request(method, full_url, **kwargs)

    def options(self, url: str | bytes, **kwargs) -> requests.Response:
        return self.session.options(
            self.join_base_url(self.base_url, url), **kwargs
        )

    def head(self, url: str | bytes, **kwargs) -> requests.Response:
        return self.session.head(
            self.join_base_url(self.base_url, url), **kwargs
        )

    def get(self, url: str | bytes, **kwargs) -> requests.Response:
        return self.session.get(
            self.join_base_url(self.base_url, url), **kwargs
        )

    def post(self, url: str | bytes, **kwargs) -> requests.Response:
        return self.session.post(
            self.join_base_url(self.base_url, url), **kwargs
        )

    def put(self, url: str | bytes, **kwargs) -> requests.Response:
        return self.session.put(
            self.join_base_url(self.base_url, url), **kwargs
        )

    def patch(self, url: str | bytes, **kwargs) -> requests.Response:
        return self.session.patch(
            self.join_base_url(self.base_url, url), **kwargs
        )

    def delete(self, url: str | bytes, **kwargs) -> requests.Response:
        return self.session.delete(
            self.join_base_url(self.base_url, url), **kwargs
        )

    def create_cookie(self, **kwargs) -> Cookie:
        return requests.cookies.create_cookie(**kwargs)

    def set_cookie(self, cookie: Cookie) -> None:
        return self.session.cookies.set_cookie(cookie)

    def headers(self, header: dict) -> None:
        return self.session.headers.update(header)

    @staticmethod
    def __deep_merge(source, destination):
        for key, value in source.items():
            if isinstance(value, dict):
                node = destination.setdefault(key, {})
                RequestsApi.__deep_merge(value, node)
            else:
                destination[key] = value
        return destination
