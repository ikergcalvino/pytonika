from typing import Any

from ._base import Endpoint


class DMVPN(Endpoint):
    def get_dmvpn_config(self) -> dict[str, Any]:
        """Returns all DMVPN instances."""
        endpoint = "/dmvpn/config"

        return self._api_client.get(endpoint)

    def create_dmvpn_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates DMVPN configuration."""
        endpoint = "/dmvpn/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_dmvpn_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified DMVPN configurations."""
        endpoint = "/dmvpn/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dmvpn_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified DMVPN configurations."""
        return [self.delete_dmvpn_config_by_id(dmvpn_id) for dmvpn_id in config]

    def get_dmvpn_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified DMVPN configuration."""
        endpoint = f"/dmvpn/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_dmvpn_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified DMVPN configuration."""
        endpoint = f"/dmvpn/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dmvpn_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified DMVPN configuration."""
        endpoint = f"/dmvpn/config/{config_id}"

        return self._api_client.delete(endpoint)
