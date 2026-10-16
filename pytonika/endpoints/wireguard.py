from typing import Any

from ._endpoint import Endpoint


class WireGuard(Endpoint):
    def wireguard_actions_generate_keys(self) -> dict[str, Any]:
        """Generates Private and Public keys."""
        return self._client.request("POST", "/wireguard/actions/generate_keys")

    def get_wireguard_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Wireguard configurations."""
        return self._client.request("GET", "/wireguard/config", params={"all_options": all_options})

    def create_wireguard_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a Wireguard configuration."""
        return self._client.request("POST", "/wireguard/config", json={"data": config})

    def update_wireguard_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified wireguard configurations."""
        return self._client.request("PUT", "/wireguard/config", json={"data": config})

    def delete_wireguard_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified wireguard configurations."""
        return self._client.request("DELETE", "/wireguard/config", json={"data": config})

    def get_wireguard_config_by_id(self, wireguard_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Wireguard configuration."""
        return self._client.request("GET", f"/wireguard/config/{wireguard_id}", params={"all_options": all_options})

    def update_wireguard_config_by_id(self, wireguard_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Wireguard configuration."""
        return self._client.request("PUT", f"/wireguard/config/{wireguard_id}", json={"data": config})

    def delete_wireguard_config_by_id(self, wireguard_id: str) -> dict[str, Any]:
        """Deletes the specified Wireguard configuration."""
        return self._client.request("DELETE", f"/wireguard/config/{wireguard_id}")

    def get_wireguard_peers_config(self, wireguard_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all wireguard peer configuration sections."""
        return self._client.request(
            "GET", f"/wireguard/{wireguard_id}/peers/config", params={"all_options": all_options}
        )

    def create_wireguard_peers_config(self, wireguard_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates wireguard peer section."""
        return self._client.request("POST", f"/wireguard/{wireguard_id}/peers/config", json={"data": config})

    def update_wireguard_peers_config(self, wireguard_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified wireguard peer configurations."""
        return self._client.request("PUT", f"/wireguard/{wireguard_id}/peers/config", json={"data": config})

    def delete_wireguard_peers_config(self, wireguard_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes specified wireguard peer configurations."""
        return self._client.request("DELETE", f"/wireguard/{wireguard_id}/peers/config", json={"data": config})

    def get_wireguard_peers_config_by_id(
        self, wireguard_id: str, peer_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns specified wireguard peer section."""
        return self._client.request(
            "GET", f"/wireguard/{wireguard_id}/peers/config/{peer_id}", params={"all_options": all_options}
        )

    def update_wireguard_peers_config_by_id(
        self, wireguard_id: str, peer_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified wireguard peer configuration."""
        return self._client.request("PUT", f"/wireguard/{wireguard_id}/peers/config/{peer_id}", json={"data": config})

    def delete_wireguard_peers_config_by_id(self, wireguard_id: str, peer_id: str) -> dict[str, Any]:
        """Deletes specified wireguard peer configuration."""
        return self._client.request("DELETE", f"/wireguard/{wireguard_id}/peers/config/{peer_id}")
