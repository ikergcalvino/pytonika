from typing import Any

from ._endpoint import Endpoint


class DLMS(Endpoint):
    def get_dlms_connections_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Connections configurations."""
        return self._client.request("GET", "/dlms/connections/config", params={"all_options": all_options})

    def create_dlms_connections_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Connections configuration."""
        return self._client.request("POST", "/dlms/connections/config", json={"data": config})

    def update_dlms_connections_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Connections configurations."""
        return self._client.request("PUT", "/dlms/connections/config", json={"data": config})

    def delete_dlms_connections_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Connections configurations."""
        return self._client.request("DELETE", "/dlms/connections/config", json={"data": config})

    def get_dlms_connections_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Connections configuration."""
        return self._client.request("GET", f"/dlms/connections/config/{config_id}", params={"all_options": all_options})

    def update_dlms_connections_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Connections configuration."""
        return self._client.request("PUT", f"/dlms/connections/config/{config_id}", json={"data": config})

    def delete_dlms_connections_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Connections configuration."""
        return self._client.request("DELETE", f"/dlms/connections/config/{config_id}")

    def dlms_cosem_group_actions_test(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Test COSEM group configuration."""
        return self._client.request(
            "POST", "/dlms/cosem_group/actions/test", json=None if data is None else {"data": data}
        )

    def get_dlms_cosem_group_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all COSEM group configurations."""
        return self._client.request("GET", "/dlms/cosem_group/config", params={"all_options": all_options})

    def create_dlms_cosem_group_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates COSEM group configuration."""
        return self._client.request("POST", "/dlms/cosem_group/config", json={"data": config})

    def update_dlms_cosem_group_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified COSEM group configurations."""
        return self._client.request("PUT", "/dlms/cosem_group/config", json={"data": config})

    def delete_dlms_cosem_group_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified COSEM group configurations."""
        return self._client.request("DELETE", "/dlms/cosem_group/config", json={"data": config})

    def get_dlms_cosem_group_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified COSEM group configuration."""
        return self._client.request("GET", f"/dlms/cosem_group/config/{config_id}", params={"all_options": all_options})

    def update_dlms_cosem_group_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified COSEM group configuration."""
        return self._client.request("PUT", f"/dlms/cosem_group/config/{config_id}", json={"data": config})

    def delete_dlms_cosem_group_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified COSEM group configuration."""
        return self._client.request("DELETE", f"/dlms/cosem_group/config/{config_id}")

    def get_dlms_cosem_group_status(self) -> dict[str, Any]:
        """Returns DLMS status."""
        return self._client.request("GET", "/dlms/cosem_group/status")

    def get_dlms_cosem_group_status_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns cosem group current value."""
        return self._client.request("GET", f"/dlms/cosem_group/status/{config_id}")

    def get_dlms_cosem_group_cosem_config(
        self, cosem_group_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns all DLMS COSEM configurations."""
        return self._client.request(
            "GET", f"/dlms/cosem_group/{cosem_group_id}/cosem/config", params={"all_options": all_options}
        )

    def create_dlms_cosem_group_cosem_config(self, cosem_group_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates DLMS COSEM configuration."""
        return self._client.request("POST", f"/dlms/cosem_group/{cosem_group_id}/cosem/config", json={"data": config})

    def update_dlms_cosem_group_cosem_config(self, cosem_group_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified DLMS COSEM configurations."""
        return self._client.request("PUT", f"/dlms/cosem_group/{cosem_group_id}/cosem/config", json={"data": config})

    def delete_dlms_cosem_group_cosem_config(self, cosem_group_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes specified DLMS COSEM configurations."""
        return self._client.request("DELETE", f"/dlms/cosem_group/{cosem_group_id}/cosem/config", json={"data": config})

    def get_dlms_cosem_group_cosem_config_by_id(
        self, cosem_group_id: str, cosem_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified DLMS COSEM configuration."""
        return self._client.request(
            "GET", f"/dlms/cosem_group/{cosem_group_id}/cosem/config/{cosem_id}", params={"all_options": all_options}
        )

    def update_dlms_cosem_group_cosem_config_by_id(
        self, cosem_group_id: str, cosem_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified DLMS COSEM configuration."""
        return self._client.request(
            "PUT", f"/dlms/cosem_group/{cosem_group_id}/cosem/config/{cosem_id}", json={"data": config}
        )

    def delete_dlms_cosem_group_cosem_config_by_id(self, cosem_group_id: str, cosem_id: str) -> dict[str, Any]:
        """Deletes the specified DLMS COSEM configuration."""
        return self._client.request("DELETE", f"/dlms/cosem_group/{cosem_group_id}/cosem/config/{cosem_id}")

    def get_dlms_cosem_group_cosem_status_by_id(
        self, cosem_group_id: str, cosem_id: str, *, device: str | None = None, attribute: str | None = None
    ) -> dict[str, Any]:
        """Returns the specified DLMS COSEM configuration."""
        return self._client.request(
            "GET",
            f"/dlms/cosem_group/{cosem_group_id}/cosem/status/{cosem_id}",
            params={"device": device, "attribute": attribute},
        )

    def get_dlms_database_entries_status(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        id: str | None = None,
        group_name: str | None = None,
        group_id: str | None = None,
    ) -> dict[str, Any]:
        """Returns all DLMS database entries."""
        return self._client.request(
            "GET",
            "/dlms/database/entries/status",
            params={"limit": limit, "offset": offset, "id": id, "group_name": group_name, "group_id": group_id},
        )

    def dlms_devices_actions_test(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Test DLMS physDevices configuration."""
        return self._client.request("POST", "/dlms/devices/actions/test", json=None if data is None else {"data": data})

    def get_dlms_devices_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Devices configurations."""
        return self._client.request("GET", "/dlms/devices/config", params={"all_options": all_options})

    def create_dlms_devices_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Devices configuration."""
        return self._client.request("POST", "/dlms/devices/config", json={"data": config})

    def update_dlms_devices_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Devices configurations."""
        return self._client.request("PUT", "/dlms/devices/config", json={"data": config})

    def delete_dlms_devices_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Devices configurations."""
        return self._client.request("DELETE", "/dlms/devices/config", json={"data": config})

    def get_dlms_devices_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Devices configuration."""
        return self._client.request("GET", f"/dlms/devices/config/{config_id}", params={"all_options": all_options})

    def update_dlms_devices_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Devices configuration."""
        return self._client.request("PUT", f"/dlms/devices/config/{config_id}", json={"data": config})

    def delete_dlms_devices_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Devices configuration."""
        return self._client.request("DELETE", f"/dlms/devices/config/{config_id}")

    def get_dlms_found_parameters_status(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        search: str | None = None,
        devices: str | None = None,
    ) -> dict[str, Any]:
        """Returns DLMS scan results."""
        return self._client.request(
            "GET",
            "/dlms/found_parameters/status",
            params={"limit": limit, "offset": offset, "search": search, "devices": devices},
        )

    def get_dlms_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all DLMS global settings configurations."""
        return self._client.request("GET", "/dlms/global", params={"all_options": all_options})

    def update_dlms_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified DLMS global settings configurations."""
        return self._client.request("PUT", "/dlms/global", json={"data": config})

    def dlms_scan_actions_start(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Starts DLMS scan."""
        return self._client.request("POST", "/dlms/scan/actions/start", json=None if data is None else {"data": data})

    def dlms_scan_actions_stop(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Stops DLMS scan."""
        return self._client.request("POST", "/dlms/scan/actions/stop", json=None if data is None else {"data": data})

    def get_dlms_scan_status(self) -> dict[str, Any]:
        """Returns DLMS scan status."""
        return self._client.request("GET", "/dlms/scan/status")
