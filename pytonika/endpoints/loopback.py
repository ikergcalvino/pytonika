from typing import Any

from ._endpoint import Endpoint


class Loopback(Endpoint):
    def get_loopback_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns loopback detection configurations."""
        return self._client.request("GET", "/loopback/config", params={"all_options": all_options})

    def update_loopback_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates loopback detection configurations."""
        return self._client.request("PUT", "/loopback/config", json={"data": config})

    def get_loopback_config_by_id(self, loopback_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns loopback detection configuration."""
        return self._client.request("GET", f"/loopback/config/{loopback_id}", params={"all_options": all_options})

    def update_loopback_config_by_id(self, loopback_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates loopback detection configuration."""
        return self._client.request("PUT", f"/loopback/config/{loopback_id}", json={"data": config})

    def get_loopback_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns loopback global configuration."""
        return self._client.request("GET", "/loopback/global", params={"all_options": all_options})

    def update_loopback_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates loopback global configuration."""
        return self._client.request("PUT", "/loopback/global", json={"data": config})

    def get_loopback_status(self) -> dict[str, Any]:
        """Returns loopback detection status."""
        return self._client.request("GET", "/loopback/status")
