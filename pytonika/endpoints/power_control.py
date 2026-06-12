from typing import Any

from ._base import Endpoint


class PowerControl(Endpoint):
    def get_power_control_status(self) -> dict[str, Any]:
        """Returns all Power Control pins status."""
        endpoint = "/power_control/status"

        return self._api_client.get(endpoint)

    def get_power_control_status_by_id(self, power_control_id: str) -> dict[str, Any]:
        """Returns the specified Power Control pin status."""
        endpoint = f"/power_control/status/{power_control_id}"

        return self._api_client.get(endpoint)

    def get_power_control_config(self) -> dict[str, Any]:
        """Returns Power Control configurations."""
        endpoint = "/power_control/config"

        return self._api_client.get(endpoint)

    def update_power_control_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Power Control configurations."""
        endpoint = "/power_control/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_power_control_config_by_id(self, power_control_id: str) -> dict[str, Any]:
        """Returns the specified Power Control configuration."""
        endpoint = f"/power_control/config/{power_control_id}"

        return self._api_client.get(endpoint)

    def update_power_control_config_by_id(self, power_control_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update the specified Power Control configuration."""
        endpoint = f"/power_control/config/{power_control_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
