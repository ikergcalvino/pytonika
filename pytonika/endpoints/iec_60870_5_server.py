from typing import Any

from ._endpoint import Endpoint


class IEC608705Server(Endpoint):
    def get_iec60870_server_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get IEC 60870-5 Server global configuration."""
        return self._client.request("GET", "/iec60870/server/global", params={"all_options": all_options})

    def update_iec60870_server_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Update IEC 60870-5 Server global configuration."""
        return self._client.request("PUT", "/iec60870/server/global", json={"data": config})

    def get_iec60870_server_instances_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """List IEC 60870-5 Server instances."""
        return self._client.request("GET", "/iec60870/server/instances/config", params={"all_options": all_options})

    def create_iec60870_server_instances_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create IEC 60870-5 Server instance."""
        return self._client.request("POST", "/iec60870/server/instances/config", json={"data": config})

    def update_iec60870_server_instances_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update IEC 60870-5 Server instances."""
        return self._client.request("PUT", "/iec60870/server/instances/config", json={"data": config})

    def delete_iec60870_server_instances_config(self, config: list[str]) -> dict[str, Any]:
        """Delete IEC 60870-5 Server instances."""
        return self._client.request("DELETE", "/iec60870/server/instances/config", json={"data": config})

    def get_iec60870_server_instances_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified IEC 60870-5 Server instance."""
        return self._client.request(
            "GET", f"/iec60870/server/instances/config/{config_id}", params={"all_options": all_options}
        )

    def update_iec60870_server_instances_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update IEC 60870-5 Server instance."""
        return self._client.request("PUT", f"/iec60870/server/instances/config/{config_id}", json={"data": config})

    def delete_iec60870_server_instances_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete IEC 60870-5 Server instance."""
        return self._client.request("DELETE", f"/iec60870/server/instances/config/{config_id}")

    def get_iec60870_server_objects_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """List IEC 60870-5 Server information objects."""
        return self._client.request("GET", "/iec60870/server/objects/config", params={"all_options": all_options})

    def create_iec60870_server_objects_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create IEC 60870-5 Server information object."""
        return self._client.request("POST", "/iec60870/server/objects/config", json={"data": config})

    def update_iec60870_server_objects_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update IEC 60870-5 Server information objects."""
        return self._client.request("PUT", "/iec60870/server/objects/config", json={"data": config})

    def delete_iec60870_server_objects_config(self, config: list[str]) -> dict[str, Any]:
        """Delete IEC 60870-5 Server information objects."""
        return self._client.request("DELETE", "/iec60870/server/objects/config", json={"data": config})

    def get_iec60870_server_objects_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified IEC 60870-5 Server information object."""
        return self._client.request(
            "GET", f"/iec60870/server/objects/config/{config_id}", params={"all_options": all_options}
        )

    def update_iec60870_server_objects_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update IEC 60870-5 Server information object."""
        return self._client.request("PUT", f"/iec60870/server/objects/config/{config_id}", json={"data": config})

    def delete_iec60870_server_objects_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete IEC 60870-5 Server information object."""
        return self._client.request("DELETE", f"/iec60870/server/objects/config/{config_id}")

    def get_iec60870_server_status(self) -> dict[str, Any]:
        """Get IEC 60870-5 Server service status."""
        return self._client.request("GET", "/iec60870/server/status")
