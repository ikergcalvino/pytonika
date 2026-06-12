from typing import Any

from ._base import Endpoint


class Network(Endpoint):
    def get_network_devices_vxlan_config(self) -> dict[str, Any]:
        """Returns VXLAN network device configurations."""
        endpoint = "/network/devices/vxlan/config"

        return self._api_client.get(endpoint)

    def create_network_devices_vxlan_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates VXLAN network device configuration."""
        endpoint = "/network/devices/vxlan/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_network_devices_vxlan_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates VXLAN network device configurations."""
        endpoint = "/network/devices/vxlan/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_network_devices_vxlan_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes VXLAN network device configurations."""
        return [self.delete_network_devices_vxlan_config_by_id(vxlan_id) for vxlan_id in config]

    def get_network_devices_vxlan_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns VXLAN network device configuration."""
        endpoint = f"/network/devices/vxlan/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_network_devices_vxlan_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates VXLAN network device configuration."""
        endpoint = f"/network/devices/vxlan/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_network_devices_vxlan_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes VXLAN network device configuration."""
        endpoint = f"/network/devices/vxlan/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_network_devices_vxlan_status(self) -> dict[str, Any]:
        """Returns VXLAN network devices status."""
        endpoint = "/network/devices/vxlan/status"

        return self._api_client.get(endpoint)

    def get_network_devices_vxlan_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns specified VXLAN network device status."""
        endpoint = f"/network/devices/vxlan/status/{status_id}"

        return self._api_client.get(endpoint)

    def get_network_devices_config(self) -> dict[str, Any]:
        """Returns network device configurations."""
        endpoint = "/network/devices/config"

        return self._api_client.get(endpoint)

    def get_network_devices_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns network device configuration."""
        endpoint = f"/network/devices/config/{config_id}"

        return self._api_client.get(endpoint)

    def get_network_devices_status(self) -> dict[str, Any]:
        """Returns network devices status."""
        endpoint = "/network/devices/status"

        return self._api_client.get(endpoint)

    def get_network_devices_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns specified network device status."""
        endpoint = f"/network/devices/status/{status_id}"

        return self._api_client.get(endpoint)

    def get_network_devices_bridge_config(self) -> dict[str, Any]:
        """Returns bridge network device configurations."""
        endpoint = "/network/devices/bridge/config"

        return self._api_client.get(endpoint)

    def create_network_devices_bridge_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates bridge network device configuration."""
        endpoint = "/network/devices/bridge/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_network_devices_bridge_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates bridge network device configurations."""
        endpoint = "/network/devices/bridge/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_network_devices_bridge_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes bridge network device configurations."""
        return [self.delete_network_devices_bridge_config_by_id(bridge_id) for bridge_id in config]

    def get_network_devices_bridge_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns bridge network device configuration."""
        endpoint = f"/network/devices/bridge/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_network_devices_bridge_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates bridge network device configuration."""
        endpoint = f"/network/devices/bridge/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_network_devices_bridge_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes bridge network device configuration."""
        endpoint = f"/network/devices/bridge/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_network_devices_bridge_status(self) -> dict[str, Any]:
        """Returns bridge network devices status."""
        endpoint = "/network/devices/bridge/status"

        return self._api_client.get(endpoint)

    def get_network_devices_bridge_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns specified bridge network device status."""
        endpoint = f"/network/devices/bridge/status/{status_id}"

        return self._api_client.get(endpoint)

    def get_network_devices_ethernet_config(self) -> dict[str, Any]:
        """Returns ethernet network device configurations."""
        endpoint = "/network/devices/ethernet/config"

        return self._api_client.get(endpoint)

    def create_network_devices_ethernet_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates ethernet network device configuration."""
        endpoint = "/network/devices/ethernet/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_network_devices_ethernet_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates ethernet network device configurations."""
        endpoint = "/network/devices/ethernet/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_network_devices_ethernet_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes ethernet network device configurations."""
        return [self.delete_network_devices_ethernet_config_by_id(eth_id) for eth_id in config]

    def get_network_devices_ethernet_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns ethernet network device configuration."""
        endpoint = f"/network/devices/ethernet/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_network_devices_ethernet_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates ethernet network device configuration."""
        endpoint = f"/network/devices/ethernet/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_network_devices_ethernet_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes ethernet network device configuration."""
        endpoint = f"/network/devices/ethernet/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_network_devices_ethernet_status(self) -> dict[str, Any]:
        """Returns ethernet network devices status."""
        endpoint = "/network/devices/ethernet/status"

        return self._api_client.get(endpoint)

    def get_network_devices_ethernet_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns specified ethernet network device status."""
        endpoint = f"/network/devices/ethernet/status/{status_id}"

        return self._api_client.get(endpoint)
