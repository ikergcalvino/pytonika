from typing import Any

from ._base import Endpoint


class SIMSwitch(Endpoint):
    def get_sim_switch_config(self) -> dict[str, Any]:
        """Returns multiple SIM switch configurations."""
        endpoint = "/sim_switch/config"

        return self._api_client.get(endpoint)

    def update_sim_switch_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple SIM switch configurations."""
        endpoint = "/sim_switch/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_sim_switch_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified SIM switch configuration."""
        endpoint = f"/sim_switch/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_sim_switch_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified SIM switch configuration."""
        endpoint = f"/sim_switch/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
