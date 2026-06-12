from typing import Any

from ._base import Endpoint


class IEC608705Client(Endpoint):
    def get_iec60870_client_global(self) -> dict[str, Any]:
        """Get IEC 60870-5 Client global configuration."""
        endpoint = "/iec60870/client/global"

        return self._api_client.get(endpoint)

    def update_iec60870_client_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Update IEC 60870-5 Client global configuration."""
        endpoint = "/iec60870/client/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_iec60870_client_status(self) -> dict[str, Any]:
        """Get IEC 60870-5 Client service status."""
        endpoint = "/iec60870/client/status"

        return self._api_client.get(endpoint)

    def iec60870_client_test_information_objects(self, data: dict[str, Any]) -> dict[str, Any]:
        """Try reading the specified information objects from an IEC 60870-5 server."""
        endpoint = "/iec60870/client/actions/test_information_objects"

        return self._api_client.post(endpoint, data={"data": data})

    def iec60870_client_list_information_objects(self, data: dict[str, Any]) -> dict[str, Any]:
        """List available information objects on IEC 60870-5 server."""
        endpoint = "/iec60870/client/actions/list_information_objects"

        return self._api_client.post(endpoint, data={"data": data})

    def get_iec60870_client_database_entries_status(self) -> dict[str, Any]:
        """Returns all IEC 60870-5 client service database entries."""
        endpoint = "/iec60870/client/database/entries/status"

        return self._api_client.get(endpoint)

    def get_iec60870_client_instances_config(self) -> dict[str, Any]:
        """Read IEC 60870-5 Client instances."""
        endpoint = "/iec60870/client/instances/config"

        return self._api_client.get(endpoint)

    def create_iec60870_client_instances_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create IEC 60870-5 Client instance."""
        endpoint = "/iec60870/client/instances/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_iec60870_client_instances_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update IEC 60870-5 Client instances."""
        endpoint = "/iec60870/client/instances/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_iec60870_client_instances_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete IEC 60870-5 Client instances."""
        return [self.delete_iec60870_client_instances_config_by_id(instance_id) for instance_id in config]

    def get_iec60870_client_instances_config_by_id(self, instance_id: str) -> dict[str, Any]:
        """Read IEC 60870-5 Client instance."""
        endpoint = f"/iec60870/client/instances/config/{instance_id}"

        return self._api_client.get(endpoint)

    def update_iec60870_client_instances_config_by_id(self, instance_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update IEC 60870-5 Client instance."""
        endpoint = f"/iec60870/client/instances/config/{instance_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_iec60870_client_instances_config_by_id(self, instance_id: str) -> dict[str, Any]:
        """Delete IEC 60870-5 Client instance."""
        endpoint = f"/iec60870/client/instances/config/{instance_id}"

        return self._api_client.delete(endpoint)
