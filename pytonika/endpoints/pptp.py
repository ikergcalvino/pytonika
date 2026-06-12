from typing import Any

from ._base import Endpoint


class PPTP(Endpoint):
    def get_pptp_client_config(self) -> dict[str, Any]:
        """Get pptp client configurations."""
        endpoint = "/pptp/client/config"

        return self._api_client.get(endpoint)

    def create_pptp_client_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create pptp client configuration."""
        endpoint = "/pptp/client/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_pptp_client_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update pptp client configurations."""
        endpoint = "/pptp/client/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_pptp_client_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete pptp client configurations."""
        return [self.delete_pptp_client_config_by_id(client_id) for client_id in config]

    def get_pptp_client_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Get pptp client configuration."""
        endpoint = f"/pptp/client/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_pptp_client_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update pptp client configuration."""
        endpoint = f"/pptp/client/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_pptp_client_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete pptp client configuration."""
        endpoint = f"/pptp/client/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_pptp_server_config(self) -> dict[str, Any]:
        """Delete pptp server configurations."""
        endpoint = "/pptp/server/config"

        return self._api_client.get(endpoint)

    def create_pptp_server_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create pptp server configuration."""
        endpoint = "/pptp/server/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_pptp_server_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update pptp server configurations."""
        endpoint = "/pptp/server/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_pptp_server_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete pptp server configurations."""
        return [self.delete_pptp_server_config_by_id(server_id) for server_id in config]

    def get_pptp_server_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Get pptp server configuration."""
        endpoint = f"/pptp/server/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_pptp_server_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update pptp server configuration."""
        endpoint = f"/pptp/server/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_pptp_server_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete pptp server configuration."""
        endpoint = f"/pptp/server/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_pptp_server_users_config(self, server_id: str) -> dict[str, Any]:
        """Get pptp users configurations."""
        endpoint = f"/pptp/server/{server_id}/users/config"

        return self._api_client.get(endpoint)

    def create_pptp_server_users_config(self, server_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Create pptp user configuration."""
        endpoint = f"/pptp/server/{server_id}/users/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_pptp_server_users_config(self, server_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update pptp user configurations."""
        endpoint = f"/pptp/server/{server_id}/users/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_pptp_server_users_config(self, server_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Delete pptp user configurations."""
        return [self.delete_pptp_server_users_config_by_id(server_id, user_id) for user_id in config]

    def get_pptp_server_users_config_by_id(self, server_id: str, users_id: str) -> dict[str, Any]:
        """Get pptp user configuration."""
        endpoint = f"/pptp/server/{server_id}/users/config/{users_id}"

        return self._api_client.get(endpoint)

    def update_pptp_server_users_config_by_id(
        self, server_id: str, users_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Update pptp user configuration."""
        endpoint = f"/pptp/server/{server_id}/users/config/{users_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_pptp_server_users_config_by_id(self, server_id: str, users_id: str) -> dict[str, Any]:
        """Delete pptp user configuration."""
        endpoint = f"/pptp/server/{server_id}/users/config/{users_id}"

        return self._api_client.delete(endpoint)
