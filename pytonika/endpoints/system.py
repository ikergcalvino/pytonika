from typing import Any

from ._endpoint import Endpoint


class System(Endpoint):
    def system_actions_change_password_firstlogin(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Changes password on first login."""
        return self._client.request(
            "POST", "/system/actions/change_password_firstlogin", json=None if config is None else {"data": config}
        )

    def system_actions_reboot(self) -> dict[str, Any]:
        """Reboots device."""
        return self._client.request("POST", "/system/actions/reboot")

    def get_system_banner_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all banner configuration sections."""
        return self._client.request("GET", "/system/banner/config", params={"all_options": all_options})

    def update_system_banner_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates banner configuration sections."""
        return self._client.request("PUT", "/system/banner/config", json={"data": config})

    def get_system_banner_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified banner configuration section."""
        return self._client.request("GET", f"/system/banner/config/{config_id}", params={"all_options": all_options})

    def update_system_banner_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified banner configuration section."""
        return self._client.request("PUT", f"/system/banner/config/{config_id}", json={"data": config})

    def get_system_buttons_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Administration Button configuration sections."""
        return self._client.request("GET", "/system/buttons/config", params={"all_options": all_options})

    def update_system_buttons_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Administration Button configuration sections."""
        return self._client.request("PUT", "/system/buttons/config", json={"data": config})

    def get_system_buttons_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Administration Button configuration."""
        return self._client.request("GET", f"/system/buttons/config/{config_id}", params={"all_options": all_options})

    def update_system_buttons_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Administration Button configuration."""
        return self._client.request("PUT", f"/system/buttons/config/{config_id}", json={"data": config})

    def get_system_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the Administration General configuration."""
        return self._client.request("GET", "/system/config", params={"all_options": all_options})

    def update_system_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the Administration General configuration."""
        return self._client.request("PUT", "/system/config", json={"data": config})

    def get_system_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the Administration General configuration."""
        return self._client.request("GET", f"/system/config/{config_id}", params={"all_options": all_options})

    def update_system_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the Administration General configuration."""
        return self._client.request("PUT", f"/system/config/{config_id}", json={"data": config})

    def get_system_device_load_status(self) -> dict[str, Any]:
        """Returns device CPU load over a period of time."""
        return self._client.request("GET", "/system/device/load/status")

    def get_system_device_status(self) -> dict[str, Any]:
        """Returns system information."""
        return self._client.request("GET", "/system/device/status")

    def get_system_device_usage_status(self, *, data: str | None = None, exclude: str | None = None) -> dict[str, Any]:
        """Returns system status."""
        return self._client.request("GET", "/system/device/usage/status", params={"data": data, "exclude": exclude})

    def get_system_languages_options(self) -> dict[str, Any]:
        """Returns installed languages."""
        return self._client.request("GET", "/system/languages/options")

    def get_system_led_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all LED configurations."""
        return self._client.request("GET", "/system/led/config", params={"all_options": all_options})

    def update_system_led_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected LED configurations."""
        return self._client.request("PUT", "/system/led/config", json={"data": config})

    def get_system_led_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the selected LED configuration."""
        return self._client.request("GET", f"/system/led/config/{config_id}", params={"all_options": all_options})

    def update_system_led_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected LED configuration."""
        return self._client.request("PUT", f"/system/led/config/{config_id}", json={"data": config})
