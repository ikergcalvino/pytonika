from typing import Any

from ._base import Endpoint


class TR069(Endpoint):
    def get_tr069_config(self) -> dict[str, Any]:
        """Returns the TR-069 configuration in an array."""
        endpoint = "/tr069/config"

        return self._api_client.get(endpoint)

    def update_tr069_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the TR-069 configuration in an array."""
        endpoint = "/tr069/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_tr069_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the TR-069 configuration."""
        endpoint = f"/tr069/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_tr069_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the TR-069 configuration."""
        endpoint = f"/tr069/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
