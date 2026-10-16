from typing import Any

from ._endpoint import Endpoint


class SIMIdleProtection(Endpoint):
    def get_sim_idle_protection_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns multiple SIM idle protection configurations."""
        return self._client.request("GET", "/sim_idle_protection/config", params={"all_options": all_options})

    def update_sim_idle_protection_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update multiple SIM idle protection configurations."""
        return self._client.request("PUT", "/sim_idle_protection/config", json={"data": config})

    def get_sim_idle_protection_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns specified SIM idle protection configuration."""
        return self._client.request(
            "GET", f"/sim_idle_protection/config/{config_id}", params={"all_options": all_options}
        )

    def update_sim_idle_protection_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update specified SIM idle protection configuration."""
        return self._client.request("PUT", f"/sim_idle_protection/config/{config_id}", json={"data": config})
