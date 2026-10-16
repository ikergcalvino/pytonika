from typing import Any

from ._endpoint import Endpoint


class LLDP(Endpoint):
    def get_lldp_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all LLDP configurations."""
        return self._client.request("GET", "/lldp/config", params={"all_options": all_options})

    def update_lldp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified LLDP configurations."""
        return self._client.request("PUT", "/lldp/config", json={"data": config})

    def get_lldp_config_by_id(self, lldp_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified LLDP configuration."""
        return self._client.request("GET", f"/lldp/config/{lldp_id}", params={"all_options": all_options})

    def update_lldp_config_by_id(self, lldp_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified LLDP configuration."""
        return self._client.request("PUT", f"/lldp/config/{lldp_id}", json={"data": config})

    def get_lldp_neighbor_status(self) -> dict[str, Any]:
        """Returns all status information."""
        return self._client.request("GET", "/lldp/neighbor/status")
