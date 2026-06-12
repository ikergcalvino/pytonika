from typing import Any

from ._base import Endpoint


class Tailscale(Endpoint):
    def get_tailscale_config(self) -> dict[str, Any]:
        """Returns Tailscale configurations."""
        endpoint = "/tailscale/config"

        return self._api_client.get(endpoint)

    def update_tailscale_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Tailscale configurations."""
        endpoint = "/tailscale/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_tailscale_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Tailscale configuration."""
        endpoint = f"/tailscale/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_tailscale_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Tailscale configuration."""
        endpoint = f"/tailscale/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_tailscale_status(self) -> dict[str, Any]:
        """Returns Tailscale status."""
        endpoint = "/tailscale/status"

        return self._api_client.get(endpoint)
