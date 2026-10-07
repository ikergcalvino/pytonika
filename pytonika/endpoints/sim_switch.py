from typing import Any

from ._endpoint import Endpoint


class SIMSwitch(Endpoint):
    def get_sim_switch_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns multiple SIM switch configurations."""
        return self._client.request("GET", "/sim_switch/config", params={"all_options": all_options})

    def update_sim_switch_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple SIM switch configurations."""
        return self._client.request("PUT", "/sim_switch/config", json={"data": config})

    def get_sim_switch_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified SIM switch configuration."""
        return self._client.request("GET", f"/sim_switch/config/{config_id}", params={"all_options": all_options})

    def update_sim_switch_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified SIM switch configuration."""
        return self._client.request("PUT", f"/sim_switch/config/{config_id}", json={"data": config})
