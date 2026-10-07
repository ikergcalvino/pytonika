from typing import Any

from ._endpoint import Endpoint


class PortBasedVlan(Endpoint):
    def get_port_based_vlan_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Port Based VLANs."""
        return self._client.request("GET", "/port_based_vlan/config", params={"all_options": all_options})

    def create_port_based_vlan_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Port Based VLAN."""
        return self._client.request("POST", "/port_based_vlan/config", json={"data": config})

    def update_port_based_vlan_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Port Based VLANs."""
        return self._client.request("PUT", "/port_based_vlan/config", json={"data": config})

    def delete_port_based_vlan_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes Port Based VLANs."""
        return self._client.request("DELETE", "/port_based_vlan/config", json={"data": config})

    def get_port_based_vlan_config_by_id(self, vlan_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Port Based VLAN."""
        return self._client.request("GET", f"/port_based_vlan/config/{vlan_id}", params={"all_options": all_options})

    def update_port_based_vlan_config_by_id(self, vlan_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Port Based VLAN."""
        return self._client.request("PUT", f"/port_based_vlan/config/{vlan_id}", json={"data": config})

    def delete_port_based_vlan_config_by_id(self, vlan_id: str) -> dict[str, Any]:
        """Deletes Port Based VLAN."""
        return self._client.request("DELETE", f"/port_based_vlan/config/{vlan_id}")
