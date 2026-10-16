from typing import Any

from ._endpoint import Endpoint


class PPTP(Endpoint):
    def get_pptp_client_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get pptp client configurations."""
        return self._client.request("GET", "/pptp/client/config", params={"all_options": all_options})

    def create_pptp_client_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create pptp client configuration."""
        return self._client.request("POST", "/pptp/client/config", json={"data": config})

    def update_pptp_client_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update pptp client configurations."""
        return self._client.request("PUT", "/pptp/client/config", json={"data": config})

    def delete_pptp_client_config(self, config: list[str]) -> dict[str, Any]:
        """Delete pptp client configurations."""
        return self._client.request("DELETE", "/pptp/client/config", json={"data": config})

    def get_pptp_client_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get pptp client configuration."""
        return self._client.request("GET", f"/pptp/client/config/{config_id}", params={"all_options": all_options})

    def update_pptp_client_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update pptp client configuration."""
        return self._client.request("PUT", f"/pptp/client/config/{config_id}", json={"data": config})

    def delete_pptp_client_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete pptp client configuration."""
        return self._client.request("DELETE", f"/pptp/client/config/{config_id}")

    def get_pptp_server_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Delete pptp server configurations."""
        return self._client.request("GET", "/pptp/server/config", params={"all_options": all_options})

    def create_pptp_server_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create pptp server configuration."""
        return self._client.request("POST", "/pptp/server/config", json={"data": config})

    def update_pptp_server_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update pptp server configurations."""
        return self._client.request("PUT", "/pptp/server/config", json={"data": config})

    def delete_pptp_server_config(self, config: list[str]) -> dict[str, Any]:
        """Delete pptp server configurations."""
        return self._client.request("DELETE", "/pptp/server/config", json={"data": config})

    def get_pptp_server_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get pptp server configuration."""
        return self._client.request("GET", f"/pptp/server/config/{config_id}", params={"all_options": all_options})

    def update_pptp_server_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update pptp server configuration."""
        return self._client.request("PUT", f"/pptp/server/config/{config_id}", json={"data": config})

    def delete_pptp_server_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete pptp server configuration."""
        return self._client.request("DELETE", f"/pptp/server/config/{config_id}")

    def get_pptp_server_users_config(self, server_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get pptp users configurations."""
        return self._client.request(
            "GET", f"/pptp/server/{server_id}/users/config", params={"all_options": all_options}
        )

    def create_pptp_server_users_config(self, server_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Create pptp user configuration."""
        return self._client.request("POST", f"/pptp/server/{server_id}/users/config", json={"data": config})

    def update_pptp_server_users_config(self, server_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update pptp user configurations."""
        return self._client.request("PUT", f"/pptp/server/{server_id}/users/config", json={"data": config})

    def delete_pptp_server_users_config(self, server_id: str, config: list[str]) -> dict[str, Any]:
        """Delete pptp user configurations."""
        return self._client.request("DELETE", f"/pptp/server/{server_id}/users/config", json={"data": config})

    def get_pptp_server_users_config_by_id(
        self, server_id: str, users_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Get pptp user configuration."""
        return self._client.request(
            "GET", f"/pptp/server/{server_id}/users/config/{users_id}", params={"all_options": all_options}
        )

    def update_pptp_server_users_config_by_id(
        self, server_id: str, users_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Update pptp user configuration."""
        return self._client.request("PUT", f"/pptp/server/{server_id}/users/config/{users_id}", json={"data": config})

    def delete_pptp_server_users_config_by_id(self, server_id: str, users_id: str) -> dict[str, Any]:
        """Delete pptp user configuration."""
        return self._client.request("DELETE", f"/pptp/server/{server_id}/users/config/{users_id}")

    def get_pptp_status(self) -> dict[str, Any]:
        """Returns the status of all pptp instances."""
        return self._client.request("GET", "/pptp/status")

    def get_pptp_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Return the status of the pptp instance."""
        return self._client.request("GET", f"/pptp/status/{status_id}")
