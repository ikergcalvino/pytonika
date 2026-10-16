from typing import Any

from ._endpoint import Endpoint


class WiFiScanner(Endpoint):
    def get_wifi_scanner_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Wifi Scanner configurations."""
        return self._client.request("GET", "/wifi_scanner/config", params={"all_options": all_options})

    def update_wifi_scanner_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Wifi Scanner configurations."""
        return self._client.request("PUT", "/wifi_scanner/config", json={"data": config})

    def get_wifi_scanner_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Wifi Scanner configuration."""
        return self._client.request("GET", f"/wifi_scanner/config/{config_id}", params={"all_options": all_options})

    def update_wifi_scanner_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Wifi Scanner configuration."""
        return self._client.request("PUT", f"/wifi_scanner/config/{config_id}", json={"data": config})
