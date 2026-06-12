from typing import Any

from ._base import Endpoint


class L2TP(Endpoint):
    def get_l2tp_status(self) -> dict[str, Any]:
        """Returns the status of all l2tp instances."""
        endpoint = "/l2tp/status"

        return self._api_client.get(endpoint)

    def get_l2tp_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Return the status of the l2tp instance."""
        endpoint = f"/l2tp/status/{status_id}"

        return self._api_client.get(endpoint)

    def get_l2tp_client_config(self) -> dict[str, Any]:
        """Get l2tp client configurations."""
        endpoint = "/l2tp/client/config"

        return self._api_client.get(endpoint)

    def create_l2tp_client_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create l2tp client configuration."""
        endpoint = "/l2tp/client/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_l2tp_client_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update l2tp client configurations."""
        endpoint = "/l2tp/client/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_l2tp_client_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete l2tp client configurations."""
        return [self.delete_l2tp_client_config_by_id(config_id) for config_id in config]

    def get_l2tp_client_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Get l2tp client configuration."""
        endpoint = f"/l2tp/client/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_l2tp_client_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update l2tp client configuration."""
        endpoint = f"/l2tp/client/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_l2tp_client_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete l2tp client configuration."""
        endpoint = f"/l2tp/client/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_l2tp_server_config(self) -> dict[str, Any]:
        """Get l2tp server configurations."""
        endpoint = "/l2tp/server/config"

        return self._api_client.get(endpoint)

    def create_l2tp_server_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create l2tp server configuration."""
        endpoint = "/l2tp/server/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_l2tp_server_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update l2tp server configurations."""
        endpoint = "/l2tp/server/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_l2tp_server_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete l2tp server configurations."""
        return [self.delete_l2tp_server_config_by_id(config_id) for config_id in config]

    def get_l2tp_server_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Get l2tp server configuration."""
        endpoint = f"/l2tp/server/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_l2tp_server_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update l2tp server configuration."""
        endpoint = f"/l2tp/server/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_l2tp_server_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete l2tp server configuration."""
        endpoint = f"/l2tp/server/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_l2tp_users_config(self) -> dict[str, Any]:
        """Get l2tp user configurations."""
        endpoint = "/l2tp/users/config"

        return self._api_client.get(endpoint)

    def create_l2tp_users_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create l2tp user configurations."""
        endpoint = "/l2tp/users/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_l2tp_users_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update l2tp user configurations."""
        endpoint = "/l2tp/users/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_l2tp_users_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete l2tp user configurations."""
        return [self.delete_l2tp_users_config_by_id(config_id) for config_id in config]

    def get_l2tp_users_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Get user configuration."""
        endpoint = f"/l2tp/users/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_l2tp_users_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update user configuration."""
        endpoint = f"/l2tp/users/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_l2tp_users_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete user configuration."""
        endpoint = f"/l2tp/users/config/{config_id}"

        return self._api_client.delete(endpoint)
