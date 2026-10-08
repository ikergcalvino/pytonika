from typing import Any, Literal

from ._endpoint import Endpoint, File


class OSPF(Endpoint):
    def get_ospf_area_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all OSPF area configurations."""
        return self._client.request("GET", "/ospf/area/config", params={"all_options": all_options})

    def create_ospf_area_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Creates OSPF area configuration."""
        return self._client.request("POST", "/ospf/area/config", json={"data": config})

    def update_ospf_area_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OSPF area configurations."""
        return self._client.request("PUT", "/ospf/area/config", json={"data": config})

    def delete_ospf_area_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified OSPF area configurations."""
        return self._client.request("DELETE", "/ospf/area/config", json={"data": config})

    def get_ospf_area_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified OSPF area configuration."""
        return self._client.request("GET", f"/ospf/area/config/{config_id}", params={"all_options": all_options})

    def update_ospf_area_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified ospf area configuration."""
        return self._client.request("PUT", f"/ospf/area/config/{config_id}", json={"data": config})

    def delete_ospf_area_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified OSPF area configuration."""
        return self._client.request("DELETE", f"/ospf/area/config/{config_id}")

    def get_ospf_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns ospf global configuration."""
        return self._client.request("GET", "/ospf/global", params={"all_options": all_options})

    def upload_ospf_global(self, file: File, *, option: Literal["ospfd_custom_conf"] | None = None) -> dict[str, Any]:
        """Uploads custom OSPF configuration file."""
        return self._client.request("POST", "/ospf/global", files={"file": file}, form={"option": option})

    def update_ospf_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates OSPF global configuration."""
        return self._client.request("PUT", "/ospf/global", json={"data": config})

    def get_ospf_interface_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all OSPF interface configurations."""
        return self._client.request("GET", "/ospf/interface/config", params={"all_options": all_options})

    def create_ospf_interface_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Creates OSPF interface configuration."""
        return self._client.request("POST", "/ospf/interface/config", json={"data": config})

    def update_ospf_interface_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OSPF interface configurations."""
        return self._client.request("PUT", "/ospf/interface/config", json={"data": config})

    def delete_ospf_interface_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified OSPF interface configurations."""
        return self._client.request("DELETE", "/ospf/interface/config", json={"data": config})

    def get_ospf_interface_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified OSPF interface configuration."""
        return self._client.request("GET", f"/ospf/interface/config/{config_id}", params={"all_options": all_options})

    def update_ospf_interface_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified OSPF interface configuration."""
        return self._client.request("PUT", f"/ospf/interface/config/{config_id}", json={"data": config})

    def delete_ospf_interface_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified OSPF interface configuration."""
        return self._client.request("DELETE", f"/ospf/interface/config/{config_id}")

    def get_ospf_interface_options(self) -> dict[str, Any]:
        """Your GET endpoint."""
        return self._client.request("GET", "/ospf/interface/options")

    def get_ospf_neighbor_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all OSPF neighbor configurations."""
        return self._client.request("GET", "/ospf/neighbor/config", params={"all_options": all_options})

    def create_ospf_neighbor_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Creates OSPF neighbor configuration."""
        return self._client.request("POST", "/ospf/neighbor/config", json={"data": config})

    def update_ospf_neighbor_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OSPF neighbor configurations."""
        return self._client.request("PUT", "/ospf/neighbor/config", json={"data": config})

    def delete_ospf_neighbor_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified OSPF neighbor configurations."""
        return self._client.request("DELETE", "/ospf/neighbor/config", json={"data": config})

    def get_ospf_neighbor_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified OSPF neighbor configuration."""
        return self._client.request("GET", f"/ospf/neighbor/config/{config_id}", params={"all_options": all_options})

    def update_ospf_neighbor_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified OSPF neighbor configuration."""
        return self._client.request("PUT", f"/ospf/neighbor/config/{config_id}", json={"data": config})

    def delete_ospf_neighbor_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified OSPF neighbor configuration."""
        return self._client.request("DELETE", f"/ospf/neighbor/config/{config_id}")

    def get_ospf_network_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all OSPF network configurations."""
        return self._client.request("GET", "/ospf/network/config", params={"all_options": all_options})

    def create_ospf_network_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Creates OSPF network configuration."""
        return self._client.request("POST", "/ospf/network/config", json={"data": config})

    def update_ospf_network_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OSPF network configurations."""
        return self._client.request("PUT", "/ospf/network/config", json={"data": config})

    def delete_ospf_network_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified OSPF network configurations."""
        return self._client.request("DELETE", "/ospf/network/config", json={"data": config})

    def get_ospf_network_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified OSPF network configuration."""
        return self._client.request("GET", f"/ospf/network/config/{config_id}", params={"all_options": all_options})

    def update_ospf_network_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified OSPF network configuration."""
        return self._client.request("PUT", f"/ospf/network/config/{config_id}", json={"data": config})

    def delete_ospf_network_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified OSPF network configuration."""
        return self._client.request("DELETE", f"/ospf/network/config/{config_id}")

    def get_ospf_status(self) -> dict[str, Any]:
        """Fetches data about OSPF neighbors."""
        return self._client.request("GET", "/ospf/status")
