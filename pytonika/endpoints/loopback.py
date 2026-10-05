from typing import Any

from ._base import Endpoint


class Loopback(Endpoint):
    def get_loopback_config(self) -> dict[str, Any]:
        """Returns loopback detection configurations."""
        endpoint = "/loopback/config"

        return self._client.request("GET", endpoint)

    def update_loopback_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates loopback detection configurations."""
        endpoint = "/loopback/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def get_loopback_config_by_id(self, loopback_id: str) -> dict[str, Any]:
        """Returns loopback detection configuration."""
        endpoint = f"/loopback/config/{loopback_id}"

        return self._client.request("GET", endpoint)

    def update_loopback_config_by_id(self, loopback_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates loopback detection configuration."""
        endpoint = f"/loopback/config/{loopback_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def get_loopback_status(self) -> dict[str, Any]:
        """Returns loopback detection status."""
        endpoint = "/loopback/status"

        return self._client.request("GET", endpoint)

    def get_loopback_global(self) -> dict[str, Any]:
        """Returns loopback global configuration."""
        endpoint = "/loopback/global"

        return self._client.request("GET", endpoint)

    def update_loopback_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates loopback global configuration."""
        endpoint = "/loopback/global"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)
