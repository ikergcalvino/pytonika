from typing import Any

from ._endpoint import Endpoint


class EoIP(Endpoint):
    def get_eoip_config(self) -> dict[str, Any]:
        """Returns all EoIP configurations."""
        return self._client.request("GET", "/eoip/config")

    def create_eoip_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates EoIP configuration."""
        return self._client.request("POST", "/eoip/config", json={"data": config})

    def update_eoip_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified EoIP configurations."""
        return self._client.request("PUT", "/eoip/config", json={"data": config})

    def delete_eoip_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified EoIP configurations."""
        return self._client.request("DELETE", "/eoip/config", json={"data": config})

    def get_eoip_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified EoIP configuration."""
        return self._client.request("GET", f"/eoip/config/{config_id}")

    def update_eoip_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified EoIP configuration."""
        return self._client.request("PUT", f"/eoip/config/{config_id}", json={"data": config})

    def delete_eoip_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified EoIP configuration."""
        return self._client.request("DELETE", f"/eoip/config/{config_id}")
