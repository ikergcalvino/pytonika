from typing import Any

from ._endpoint import Endpoint


class IEC608705Client(Endpoint):
    def iec60870_client_actions_list_information_objects(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """List available information objects on IEC 60870-5 server."""
        return self._client.request(
            "POST", "/iec60870/client/actions/list_information_objects", json=None if data is None else {"data": data}
        )

    def iec60870_client_actions_test_information_objects(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Try reading the specified information objects from an IEC 60870-5 server."""
        return self._client.request(
            "POST", "/iec60870/client/actions/test_information_objects", json=None if data is None else {"data": data}
        )

    def get_iec60870_client_database_entries_status(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        id: str | None = None,
        client_id: str | None = None,
        information_object_address: str | None = None,
        common_address: str | None = None,
        data_type: str | None = None,
        cause_of_transmission: str | None = None,
    ) -> dict[str, Any]:
        """Returns all IEC 60870-5 client service database entries."""
        return self._client.request(
            "GET",
            "/iec60870/client/database/entries/status",
            params={
                "limit": limit,
                "offset": offset,
                "id": id,
                "client_id": client_id,
                "information_object_address": information_object_address,
                "common_address": common_address,
                "data_type": data_type,
                "cause_of_transmission": cause_of_transmission,
            },
        )

    def get_iec60870_client_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get IEC 60870-5 Client global configuration."""
        return self._client.request("GET", "/iec60870/client/global", params={"all_options": all_options})

    def update_iec60870_client_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Update IEC 60870-5 Client global configuration."""
        return self._client.request("PUT", "/iec60870/client/global", json={"data": config})

    def get_iec60870_client_instances_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Read IEC 60870-5 Client instances."""
        return self._client.request("GET", "/iec60870/client/instances/config", params={"all_options": all_options})

    def create_iec60870_client_instances_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create IEC 60870-5 Client instance."""
        return self._client.request("POST", "/iec60870/client/instances/config", json={"data": config})

    def update_iec60870_client_instances_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update IEC 60870-5 Client instances."""
        return self._client.request("PUT", "/iec60870/client/instances/config", json={"data": config})

    def delete_iec60870_client_instances_config(self, config: list[str]) -> dict[str, Any]:
        """Delete IEC 60870-5 Client instances."""
        return self._client.request("DELETE", "/iec60870/client/instances/config", json={"data": config})

    def get_iec60870_client_instances_config_by_id(
        self, instance_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Read IEC 60870-5 Client instance."""
        return self._client.request(
            "GET", f"/iec60870/client/instances/config/{instance_id}", params={"all_options": all_options}
        )

    def update_iec60870_client_instances_config_by_id(self, instance_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update IEC 60870-5 Client instance."""
        return self._client.request("PUT", f"/iec60870/client/instances/config/{instance_id}", json={"data": config})

    def delete_iec60870_client_instances_config_by_id(self, instance_id: str) -> dict[str, Any]:
        """Delete IEC 60870-5 Client instance."""
        return self._client.request("DELETE", f"/iec60870/client/instances/config/{instance_id}")

    def get_iec60870_client_serial_devices_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Read IEC 60870-5 Serial device configurations."""
        return self._client.request(
            "GET", "/iec60870/client/serial_devices/config", params={"all_options": all_options}
        )

    def create_iec60870_client_serial_devices_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create IEC 60870-5 Serial device configurations."""
        return self._client.request("POST", "/iec60870/client/serial_devices/config", json={"data": config})

    def update_iec60870_client_serial_devices_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update IEC 60870-5 Serial device configurations."""
        return self._client.request("PUT", "/iec60870/client/serial_devices/config", json={"data": config})

    def delete_iec60870_client_serial_devices_config(self, config: list[str]) -> dict[str, Any]:
        """Delete IEC 60870 Client Serial device configurations."""
        return self._client.request("DELETE", "/iec60870/client/serial_devices/config", json={"data": config})

    def get_iec60870_client_serial_devices_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Read IEC 60870-5 Serial device configuration."""
        return self._client.request(
            "GET", f"/iec60870/client/serial_devices/config/{config_id}", params={"all_options": all_options}
        )

    def update_iec60870_client_serial_devices_config_by_id(
        self, config_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Update IEC 60870-5 Serial device configuration."""
        return self._client.request("PUT", f"/iec60870/client/serial_devices/config/{config_id}", json={"data": config})

    def delete_iec60870_client_serial_devices_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete IEC 60870-5 Serial device configuration."""
        return self._client.request("DELETE", f"/iec60870/client/serial_devices/config/{config_id}")

    def get_iec60870_client_status(self) -> dict[str, Any]:
        """Get IEC 60870-5 Client service status."""
        return self._client.request("GET", "/iec60870/client/status")
