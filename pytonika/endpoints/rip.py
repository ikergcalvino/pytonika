from typing import Any

from ._base import Endpoint


class RIP(Endpoint):
    def get_rip_access_config(self) -> dict[str, Any]:
        """Returns all RIP access configurations."""
        endpoint = "/rip/access/config"

        return self._api_client.get(endpoint)

    def create_rip_access_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates RIP access configuration."""
        endpoint = "/rip/access/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_rip_access_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified RIP access configurations."""
        endpoint = "/rip/access/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_rip_access_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified RIP access configurations."""
        return [self.delete_rip_access_config_by_id(access_id) for access_id in config]

    def get_rip_access_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified RIP access configuration."""
        endpoint = f"/rip/access/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_rip_access_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified RIP access configuration."""
        endpoint = f"/rip/access/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_rip_access_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified RIP access configuration."""
        endpoint = f"/rip/access/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_rip_global(self) -> dict[str, Any]:
        """Returns RIP global configuration."""
        endpoint = "/rip/global"

        return self._api_client.get(endpoint)

    def upload_rip_global(self, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads custom RIP configuration file."""
        endpoint = "/rip/global"

        return self._api_client.post(endpoint, data={"data": data})

    def update_rip_global(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified RIP global configuration."""
        endpoint = "/rip/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_rip_status(self) -> dict[str, Any]:
        """Fetches data about RIP neighbors."""
        endpoint = "/rip/status"

        return self._api_client.get(endpoint)

    def get_rip_interface_config(self) -> dict[str, Any]:
        """Returns all RIP interface configurations."""
        endpoint = "/rip/interface/config"

        return self._api_client.get(endpoint)

    def create_rip_interface_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates rip interface configuration."""
        endpoint = "/rip/interface/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_rip_interface_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified RIP interface configurations."""
        endpoint = "/rip/interface/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_rip_interface_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified RIP interface configurations."""
        return [self.delete_rip_interface_config_by_id(iface_id) for iface_id in config]

    def get_rip_interface_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified RIP interface configuration."""
        endpoint = f"/rip/interface/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_rip_interface_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified RIP interface configuration."""
        endpoint = f"/rip/interface/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_rip_interface_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified RIP interface configuration."""
        endpoint = f"/rip/interface/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_rip_interface_options(self) -> dict[str, Any]:
        """Your GET endpoint."""
        endpoint = "/rip/interface/options"

        return self._api_client.get(endpoint)
