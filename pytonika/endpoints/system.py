from typing import Any

from ._base import Endpoint


class System(Endpoint):
    def get_system_device_status(self) -> dict[str, Any]:
        """Returns system information."""
        endpoint = "/system/device/status"

        return self._api_client.get(endpoint)

    def get_system_device_usage_status(self) -> dict[str, Any]:
        """Returns system status."""
        endpoint = "/system/device/usage/status"

        return self._api_client.get(endpoint)

    def get_system_device_load_status(self) -> dict[str, Any]:
        """Returns device CPU load over a period of time.

        .. deprecated::
        """
        endpoint = "/system/device/load/status"

        return self._api_client.get(endpoint)

    def get_system_languages_options(self) -> dict[str, Any]:
        """Returns installed languages."""
        endpoint = "/system/languages/options"

        return self._api_client.get(endpoint)

    def get_system_config(self) -> dict[str, Any]:
        """Returns the Administration General configuration."""
        endpoint = "/system/config"

        return self._api_client.get(endpoint)

    def update_system_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the Administration General configuration."""
        endpoint = "/system/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_system_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the Administration General configuration."""
        endpoint = f"/system/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_system_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the Administration General configuration."""
        endpoint = f"/system/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def system_actions_change_password_firstlogin(self, config: dict[str, Any]) -> dict[str, Any]:
        """Changes password on first login."""
        endpoint = "/system/actions/change_password_firstlogin"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def system_actions_reboot(self) -> dict[str, Any]:
        """Reboots device."""
        endpoint = "/system/actions/reboot"

        return self._api_client.post(endpoint)

    def get_system_banner_config(self) -> dict[str, Any]:
        """Returns all banner configuration sections."""
        endpoint = "/system/banner/config"

        return self._api_client.get(endpoint)

    def update_system_banner_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates banner configuration sections."""
        endpoint = "/system/banner/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_system_banner_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified banner configuration section."""
        endpoint = f"/system/banner/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_system_banner_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified banner configuration section."""
        endpoint = f"/system/banner/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_system_led_config(self) -> dict[str, Any]:
        """Returns all LED configurations."""
        endpoint = "/system/led/config"

        return self._api_client.get(endpoint)

    def update_system_led_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected LED configurations."""
        endpoint = "/system/led/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_system_led_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the selected LED configuration."""
        endpoint = f"/system/led/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_system_led_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected LED configuration."""
        endpoint = f"/system/led/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_system_buttons_config(self) -> dict[str, Any]:
        """Returns all Administration Button configuration sections."""
        endpoint = "/system/buttons/config"

        return self._api_client.get(endpoint)

    def get_system_buttons_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified Administration Button configuration."""
        endpoint = f"/system/buttons/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_system_buttons_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Administration Button configuration."""
        endpoint = f"/system/buttons/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def update_system_buttons_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Administration Button configuration sections."""
        endpoint = "/system/buttons/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
