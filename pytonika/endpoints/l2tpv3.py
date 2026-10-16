from typing import Any

from ._endpoint import Endpoint


class L2TPv3(Endpoint):
    def get_l2tpv3_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get l2tpv3 configurations."""
        return self._client.request("GET", "/l2tpv3/config", params={"all_options": all_options})

    def create_l2tpv3_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create l2tpv3 configuration."""
        return self._client.request("POST", "/l2tpv3/config", json={"data": config})

    def update_l2tpv3_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update l2tpv3 configurations."""
        return self._client.request("PUT", "/l2tpv3/config", json={"data": config})

    def delete_l2tpv3_config(self, config: list[str]) -> dict[str, Any]:
        """Delete l2tpv3 configurations."""
        return self._client.request("DELETE", "/l2tpv3/config", json={"data": config})

    def get_l2tpv3_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get l2tpv3 configuration."""
        return self._client.request("GET", f"/l2tpv3/config/{config_id}", params={"all_options": all_options})

    def update_l2tpv3_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update l2tpv3 configuration."""
        return self._client.request("PUT", f"/l2tpv3/config/{config_id}", json={"data": config})

    def delete_l2tpv3_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete l2tpv3 configuration."""
        return self._client.request("DELETE", f"/l2tpv3/config/{config_id}")
