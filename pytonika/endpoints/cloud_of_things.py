from typing import Any

from ._base import Endpoint


class CloudOfThings(Endpoint):
    def get_cloud_of_things_status(self) -> dict[str, Any]:
        """Returns Cloud of Things status."""
        endpoint = "/cloud_of_things/status"

        return self._api_client.get(endpoint)

    def get_cloud_of_things_config(self) -> dict[str, Any]:
        """Returns Cloud of Things configuration in an array."""
        endpoint = "/cloud_of_things/config"

        return self._api_client.get(endpoint)

    def update_cloud_of_things_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Cloud of Things configuration in an array."""
        endpoint = "/cloud_of_things/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_cloud_of_things_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Cloud of Things configuration."""
        endpoint = f"/cloud_of_things/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_cloud_of_things_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Cloud of Things configuration."""
        endpoint = f"/cloud_of_things/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def cloud_of_things_reset_auth(self, data: dict[str, Any]) -> dict[str, Any]:
        """Resets authentication data."""
        endpoint = "/cloud_of_things/actions/reset_auth"

        return self._api_client.post(endpoint, data={"data": data})
