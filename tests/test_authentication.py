import httpx
import pytest
import respx

from pytonika import AccessPoint, Gateway, Router, Switch

from .conftest import BASE_URL


def test_login_stores_token(api: respx.MockRouter) -> None:
    api.post("/login").respond(json={"success": True, "data": {"username": "admin", "token": "abc123"}})
    api.post("/logout").respond(json={"success": True, "data": {}})
    status = api.get("/session/status").respond(json={"success": True, "data": {"active": True}})

    with Router(BASE_URL) as router:
        router.authentication.login("admin", "secret")
        router.authentication.get_session_status()

    assert status.calls.last.request.headers["Authorization"] == "Bearer abc123"


def test_login_sends_credentials(api: respx.MockRouter) -> None:
    login = api.post("/login").respond(json={"success": True, "data": {"token": "abc123"}})
    api.post("/logout").respond(json={"success": True, "data": {}})

    with Router(BASE_URL) as router:
        router.authentication.login("admin", "secret")

    assert login.calls.last.request.read() == b'{"username":"admin","password":"secret"}'


def test_failed_login_returns_errors_without_token(api: respx.MockRouter) -> None:
    failed = {"success": False, "errors": [{"code": 120, "error": "Unauthorized access", "source": "Login"}]}
    api.post("/login").respond(401, json=failed)
    status = api.get("/session/status").respond(json={"success": False})

    with Router(BASE_URL) as router:
        assert router.authentication.login("admin", "wrong") == failed
        router.authentication.get_session_status()

    assert "Authorization" not in status.calls.last.request.headers


def test_logout_clears_token(api: respx.MockRouter) -> None:
    api.post("/login").respond(json={"success": True, "data": {"token": "abc123"}})
    api.post("/logout").respond(json={"success": True})
    status = api.get("/session/status").respond(json={"success": False})

    with Router(BASE_URL) as router:
        router.authentication.login("admin", "secret")
        router.authentication.logout()
        router.authentication.get_session_status()

    assert "Authorization" not in status.calls.last.request.headers


@pytest.mark.parametrize("family", [Router, Gateway, AccessPoint, Switch], ids=lambda cls: cls.__name__)
def test_closing_logs_out_an_open_session(api: respx.MockRouter, family: type) -> None:
    api.post("/login").respond(json={"success": True, "data": {"token": "abc123"}})
    logout = api.post("/logout").respond(json={"success": True, "data": {}})

    with family(BASE_URL) as device:
        device.authentication.login("admin", "secret")

    assert logout.call_count == 1
    assert logout.calls.last.request.headers["Authorization"] == "Bearer abc123"


def test_closing_without_session_does_not_log_out(api: respx.MockRouter) -> None:
    logout = api.post("/logout").respond(json={"success": True, "data": {}})

    with Router(BASE_URL):
        pass

    assert not logout.called


def test_explicit_logout_is_not_repeated_on_close(api: respx.MockRouter) -> None:
    api.post("/login").respond(json={"success": True, "data": {"token": "abc123"}})
    logout = api.post("/logout").respond(json={"success": True, "data": {}})

    with Router(BASE_URL) as router:
        router.authentication.login("admin", "secret")
        router.authentication.logout()

    assert logout.call_count == 1


@pytest.mark.parametrize("failure", [httpx.ConnectError("unreachable"), httpx.ReadTimeout("timeout")])
def test_closing_survives_an_unreachable_device(api: respx.MockRouter, failure: Exception) -> None:
    api.post("/login").respond(json={"success": True, "data": {"token": "abc123"}})
    api.post("/logout").mock(side_effect=failure)

    with Router(BASE_URL) as router:
        router.authentication.login("admin", "secret")

    assert router._client._session.is_closed
