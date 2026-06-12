from typing import Any

from ._base import Endpoint


class SiteManager(Endpoint):
    def get_site_manager_interfaces_config(self) -> dict[str, Any]:
        """Returns all Site manager network interface configurations."""
        endpoint = "/site_manager/interfaces/config"

        return self._api_client.get(endpoint)

    def update_site_manager_interfaces_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Site manager network interface configurations."""
        endpoint = "/site_manager/interfaces/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_site_manager_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Returns the selected Site manager network interface configuration."""
        endpoint = f"/site_manager/interfaces/config/{interface_id}"

        return self._api_client.get(endpoint)

    def update_site_manager_interfaces_config_by_id(self, interface_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected Site manager network interface configuration."""
        endpoint = f"/site_manager/interfaces/config/{interface_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_site_manager_wireless_interfaces_config(self) -> dict[str, Any]:
        """Returns all Site manager wireless interface configurations."""
        endpoint = "/site_manager/wireless/interfaces/config"

        return self._api_client.get(endpoint)

    def create_site_manager_wireless_interfaces_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Site manager wireless interface configuration."""
        endpoint = "/site_manager/wireless/interfaces/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_site_manager_wireless_interfaces_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Site manager wireless interface configurations."""
        endpoint = "/site_manager/wireless/interfaces/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_site_manager_wireless_interfaces_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected Site manager wireless interface configurations."""
        return [self.delete_site_manager_wireless_interfaces_config_by_id(interface_id) for interface_id in config]

    def get_site_manager_wireless_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Returns the selected Site manager wireless interface configuration."""
        endpoint = f"/site_manager/wireless/interfaces/config/{interface_id}"

        return self._api_client.get(endpoint)

    def update_site_manager_wireless_interfaces_config_by_id(
        self, interface_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the selected Site manager wireless interface configuration."""
        endpoint = f"/site_manager/wireless/interfaces/config/{interface_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_site_manager_wireless_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Deletes the selected Site manager wireless interface configuration."""
        endpoint = f"/site_manager/wireless/interfaces/config/{interface_id}"

        return self._api_client.delete(endpoint)

    def get_site_manager_global(self) -> dict[str, Any]:
        """Returns Site manager global configuration."""
        endpoint = "/site_manager/global"

        return self._api_client.get(endpoint)

    def update_site_manager_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Site manager global configuration."""
        endpoint = "/site_manager/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_site_manager_groups_config(self) -> dict[str, Any]:
        """Returns all Site manager group configurations."""
        endpoint = "/site_manager/groups/config"

        return self._api_client.get(endpoint)

    def create_site_manager_groups_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Site manager group configuration."""
        endpoint = "/site_manager/groups/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_site_manager_groups_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Site manager group configurations."""
        endpoint = "/site_manager/groups/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_site_manager_groups_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected Site manager group configurations."""
        return [self.delete_site_manager_groups_config_by_id(group_id) for group_id in config]

    def get_site_manager_groups_config_by_id(self, group_id: str) -> dict[str, Any]:
        """Returns the selected Site manager group configuration."""
        endpoint = f"/site_manager/groups/config/{group_id}"

        return self._api_client.get(endpoint)

    def update_site_manager_groups_config_by_id(self, group_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected Site manager group configuration."""
        endpoint = f"/site_manager/groups/config/{group_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_site_manager_groups_config_by_id(self, group_id: str) -> dict[str, Any]:
        """Deletes the selected Site manager group configuration."""
        endpoint = f"/site_manager/groups/config/{group_id}"

        return self._api_client.delete(endpoint)

    def get_site_manager_ports_settings_config(self) -> dict[str, Any]:
        """Returns all Site manager switch port configurations."""
        endpoint = "/site_manager/ports_settings/config"

        return self._api_client.get(endpoint)

    def update_site_manager_ports_settings_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Site manager switch port configurations."""
        endpoint = "/site_manager/ports_settings/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_site_manager_ports_settings_config_by_id(self, ports_setting_id: str) -> dict[str, Any]:
        """Returns the selected Site manager switch port configuration."""
        endpoint = f"/site_manager/ports_settings/config/{ports_setting_id}"

        return self._api_client.get(endpoint)

    def update_site_manager_ports_settings_config_by_id(
        self, ports_setting_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the selected Site manager switch port configuration."""
        endpoint = f"/site_manager/ports_settings/config/{ports_setting_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_site_manager_switch_interfaces_config(self) -> dict[str, Any]:
        """Returns all Site manager switch interface configurations."""
        endpoint = "/site_manager/switch/interfaces/config"

        return self._api_client.get(endpoint)

    def create_site_manager_switch_interfaces_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Site manager switch interface configuration."""
        endpoint = "/site_manager/switch/interfaces/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_site_manager_switch_interfaces_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Site manager switch interface configurations."""
        endpoint = "/site_manager/switch/interfaces/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_site_manager_switch_interfaces_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected Site manager switch interface configurations."""
        return [self.delete_site_manager_switch_interfaces_config_by_id(interface_id) for interface_id in config]

    def get_site_manager_switch_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Returns the selected Site manager switch interface configuration."""
        endpoint = f"/site_manager/switch/interfaces/config/{interface_id}"

        return self._api_client.get(endpoint)

    def update_site_manager_switch_interfaces_config_by_id(
        self, interface_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the selected Site manager switch interface configuration."""
        endpoint = f"/site_manager/switch/interfaces/config/{interface_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_site_manager_switch_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Deletes the selected Site manager switch interface configuration."""
        endpoint = f"/site_manager/switch/interfaces/config/{interface_id}"

        return self._api_client.delete(endpoint)

    def get_site_manager_switch_vlan_config(self) -> dict[str, Any]:
        """Returns all Site manager VLAN configurations."""
        endpoint = "/site_manager/switch/vlan/config"

        return self._api_client.get(endpoint)

    def create_site_manager_switch_vlan_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Site manager VLAN configuration."""
        endpoint = "/site_manager/switch/vlan/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_site_manager_switch_vlan_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Site manager VLAN configurations."""
        endpoint = "/site_manager/switch/vlan/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_site_manager_switch_vlan_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected Site manager VLAN configurations."""
        return [self.delete_site_manager_switch_vlan_config_by_id(vlan_id) for vlan_id in config]

    def get_site_manager_switch_vlan_config_by_id(self, vlan_id: str) -> dict[str, Any]:
        """Returns the selected Site manager VLAN configuration."""
        endpoint = f"/site_manager/switch/vlan/config/{vlan_id}"

        return self._api_client.get(endpoint)

    def update_site_manager_switch_vlan_config_by_id(self, vlan_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected Site manager VLAN configuration."""
        endpoint = f"/site_manager/switch/vlan/config/{vlan_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_site_manager_switch_vlan_config_by_id(self, vlan_id: str) -> dict[str, Any]:
        """Deletes the selected Site manager VLAN configuration."""
        endpoint = f"/site_manager/switch/vlan/config/{vlan_id}"

        return self._api_client.delete(endpoint)

    def get_site_manager_auto_reboot_scheduler_config(self) -> dict[str, Any]:
        """Returns all Site manager Reboot Scheduler configurations."""
        endpoint = "/site_manager/auto_reboot/scheduler/config"

        return self._api_client.get(endpoint)

    def create_site_manager_auto_reboot_scheduler_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Site manager Reboot Scheduler configuration."""
        endpoint = "/site_manager/auto_reboot/scheduler/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_site_manager_auto_reboot_scheduler_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Site manager Reboot Scheduler configurations."""
        endpoint = "/site_manager/auto_reboot/scheduler/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_site_manager_auto_reboot_scheduler_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected Site manager Reboot Scheduler configurations."""
        return [self.delete_site_manager_auto_reboot_scheduler_config_by_id(scheduler_id) for scheduler_id in config]

    def get_site_manager_auto_reboot_scheduler_config_by_id(self, scheduler_id: str) -> dict[str, Any]:
        """Returns the selected Site manager Reboot Scheduler configuration."""
        endpoint = f"/site_manager/auto_reboot/scheduler/config/{scheduler_id}"

        return self._api_client.get(endpoint)

    def update_site_manager_auto_reboot_scheduler_config_by_id(
        self, scheduler_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the selected Site manager Reboot Scheduler configuration."""
        endpoint = f"/site_manager/auto_reboot/scheduler/config/{scheduler_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_site_manager_auto_reboot_scheduler_config_by_id(self, scheduler_id: str) -> dict[str, Any]:
        """Deletes the selected Site manager Reboot Scheduler configuration."""
        endpoint = f"/site_manager/auto_reboot/scheduler/config/{scheduler_id}"

        return self._api_client.delete(endpoint)

    def get_site_manager_auto_reboot_ping_wget_config(self) -> dict[str, Any]:
        """Returns all Site manager Ping/Wget Reboot configurations."""
        endpoint = "/site_manager/auto_reboot/ping_wget/config"

        return self._api_client.get(endpoint)

    def create_site_manager_auto_reboot_ping_wget_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Site manager Ping/Wget Reboot configuration."""
        endpoint = "/site_manager/auto_reboot/ping_wget/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_site_manager_auto_reboot_ping_wget_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Site manager Ping/Wget Reboot configurations."""
        endpoint = "/site_manager/auto_reboot/ping_wget/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_site_manager_auto_reboot_ping_wget_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected Site manager Ping/Wget Reboot configurations."""
        return [self.delete_site_manager_auto_reboot_ping_wget_config_by_id(ping_wget_id) for ping_wget_id in config]

    def get_site_manager_auto_reboot_ping_wget_config_by_id(self, ping_wget_id: str) -> dict[str, Any]:
        """Returns the selected Site manager Ping/Wget Reboot configuration."""
        endpoint = f"/site_manager/auto_reboot/ping_wget/config/{ping_wget_id}"

        return self._api_client.get(endpoint)

    def update_site_manager_auto_reboot_ping_wget_config_by_id(
        self, ping_wget_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the selected Site manager Ping/Wget Reboot configuration."""
        endpoint = f"/site_manager/auto_reboot/ping_wget/config/{ping_wget_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_site_manager_auto_reboot_ping_wget_config_by_id(self, ping_wget_id: str) -> dict[str, Any]:
        """Deletes the selected Site manager Ping/Wget Reboot configuration."""
        endpoint = f"/site_manager/auto_reboot/ping_wget/config/{ping_wget_id}"

        return self._api_client.delete(endpoint)

    def get_site_manager_wireless_devices_config(self) -> dict[str, Any]:
        """Returns all Site manager wireless device configurations."""
        endpoint = "/site_manager/wireless/devices/config"

        return self._api_client.get(endpoint)

    def update_site_manager_wireless_devices_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Site manager wireless device configurations."""
        endpoint = "/site_manager/wireless/devices/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_site_manager_wireless_devices_config_by_id(self, device_id: str) -> dict[str, Any]:
        """Returns the selected Site manager wireless device configuration."""
        endpoint = f"/site_manager/wireless/devices/config/{device_id}"

        return self._api_client.get(endpoint)

    def update_site_manager_wireless_devices_config_by_id(
        self, device_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the selected Site manager wireless device configuration."""
        endpoint = f"/site_manager/wireless/devices/config/{device_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_site_manager_devices_config(self) -> dict[str, Any]:
        """Returns all paired device configurations."""
        endpoint = "/site_manager/devices/config"

        return self._api_client.get(endpoint)

    def update_site_manager_devices_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected paired device configurations."""
        endpoint = "/site_manager/devices/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_site_manager_devices_config_by_id(self, device_id: str) -> dict[str, Any]:
        """Returns the selected paired device configuration."""
        endpoint = f"/site_manager/devices/config/{device_id}"

        return self._api_client.get(endpoint)

    def update_site_manager_devices_config_by_id(self, device_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected paired device configuration."""
        endpoint = f"/site_manager/devices/config/{device_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_site_manager_devices_status(self) -> dict[str, Any]:
        """Returns the status of all devices."""
        endpoint = "/site_manager/devices/status"

        return self._api_client.get(endpoint)

    def get_site_manager_devices_status_by_id_or_mac(self, id_or_mac: str) -> dict[str, Any]:
        """Returns the status of the selected device."""
        endpoint = f"/site_manager/devices/status/{id_or_mac}"

        return self._api_client.get(endpoint)

    def get_site_manager_devices_status_full(self) -> dict[str, Any]:
        """Returns the full status of all devices."""
        endpoint = "/site_manager/devices/status_full"

        return self._api_client.get(endpoint)

    def get_site_manager_devices_status_full_by_id_or_mac(self, id_or_mac: str) -> dict[str, Any]:
        """Returns the full status of the selected device."""
        endpoint = f"/site_manager/devices/status_full/{id_or_mac}"

        return self._api_client.get(endpoint)

    def site_manager_devices_actions_pair(self, config: dict[str, Any]) -> dict[str, Any]:
        """Pairs the selected device."""
        endpoint = "/site_manager/devices/actions/pair"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def site_manager_devices_actions_unpair(self, config: dict[str, Any]) -> dict[str, Any]:
        """Unpairs the selected device."""
        endpoint = "/site_manager/devices/actions/unpair"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def site_manager_devices_actions_download(self, config: dict[str, Any]) -> dict[str, Any]:
        """Downloads a file from the selected device."""
        endpoint = "/site_manager/devices/actions/download"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def site_manager_devices_actions_reboot(self, config: dict[str, Any]) -> dict[str, Any]:
        """Reboots the selected device."""
        endpoint = "/site_manager/devices/actions/reboot"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def site_manager_devices_actions_api(self, config: dict[str, Any]) -> dict[str, Any]:
        """Proxy API request to the device."""
        endpoint = "/site_manager/devices/actions/api"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def site_manager_devices_actions_upgrade_fota(self, config: dict[str, Any]) -> dict[str, Any]:
        """Upgrades firmware for the selected devices."""
        endpoint = "/site_manager/devices/actions/upgrade_fota"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def site_manager_devices_actions_clear_errors(self, config: dict[str, Any]) -> dict[str, Any]:
        """Clears device's errors which happened during synchronization."""
        endpoint = "/site_manager/devices/actions/clear_errors"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)
