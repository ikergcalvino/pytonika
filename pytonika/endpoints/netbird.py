from typing import Any

from ._base import Endpoint


class Netbird(Endpoint):
    def get_netbird_config(self) -> dict[str, Any]:
        """Returns all NetBird configurations."""
        endpoint = "/netbird/config"

        return self._client.request("GET", endpoint)

    def update_netbird_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified NetBird configurations."""
        endpoint = "/netbird/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def get_netbird_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified NetBird configuration."""
        endpoint = f"/netbird/config/{config_id}"

        return self._client.request("GET", endpoint)

    def update_netbird_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified NetBird configuration."""
        endpoint = f"/netbird/config/{config_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def get_netbird_status(self) -> dict[str, Any]:
        """Returns NetBird status."""
        endpoint = "/netbird/status"

        return self._client.request("GET", endpoint)
