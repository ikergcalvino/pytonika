from typing import Any

from ._base import Endpoint


class IEC608705Server(Endpoint):
    def get_iec60870_server_global(self) -> dict[str, Any]:
        """Get IEC 60870-5 Server global configuration."""
        endpoint = "/iec60870/server/global"

        return self._api_client.get(endpoint)

    def update_iec60870_server_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Update IEC 60870-5 Server global configuration."""
        endpoint = "/iec60870/server/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_iec60870_server_status(self) -> dict[str, Any]:
        """Get IEC 60870-5 Server service status."""
        endpoint = "/iec60870/server/status"

        return self._api_client.get(endpoint)

    def get_iec60870_server_instances_config(self) -> dict[str, Any]:
        """List IEC 60870-5 Server instances."""
        endpoint = "/iec60870/server/instances/config"

        return self._api_client.get(endpoint)

    def create_iec60870_server_instances_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create IEC 60870-5 Server instance."""
        endpoint = "/iec60870/server/instances/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_iec60870_server_instances_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update IEC 60870-5 Server instances."""
        endpoint = "/iec60870/server/instances/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_iec60870_server_instances_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete IEC 60870-5 Server instances."""
        return [self.delete_iec60870_server_instances_config_by_id(instance_id) for instance_id in config]

    def get_iec60870_server_instances_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified IEC 60870-5 Server instance."""
        endpoint = f"/iec60870/server/instances/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_iec60870_server_instances_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update IEC 60870-5 Server instance."""
        endpoint = f"/iec60870/server/instances/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_iec60870_server_instances_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete IEC 60870-5 Server instance."""
        endpoint = f"/iec60870/server/instances/config/{config_id}"

        return self._api_client.delete(endpoint)
