from typing import Any

from ._endpoint import Endpoint


class BFD(Endpoint):
    def get_bfd_peers_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns BFD peer configurations."""
        return self._client.request("GET", "/bfd/peers/config", params={"all_options": all_options})

    def create_bfd_peers_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BFD peer configuration."""
        return self._client.request("POST", "/bfd/peers/config", json={"data": config})

    def update_bfd_peers_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates BFD peer configurations."""
        return self._client.request("PUT", "/bfd/peers/config", json={"data": config})

    def delete_bfd_peers_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes BFD peer configurations."""
        return self._client.request("DELETE", "/bfd/peers/config", json={"data": config})

    def get_bfd_peers_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns BFD peer configuration."""
        return self._client.request("GET", f"/bfd/peers/config/{config_id}", params={"all_options": all_options})

    def update_bfd_peers_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates BFD peer configuration."""
        return self._client.request("PUT", f"/bfd/peers/config/{config_id}", json=config)

    def delete_bfd_peers_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes BFD peer configuration."""
        return self._client.request("DELETE", f"/bfd/peers/config/{config_id}")

    def get_bfd_peers_status(self) -> dict[str, Any]:
        """Returns BFD peers status."""
        return self._client.request("GET", "/bfd/peers/status")

    def get_bfd_profiles_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns BFD profile configurations."""
        return self._client.request("GET", "/bfd/profiles/config", params={"all_options": all_options})

    def create_bfd_profiles_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates BFD profile configuration."""
        return self._client.request("POST", "/bfd/profiles/config", json={"data": config})

    def update_bfd_profiles_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates BFD profile configurations."""
        return self._client.request("PUT", "/bfd/profiles/config", json={"data": config})

    def delete_bfd_profiles_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes BFD profile configurations."""
        return self._client.request("DELETE", "/bfd/profiles/config", json={"data": config})

    def get_bfd_profiles_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns BFD profile configuration."""
        return self._client.request("GET", f"/bfd/profiles/config/{config_id}", params={"all_options": all_options})

    def update_bfd_profiles_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates BFD profile configuration."""
        return self._client.request("PUT", f"/bfd/profiles/config/{config_id}", json=config)

    def delete_bfd_profiles_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes BFD profile configuration."""
        return self._client.request("DELETE", f"/bfd/profiles/config/{config_id}")
