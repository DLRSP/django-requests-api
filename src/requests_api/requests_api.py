from __future__ import annotations
from http.cookiejar import Cookie

import requests
from requests import Response


class RequestsApi:
    def __init__(self, base_url: str | bytes, **kwargs):
        self.base_url = base_url
        self.session = requests.Session()
        for arg in kwargs:
            if isinstance(kwargs[arg], dict):
                kwargs[arg] = self.__deep_merge(getattr(self.session, arg), kwargs[arg])
            setattr(self.session, arg, kwargs[arg])

    def request(self, method: str | bytes, url: str | bytes, **kwargs) -> Response:
        return self.session.request(method, self.base_url + url, **kwargs)

    def head(self, url: str | bytes, **kwargs) -> Response:
        return self.session.head(self.base_url + url, **kwargs)

    def get(self, url: str | bytes, **kwargs) -> Response:
        return self.session.get(self.base_url + url, **kwargs)

    def post(self, url: str | bytes, **kwargs) -> Response:
        return self.session.post(self.base_url + url, **kwargs)

    def put(self, url: str | bytes, **kwargs) -> Response:
        return self.session.put(self.base_url + url, **kwargs)

    def patch(self, url: str | bytes, **kwargs) -> Response:
        return self.session.patch(self.base_url + url, **kwargs)

    def delete(self, url: str | bytes, **kwargs) -> Response:
        return self.session.delete(self.base_url + url, **kwargs)

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
