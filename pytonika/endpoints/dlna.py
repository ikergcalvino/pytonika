from typing import Any

from ._base import Endpoint


class DLNA(Endpoint):
    def get_minidlna_config(self) -> dict[str, Any]:
        """Returns the minidlna configuration."""
        endpoint = "/minidlna/config"

        return self._api_client.get(endpoint)

    def update_minidlna_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the minidlna configuration."""
        endpoint = "/minidlna/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_minidlna_config_by_id(self, dlna_id: str) -> dict[str, Any]:
        """Returns the minidlna configuration."""
        endpoint = f"/minidlna/config/{dlna_id}"

        return self._api_client.get(endpoint)

    def update_minidlna_config_by_id(self, dlna_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the minidlna configuration."""
        endpoint = f"/minidlna/config/{dlna_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_minidlna_status(self) -> dict[str, Any]:
        """Get minidlna status."""
        endpoint = "/minidlna/status"

        return self._api_client.get(endpoint)

    def get_minidlna_options(self) -> dict[str, Any]:
        """Get available dlna interfaces."""
        endpoint = "/minidlna/options"

        return self._api_client.get(endpoint)
