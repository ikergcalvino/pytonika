from typing import Any

from ._base import Endpoint


class WireGuard(Endpoint):
    def get_wireguard_config(self) -> dict[str, Any]:
        """Returns all Wireguard configurations."""
        endpoint = "/wireguard/config"

        return self._api_client.get(endpoint)

    def create_wireguard_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a Wireguard configuration."""
        endpoint = "/wireguard/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_wireguard_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified wireguard configurations."""
        endpoint = "/wireguard/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_wireguard_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified wireguard configurations."""
        return [self.delete_wireguard_config_by_id(wireguard_id) for wireguard_id in config]

    def get_wireguard_config_by_id(self, wireguard_id: str) -> dict[str, Any]:
        """Returns the specified Wireguard configuration."""
        endpoint = f"/wireguard/config/{wireguard_id}"

        return self._api_client.get(endpoint)

    def update_wireguard_config_by_id(self, wireguard_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Wireguard configuration."""
        endpoint = f"/wireguard/config/{wireguard_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_wireguard_config_by_id(self, wireguard_id: str) -> dict[str, Any]:
        """Deletes the specified Wireguard configuration."""
        endpoint = f"/wireguard/config/{wireguard_id}"

        return self._api_client.delete(endpoint)

    def wireguard_actions_generate_keys(self) -> dict[str, Any]:
        """Generates Private and Public keys."""
        endpoint = "/wireguard/actions/generate_keys"

        return self._api_client.post(endpoint)

    def get_wireguard_peers_config(self, wireguard_id: str) -> dict[str, Any]:
        """Returns all wireguard peer configuration sections."""
        endpoint = f"/wireguard/{wireguard_id}/peers/config"

        return self._api_client.get(endpoint)

    def create_wireguard_peers_config(self, wireguard_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates wireguard peer section."""
        endpoint = f"/wireguard/{wireguard_id}/peers/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_wireguard_peers_config(self, wireguard_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified wireguard peer configurations."""
        endpoint = f"/wireguard/{wireguard_id}/peers/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_wireguard_peers_config(self, wireguard_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified wireguard peer configurations."""
        return [self.delete_wireguard_peer_config_by_id(wireguard_id, peer_id) for peer_id in config]

    def get_wireguard_peer_config_by_id(self, wireguard_id: str, peer_id: str) -> dict[str, Any]:
        """Returns specified wireguard peer section."""
        endpoint = f"/wireguard/{wireguard_id}/peers/config/{peer_id}"

        return self._api_client.get(endpoint)

    def update_wireguard_peer_config_by_id(
        self, wireguard_id: str, peer_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified wireguard peer configuration."""
        endpoint = f"/wireguard/{wireguard_id}/peers/config/{peer_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_wireguard_peer_config_by_id(self, wireguard_id: str, peer_id: str) -> dict[str, Any]:
        """Deletes specified wireguard peer configuration."""
        endpoint = f"/wireguard/{wireguard_id}/peers/config/{peer_id}"

        return self._api_client.delete(endpoint)
