from typing import Any

from ._endpoint import Endpoint


class WakeOnLan(Endpoint):
    def wol_actions_wake_all_devices(self) -> dict[str, Any]:
        """Wakes all devices."""
        return self._client.request("POST", "/wol/actions/wake_all_devices")

    def wol_actions_wake_device(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Wakes device."""
        return self._client.request("POST", "/wol/actions/wake_device", json=None if data is None else {"data": data})

    def get_wol_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Wake on LAN devices configuration sections."""
        return self._client.request("GET", "/wol/config", params={"all_options": all_options})

    def create_wol_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Wake on LAN device section."""
        return self._client.request("POST", "/wol/config", json={"data": config})

    def update_wol_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified Wake on LAN devices configurations."""
        return self._client.request("PUT", "/wol/config", json=config)

    def delete_wol_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Wake on LAN devices configurations."""
        return self._client.request("DELETE", "/wol/config", json={"data": config})

    def get_wol_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified Wake on LAN device section."""
        return self._client.request("GET", f"/wol/config/{config_id}", params={"all_options": all_options})

    def update_wol_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified Wake on LAN device configuration."""
        return self._client.request("PUT", f"/wol/config/{config_id}", json={"data": config})

    def delete_wol_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified Wake on LAN device configuration."""
        return self._client.request("DELETE", f"/wol/config/{config_id}")

    def get_wol_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns global Wake on LAN configuration."""
        return self._client.request("GET", "/wol/global", params={"all_options": all_options})

    def update_wol_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates global Wake on LAN configuration."""
        return self._client.request("PUT", "/wol/global", json={"data": config})

    def get_wol_options(self) -> dict[str, Any]:
        """Returns valid Wake on LAN interfaces."""
        return self._client.request("GET", "/wol/options")
