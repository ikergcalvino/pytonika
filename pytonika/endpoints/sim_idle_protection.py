from typing import Any

from ._base import Endpoint


class SIMIdleProtection(Endpoint):
    def get_sim_idle_protection_config(self) -> dict[str, Any]:
        """Returns multiple SIM idle protection configurations."""
        endpoint = "/sim_idle_protection/config"

        return self._api_client.get(endpoint)

    def update_sim_idle_protection_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update multiple SIM idle protection configurations."""
        endpoint = "/sim_idle_protection/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_sim_idle_protection_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified SIM idle protection configuration."""
        endpoint = f"/sim_idle_protection/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_sim_idle_protection_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update specified SIM idle protection configuration."""
        endpoint = f"/sim_idle_protection/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
