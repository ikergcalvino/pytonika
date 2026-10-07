import ssl
from collections.abc import Mapping
from importlib.metadata import version
from typing import Any, Literal

import httpx

USER_AGENT = f"pytonika/{version('pytonika')}"


class APIClient:
    """HTTP client for the Teltonika Web API.

    Responses are returned as the device sends them, including the ``{"success": False, "errors": [...]}``
    envelope of failed requests. Transport errors such as timeouts are raised by ``httpx``.
    """

    def __init__(self, base_url: str, *, timeout: float, verify: bool | ssl.SSLContext) -> None:
        self._session = httpx.Client(
            base_url=f"{base_url.rstrip('/')}/api",
            headers={"User-Agent": USER_AGENT},
            timeout=timeout,
            verify=verify,
        )

    def close(self) -> None:
        self._session.close()

    def set_token(self, token: str) -> None:
        self._session.headers["Authorization"] = f"Bearer {token}"

    def clear_token(self) -> None:
        self._session.headers.pop("Authorization", None)

    def request(
        self,
        method: Literal["GET", "POST", "PUT", "DELETE"],
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Mapping[str, Any] | None = None,
        files: Mapping[str, Any] | None = None,
        form: Mapping[str, Any] | None = None,
        download: bool = False,
    ) -> Any:  # noqa: ANN401 - each endpoint method declares its precise return type
        """Sends a request and returns the decoded JSON response.

        With ``download=True``, a file response is returned as ``bytes`` (a JSON error is still decoded).
        """
        if params:
            params = {name: value for name, value in params.items() if value is not None}

        if form:
            form = {name: value for name, value in form.items() if value is not None}

        response = self._session.request(method, path, params=params, json=json, files=files, data=form)

        if download and not response.headers.get("Content-Type", "").startswith("application/json"):
            return response.content

        return response.json()
