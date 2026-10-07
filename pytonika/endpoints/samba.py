from typing import Any

from ._endpoint import Endpoint


class Samba(Endpoint):
    def get_samba_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get SAMBA general configuration."""
        return self._client.request("GET", "/samba/global", params={"all_options": all_options})

    def update_samba_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Update SAMBA general configuration."""
        return self._client.request("PUT", "/samba/global", json={"data": config})

    def get_samba_shares_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get SAMBA share configurations."""
        return self._client.request("GET", "/samba/shares/config", params={"all_options": all_options})

    def create_samba_shares_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create SAMBA share configuration."""
        return self._client.request("POST", "/samba/shares/config", json={"data": config})

    def update_samba_shares_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update SAMBA share configurations."""
        return self._client.request("PUT", "/samba/shares/config", json={"data": config})

    def delete_samba_shares_config(self, config: list[str]) -> dict[str, Any]:
        """Delete SAMBA share configurations."""
        return self._client.request("DELETE", "/samba/shares/config", json={"data": config})

    def get_samba_shares_config_by_id(self, share_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get SAMBA share configuration."""
        return self._client.request("GET", f"/samba/shares/config/{share_id}", params={"all_options": all_options})

    def update_samba_shares_config_by_id(self, share_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update SAMBA share configuration."""
        return self._client.request("PUT", f"/samba/shares/config/{share_id}", json={"data": config})

    def delete_samba_shares_config_by_id(self, share_id: str) -> dict[str, Any]:
        """Delete SAMBA share configuration."""
        return self._client.request("DELETE", f"/samba/shares/config/{share_id}")

    def get_samba_status(self) -> dict[str, Any]:
        """Get SAMBA instance status and all active sessions."""
        return self._client.request("GET", "/samba/status")

    def get_samba_users_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get SAMBA user configurations."""
        return self._client.request("GET", "/samba/users/config", params={"all_options": all_options})

    def create_samba_users_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create SAMBA user configuration."""
        return self._client.request("POST", "/samba/users/config", json={"data": config})

    def update_samba_users_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update SAMBA user configurations."""
        return self._client.request("PUT", "/samba/users/config", json={"data": config})

    def delete_samba_users_config(self, config: list[str]) -> dict[str, Any]:
        """Delete SAMBA user configurations."""
        return self._client.request("DELETE", "/samba/users/config", json={"data": config})

    def get_samba_users_config_by_id(self, user_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get SAMBA user configuration."""
        return self._client.request("GET", f"/samba/users/config/{user_id}", params={"all_options": all_options})

    def update_samba_users_config_by_id(self, user_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update SAMBA user configuration."""
        return self._client.request("PUT", f"/samba/users/config/{user_id}", json={"data": config})

    def delete_samba_users_config_by_id(self, user_id: str) -> dict[str, Any]:
        """Delete SAMBA user configuration."""
        return self._client.request("DELETE", f"/samba/users/config/{user_id}")
