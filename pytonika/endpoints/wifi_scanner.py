from typing import Any

from ._base import Endpoint


class WiFiScanner(Endpoint):
    def get_wifi_scanner_config(self) -> dict[str, Any]:
        """Returns Wifi Scanner configurations."""
        endpoint = "/wifi_scanner/config"

        return self._api_client.get(endpoint)

    def get_wifi_scanner_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Wifi Scanner configuration."""
        endpoint = f"/wifi_scanner/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_wifi_scanner_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Wifi Scanner configurations."""
        endpoint = "/wifi_scanner/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def update_wifi_scanner_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Wifi Scanner configuration."""
        endpoint = f"/wifi_scanner/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
