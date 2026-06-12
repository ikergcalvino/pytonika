from typing import Any

from ._base import Endpoint


class OSPF(Endpoint):
    def get_ospf_neighbor_config(self) -> dict[str, Any]:
        """Returns all OSPF neighbor configurations."""
        endpoint = "/ospf/neighbor/config"

        return self._api_client.get(endpoint)

    def create_ospf_neighbor_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates OSPF neighbor configuration."""
        endpoint = "/ospf/neighbor/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_ospf_neighbor_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OSPF neighbor configurations."""
        endpoint = "/ospf/neighbor/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ospf_neighbor_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified OSPF neighbor configurations."""
        return [self.delete_ospf_neighbor_config_by_id(neighbor_id) for neighbor_id in config]

    def get_ospf_neighbor_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified OSPF neighbor configuration."""
        endpoint = f"/ospf/neighbor/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_ospf_neighbor_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified OSPF neighbor configuration."""
        endpoint = f"/ospf/neighbor/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ospf_neighbor_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified OSPF neighbor configuration."""
        endpoint = f"/ospf/neighbor/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_ospf_interface_config(self) -> dict[str, Any]:
        """Returns all OSPF interface configurations."""
        endpoint = "/ospf/interface/config"

        return self._api_client.get(endpoint)

    def create_ospf_interface_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates OSPF interface configuration."""
        endpoint = "/ospf/interface/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_ospf_interface_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OSPF interface configurations."""
        endpoint = "/ospf/interface/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ospf_interface_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified OSPF interface configurations."""
        return [self.delete_ospf_interface_config_by_id(iface_id) for iface_id in config]

    def get_ospf_interface_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified OSPF interface configuration."""
        endpoint = f"/ospf/interface/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_ospf_interface_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified OSPF interface configuration."""
        endpoint = f"/ospf/interface/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ospf_interface_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified OSPF interface configuration."""
        endpoint = f"/ospf/interface/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_ospf_interface_options(self) -> dict[str, Any]:
        """Your GET endpoint."""
        endpoint = "/ospf/interface/options"

        return self._api_client.get(endpoint)

    def get_ospf_global(self) -> dict[str, Any]:
        """Returns ospf global configuration."""
        endpoint = "/ospf/global"

        return self._api_client.get(endpoint)

    def upload_ospf_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Uploads custom OSPF configuration file."""
        endpoint = "/ospf/global"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_ospf_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates OSPF global configuration."""
        endpoint = "/ospf/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_ospf_status(self) -> dict[str, Any]:
        """Fetches data about OSPF neighbors."""
        endpoint = "/ospf/status"

        return self._api_client.get(endpoint)

    def get_ospf_area_config(self) -> dict[str, Any]:
        """Returns all OSPF area configurations."""
        endpoint = "/ospf/area/config"

        return self._api_client.get(endpoint)

    def create_ospf_area_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates OSPF area configuration."""
        endpoint = "/ospf/area/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_ospf_area_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OSPF area configurations."""
        endpoint = "/ospf/area/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ospf_area_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified OSPF area configurations."""
        return [self.delete_ospf_area_config_by_id(area_id) for area_id in config]

    def get_ospf_area_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified OSPF area configuration."""
        endpoint = f"/ospf/area/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_ospf_area_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified ospf area configuration."""
        endpoint = f"/ospf/area/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ospf_area_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified OSPF area configuration."""
        endpoint = f"/ospf/area/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_ospf_network_config(self) -> dict[str, Any]:
        """Returns all OSPF network configurations."""
        endpoint = "/ospf/network/config"

        return self._api_client.get(endpoint)

    def create_ospf_network_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates OSPF network configuration."""
        endpoint = "/ospf/network/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_ospf_network_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OSPF network configurations."""
        endpoint = "/ospf/network/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ospf_network_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified OSPF network configurations."""
        return [self.delete_ospf_network_config_by_id(net_id) for net_id in config]

    def get_ospf_network_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified OSPF network configuration."""
        endpoint = f"/ospf/network/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_ospf_network_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified OSPF network configuration."""
        endpoint = f"/ospf/network/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ospf_network_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified OSPF network configuration."""
        endpoint = f"/ospf/network/config/{config_id}"

        return self._api_client.delete(endpoint)
