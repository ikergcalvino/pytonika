from importlib.metadata import version
from typing import Any

import httpx


class APIClient:
    def __init__(self, base_url: str, *, timeout: float, verify: bool | str) -> None:
        self._client = httpx.Client(
            base_url=base_url.rstrip("/") + "/api",
            headers={"User-Agent": f"pytonika/{version('pytonika')}"},
            timeout=timeout,
            verify=verify,
        )

    def set_token(self, token: str) -> None:
        self._client.headers["Authorization"] = f"Bearer {token}"

    def clear_token(self) -> None:
        self._client.headers.pop("Authorization", None)

    def get(self, endpoint: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        response: dict[str, Any] = self._client.get(endpoint, params=params).json()
        return response

    def post(self, endpoint: str, data: dict[str, Any] | None = None) -> dict[str, Any]:
        response: dict[str, Any] = self._client.post(endpoint, json=data).json()
        return response

    def put(self, endpoint: str, data: dict[str, Any] | None = None) -> dict[str, Any]:
        response: dict[str, Any] = self._client.put(endpoint, json=data).json()
        return response

    def delete(self, endpoint: str) -> dict[str, Any]:
        response: dict[str, Any] = self._client.delete(endpoint).json()
        return response
