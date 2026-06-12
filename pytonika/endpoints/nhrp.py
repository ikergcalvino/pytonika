from typing import Any

from ._base import Endpoint


class NHRP(Endpoint):
    def get_nhrp_global(self) -> dict[str, Any]:
        """Returns NHRP global configuration."""
        endpoint = "/nhrp/global"

        return self._api_client.get(endpoint)

    def update_nhrp_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified NHRP global configuration."""
        endpoint = "/nhrp/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_nhrp_status(self) -> dict[str, Any]:
        """Fetches data about NHRP neighbors."""
        endpoint = "/nhrp/status"

        return self._api_client.get(endpoint)

    def get_nhrp_nhs_config(self, interface_id: str) -> dict[str, Any]:
        """Returns all NHRP NHS configurations."""
        endpoint = f"/nhrp/interface/{interface_id}/nhs/config/"

        return self._api_client.get(endpoint)

    def create_nhrp_nhs_config(self, interface_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates NHRP NHS configuration."""
        endpoint = f"/nhrp/interface/{interface_id}/nhs/config/"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_nhrp_nhs_config(self, interface_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified NHRP NHS configurations."""
        endpoint = f"/nhrp/interface/{interface_id}/nhs/config/"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_nhrp_nhs_config(self, interface_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified NHRP NHS configurations."""
        return [self.delete_nhrp_nhs_config_by_id(interface_id, nhs_id) for nhs_id in config]

    def get_nhrp_nhs_config_by_id(self, interface_id: str, nhs_id: str) -> dict[str, Any]:
        """Returns specified NHRP NHS configuration."""
        endpoint = f"/nhrp/interface/{interface_id}/nhs/config/{nhs_id}"

        return self._api_client.get(endpoint)

    def update_nhrp_nhs_config_by_id(self, interface_id: str, nhs_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified NHRP NHS configuration."""
        endpoint = f"/nhrp/interface/{interface_id}/nhs/config/{nhs_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_nhrp_nhs_config_by_id(self, interface_id: str, nhs_id: str) -> dict[str, Any]:
        """Deletes specified NHRP NHS configuration."""
        endpoint = f"/nhrp/interface/{interface_id}/nhs/config/{nhs_id}"

        return self._api_client.delete(endpoint)

    def get_nhrp_mapping_config(self, interface_id: str) -> dict[str, Any]:
        """Returns all NHRP mapping configurations."""
        endpoint = f"/nhrp/interface/{interface_id}/mapping/config/"

        return self._api_client.get(endpoint)

    def create_nhrp_mapping_config(self, interface_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates NHRP mapping configuration."""
        endpoint = f"/nhrp/interface/{interface_id}/mapping/config/"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_nhrp_mapping_config(self, interface_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified NHRP mapping configurations."""
        endpoint = f"/nhrp/interface/{interface_id}/mapping/config/"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_nhrp_mapping_config(self, interface_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified NHRP mapping configurations."""
        return [self.delete_nhrp_mapping_config_by_id(interface_id, mapping_id) for mapping_id in config]

    def get_nhrp_mapping_config_by_id(self, interface_id: str, mapping_id: str) -> dict[str, Any]:
        """Returns specified NHRP mapping configuration."""
        endpoint = f"/nhrp/interface/{interface_id}/mapping/config/{mapping_id}"

        return self._api_client.get(endpoint)

    def update_nhrp_mapping_config_by_id(
        self, interface_id: str, mapping_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified NHRP mapping configuration."""
        endpoint = f"/nhrp/interface/{interface_id}/mapping/config/{mapping_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_nhrp_mapping_config_by_id(self, interface_id: str, mapping_id: str) -> dict[str, Any]:
        """Deletes specified NHRP mapping configuration."""
        endpoint = f"/nhrp/interface/{interface_id}/mapping/config/{mapping_id}"

        return self._api_client.delete(endpoint)

    def get_nhrp_interface_config(self) -> dict[str, Any]:
        """Returns all NHRP interface configurations."""
        endpoint = "/nhrp/interface/config"

        return self._api_client.get(endpoint)

    def create_nhrp_interface_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates NHRP interface configuration."""
        endpoint = "/nhrp/interface/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_nhrp_interface_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified nhrp interface configurations."""
        endpoint = "/nhrp/interface/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_nhrp_interface_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified nhrp interface configurations."""
        return [self.delete_nhrp_interface_config_by_id(iface_id) for iface_id in config]

    def get_nhrp_interface_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified NHRP interface configuration."""
        endpoint = f"/nhrp/interface/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_nhrp_interface_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified NHRP interface configuration."""
        endpoint = f"/nhrp/interface/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_nhrp_interface_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified NHRP interface configuration."""
        endpoint = f"/nhrp/interface/config/{config_id}"

        return self._api_client.delete(endpoint)
