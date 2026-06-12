from typing import Any

from ._base import Endpoint


class EoIP(Endpoint):
    def get_eoip_config(self) -> dict[str, Any]:
        """Returns all EoIP configurations."""
        endpoint = "/eoip/config"

        return self._api_client.get(endpoint)

    def create_eoip_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates EoIP configuration."""
        endpoint = "/eoip/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_eoip_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified EoIP configurations."""
        endpoint = "/eoip/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_eoip_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified EoIP configurations."""
        return [self.delete_eoip_config_by_id(config_id) for config_id in config]

    def get_eoip_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified EoIP configuration."""
        endpoint = f"/eoip/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_eoip_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified EoIP configuration."""
        endpoint = f"/eoip/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_eoip_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified EoIP configuration."""
        endpoint = f"/eoip/config/{config_id}"

        return self._api_client.delete(endpoint)
