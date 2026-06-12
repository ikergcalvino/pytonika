from typing import Any

from ._base import Endpoint


class Bacnet(Endpoint):
    def get_bacnet_bdt_config(self) -> dict[str, Any]:
        """Returns all BACnet BDT configurations."""
        endpoint = "/bacnet/bdt/config"

        return self._api_client.get(endpoint)

    def create_bacnet_bdt_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BACnet BDT configuration."""
        endpoint = "/bacnet/bdt/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_bacnet_bdt_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified BACnet BDT configurations."""
        endpoint = "/bacnet/bdt/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bacnet_bdt_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified BACnet BDT configurations."""
        return [self.delete_bacnet_bdt_config_by_id(bdt_id) for bdt_id in config]

    def get_bacnet_bdt_config_by_id(self, bdt_id: str) -> dict[str, Any]:
        """Returns the specified BACnet BDT configuration."""
        endpoint = f"/bacnet/bdt/config/{bdt_id}"

        return self._api_client.get(endpoint)

    def update_bacnet_bdt_config_by_id(self, bdt_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified BACnet BDT configuration."""
        endpoint = f"/bacnet/bdt/config/{bdt_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bacnet_bdt_config_by_id(self, bdt_id: str) -> dict[str, Any]:
        """Deletes the specified BACnet BDT configuration."""
        endpoint = f"/bacnet/bdt/config/{bdt_id}"

        return self._api_client.delete(endpoint)

    def get_bacnet_config(self) -> dict[str, Any]:
        """Returns all BACnet configurations."""
        endpoint = "/bacnet/config"

        return self._api_client.get(endpoint)

    def update_bacnet_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified BACnet configurations."""
        endpoint = "/bacnet/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_bacnet_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified BACnet configuration."""
        endpoint = f"/bacnet/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_bacnet_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified BACnet configuration."""
        endpoint = f"/bacnet/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_bacnet_bip_config(self) -> dict[str, Any]:
        """Returns all BACnet Over Internet Protocol configurations."""
        endpoint = "/bacnet/bip/config"

        return self._api_client.get(endpoint)

    def create_bacnet_bip_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BACnet Over Internet Protocol configurations."""
        endpoint = "/bacnet/bip/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_bacnet_bip_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified BACnet Over Internet Protocol configurations."""
        endpoint = "/bacnet/bip/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bacnet_bip_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes BACnet configurations."""
        return [self.delete_bacnet_bip_config_by_id(bip_id) for bip_id in config]

    def get_bacnet_bip_config_by_id(self, bip_id: str) -> dict[str, Any]:
        """Returns the specified BACnet Over Internet Protocol configurations."""
        endpoint = f"/bacnet/bip/config/{bip_id}"

        return self._api_client.get(endpoint)

    def update_bacnet_bip_config_by_id(self, bip_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified BACnet Over Internet Protocol configuration."""
        endpoint = f"/bacnet/bip/config/{bip_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bacnet_bip_config_by_id(self, bip_id: str) -> dict[str, Any]:
        """Deletes the specified BACnet configuration."""
        endpoint = f"/bacnet/bip/config/{bip_id}"

        return self._api_client.delete(endpoint)

    def get_bacnet_mstp_config(self) -> dict[str, Any]:
        """Returns all BACnet Server/Client token passing configurations."""
        endpoint = "/bacnet/mstp/config"

        return self._api_client.get(endpoint)

    def create_bacnet_mstp_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BACnet Server/Client token passing instance."""
        endpoint = "/bacnet/mstp/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_bacnet_mstp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified BACnet Server/Client token passing configurations."""
        endpoint = "/bacnet/mstp/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bacnet_mstp_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes BACnet Server/Client token passing configurations."""
        return [self.delete_bacnet_mstp_config_by_id(mstp_id) for mstp_id in config]

    def get_bacnet_mstp_config_by_id(self, mstp_id: str) -> dict[str, Any]:
        """Returns the specified BACnet Server/Client token passing configuration."""
        endpoint = f"/bacnet/mstp/config/{mstp_id}"

        return self._api_client.get(endpoint)

    def update_bacnet_mstp_config_by_id(self, mstp_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified BACnet Server/Client token passing configuration."""
        endpoint = f"/bacnet/mstp/config/{mstp_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bacnet_mstp_config_by_id(self, mstp_id: str) -> dict[str, Any]:
        """Deletes BACnet Server/Client token passing configuration."""
        endpoint = f"/bacnet/mstp/config/{mstp_id}"

        return self._api_client.delete(endpoint)
