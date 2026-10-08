import respx

from pytonika import Router

from .conftest import BASE_URL


def test_login_stores_token(api: respx.MockRouter) -> None:
    api.post("/login").respond(json={"success": True, "data": {"username": "admin", "token": "abc123"}})
    status = api.get("/session/status").respond(json={"success": True, "data": {"active": True}})

    with Router(BASE_URL) as router:
        router.authentication.login("admin", "secret")
        router.authentication.get_session_status()

    assert status.calls.last.request.headers["Authorization"] == "Bearer abc123"


def test_login_sends_credentials(api: respx.MockRouter) -> None:
    login = api.post("/login").respond(json={"success": True, "data": {"token": "abc123"}})

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
