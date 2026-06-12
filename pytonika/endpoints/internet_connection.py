from typing import Any

from ._base import Endpoint


class InternetConnection(Endpoint):
    def get_internet_connection_global(self) -> dict[str, Any]:
        """Returns internet global configuration."""
        endpoint = "/internet_connection/global"

        return self._api_client.get(endpoint)

    def update_internet_connection_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates internet global configuration."""
        endpoint = "/internet_connection/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_internet_connection_status(self) -> dict[str, Any]:
        """Returns internet status."""
        endpoint = "/internet_connection/status"

        return self._api_client.get(endpoint)
