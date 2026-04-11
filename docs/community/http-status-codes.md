# HTTP status codes (quick reference)

When you call remote APIs with `RequestsApi`, inspect `response.status_code` (integer) or use `response.raise_for_status()` from **requests** for 4xx/5xx.

This page is a **compact cheat sheet**. Authoritative definitions are in [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html#name-status-codes) and the [MDN HTTP status reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status).

## 1xx — Informational

Rare in typical `requests` usage; often handled by the HTTP stack before you see a final response.

| Code | Name | Meaning |
|------|------|---------|
| 100 | Continue | Client may send the rest of the request body. |
| 101 | Switching Protocols | Protocol upgrade (for example WebSocket). |
| 103 | Early Hints | Hints while the final response is prepared. |

## 2xx — Success

| Code | Name | Meaning |
|------|------|---------|
| 200 | OK | Request succeeded; meaning depends on method (GET: resource returned, etc.). |
| 201 | Created | Resource created; often includes `Location`. |
| 202 | Accepted | Accepted for processing, not completed yet. |
| 204 | No Content | Success with an empty body. |
| 206 | Partial Content | Part of a resource (range requests). |

## 3xx — Redirection

Follow redirects automatically unless you pass `allow_redirects=False` to **requests**.

| Code | Name | Meaning |
|------|------|---------|
| 301 | Moved Permanently | Resource has a new permanent URI. |
| 302 | Found | Temporary redirect (historically “moved temporarily”). |
| 303 | See Other | GET the URI in `Location`. |
| 304 | Not Modified | Cached version still valid (conditional GET). |
| 307 | Temporary Redirect | Repeat request to `Location` with the same method. |
| 308 | Permanent Redirect | Like 301 but method must not change. |

## 4xx — Client errors

The server understood the request but refuses or cannot satisfy it because of the client (auth, validation, wrong URL, etc.).

| Code | Name | Meaning |
|------|------|---------|
| 400 | Bad Request | Malformed syntax or invalid message framing. |
| 401 | Unauthorized | Authentication required or failed. |
| 402 | Payment Required | Reserved; rarely used in practice. |
| 403 | Forbidden | Authenticated but not allowed to access the resource. |
| 404 | Not Found | No matching resource for the URI. |
| 405 | Method Not Allowed | HTTP method not supported for this resource. |
| 406 | Not Acceptable | Cannot produce a response matching `Accept`. |
| 408 | Request Timeout | Server gave up waiting for the full request. |
| 409 | Conflict | Conflict with current state (for example duplicate create). |
| 410 | Gone | Resource existed but is permanently gone. |
| 413 | Payload Too Large | Request body too large. |
| 414 | URI Too Long | Request URI longer than the server accepts. |
| 415 | Unsupported Media Type | Body media type not supported. |
| 422 | Unprocessable Entity | Common in JSON APIs: validation failed (WebDAV / API convention). |
| 429 | Too Many Requests | Rate limited; often includes `Retry-After`. |

## 5xx — Server errors

The server failed to fulfill an apparently valid request.

| Code | Name | Meaning |
|------|------|---------|
| 500 | Internal Server Error | Generic server-side failure. |
| 501 | Not Implemented | Server does not support the functionality. |
| 502 | Bad Gateway | Upstream server returned an invalid response. |
| 503 | Service Unavailable | Temporarily overloaded or down; may include `Retry-After`. |
| 504 | Gateway Timeout | Upstream did not respond in time. |

## Using this with `RequestsApi`

```python
from requests import HTTPError

client = RequestsApi("https://api.example.com")
r = client.get("v1/items")
try:
    r.raise_for_status()
except HTTPError:
    # r.status_code tells you which row above applies
    raise
data = r.json()
```

For APIs that return errors in JSON bodies with HTTP 200, you still need to read the payload—status codes alone are not enough.
