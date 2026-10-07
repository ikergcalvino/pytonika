from typing import Any

from ._endpoint import Endpoint


class InternetConnection(Endpoint):
    def get_internet_connection_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns internet global configuration."""
        return self._client.request("GET", "/internet_connection/global", params={"all_options": all_options})

    def update_internet_connection_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates internet global configuration."""
        return self._client.request("PUT", "/internet_connection/global", json=config)

    def get_internet_connection_status(self) -> dict[str, Any]:
        """Returns internet status."""
        return self._client.request("GET", "/internet_connection/status")
