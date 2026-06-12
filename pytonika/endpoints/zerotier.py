from typing import Any

from ._base import Endpoint


class Zerotier(Endpoint):
    def get_zerotier_networks_config(self, zerotier_id: str) -> dict[str, Any]:
        """Returns all Zerotier Network configurations."""
        endpoint = f"/zerotier/{zerotier_id}/networks/config"

        return self._api_client.get(endpoint)

    def create_zerotier_networks_config(self, zerotier_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Zerotier Network configuration."""
        endpoint = f"/zerotier/{zerotier_id}/networks/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_zerotier_networks_config(self, zerotier_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Zerotier Network configurations."""
        endpoint = f"/zerotier/{zerotier_id}/networks/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_zerotier_networks_config(self, zerotier_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Zerotier network configurations."""
        return [self.delete_zerotier_networks_config_by_id(zerotier_id, network_id) for network_id in config]

    def get_zerotier_networks_config_by_id(self, zerotier_id: str, network_id: str) -> dict[str, Any]:
        """Returns the specified Zerotier Network configuration."""
        endpoint = f"/zerotier/{zerotier_id}/networks/config/{network_id}"

        return self._api_client.get(endpoint)

    def update_zerotier_networks_config_by_id(
        self, zerotier_id: str, network_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified Zerotier Network configuration."""
        endpoint = f"/zerotier/{zerotier_id}/networks/config/{network_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_zerotier_networks_config_by_id(self, zerotier_id: str, network_id: str) -> dict[str, Any]:
        """Deletes the specified Zerotier Network configuration."""
        endpoint = f"/zerotier/{zerotier_id}/networks/config/{network_id}"

        return self._api_client.delete(endpoint)

    def upload_zerotier_planet_file(self, zerotier_id: str, network_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads planet file for the specified Zerotier Network configuration."""
        endpoint = f"/zerotier/{zerotier_id}/networks/config/{network_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def get_zerotier_config(self) -> dict[str, Any]:
        """Returns all Zerotier configurations."""
        endpoint = "/zerotier/config"

        return self._api_client.get(endpoint)

    def create_zerotier_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Zerotier configuration."""
        endpoint = "/zerotier/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_zerotier_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Zerotier configurations."""
        endpoint = "/zerotier/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_zerotier_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Zerotier configurations."""
        return [self.delete_zerotier_config_by_id(zt_id) for zt_id in config]

    def get_zerotier_config_by_id(self, zerotier_id: str) -> dict[str, Any]:
        """Returns the specified Zerotier configuration."""
        endpoint = f"/zerotier/config/{zerotier_id}"

        return self._api_client.get(endpoint)

    def update_zerotier_config_by_id(self, zerotier_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Zerotier configuration."""
        endpoint = f"/zerotier/config/{zerotier_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_zerotier_config_by_id(self, zerotier_id: str) -> dict[str, Any]:
        """Deletes the specified Zerotier configuration."""
        endpoint = f"/zerotier/config/{zerotier_id}"

        return self._api_client.delete(endpoint)
