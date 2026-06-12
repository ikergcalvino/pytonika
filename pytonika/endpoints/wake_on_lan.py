from typing import Any

from ._base import Endpoint


class WakeOnLan(Endpoint):
    def get_wol_options(self) -> dict[str, Any]:
        """Returns valid Wake on LAN interfaces."""
        endpoint = "/wol/options"

        return self._api_client.get(endpoint)

    def get_wol_global(self) -> dict[str, Any]:
        """Returns global Wake on LAN configuration."""
        endpoint = "/wol/global"

        return self._api_client.get(endpoint)

    def update_wol_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates global Wake on LAN configuration."""
        endpoint = "/wol/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_wol_config(self) -> dict[str, Any]:
        """Returns all Wake on LAN devices configuration sections."""
        endpoint = "/wol/config"

        return self._api_client.get(endpoint)

    def create_wol_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Wake on LAN device section."""
        endpoint = "/wol/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_wol_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Wake on LAN devices configurations."""
        endpoint = "/wol/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_wol_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Wake on LAN devices configurations."""
        return [self.delete_wol_config_by_id(config_id) for config_id in config]

    def get_wol_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified Wake on LAN device section."""
        endpoint = f"/wol/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_wol_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified Wake on LAN device configuration."""
        endpoint = f"/wol/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_wol_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified Wake on LAN device configuration."""
        endpoint = f"/wol/config/{config_id}"

        return self._api_client.delete(endpoint)

    def wol_actions_wake_device(self, data: dict[str, Any]) -> dict[str, Any]:
        """Wakes device."""
        endpoint = "/wol/actions/wake_device"

        return self._api_client.post(endpoint, data={"data": data})

    def wol_actions_wake_all_devices(self) -> dict[str, Any]:
        """Wakes all devices."""
        endpoint = "/wol/actions/wake_all_devices"

        return self._api_client.post(endpoint)
