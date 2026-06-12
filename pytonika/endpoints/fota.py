from typing import Any

from ._base import Endpoint


class FOTA(Endpoint):
    def get_fota_config(self) -> dict[str, Any]:
        """Returns Fota configuration."""
        endpoint = "/fota/config"

        return self._api_client.get(endpoint)

    def update_fota_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Fota configuration."""
        endpoint = "/fota/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_fota_config_by_id(self, fota_id: str) -> dict[str, Any]:
        """Returns Fota configuration."""
        endpoint = f"/fota/config/{fota_id}"

        return self._api_client.get(endpoint)

    def update_fota_config_by_id(self, fota_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Fota configuration."""
        endpoint = f"/fota/config/{fota_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
