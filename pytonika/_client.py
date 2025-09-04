import httpx
from . import __version__


class APIClient:
    def __init__(self, base_url: str, timeout: float = 10.0) -> None:
        self._client = httpx.Client(
            base_url=base_url.rstrip("/") + "/api",
            timeout=timeout,
            headers={"User-Agent": f"pytonika/{__version__}"},
        )

    def set_token(self, token: str) -> None:
        self._client.headers["Authorization"] = f"Bearer {token}"

    def clear_token(self) -> None:
        self._client.headers.pop("Authorization", None)

    def get(self, endpoint: str, params: dict[str, object] | None = None) -> dict[str, object]:
        return self._client.get(endpoint, params=params).json()

    def post(self, endpoint: str, data: dict[str, object] | None = None) -> dict[str, object]:
        return self._client.post(endpoint, json=data).json()

    def put(self, endpoint: str, data: dict[str, object] | None = None) -> dict[str, object]:
        return self._client.put(endpoint, json=data).json()

    def delete(self, endpoint: str, data: dict[str, object] | None = None) -> dict[str, object]:
        return self._client.delete(endpoint, json=data).json()
