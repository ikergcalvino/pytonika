from typing import Any

from ._endpoint import Endpoint


class LwM2MClient(Endpoint):
    def get_lwm2m_client_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get LwM2M Client global configuration."""
        return self._client.request("GET", "/lwm2m/client/global", params={"all_options": all_options})

    def update_lwm2m_client_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Update LwM2M Client global configuration."""
        return self._client.request("PUT", "/lwm2m/client/global", json={"data": config})

    def get_lwm2m_client_objects_security_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get LwM2M Client security object instances."""
        return self._client.request("GET", "/lwm2m/client/objects/security/config", params={"all_options": all_options})

    def create_lwm2m_client_objects_security_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create LwM2M Client security object instance."""
        return self._client.request("POST", "/lwm2m/client/objects/security/config", json={"data": config})

    def update_lwm2m_client_objects_security_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update LwM2M Client security object instances."""
        return self._client.request("PUT", "/lwm2m/client/objects/security/config", json={"data": config})

    def delete_lwm2m_client_objects_security_config(self, config: list[str]) -> dict[str, Any]:
        """Delete LwM2M Client security object instances."""
        return self._client.request("DELETE", "/lwm2m/client/objects/security/config", json={"data": config})

    def get_lwm2m_client_objects_security_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Get LwM2M Client security object instance."""
        return self._client.request(
            "GET", f"/lwm2m/client/objects/security/config/{config_id}", params={"all_options": all_options}
        )

    def update_lwm2m_client_objects_security_config_by_id(
        self, config_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Update LwM2M Client security object instance."""
        return self._client.request("PUT", f"/lwm2m/client/objects/security/config/{config_id}", json={"data": config})

    def delete_lwm2m_client_objects_security_config_by_id(
        self, config_id: str, config: list[str] | None = None
    ) -> dict[str, Any]:
        """Delete LwM2M Client security object instance."""
        return self._client.request(
            "DELETE",
            f"/lwm2m/client/objects/security/config/{config_id}",
            json=None if config is None else {"data": config},
        )

    def get_lwm2m_client_objects_server_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get LwM2M Client server object instances."""
        return self._client.request("GET", "/lwm2m/client/objects/server/config", params={"all_options": all_options})

    def create_lwm2m_client_objects_server_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create LwM2M Client server object instance."""
        return self._client.request("POST", "/lwm2m/client/objects/server/config", json={"data": config})

    def update_lwm2m_client_objects_server_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update LwM2M Client server object instances."""
        return self._client.request("PUT", "/lwm2m/client/objects/server/config", json={"data": config})

    def delete_lwm2m_client_objects_server_config(self, config: list[str]) -> dict[str, Any]:
        """Delete LwM2M Client server object instances."""
        return self._client.request("DELETE", "/lwm2m/client/objects/server/config", json={"data": config})

    def get_lwm2m_client_objects_server_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Get LwM2M Client server object instance."""
        return self._client.request(
            "GET", f"/lwm2m/client/objects/server/config/{config_id}", params={"all_options": all_options}
        )

    def update_lwm2m_client_objects_server_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update LwM2M Client server object instance."""
        return self._client.request("PUT", f"/lwm2m/client/objects/server/config/{config_id}", json={"data": config})

    def delete_lwm2m_client_objects_server_config_by_id(
        self, config_id: str, config: list[str] | None = None
    ) -> dict[str, Any]:
        """Delete LwM2M Client server object instance."""
        return self._client.request(
            "DELETE",
            f"/lwm2m/client/objects/server/config/{config_id}",
            json=None if config is None else {"data": config},
        )

    def get_lwm2m_client_status(self) -> dict[str, Any]:
        """Get LwM2M client status."""
        return self._client.request("GET", "/lwm2m/client/status")
