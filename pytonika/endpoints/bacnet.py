from typing import Any

from ._endpoint import Endpoint


class Bacnet(Endpoint):
    def get_bacnet_bdt_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all BACnet BDT configurations."""
        return self._client.request("GET", "/bacnet/bdt/config", params={"all_options": all_options})

    def create_bacnet_bdt_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BACnet BDT configuration."""
        return self._client.request("POST", "/bacnet/bdt/config", json={"data": config})

    def update_bacnet_bdt_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified BACnet BDT configurations."""
        return self._client.request("PUT", "/bacnet/bdt/config", json={"data": config})

    def delete_bacnet_bdt_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified BACnet BDT configurations."""
        return self._client.request("DELETE", "/bacnet/bdt/config", json={"data": config})

    def get_bacnet_bdt_config_by_id(self, bdt_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified BACnet BDT configuration."""
        return self._client.request("GET", f"/bacnet/bdt/config/{bdt_id}", params={"all_options": all_options})

    def update_bacnet_bdt_config_by_id(self, bdt_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified BACnet BDT configuration."""
        return self._client.request("PUT", f"/bacnet/bdt/config/{bdt_id}", json={"data": config})

    def delete_bacnet_bdt_config_by_id(self, bdt_id: str) -> dict[str, Any]:
        """Deletes the specified BACnet BDT configuration."""
        return self._client.request("DELETE", f"/bacnet/bdt/config/{bdt_id}")

    def get_bacnet_bip_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all BACnet Over Internet Protocol configurations."""
        return self._client.request("GET", "/bacnet/bip/config", params={"all_options": all_options})

    def create_bacnet_bip_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BACnet Over Internet Protocol configurations."""
        return self._client.request("POST", "/bacnet/bip/config", json={"data": config})

    def update_bacnet_bip_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified BACnet Over Internet Protocol configurations."""
        return self._client.request("PUT", "/bacnet/bip/config", json={"data": config})

    def delete_bacnet_bip_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes BACnet configurations."""
        return self._client.request("DELETE", "/bacnet/bip/config", json={"data": config})

    def get_bacnet_bip_config_by_id(self, bip_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified BACnet Over Internet Protocol configurations."""
        return self._client.request("GET", f"/bacnet/bip/config/{bip_id}", params={"all_options": all_options})

    def update_bacnet_bip_config_by_id(self, bip_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified BACnet Over Internet Protocol configuration."""
        return self._client.request("PUT", f"/bacnet/bip/config/{bip_id}", json={"data": config})

    def delete_bacnet_bip_config_by_id(self, bip_id: str) -> dict[str, Any]:
        """Deletes the specified BACnet configuration."""
        return self._client.request("DELETE", f"/bacnet/bip/config/{bip_id}")

    def get_bacnet_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all BACnet configurations."""
        return self._client.request("GET", "/bacnet/config", params={"all_options": all_options})

    def update_bacnet_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified BACnet configurations."""
        return self._client.request("PUT", "/bacnet/config", json={"data": config})

    def get_bacnet_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified BACnet configuration."""
        return self._client.request("GET", f"/bacnet/config/{config_id}", params={"all_options": all_options})

    def update_bacnet_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified BACnet configuration."""
        return self._client.request("PUT", f"/bacnet/config/{config_id}", json={"data": config})

    def get_bacnet_mstp_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all BACnet Server/Client token passing configurations."""
        return self._client.request("GET", "/bacnet/mstp/config", params={"all_options": all_options})

    def create_bacnet_mstp_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BACnet Server/Client token passing instance."""
        return self._client.request("POST", "/bacnet/mstp/config", json={"data": config})

    def update_bacnet_mstp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified BACnet Server/Client token passing configurations."""
        return self._client.request("PUT", "/bacnet/mstp/config", json={"data": config})

    def delete_bacnet_mstp_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes BACnet Server/Client token passing configurations."""
        return self._client.request("DELETE", "/bacnet/mstp/config", json={"data": config})

    def get_bacnet_mstp_config_by_id(self, mstp_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified BACnet Server/Client token passing configuration."""
        return self._client.request("GET", f"/bacnet/mstp/config/{mstp_id}", params={"all_options": all_options})

    def update_bacnet_mstp_config_by_id(self, mstp_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified BACnet Server/Client token passing configuration."""
        return self._client.request("PUT", f"/bacnet/mstp/config/{mstp_id}", json={"data": config})

    def delete_bacnet_mstp_config_by_id(self, mstp_id: str) -> dict[str, Any]:
        """Deletes BACnet Server/Client token passing configuration."""
        return self._client.request("DELETE", f"/bacnet/mstp/config/{mstp_id}")
