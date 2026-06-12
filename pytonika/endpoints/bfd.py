from typing import Any

from ._base import Endpoint


class BFD(Endpoint):
    def get_bfd_peers_config(self) -> dict[str, Any]:
        """Returns BFD peer configurations."""
        endpoint = "/bfd/peers/config"

        return self._api_client.get(endpoint)

    def create_bfd_peers_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BFD peer configuration."""
        endpoint = "/bfd/peers/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_bfd_peers_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates BFD peer configurations."""
        endpoint = "/bfd/peers/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bfd_peers_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes BFD peer configurations."""
        return [self.delete_bfd_peers_config_by_id(peer_id) for peer_id in config]

    def get_bfd_peers_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns BFD peer configuration."""
        endpoint = f"/bfd/peers/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_bfd_peers_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates BFD peer configuration."""
        endpoint = f"/bfd/peers/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bfd_peers_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes BFD peer configuration."""
        endpoint = f"/bfd/peers/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_bfd_peers_status(self) -> dict[str, Any]:
        """Returns BFD peers status."""
        endpoint = "/bfd/peers/status"

        return self._api_client.get(endpoint)

    def get_bfd_profiles_config(self) -> dict[str, Any]:
        """Returns BFD profile configurations."""
        endpoint = "/bfd/profiles/config"

        return self._api_client.get(endpoint)

    def create_bfd_profiles_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BFD profile configuration."""
        endpoint = "/bfd/profiles/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_bfd_profiles_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates BFD profile configurations."""
        endpoint = "/bfd/profiles/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bfd_profiles_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes BFD profile configurations."""
        return [self.delete_bfd_profiles_config_by_id(profile_id) for profile_id in config]

    def get_bfd_profiles_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns BFD profile configuration."""
        endpoint = f"/bfd/profiles/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_bfd_profiles_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates BFD profile configuration."""
        endpoint = f"/bfd/profiles/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_bfd_profiles_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes BFD profile configuration."""
        endpoint = f"/bfd/profiles/config/{config_id}"

        return self._api_client.delete(endpoint)
