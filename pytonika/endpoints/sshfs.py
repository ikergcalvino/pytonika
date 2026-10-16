from typing import Any

from ._endpoint import Endpoint


class SSHFS(Endpoint):
    def get_sshfs_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns SSHFS configurations."""
        return self._client.request("GET", "/sshfs/config", params={"all_options": all_options})

    def update_sshfs_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SSHFS configurations."""
        return self._client.request("PUT", "/sshfs/config", json={"data": config})

    def get_sshfs_config_by_id(self, sshfs_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns SSHFS configuration."""
        return self._client.request("GET", f"/sshfs/config/{sshfs_id}", params={"all_options": all_options})

    def update_sshfs_config_by_id(self, sshfs_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates SSHFS configuration."""
        return self._client.request("PUT", f"/sshfs/config/{sshfs_id}", json={"data": config})

    def get_sshfs_status(self) -> dict[str, Any]:
        """Returns information about SSHFS instances."""
        return self._client.request("GET", "/sshfs/status")
