from typing import Any

from ._base import Endpoint


class Cumulocity(Endpoint):
    def get_cumulocity_status(self) -> dict[str, Any]:
        """Returns Cumulocity status."""
        endpoint = "/cumulocity/status"

        return self._api_client.get(endpoint)

    def get_cumulocity_config(self) -> dict[str, Any]:
        """Returns Cumulocity configuration in an array."""
        endpoint = "/cumulocity/config"

        return self._api_client.get(endpoint)

    def update_cumulocity_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Cumulocity configuration in an array."""
        endpoint = "/cumulocity/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_cumulocity_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Cumulocity configuration."""
        endpoint = f"/cumulocity/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_cumulocity_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Cumulocity configuration."""
        endpoint = f"/cumulocity/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def cumulocity_reset_auth(self, data: dict[str, Any]) -> dict[str, Any]:
        """Resets authentication data."""
        endpoint = "/cumulocity/actions/reset_auth"

        return self._api_client.post(endpoint, data={"data": data})
