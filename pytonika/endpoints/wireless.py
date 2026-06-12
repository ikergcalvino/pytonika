from typing import Any

from ._base import Endpoint


class Wireless(Endpoint):
    def get_wireless_multi_ap_config(self) -> dict[str, Any]:
        """Returns wireless Multi AP configurations."""
        endpoint = "/wireless/multi_ap/config"

        return self._api_client.get(endpoint)

    def create_wireless_multi_ap_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates wireless Multi AP configuration."""
        endpoint = "/wireless/multi_ap/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_wireless_multi_ap_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates wireless Multi AP configurations."""
        endpoint = "/wireless/multi_ap/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_wireless_multi_ap_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes wireless Multi AP configurations."""
        return [self.delete_wireless_multi_ap_config_by_id(ap_id) for ap_id in config]

    def get_wireless_multi_ap_config_by_id(self, ap_id: str) -> dict[str, Any]:
        """Returns wireless Multi AP configuration."""
        endpoint = f"/wireless/multi_ap/config/{ap_id}"

        return self._api_client.get(endpoint)

    def update_wireless_multi_ap_config_by_id(self, ap_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates wireless Multi AP configuration."""
        endpoint = f"/wireless/multi_ap/config/{ap_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_wireless_multi_ap_config_by_id(self, ap_id: str) -> dict[str, Any]:
        """Deletes wireless Multi AP configuration."""
        endpoint = f"/wireless/multi_ap/config/{ap_id}"

        return self._api_client.delete(endpoint)

    def get_wireless_devices_config(self) -> dict[str, Any]:
        """Returns wireless device configurations."""
        endpoint = "/wireless/devices/config"

        return self._api_client.get(endpoint)

    def update_wireless_devices_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates wireless device configurations."""
        endpoint = "/wireless/devices/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_wireless_devices_config_by_id(self, device_id: str) -> dict[str, Any]:
        """Returns wireless device configuration."""
        endpoint = f"/wireless/devices/config/{device_id}"

        return self._api_client.get(endpoint)

    def update_wireless_devices_config_by_id(self, device_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates wireless device configuration."""
        endpoint = f"/wireless/devices/config/{device_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_wireless_devices_global(self) -> dict[str, Any]:
        """Returns wireless device global configuration."""
        endpoint = "/wireless/devices/global"

        return self._api_client.get(endpoint)

    def update_wireless_devices_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates wireless device global configuration."""
        endpoint = "/wireless/devices/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_wireless_devices_status(self) -> dict[str, Any]:
        """Returns wireless device statuses."""
        endpoint = "/wireless/devices/status"

        return self._api_client.get(endpoint)

    def get_wireless_devices_status_by_id(self, device_id: str) -> dict[str, Any]:
        """Returns wireless device status."""
        endpoint = f"/wireless/devices/status/{device_id}"

        return self._api_client.get(endpoint)

    def get_wireless_devices_options(self) -> dict[str, Any]:
        """Returns wireless device options."""
        endpoint = "/wireless/devices/options"

        return self._api_client.get(endpoint)

    def get_wireless_devices_options_by_id(self, device_id: str) -> dict[str, Any]:
        """Returns wireless device options."""
        endpoint = f"/wireless/devices/options/{device_id}"

        return self._api_client.get(endpoint)

    def wireless_actions_join(self, data: dict[str, Any]) -> dict[str, Any]:
        """Joins the specified Wi-Fi network."""
        endpoint = "/wireless/actions/join"

        return self._api_client.post(endpoint, data={"data": data})

    def wireless_actions_scan(self, data: dict[str, Any]) -> dict[str, Any]:
        """Scans the environment for nearby Wi-Fi networks."""
        endpoint = "/wireless/actions/scan"

        return self._api_client.post(endpoint, data={"data": data})

    def wireless_actions_reconnect(self, data: dict[str, Any]) -> dict[str, Any]:
        """Sends a signal to try to reconnect to wireless AP."""
        endpoint = "/wireless/actions/reconnect"

        return self._api_client.post(endpoint, data={"data": data})

    def wireless_actions_disconnect(self, data: dict[str, Any]) -> dict[str, Any]:
        """Sends a signal to disconnect from wireless AP."""
        endpoint = "/wireless/actions/disconnect"

        return self._api_client.post(endpoint, data={"data": data})

    def get_wireless_interfaces_config(self) -> dict[str, Any]:
        """Returns wireless interface configurations."""
        endpoint = "/wireless/interfaces/config"

        return self._api_client.get(endpoint)

    def create_wireless_interfaces_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates wireless interface configuration."""
        endpoint = "/wireless/interfaces/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_wireless_interfaces_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates wireless interface configurations."""
        endpoint = "/wireless/interfaces/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_wireless_interfaces_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes wireless interface configurations."""
        return [self.delete_wireless_interfaces_config_by_id(interface_id) for interface_id in config]

    def get_wireless_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Returns wireless interface configuration."""
        endpoint = f"/wireless/interfaces/config/{interface_id}"

        return self._api_client.get(endpoint)

    def upload_wireless_interfaces_config_by_id(self, interface_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads certificate file."""
        endpoint = f"/wireless/interfaces/config/{interface_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_wireless_interfaces_config_by_id(self, interface_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates wireless interface configuration."""
        endpoint = f"/wireless/interfaces/config/{interface_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_wireless_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Deletes wireless interface configuration."""
        endpoint = f"/wireless/interfaces/config/{interface_id}"

        return self._api_client.delete(endpoint)

    def get_wireless_interfaces_status(self) -> dict[str, Any]:
        """Returns wireless interfaces status."""
        endpoint = "/wireless/interfaces/status"

        return self._api_client.get(endpoint)

    def get_wireless_interfaces_status_by_id(self, interface_id: str) -> dict[str, Any]:
        """Returns wireless interface status."""
        endpoint = f"/wireless/interfaces/status/{interface_id}"

        return self._api_client.get(endpoint)
