from typing import Any

from ._base import Endpoint


class L2TPv3(Endpoint):
    def get_l2tpv3_config(self) -> dict[str, Any]:
        """Get l2tpv3 configurations."""
        endpoint = "/l2tpv3/config"

        return self._api_client.get(endpoint)

    def create_l2tpv3_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create l2tpv3 configuration."""
        endpoint = "/l2tpv3/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_l2tpv3_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update l2tpv3 configurations."""
        endpoint = "/l2tpv3/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_l2tpv3_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete l2tpv3 configurations."""
        return [self.delete_l2tpv3_config_by_id(config_id) for config_id in config]

    def get_l2tpv3_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Get l2tpv3 configuration."""
        endpoint = f"/l2tpv3/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_l2tpv3_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update l2tpv3 configuration."""
        endpoint = f"/l2tpv3/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_l2tpv3_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete l2tpv3 configuration."""
        endpoint = f"/l2tpv3/config/{config_id}"

        return self._api_client.delete(endpoint)
