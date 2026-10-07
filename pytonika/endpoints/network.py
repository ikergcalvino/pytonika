from typing import Any

from ._endpoint import Endpoint


class Network(Endpoint):
    def get_network_devices_bridge_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns bridge network device configurations."""
        return self._client.request("GET", "/network/devices/bridge/config", params={"all_options": all_options})

    def create_network_devices_bridge_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates bridge network device configuration."""
        return self._client.request("POST", "/network/devices/bridge/config", json={"data": config})

    def update_network_devices_bridge_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates bridge network device configurations."""
        return self._client.request("PUT", "/network/devices/bridge/config", json={"data": config})

    def delete_network_devices_bridge_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes bridge network device configurations."""
        return self._client.request("DELETE", "/network/devices/bridge/config", json={"data": config})

    def get_network_devices_bridge_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns bridge network device configuration."""
        return self._client.request(
            "GET", f"/network/devices/bridge/config/{config_id}", params={"all_options": all_options}
        )

    def update_network_devices_bridge_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates bridge network device configuration."""
        return self._client.request("PUT", f"/network/devices/bridge/config/{config_id}", json={"data": config})

    def delete_network_devices_bridge_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes bridge network device configuration."""
        return self._client.request("DELETE", f"/network/devices/bridge/config/{config_id}")

    def get_network_devices_bridge_status(self) -> dict[str, Any]:
        """Returns bridge network devices status."""
        return self._client.request("GET", "/network/devices/bridge/status")

    def get_network_devices_bridge_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns specified bridge network device status."""
        return self._client.request("GET", f"/network/devices/bridge/status/{status_id}")

    def get_network_devices_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns network device configurations."""
        return self._client.request("GET", "/network/devices/config", params={"all_options": all_options})

    def get_network_devices_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns network device configuration."""
        return self._client.request("GET", f"/network/devices/config/{config_id}", params={"all_options": all_options})

    def get_network_devices_ethernet_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns ethernet network device configurations."""
        return self._client.request("GET", "/network/devices/ethernet/config", params={"all_options": all_options})

    def create_network_devices_ethernet_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates ethernet network device configuration."""
        return self._client.request("POST", "/network/devices/ethernet/config", json={"data": config})

    def update_network_devices_ethernet_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates ethernet network device configurations."""
        return self._client.request("PUT", "/network/devices/ethernet/config", json={"data": config})

    def delete_network_devices_ethernet_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes ethernet network device configurations."""
        return self._client.request("DELETE", "/network/devices/ethernet/config", json={"data": config})

    def get_network_devices_ethernet_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns ethernet network device configuration."""
        return self._client.request(
            "GET", f"/network/devices/ethernet/config/{config_id}", params={"all_options": all_options}
        )

    def update_network_devices_ethernet_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates ethernet network device configuration."""
        return self._client.request("PUT", f"/network/devices/ethernet/config/{config_id}", json={"data": config})

    def delete_network_devices_ethernet_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes ethernet network device configuration."""
        return self._client.request("DELETE", f"/network/devices/ethernet/config/{config_id}")

    def get_network_devices_ethernet_status(self) -> dict[str, Any]:
        """Returns ethernet network devices status."""
        return self._client.request("GET", "/network/devices/ethernet/status")

    def get_network_devices_ethernet_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns specified ethernet network device status."""
        return self._client.request("GET", f"/network/devices/ethernet/status/{status_id}")

    def get_network_devices_status(self) -> dict[str, Any]:
        """Returns network devices status."""
        return self._client.request("GET", "/network/devices/status")

    def get_network_devices_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns specified network device status."""
        return self._client.request("GET", f"/network/devices/status/{status_id}")

    def get_network_devices_vxlan_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns VXLAN network device configurations."""
        return self._client.request("GET", "/network/devices/vxlan/config", params={"all_options": all_options})

    def create_network_devices_vxlan_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates VXLAN network device configuration."""
        return self._client.request("POST", "/network/devices/vxlan/config", json={"data": config})

    def update_network_devices_vxlan_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates VXLAN network device configurations."""
        return self._client.request("PUT", "/network/devices/vxlan/config", json={"data": config})

    def delete_network_devices_vxlan_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes VXLAN network device configurations."""
        return self._client.request("DELETE", "/network/devices/vxlan/config", json={"data": config})

    def get_network_devices_vxlan_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns VXLAN network device configuration."""
        return self._client.request(
            "GET", f"/network/devices/vxlan/config/{config_id}", params={"all_options": all_options}
        )

    def update_network_devices_vxlan_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates VXLAN network device configuration."""
        return self._client.request("PUT", f"/network/devices/vxlan/config/{config_id}", json={"data": config})

    def delete_network_devices_vxlan_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes VXLAN network device configuration."""
        return self._client.request("DELETE", f"/network/devices/vxlan/config/{config_id}")

    def get_network_devices_vxlan_status(self) -> dict[str, Any]:
        """Returns VXLAN network devices status."""
        return self._client.request("GET", "/network/devices/vxlan/status")

    def get_network_devices_vxlan_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns specified VXLAN network device status."""
        return self._client.request("GET", f"/network/devices/vxlan/status/{status_id}")
