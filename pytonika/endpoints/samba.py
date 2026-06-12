from typing import Any

from ._base import Endpoint


class Samba(Endpoint):
    def get_samba_global(self) -> dict[str, Any]:
        """Get SAMBA general configuration."""
        endpoint = "/samba/global"

        return self._api_client.get(endpoint)

    def update_samba_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Update SAMBA general configuration."""
        endpoint = "/samba/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_samba_status(self) -> dict[str, Any]:
        """Get SAMBA instance status and all active sessions."""
        endpoint = "/samba/status"

        return self._api_client.get(endpoint)

    def get_samba_shares_config(self) -> dict[str, Any]:
        """Get SAMBA share configurations."""
        endpoint = "/samba/shares/config"

        return self._api_client.get(endpoint)

    def create_samba_shares_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create SAMBA share configuration."""
        endpoint = "/samba/shares/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_samba_shares_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update SAMBA share configurations."""
        endpoint = "/samba/shares/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_samba_shares_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete SAMBA share configurations."""
        return [self.delete_samba_shares_config_by_id(share_id) for share_id in config]

    def get_samba_shares_config_by_id(self, share_id: str) -> dict[str, Any]:
        """Get SAMBA share configuration."""
        endpoint = f"/samba/shares/config/{share_id}"

        return self._api_client.get(endpoint)

    def update_samba_shares_config_by_id(self, share_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update SAMBA share configuration."""
        endpoint = f"/samba/shares/config/{share_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_samba_shares_config_by_id(self, share_id: str) -> dict[str, Any]:
        """Delete SAMBA share configuration."""
        endpoint = f"/samba/shares/config/{share_id}"

        return self._api_client.delete(endpoint)

    def get_samba_users_config(self) -> dict[str, Any]:
        """Get SAMBA user configurations."""
        endpoint = "/samba/users/config"

        return self._api_client.get(endpoint)

    def create_samba_users_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create SAMBA user configuration."""
        endpoint = "/samba/users/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_samba_users_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update SAMBA user configurations."""
        endpoint = "/samba/users/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_samba_users_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete SAMBA user configurations."""
        return [self.delete_samba_users_config_by_id(user_id) for user_id in config]

    def get_samba_users_config_by_id(self, user_id: str) -> dict[str, Any]:
        """Get SAMBA user configuration."""
        endpoint = f"/samba/users/config/{user_id}"

        return self._api_client.get(endpoint)

    def update_samba_users_config_by_id(self, user_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update SAMBA user configuration."""
        endpoint = f"/samba/users/config/{user_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_samba_users_config_by_id(self, user_id: str) -> dict[str, Any]:
        """Delete SAMBA user configuration."""
        endpoint = f"/samba/users/config/{user_id}"

        return self._api_client.delete(endpoint)
