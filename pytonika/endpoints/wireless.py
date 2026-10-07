from typing import Any

from ._endpoint import Endpoint, File


class Wireless(Endpoint):
    def wireless_actions_ban(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Bans the specified client from the network."""
        return self._client.request("POST", "/wireless/actions/ban", json=None if data is None else {"data": data})

    def wireless_actions_disconnect(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Sends a signal to disconnect from wireless AP."""
        return self._client.request(
            "POST", "/wireless/actions/disconnect", json=None if data is None else {"data": data}
        )

    def wireless_actions_join(
        self, data: dict[str, Any] | None = None, *, use_cache: bool | None = None
    ) -> dict[str, Any]:
        """Joins the specified Wi-Fi network."""
        return self._client.request(
            "POST",
            "/wireless/actions/join",
            params={"use_cache": use_cache},
            json=None if data is None else {"data": data},
        )

    def wireless_actions_kick(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Kicks the specified client from the network."""
        return self._client.request("POST", "/wireless/actions/kick", json=None if data is None else {"data": data})

    def wireless_actions_reconnect(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Sends a signal to try to reconnect to wireless AP."""
        return self._client.request(
            "POST", "/wireless/actions/reconnect", json=None if data is None else {"data": data}
        )

    def wireless_actions_scan(
        self, data: dict[str, Any] | None = None, *, use_cache: str | None = None
    ) -> dict[str, Any]:
        """Scans the environment for nearby Wi-Fi networks."""
        return self._client.request(
            "POST",
            "/wireless/actions/scan",
            params={"use_cache": use_cache},
            json=None if data is None else {"data": data},
        )

    def get_wireless_devices_config(self) -> dict[str, Any]:
        """Returns wireless device configurations."""
        return self._client.request("GET", "/wireless/devices/config")

    def update_wireless_devices_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates wireless device configurations."""
        return self._client.request("PUT", "/wireless/devices/config", json={"data": config})

    def get_wireless_devices_config_by_id(self, device_id: str) -> dict[str, Any]:
        """Returns wireless device configuration."""
        return self._client.request("GET", f"/wireless/devices/config/{device_id}")

    def update_wireless_devices_config_by_id(self, device_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates wireless device configuration."""
        return self._client.request("PUT", f"/wireless/devices/config/{device_id}", json={"data": config})

    def get_wireless_devices_global(self) -> dict[str, Any]:
        """Returns wireless device global configuration."""
        return self._client.request("GET", "/wireless/devices/global")

    def update_wireless_devices_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates wireless device global configuration."""
        return self._client.request("PUT", "/wireless/devices/global", json={"data": config})

    def get_wireless_devices_options(self) -> dict[str, Any]:
        """Returns wireless device options."""
        return self._client.request("GET", "/wireless/devices/options")

    def get_wireless_devices_options_by_id(self, device_id: str) -> dict[str, Any]:
        """Returns wireless device options."""
        return self._client.request("GET", f"/wireless/devices/options/{device_id}")

    def get_wireless_devices_status(self) -> dict[str, Any]:
        """Returns wireless device statuses."""
        return self._client.request("GET", "/wireless/devices/status")

    def get_wireless_devices_status_by_id(self, device_id: str) -> dict[str, Any]:
        """Returns wireless device status."""
        return self._client.request("GET", f"/wireless/devices/status/{device_id}")

    def get_wireless_guest_network_general_config_general(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns guest network general configuration."""
        return self._client.request(
            "GET", "/wireless/guest_network/general/config/general", params={"all_options": all_options}
        )

    def update_wireless_guest_network_general_config_general(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates guest network general configuration."""
        return self._client.request("PUT", "/wireless/guest_network/general/config/general", json={"data": config})

    def get_wireless_guest_network_general_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns guest network configuration."""
        return self._client.request(
            "GET", f"/wireless/guest_network/general/config/{config_id}", params={"all_options": all_options}
        )

    def update_wireless_guest_network_general_config_by_id(
        self, config_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates guest network configuration."""
        return self._client.request("PUT", f"/wireless/guest_network/general/config/{config_id}", json={"data": config})

    def get_wireless_guest_network_interfaces_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all guest network interface sections."""
        return self._client.request(
            "GET", "/wireless/guest_network/interfaces/config", params={"all_options": all_options}
        )

    def create_wireless_guest_network_interfaces_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new guest network interface section."""
        return self._client.request("POST", "/wireless/guest_network/interfaces/config", json={"data": config})

    def update_wireless_guest_network_interfaces_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected guest network interface sections."""
        return self._client.request("PUT", "/wireless/guest_network/interfaces/config", json={"data": config})

    def delete_wireless_guest_network_interfaces_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes guest network interface configurations."""
        return self._client.request("DELETE", "/wireless/guest_network/interfaces/config", json={"data": config})

    def get_wireless_guest_network_interfaces_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the selected guest network interface section."""
        return self._client.request(
            "GET", f"/wireless/guest_network/interfaces/config/{config_id}", params={"all_options": all_options}
        )

    def update_wireless_guest_network_interfaces_config_by_id(
        self, config_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the selected guest network interface section."""
        return self._client.request(
            "PUT", f"/wireless/guest_network/interfaces/config/{config_id}", json={"data": config}
        )

    def delete_wireless_guest_network_interfaces_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the selected guest network interface section."""
        return self._client.request("DELETE", f"/wireless/guest_network/interfaces/config/{config_id}")

    def get_wireless_interfaces_config(self) -> dict[str, Any]:
        """Returns wireless interface configurations."""
        return self._client.request("GET", "/wireless/interfaces/config")

    def create_wireless_interfaces_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates wireless interface configuration."""
        return self._client.request("POST", "/wireless/interfaces/config", json={"data": config})

    def update_wireless_interfaces_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates wireless interface configurations."""
        return self._client.request("PUT", "/wireless/interfaces/config", json={"data": config})

    def delete_wireless_interfaces_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes wireless interface configurations."""
        return self._client.request("DELETE", "/wireless/interfaces/config", json={"data": config})

    def get_wireless_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Returns wireless interface configuration."""
        return self._client.request("GET", f"/wireless/interfaces/config/{interface_id}")

    def upload_wireless_interfaces_config_by_id(
        self, interface_id: str, file: File, *, option: str | None = None
    ) -> dict[str, Any]:
        """Uploads certificate file."""
        return self._client.request(
            "POST", f"/wireless/interfaces/config/{interface_id}", files={"file": file}, form={"option": option}
        )

    def update_wireless_interfaces_config_by_id(self, interface_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates wireless interface configuration."""
        return self._client.request("PUT", f"/wireless/interfaces/config/{interface_id}", json={"data": config})

    def delete_wireless_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Deletes wireless interface configuration."""
        return self._client.request("DELETE", f"/wireless/interfaces/config/{interface_id}")

    def get_wireless_interfaces_status(self) -> dict[str, Any]:
        """Returns wireless interfaces status."""
        return self._client.request("GET", "/wireless/interfaces/status")

    def get_wireless_interfaces_status_by_id(self, interface_id: str) -> dict[str, Any]:
        """Returns wireless interface status."""
        return self._client.request("GET", f"/wireless/interfaces/status/{interface_id}")

    def get_wireless_multi_ap_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns wireless Multi AP configurations."""
        return self._client.request("GET", "/wireless/multi_ap/config", params={"all_options": all_options})

    def upload_wireless_multi_ap_config(self, file: File) -> dict[str, Any]:
        """Creates wireless Multi AP configuration."""
        return self._client.request("POST", "/wireless/multi_ap/config", files={"file": file})

    def update_wireless_multi_ap_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates wireless Multi AP configurations."""
        return self._client.request("PUT", "/wireless/multi_ap/config", json={"data": config})

    def delete_wireless_multi_ap_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes wireless Multi AP configurations."""
        return self._client.request("DELETE", "/wireless/multi_ap/config", json={"data": config})

    def get_wireless_multi_ap_config_by_id(self, ap_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns wireless Multi AP configuration."""
        return self._client.request("GET", f"/wireless/multi_ap/config/{ap_id}", params={"all_options": all_options})

    def update_wireless_multi_ap_config_by_id(self, ap_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates wireless Multi AP configuration."""
        return self._client.request("PUT", f"/wireless/multi_ap/config/{ap_id}", json={"data": config})

    def delete_wireless_multi_ap_config_by_id(self, ap_id: str) -> dict[str, Any]:
        """Deletes wireless Multi AP configuration."""
        return self._client.request("DELETE", f"/wireless/multi_ap/config/{ap_id}")

    def get_wireless_ppsk_groups_config(self) -> dict[str, Any]:
        """Returns all wireless groups."""
        return self._client.request("GET", "/wireless/ppsk/groups/config")

    def create_wireless_ppsk_groups_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a wireless group configuration."""
        return self._client.request("POST", "/wireless/ppsk/groups/config", json={"data": config})

    def update_wireless_ppsk_groups_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates wireless groups."""
        return self._client.request("PUT", "/wireless/ppsk/groups/config", json={"data": config})

    def delete_wireless_ppsk_groups_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes wireless group configurations."""
        return self._client.request("DELETE", "/wireless/ppsk/groups/config", json={"data": config})

    def get_wireless_ppsk_groups_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Return wireless group configuration."""
        return self._client.request("GET", f"/wireless/ppsk/groups/config/{config_id}")

    def update_wireless_ppsk_groups_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates wireless group configuration."""
        return self._client.request("PUT", f"/wireless/ppsk/groups/config/{config_id}", json={"data": config})

    def delete_wireless_ppsk_groups_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes wireless group configuration."""
        return self._client.request("DELETE", f"/wireless/ppsk/groups/config/{config_id}")

    def get_wireless_stations_config(self) -> dict[str, Any]:
        """Returns all wireless stations."""
        return self._client.request("GET", "/wireless/stations/config")

    def create_wireless_stations_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a wireless station configuration."""
        return self._client.request("POST", "/wireless/stations/config", json={"data": config})

    def update_wireless_stations_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates wireless stations."""
        return self._client.request("PUT", "/wireless/stations/config", json={"data": config})

    def delete_wireless_stations_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes wireless station configurations."""
        return self._client.request("DELETE", "/wireless/stations/config", json={"data": config})

    def get_wireless_stations_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Return wireless station configuration."""
        return self._client.request("GET", f"/wireless/stations/config/{config_id}")

    def upload_wireless_stations_config_by_id(self, config_id: str, file: File) -> dict[str, Any]:
        """Uploads PPSK users file for the group."""
        return self._client.request("POST", f"/wireless/stations/config/{config_id}", files={"file": file})

    def update_wireless_stations_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates wireless station configuration."""
        return self._client.request("PUT", f"/wireless/stations/config/{config_id}", json={"data": config})

    def delete_wireless_stations_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes wireless station configuration."""
        return self._client.request("DELETE", f"/wireless/stations/config/{config_id}")

    def get_wireless_vlans_config(self) -> dict[str, Any]:
        """Returns all wireless VLANs."""
        return self._client.request("GET", "/wireless/vlans/config")

    def create_wireless_vlans_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a wireless VLAN configuration."""
        return self._client.request("POST", "/wireless/vlans/config", json={"data": config})

    def update_wireless_vlans_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates wireless VLANs."""
        return self._client.request("PUT", "/wireless/vlans/config", json={"data": config})

    def delete_wireless_vlans_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes wireless VLAN configurations."""
        return self._client.request("DELETE", "/wireless/vlans/config", json={"data": config})

    def get_wireless_vlans_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Return wireless VLAN configuration."""
        return self._client.request("GET", f"/wireless/vlans/config/{config_id}")

    def update_wireless_vlans_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates wireless VLAN configuration."""
        return self._client.request("PUT", f"/wireless/vlans/config/{config_id}", json={"data": config})

    def delete_wireless_vlans_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes wireless VLAN configuration."""
        return self._client.request("DELETE", f"/wireless/vlans/config/{config_id}")
