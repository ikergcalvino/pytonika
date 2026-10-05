from typing import Any

from ._endpoint import Endpoint


class FOTA(Endpoint):
    def get_fota_config(self) -> dict[str, Any]:
        """Returns Fota configuration."""
        endpoint = "/fota/config"

        return self._client.request("GET", endpoint)

    def update_fota_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Fota configuration."""
        endpoint = "/fota/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def get_fota_config_by_id(self, fota_id: str) -> dict[str, Any]:
        """Returns Fota configuration."""
        endpoint = f"/fota/config/{fota_id}"

        return self._client.request("GET", endpoint)

    def update_fota_config_by_id(self, fota_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Fota configuration."""
        endpoint = f"/fota/config/{fota_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)
