from typing import Any

from ._endpoint import Endpoint


class PowerControl(Endpoint):
    def get_power_control_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Power Control configurations."""
        return self._client.request("GET", "/power_control/config", params={"all_options": all_options})

    def update_power_control_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Power Control configurations."""
        return self._client.request("PUT", "/power_control/config", json={"data": config})

    def get_power_control_config_by_id(
        self, power_control_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Power Control configuration."""
        return self._client.request(
            "GET", f"/power_control/config/{power_control_id}", params={"all_options": all_options}
        )

    def update_power_control_config_by_id(self, power_control_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update the specified Power Control configuration."""
        return self._client.request("PUT", f"/power_control/config/{power_control_id}", json={"data": config})

    def get_power_control_status(self) -> dict[str, Any]:
        """Returns all Power Control pins status."""
        return self._client.request("GET", "/power_control/status")

    def get_power_control_status_by_id(self, power_control_id: str) -> dict[str, Any]:
        """Returns the specified Power Control pin status."""
        return self._client.request("GET", f"/power_control/status/{power_control_id}")
