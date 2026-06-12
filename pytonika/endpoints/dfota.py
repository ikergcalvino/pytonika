from typing import Any

from ._base import Endpoint


class DFOTA(Endpoint):
    def get_dfota_config(self) -> dict[str, Any]:
        """Returns multiple DFOTA configurations."""
        endpoint = "/dfota/config"

        return self._api_client.get(endpoint)

    def update_dfota_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple DFOTA configurations."""
        endpoint = "/dfota/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_dfota_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns DFOTA configuration."""
        endpoint = f"/dfota/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_dfota_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates DFOTA configuration."""
        endpoint = f"/dfota/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
