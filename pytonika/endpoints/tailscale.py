from typing import Any

from ._endpoint import Endpoint


class Tailscale(Endpoint):
    def tailscale_actions_logout(self) -> dict[str, Any]:
        """Log out current device from the Tailscale network."""
        return self._client.request("POST", "/tailscale/actions/logout")

    def get_tailscale_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Tailscale configurations."""
        return self._client.request("GET", "/tailscale/config", params={"all_options": all_options})

    def update_tailscale_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Tailscale configurations."""
        return self._client.request("PUT", "/tailscale/config", json={"data": config})

    def get_tailscale_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Tailscale configuration."""
        return self._client.request("GET", f"/tailscale/config/{config_id}", params={"all_options": all_options})

    def update_tailscale_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Tailscale configuration."""
        return self._client.request("PUT", f"/tailscale/config/{config_id}", json={"data": config})

    def get_tailscale_status(self) -> dict[str, Any]:
        """Returns Tailscale status."""
        return self._client.request("GET", "/tailscale/status")
