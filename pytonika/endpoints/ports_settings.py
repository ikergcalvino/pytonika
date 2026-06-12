from typing import Any

from ._base import Endpoint


class PortsSettings(Endpoint):
    def get_ports_settings_config(self) -> dict[str, Any]:
        """Returns port configurations."""
        endpoint = "/ports_settings/config"

        return self._api_client.get(endpoint)

    def update_ports_settings_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates port configurations."""
        endpoint = "/ports_settings/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_ports_settings_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns port configuration."""
        endpoint = f"/ports_settings/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_ports_settings_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates port configuration."""
        endpoint = f"/ports_settings/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_ports_settings_status(self) -> dict[str, Any]:
        """Returns port status."""
        endpoint = "/ports_settings/status"

        return self._api_client.get(endpoint)
