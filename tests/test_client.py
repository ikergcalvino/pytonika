import json
import ssl
from importlib.metadata import version
from typing import Literal

import pytest
import respx

from pytonika._client import APIClient

from .conftest import API_URL, BASE_URL

OK = {"success": True, "data": {}}
FAILED = {"success": False, "errors": [{"code": 120, "error": "Unauthorized access", "source": "Authorization"}]}


@pytest.mark.parametrize("base_url", [BASE_URL, f"{BASE_URL}/"])
def test_base_url_gets_api_prefix(api: respx.MockRouter, base_url: str) -> None:
    route = api.get("/system/device/status").respond(json=OK)
    client = APIClient(base_url, timeout=5.0, verify=True)

    assert client.request("GET", "/system/device/status") == OK
    assert str(route.calls.last.request.url) == f"{API_URL}/system/device/status"
    client.close()


def test_sends_user_agent(api: respx.MockRouter, client: APIClient) -> None:
    route = api.get("/session/status").respond(json=OK)

    client.request("GET", "/session/status")

    assert route.calls.last.request.headers["User-Agent"] == f"pytonika/{version('pytonika')}"


def test_token_is_set_and_cleared(api: respx.MockRouter, client: APIClient) -> None:
    route = api.get("/session/status").respond(json=OK)

    client.set_token("abc123")
    client.request("GET", "/session/status")
    assert route.calls.last.request.headers["Authorization"] == "Bearer abc123"

    client.clear_token()
    client.request("GET", "/session/status")
    assert "Authorization" not in route.calls.last.request.headers


def test_clear_token_without_token_is_a_no_op(client: APIClient) -> None:
    client.clear_token()


def test_error_envelope_is_returned_unchanged(api: respx.MockRouter, client: APIClient) -> None:
    api.get("/users/config").respond(401, json=FAILED)

    assert client.request("GET", "/users/config") == FAILED


def test_query_params_skip_none(api: respx.MockRouter, client: APIClient) -> None:
    route = api.get("/wireguard/config").respond(json=OK)

    client.request("GET", "/wireguard/config", params={"all_options": True, "limit": 10, "search": None})

    assert dict(route.calls.last.request.url.params) == {"all_options": "true", "limit": "10"}


@pytest.mark.parametrize("method", ["POST", "PUT", "DELETE"])
def test_json_body(api: respx.MockRouter, client: APIClient, method: Literal["POST", "PUT", "DELETE"]) -> None:
    route = api.route(method=method, path="/wireguard/config").respond(json=OK)

    client.request(method, "/wireguard/config", json={"data": ["cfg01"]})

    request = route.calls.last.request
    assert request.headers["Content-Type"] == "application/json"
    assert json.loads(request.content) == {"data": ["cfg01"]}


def test_request_without_body(api: respx.MockRouter, client: APIClient) -> None:
    route = api.post("/logout").respond(json=OK)

    client.request("POST", "/logout")

    assert route.calls.last.request.content == b""


def test_multipart_upload(api: respx.MockRouter, client: APIClient) -> None:
    route = api.post("/firmware/device/upload").respond(json=OK)

    client.request(
        "POST",
        "/firmware/device/upload",
        files={"file": ("firmware.bin", b"\x00\x01")},
        form={"force_upgrade": "1"},
    )

    request = route.calls.last.request
    assert request.headers["Content-Type"].startswith("multipart/form-data")
    assert b'name="file"; filename="firmware.bin"' in request.content
    assert b'name="force_upgrade"' in request.content


def test_download_returns_bytes(api: respx.MockRouter, client: APIClient) -> None:
    api.post("/backup/actions/download").respond(content=b"\x1f\x8b", headers={"Content-Type": "application/x-targz"})

    assert client.request("POST", "/backup/actions/download", download=True) == b"\x1f\x8b"


def test_download_returns_error_envelope(api: respx.MockRouter, client: APIClient) -> None:
    api.post("/backup/actions/download").respond(400, json=FAILED)

    assert client.request("POST", "/backup/actions/download", download=True) == FAILED


def test_non_json_response_without_download_raises(api: respx.MockRouter, client: APIClient) -> None:
    api.get("/system/device/status").respond(502, text="<html>Bad Gateway</html>")

    with pytest.raises(json.JSONDecodeError):
        client.request("GET", "/system/device/status")


def test_verify_accepts_ssl_context() -> None:
    APIClient(BASE_URL, timeout=5.0, verify=ssl.create_default_context()).close()


def test_close(client: APIClient) -> None:
    client.close()

    assert client._session.is_closed
