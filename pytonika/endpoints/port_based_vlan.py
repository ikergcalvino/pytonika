from typing import Any

from ._base import Endpoint


class PortBasedVlan(Endpoint):
    def get_port_based_vlan_config(self) -> dict[str, Any]:
        """Returns Port Based VLANs."""
        endpoint = "/port_based_vlan/config"

        return self._api_client.get(endpoint)

    def create_port_based_vlan_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Port Based VLAN."""
        endpoint = "/port_based_vlan/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_port_based_vlan_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Port Based VLANs."""
        endpoint = "/port_based_vlan/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_port_based_vlan_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes Port Based VLANs."""
        return [self.delete_port_based_vlan_config_by_id(vlan_id) for vlan_id in config]

    def get_port_based_vlan_config_by_id(self, vlan_id: str) -> dict[str, Any]:
        """Returns Port Based VLAN."""
        endpoint = f"/port_based_vlan/config/{vlan_id}"

        return self._api_client.get(endpoint)

    def update_port_based_vlan_config_by_id(self, vlan_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Port Based VLAN."""
        endpoint = f"/port_based_vlan/config/{vlan_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_port_based_vlan_config_by_id(self, vlan_id: str) -> dict[str, Any]:
        """Deletes Port Based VLAN."""
        endpoint = f"/port_based_vlan/config/{vlan_id}"

        return self._api_client.delete(endpoint)
