from typing import Any

from ._endpoint import Endpoint


class L2TP(Endpoint):
    def get_l2tp_client_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get l2tp client configurations."""
        return self._client.request("GET", "/l2tp/client/config", params={"all_options": all_options})

    def create_l2tp_client_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create l2tp client configuration."""
        return self._client.request("POST", "/l2tp/client/config", json={"data": config})

    def update_l2tp_client_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update l2tp client configurations."""
        return self._client.request("PUT", "/l2tp/client/config", json={"data": config})

    def delete_l2tp_client_config(self, config: list[str]) -> dict[str, Any]:
        """Delete l2tp client configurations."""
        return self._client.request("DELETE", "/l2tp/client/config", json={"data": config})

    def get_l2tp_client_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get l2tp client configuration."""
        return self._client.request("GET", f"/l2tp/client/config/{config_id}", params={"all_options": all_options})

    def update_l2tp_client_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update l2tp client configuration."""
        return self._client.request("PUT", f"/l2tp/client/config/{config_id}", json={"data": config})

    def delete_l2tp_client_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete l2tp client configuration."""
        return self._client.request("DELETE", f"/l2tp/client/config/{config_id}")

    def get_l2tp_server_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get l2tp server configurations."""
        return self._client.request("GET", "/l2tp/server/config", params={"all_options": all_options})

    def create_l2tp_server_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create l2tp server configuration."""
        return self._client.request("POST", "/l2tp/server/config", json={"data": config})

    def update_l2tp_server_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update l2tp server configurations."""
        return self._client.request("PUT", "/l2tp/server/config", json={"data": config})

    def delete_l2tp_server_config(self, config: list[str]) -> dict[str, Any]:
        """Delete l2tp server configurations."""
        return self._client.request("DELETE", "/l2tp/server/config", json={"data": config})

    def get_l2tp_server_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get l2tp server configuration."""
        return self._client.request("GET", f"/l2tp/server/config/{config_id}", params={"all_options": all_options})

    def update_l2tp_server_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update l2tp server configuration."""
        return self._client.request("PUT", f"/l2tp/server/config/{config_id}", json={"data": config})

    def delete_l2tp_server_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete l2tp server configuration."""
        return self._client.request("DELETE", f"/l2tp/server/config/{config_id}")

    def get_l2tp_status(self) -> dict[str, Any]:
        """Returns the status of all l2tp instances."""
        return self._client.request("GET", "/l2tp/status")

    def get_l2tp_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Return the status of the l2tp instance."""
        return self._client.request("GET", f"/l2tp/status/{status_id}")

    def get_l2tp_users_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get l2tp user configurations."""
        return self._client.request("GET", "/l2tp/users/config", params={"all_options": all_options})

    def create_l2tp_users_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create l2tp user configurations."""
        return self._client.request("POST", "/l2tp/users/config", json={"data": config})

    def update_l2tp_users_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update l2tp user configurations."""
        return self._client.request("PUT", "/l2tp/users/config", json={"data": config})

    def delete_l2tp_users_config(self, config: list[str]) -> dict[str, Any]:
        """Delete l2tp user configurations."""
        return self._client.request("DELETE", "/l2tp/users/config", json={"data": config})

    def get_l2tp_users_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get user configuration."""
        return self._client.request("GET", f"/l2tp/users/config/{config_id}", params={"all_options": all_options})

    def update_l2tp_users_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update user configuration."""
        return self._client.request("PUT", f"/l2tp/users/config/{config_id}", json={"data": config})

    def delete_l2tp_users_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete user configuration."""
        return self._client.request("DELETE", f"/l2tp/users/config/{config_id}")
