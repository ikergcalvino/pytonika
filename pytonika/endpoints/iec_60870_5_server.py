from typing import Any

from ._endpoint import Endpoint


class IEC608705Server(Endpoint):
    def get_iec60870_server_global(self) -> dict[str, Any]:
        """Get IEC 60870-5 Server global configuration."""
        endpoint = "/iec60870/server/global"

        return self._client.request("GET", endpoint)

    def update_iec60870_server_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Update IEC 60870-5 Server global configuration."""
        endpoint = "/iec60870/server/global"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def get_iec60870_server_status(self) -> dict[str, Any]:
        """Get IEC 60870-5 Server service status."""
        endpoint = "/iec60870/server/status"

        return self._client.request("GET", endpoint)

    def get_iec60870_server_instances_config(self) -> dict[str, Any]:
        """List IEC 60870-5 Server instances."""
        endpoint = "/iec60870/server/instances/config"

        return self._client.request("GET", endpoint)

    def create_iec60870_server_instances_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create IEC 60870-5 Server instance."""
        endpoint = "/iec60870/server/instances/config"

        data = {"data": config}

        return self._client.request("POST", endpoint, json=data)

    def update_iec60870_server_instances_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update IEC 60870-5 Server instances."""
        endpoint = "/iec60870/server/instances/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_iec60870_server_instances_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete IEC 60870-5 Server instances."""
        return [self.delete_iec60870_server_instances_config_by_id(instance_id) for instance_id in config]

    def get_iec60870_server_instances_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified IEC 60870-5 Server instance."""
        endpoint = f"/iec60870/server/instances/config/{config_id}"

        return self._client.request("GET", endpoint)

    def update_iec60870_server_instances_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update IEC 60870-5 Server instance."""
        endpoint = f"/iec60870/server/instances/config/{config_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_iec60870_server_instances_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete IEC 60870-5 Server instance."""
        endpoint = f"/iec60870/server/instances/config/{config_id}"

        return self._client.request("DELETE", endpoint)
