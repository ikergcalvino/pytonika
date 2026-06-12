from typing import Any

from ._base import Endpoint


class SSHFS(Endpoint):
    def get_sshfs_config(self) -> dict[str, Any]:
        """Returns SSHFS configurations."""
        endpoint = "/sshfs/config"

        return self._api_client.get(endpoint)

    def update_sshfs_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SSHFS configurations."""
        endpoint = "/sshfs/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_sshfs_config_by_id(self, sshfs_id: str) -> dict[str, Any]:
        """Returns SSHFS configuration."""
        endpoint = f"/sshfs/config/{sshfs_id}"

        return self._api_client.get(endpoint)

    def update_sshfs_config_by_id(self, sshfs_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates SSHFS configuration."""
        endpoint = f"/sshfs/config/{sshfs_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_sshfs_status(self) -> dict[str, Any]:
        """Returns information about SSHFS instances."""
        endpoint = "/sshfs/status"

        return self._api_client.get(endpoint)
