from typing import Any

from ._endpoint import Endpoint


class SiteManager(Endpoint):
    def get_site_manager_auto_reboot_ping_wget_config(self) -> dict[str, Any]:
        """Returns all Site manager Ping/Wget Reboot configurations."""
        return self._client.request("GET", "/site_manager/auto_reboot/ping_wget/config")

    def create_site_manager_auto_reboot_ping_wget_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Site manager Ping/Wget Reboot configuration."""
        return self._client.request("POST", "/site_manager/auto_reboot/ping_wget/config", json={"data": config})

    def update_site_manager_auto_reboot_ping_wget_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Site manager Ping/Wget Reboot configurations."""
        return self._client.request("PUT", "/site_manager/auto_reboot/ping_wget/config", json={"data": config})

    def delete_site_manager_auto_reboot_ping_wget_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the selected Site manager Ping/Wget Reboot configurations."""
        return self._client.request("DELETE", "/site_manager/auto_reboot/ping_wget/config", json={"data": config})

    def get_site_manager_auto_reboot_ping_wget_config_by_id(self, ping_wget_id: str) -> dict[str, Any]:
        """Returns the selected Site manager Ping/Wget Reboot configuration."""
        return self._client.request("GET", f"/site_manager/auto_reboot/ping_wget/config/{ping_wget_id}")

    def update_site_manager_auto_reboot_ping_wget_config_by_id(
        self, ping_wget_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the selected Site manager Ping/Wget Reboot configuration."""
        return self._client.request(
            "PUT", f"/site_manager/auto_reboot/ping_wget/config/{ping_wget_id}", json={"data": config}
        )

    def delete_site_manager_auto_reboot_ping_wget_config_by_id(self, ping_wget_id: str) -> dict[str, Any]:
        """Deletes the selected Site manager Ping/Wget Reboot configuration."""
        return self._client.request("DELETE", f"/site_manager/auto_reboot/ping_wget/config/{ping_wget_id}")

    def get_site_manager_auto_reboot_scheduler_config(self) -> dict[str, Any]:
        """Returns all Site manager Reboot Scheduler configurations."""
        return self._client.request("GET", "/site_manager/auto_reboot/scheduler/config")

    def create_site_manager_auto_reboot_scheduler_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Site manager Reboot Scheduler configuration."""
        return self._client.request("POST", "/site_manager/auto_reboot/scheduler/config", json={"data": config})

    def update_site_manager_auto_reboot_scheduler_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Site manager Reboot Scheduler configurations."""
        return self._client.request("PUT", "/site_manager/auto_reboot/scheduler/config", json={"data": config})

    def delete_site_manager_auto_reboot_scheduler_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the selected Site manager Reboot Scheduler configurations."""
        return self._client.request("DELETE", "/site_manager/auto_reboot/scheduler/config", json={"data": config})

    def get_site_manager_auto_reboot_scheduler_config_by_id(self, scheduler_id: str) -> dict[str, Any]:
        """Returns the selected Site manager Reboot Scheduler configuration."""
        return self._client.request("GET", f"/site_manager/auto_reboot/scheduler/config/{scheduler_id}")

    def update_site_manager_auto_reboot_scheduler_config_by_id(
        self, scheduler_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the selected Site manager Reboot Scheduler configuration."""
        return self._client.request(
            "PUT", f"/site_manager/auto_reboot/scheduler/config/{scheduler_id}", json={"data": config}
        )

    def delete_site_manager_auto_reboot_scheduler_config_by_id(self, scheduler_id: str) -> dict[str, Any]:
        """Deletes the selected Site manager Reboot Scheduler configuration."""
        return self._client.request("DELETE", f"/site_manager/auto_reboot/scheduler/config/{scheduler_id}")

    def site_manager_devices_actions_api(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Proxy API request to the device."""
        return self._client.request(
            "POST", "/site_manager/devices/actions/api", json=None if config is None else {"data": config}
        )

    def site_manager_devices_actions_clear_errors(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Clears device's errors which happened during synchronization."""
        return self._client.request(
            "POST", "/site_manager/devices/actions/clear_errors", json=None if config is None else {"data": config}
        )

    def site_manager_devices_actions_download(self, config: dict[str, Any] | None = None) -> bytes | dict[str, Any]:
        """Downloads a file from the selected device."""
        return self._client.request(
            "POST",
            "/site_manager/devices/actions/download",
            json=None if config is None else {"data": config},
            download=True,
        )

    def site_manager_devices_actions_pair(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Pairs the selected device."""
        return self._client.request(
            "POST", "/site_manager/devices/actions/pair", json=None if config is None else {"data": config}
        )

    def site_manager_devices_actions_reboot(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Reboots the selected device."""
        return self._client.request(
            "POST", "/site_manager/devices/actions/reboot", json=None if config is None else {"data": config}
        )

    def site_manager_devices_actions_unpair(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Unpairs the selected device."""
        return self._client.request(
            "POST", "/site_manager/devices/actions/unpair", json=None if config is None else {"data": config}
        )

    def site_manager_devices_actions_upgrade_fota(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Upgrades firmware for the selected devices."""
        return self._client.request(
            "POST", "/site_manager/devices/actions/upgrade_fota", json=None if config is None else {"data": config}
        )

    def get_site_manager_devices_config(self) -> dict[str, Any]:
        """Returns all paired device configurations."""
        return self._client.request("GET", "/site_manager/devices/config")

    def update_site_manager_devices_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected paired device configurations."""
        return self._client.request("PUT", "/site_manager/devices/config", json={"data": config})

    def get_site_manager_devices_config_by_id(self, device_id: str) -> dict[str, Any]:
        """Returns the selected paired device configuration."""
        return self._client.request("GET", f"/site_manager/devices/config/{device_id}")

    def update_site_manager_devices_config_by_id(self, device_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected paired device configuration."""
        return self._client.request("PUT", f"/site_manager/devices/config/{device_id}", json={"data": config})

    def get_site_manager_devices_status(self, *, exclude_firmware_status: int | None = None) -> dict[str, Any]:
        """Returns the status of all devices."""
        return self._client.request(
            "GET", "/site_manager/devices/status", params={"exclude_firmware_status": exclude_firmware_status}
        )

    def get_site_manager_devices_status_by_id_or_mac(
        self, id_or_mac: str, *, exclude_firmware_status: int | None = None
    ) -> dict[str, Any]:
        """Returns the status of the selected device."""
        return self._client.request(
            "GET",
            f"/site_manager/devices/status/{id_or_mac}",
            params={"exclude_firmware_status": exclude_firmware_status},
        )

    def get_site_manager_devices_status_full(
        self,
        *,
        events_log_limit: int | None = None,
        data: str | None = None,
        exclude_firmware_status: int | None = None,
    ) -> dict[str, Any]:
        """Returns the full status of all devices."""
        return self._client.request(
            "GET",
            "/site_manager/devices/status_full",
            params={
                "events_log_limit": events_log_limit,
                "data": data,
                "exclude_firmware_status": exclude_firmware_status,
            },
        )

    def get_site_manager_devices_status_full_by_id_or_mac(
        self,
        id_or_mac: str,
        *,
        events_log_limit: int | None = None,
        data: str | None = None,
        exclude_firmware_status: int | None = None,
    ) -> dict[str, Any]:
        """Returns the full status of the selected device."""
        return self._client.request(
            "GET",
            f"/site_manager/devices/status_full/{id_or_mac}",
            params={
                "events_log_limit": events_log_limit,
                "data": data,
                "exclude_firmware_status": exclude_firmware_status,
            },
        )

    def get_site_manager_global(self) -> dict[str, Any]:
        """Returns Site manager global configuration."""
        return self._client.request("GET", "/site_manager/global")

    def update_site_manager_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Site manager global configuration."""
        return self._client.request("PUT", "/site_manager/global", json={"data": config})

    def get_site_manager_groups_config(self) -> dict[str, Any]:
        """Returns all Site manager group configurations."""
        return self._client.request("GET", "/site_manager/groups/config")

    def create_site_manager_groups_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Site manager group configuration."""
        return self._client.request("POST", "/site_manager/groups/config", json={"data": config})

    def update_site_manager_groups_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Site manager group configurations."""
        return self._client.request("PUT", "/site_manager/groups/config", json={"data": config})

    def delete_site_manager_groups_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the selected Site manager group configurations."""
        return self._client.request("DELETE", "/site_manager/groups/config", json={"data": config})

    def get_site_manager_groups_config_by_id(self, group_id: str) -> dict[str, Any]:
        """Returns the selected Site manager group configuration."""
        return self._client.request("GET", f"/site_manager/groups/config/{group_id}")

    def update_site_manager_groups_config_by_id(self, group_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected Site manager group configuration."""
        return self._client.request("PUT", f"/site_manager/groups/config/{group_id}", json={"data": config})

    def delete_site_manager_groups_config_by_id(self, group_id: str) -> dict[str, Any]:
        """Deletes the selected Site manager group configuration."""
        return self._client.request("DELETE", f"/site_manager/groups/config/{group_id}")

    def get_site_manager_interfaces_config(self) -> dict[str, Any]:
        """Returns all Site manager network interface configurations."""
        return self._client.request("GET", "/site_manager/interfaces/config")

    def update_site_manager_interfaces_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Site manager network interface configurations."""
        return self._client.request("PUT", "/site_manager/interfaces/config", json={"data": config})

    def get_site_manager_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Returns the selected Site manager network interface configuration."""
        return self._client.request("GET", f"/site_manager/interfaces/config/{interface_id}")

    def update_site_manager_interfaces_config_by_id(self, interface_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected Site manager network interface configuration."""
        return self._client.request("PUT", f"/site_manager/interfaces/config/{interface_id}", json={"data": config})

    def get_site_manager_ports_settings_config(self) -> dict[str, Any]:
        """Returns all Site manager switch port configurations."""
        return self._client.request("GET", "/site_manager/ports_settings/config")

    def update_site_manager_ports_settings_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Site manager switch port configurations."""
        return self._client.request("PUT", "/site_manager/ports_settings/config", json={"data": config})

    def get_site_manager_ports_settings_config_by_id(self, ports_setting_id: str) -> dict[str, Any]:
        """Returns the selected Site manager switch port configuration."""
        return self._client.request("GET", f"/site_manager/ports_settings/config/{ports_setting_id}")

    def update_site_manager_ports_settings_config_by_id(
        self, ports_setting_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the selected Site manager switch port configuration."""
        return self._client.request(
            "PUT", f"/site_manager/ports_settings/config/{ports_setting_id}", json={"data": config}
        )

    def get_site_manager_switch_interfaces_config(self) -> dict[str, Any]:
        """Returns all Site manager switch interface configurations."""
        return self._client.request("GET", "/site_manager/switch/interfaces/config")

    def create_site_manager_switch_interfaces_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Site manager switch interface configuration."""
        return self._client.request("POST", "/site_manager/switch/interfaces/config", json={"data": config})

    def update_site_manager_switch_interfaces_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Site manager switch interface configurations."""
        return self._client.request("PUT", "/site_manager/switch/interfaces/config", json={"data": config})

    def delete_site_manager_switch_interfaces_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the selected Site manager switch interface configurations."""
        return self._client.request("DELETE", "/site_manager/switch/interfaces/config", json={"data": config})

    def get_site_manager_switch_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Returns the selected Site manager switch interface configuration."""
        return self._client.request("GET", f"/site_manager/switch/interfaces/config/{interface_id}")

    def update_site_manager_switch_interfaces_config_by_id(
        self, interface_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the selected Site manager switch interface configuration."""
        return self._client.request(
            "PUT", f"/site_manager/switch/interfaces/config/{interface_id}", json={"data": config}
        )

    def delete_site_manager_switch_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Deletes the selected Site manager switch interface configuration."""
        return self._client.request("DELETE", f"/site_manager/switch/interfaces/config/{interface_id}")

    def get_site_manager_switch_vlan_config(self) -> dict[str, Any]:
        """Returns all Site manager VLAN configurations."""
        return self._client.request("GET", "/site_manager/switch/vlan/config")

    def create_site_manager_switch_vlan_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Site manager VLAN configuration."""
        return self._client.request("POST", "/site_manager/switch/vlan/config", json={"data": config})

    def update_site_manager_switch_vlan_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Site manager VLAN configurations."""
        return self._client.request("PUT", "/site_manager/switch/vlan/config", json={"data": config})

    def delete_site_manager_switch_vlan_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the selected Site manager VLAN configurations."""
        return self._client.request("DELETE", "/site_manager/switch/vlan/config", json={"data": config})

    def get_site_manager_switch_vlan_config_by_id(self, vlan_id: str) -> dict[str, Any]:
        """Returns the selected Site manager VLAN configuration."""
        return self._client.request("GET", f"/site_manager/switch/vlan/config/{vlan_id}")

    def update_site_manager_switch_vlan_config_by_id(self, vlan_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected Site manager VLAN configuration."""
        return self._client.request("PUT", f"/site_manager/switch/vlan/config/{vlan_id}", json={"data": config})

    def delete_site_manager_switch_vlan_config_by_id(self, vlan_id: str) -> dict[str, Any]:
        """Deletes the selected Site manager VLAN configuration."""
        return self._client.request("DELETE", f"/site_manager/switch/vlan/config/{vlan_id}")

    def get_site_manager_wireless_devices_config(self) -> dict[str, Any]:
        """Returns all Site manager wireless device configurations."""
        return self._client.request("GET", "/site_manager/wireless/devices/config")

    def update_site_manager_wireless_devices_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Site manager wireless device configurations."""
        return self._client.request("PUT", "/site_manager/wireless/devices/config", json={"data": config})

    def get_site_manager_wireless_devices_config_by_id(self, device_id: str) -> dict[str, Any]:
        """Returns the selected Site manager wireless device configuration."""
        return self._client.request("GET", f"/site_manager/wireless/devices/config/{device_id}")

    def update_site_manager_wireless_devices_config_by_id(
        self, device_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the selected Site manager wireless device configuration."""
        return self._client.request("PUT", f"/site_manager/wireless/devices/config/{device_id}", json={"data": config})

    def get_site_manager_wireless_interfaces_config(self) -> dict[str, Any]:
        """Returns all Site manager wireless interface configurations."""
        return self._client.request("GET", "/site_manager/wireless/interfaces/config")

    def create_site_manager_wireless_interfaces_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Site manager wireless interface configuration."""
        return self._client.request("POST", "/site_manager/wireless/interfaces/config", json={"data": config})

    def update_site_manager_wireless_interfaces_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Site manager wireless interface configurations."""
        return self._client.request("PUT", "/site_manager/wireless/interfaces/config", json={"data": config})

    def delete_site_manager_wireless_interfaces_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the selected Site manager wireless interface configurations."""
        return self._client.request("DELETE", "/site_manager/wireless/interfaces/config", json={"data": config})

    def get_site_manager_wireless_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Returns the selected Site manager wireless interface configuration."""
        return self._client.request("GET", f"/site_manager/wireless/interfaces/config/{interface_id}")

    def update_site_manager_wireless_interfaces_config_by_id(
        self, interface_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the selected Site manager wireless interface configuration."""
        return self._client.request(
            "PUT", f"/site_manager/wireless/interfaces/config/{interface_id}", json={"data": config}
        )

    def delete_site_manager_wireless_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Deletes the selected Site manager wireless interface configuration."""
        return self._client.request("DELETE", f"/site_manager/wireless/interfaces/config/{interface_id}")
