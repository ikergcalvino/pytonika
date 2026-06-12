from typing import Any

from ._base import Endpoint


class Thingworx(Endpoint):
    def get_thingworx_config(self) -> dict[str, Any]:
        """Returns the ThingWorx configuration in an array."""
        endpoint = "/thingworx/config"

        return self._api_client.get(endpoint)

    def update_thingworx_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the ThingWorx configuration in an array."""
        endpoint = "/thingworx/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_thingworx_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the ThingWorx configuration."""
        endpoint = f"/thingworx/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_thingworx_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the ThingWorx configuration."""
        endpoint = f"/thingworx/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
