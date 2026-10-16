from typing import Any

from ._endpoint import Endpoint


class Netbird(Endpoint):
    def get_netbird_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all NetBird configurations."""
        return self._client.request("GET", "/netbird/config", params={"all_options": all_options})

    def update_netbird_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified NetBird configurations."""
        return self._client.request("PUT", "/netbird/config", json={"data": config})

    def get_netbird_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified NetBird configuration."""
        return self._client.request("GET", f"/netbird/config/{config_id}", params={"all_options": all_options})

    def update_netbird_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified NetBird configuration."""
        return self._client.request("PUT", f"/netbird/config/{config_id}", json={"data": config})

    def get_netbird_status(self) -> dict[str, Any]:
        """Returns NetBird status."""
        return self._client.request("GET", "/netbird/status")
