from typing import Any

from ._endpoint import Endpoint


class ModemControl(Endpoint):
    def get_modem_control_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Modem Control configurations."""
        return self._client.request("GET", "/modem_control/config", params={"all_options": all_options})

    def create_modem_control_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Modem Control configuration."""
        return self._client.request("POST", "/modem_control/config", json={"data": config})

    def update_modem_control_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Modem Control configurations."""
        return self._client.request("PUT", "/modem_control/config", json={"data": config})

    def delete_modem_control_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Modem Control configurations."""
        return self._client.request("DELETE", "/modem_control/config", json={"data": config})

    def get_modem_control_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Modem Control configuration."""
        return self._client.request("GET", f"/modem_control/config/{config_id}", params={"all_options": all_options})

    def update_modem_control_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Modem Control configuration."""
        return self._client.request("PUT", f"/modem_control/config/{config_id}", json={"data": config})

    def delete_modem_control_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Modem Control configuration."""
        return self._client.request("DELETE", f"/modem_control/config/{config_id}")

    def get_modem_control_status(self) -> dict[str, Any]:
        """Returns Modem Control status."""
        return self._client.request("GET", "/modem_control/status")
