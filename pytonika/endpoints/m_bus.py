from typing import Any

from ._endpoint import Endpoint


class MBus(Endpoint):
    def get_mbus_client_config(self) -> dict[str, Any]:
        """List M-Bus Client configurations."""
        return self._client.request("GET", "/mbus/client/config")

    def create_mbus_client_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create M-Bus Client configuration."""
        return self._client.request("POST", "/mbus/client/config", json={"data": config})

    def update_mbus_client_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update M-Bus Client configurations."""
        return self._client.request("PUT", "/mbus/client/config", json={"data": config})

    def delete_mbus_client_config(self, config: list[str]) -> dict[str, Any]:
        """Delete M-Bus Client configurations."""
        return self._client.request("DELETE", "/mbus/client/config", json={"data": config})

    def get_mbus_client_config_by_id(self, client_id: str) -> dict[str, Any]:
        """Returns the specified M-Bus Client configuration."""
        return self._client.request("GET", f"/mbus/client/config/{client_id}")

    def update_mbus_client_config_by_id(self, client_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update M-Bus Client configuration."""
        return self._client.request("PUT", f"/mbus/client/config/{client_id}", json={"data": config})

    def delete_mbus_client_config_by_id(self, client_id: str) -> dict[str, Any]:
        """Delete M-Bus Client configuration."""
        return self._client.request("DELETE", f"/mbus/client/config/{client_id}")

    def get_mbus_database_entries_status(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        id: str | None = None,
        group_name: str | None = None,
        group_id: str | None = None,
        data_type: str | None = None,
    ) -> dict[str, Any]:
        """Returns all M-Bus database entries."""
        return self._client.request(
            "GET",
            "/mbus/database/entries/status",
            params={
                "limit": limit,
                "offset": offset,
                "id": id,
                "group_name": group_name,
                "group_id": group_id,
                "data_type": data_type,
            },
        )

    def mbus_devices_actions_get_info(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Get manufacturer information from M-Bus device."""
        return self._client.request(
            "POST", "/mbus/devices/actions/get_info", json=None if config is None else {"data": config}
        )

    def mbus_devices_actions_ping(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Test if M-Bus device is reachable."""
        return self._client.request(
            "POST", "/mbus/devices/actions/ping", json=None if config is None else {"data": config}
        )

    def mbus_devices_actions_reset(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Send reset request to M-Bus device."""
        return self._client.request(
            "POST", "/mbus/devices/actions/reset", json=None if config is None else {"data": config}
        )

    def mbus_devices_actions_test(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Send a test request to M-Bus device."""
        return self._client.request(
            "POST", "/mbus/devices/actions/test", json=None if config is None else {"data": config}
        )

    def mbus_devices_actions_update_address(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Update primary address of M-Bus device."""
        return self._client.request(
            "POST", "/mbus/devices/actions/update_address", json=None if config is None else {"data": config}
        )

    def mbus_devices_actions_update_baudrate(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Update baudrate of M-Bus device."""
        return self._client.request(
            "POST", "/mbus/devices/actions/update_baudrate", json=None if config is None else {"data": config}
        )

    def get_mbus_devices_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """List M-Bus devices."""
        return self._client.request("GET", "/mbus/devices/config", params={"all_options": all_options})

    def create_mbus_devices_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create M-Bus device."""
        return self._client.request("POST", "/mbus/devices/config", json={"data": config})

    def update_mbus_devices_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update M-Bus devices."""
        return self._client.request("PUT", "/mbus/devices/config", json={"data": config})

    def delete_mbus_devices_config(self, config: list[str]) -> dict[str, Any]:
        """Delete M-Bus devices."""
        return self._client.request("DELETE", "/mbus/devices/config", json={"data": config})

    def get_mbus_devices_config_by_id(self, device_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified M-Bus device."""
        return self._client.request("GET", f"/mbus/devices/config/{device_id}", params={"all_options": all_options})

    def update_mbus_devices_config_by_id(self, device_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update M-Bus device."""
        return self._client.request("PUT", f"/mbus/devices/config/{device_id}", json={"data": config})

    def delete_mbus_devices_config_by_id(self, device_id: str) -> dict[str, Any]:
        """Delete M-Bus device."""
        return self._client.request("DELETE", f"/mbus/devices/config/{device_id}")

    def mbus_devices_actions_update_address_by_id(
        self, device_id: str, config: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Updates the primary address of saved M-Bus device."""
        return self._client.request(
            "POST",
            f"/mbus/devices/{device_id}/actions/update_address",
            json=None if config is None else {"data": config},
        )

    def get_mbus_found_devices_status(self) -> dict[str, Any]:
        """Get M-Bus devices found during scanning process."""
        return self._client.request("GET", "/mbus/found_devices/status")

    def get_mbus_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get M-Bus global configuration."""
        return self._client.request("GET", "/mbus/global", params={"all_options": all_options})

    def update_mbus_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Update M-Bus global configuration."""
        return self._client.request("PUT", "/mbus/global", json={"data": config})

    def mbus_groups_actions_test(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Test response of group."""
        return self._client.request(
            "POST", "/mbus/groups/actions/test", json=None if config is None else {"data": config}
        )

    def get_mbus_groups_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """List M-Bus groups."""
        return self._client.request("GET", "/mbus/groups/config", params={"all_options": all_options})

    def create_mbus_groups_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create M-Bus group."""
        return self._client.request("POST", "/mbus/groups/config", json={"data": config})

    def update_mbus_groups_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update M-Bus groups."""
        return self._client.request("PUT", "/mbus/groups/config", json={"data": config})

    def delete_mbus_groups_config(self, config: list[str]) -> dict[str, Any]:
        """Delete M-Bus groups."""
        return self._client.request("DELETE", "/mbus/groups/config", json={"data": config})

    def get_mbus_groups_config_by_id(self, group_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified M-Bus group."""
        return self._client.request("GET", f"/mbus/groups/config/{group_id}", params={"all_options": all_options})

    def update_mbus_groups_config_by_id(self, group_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update M-Bus group."""
        return self._client.request("PUT", f"/mbus/groups/config/{group_id}", json={"data": config})

    def delete_mbus_groups_config_by_id(self, group_id: str) -> dict[str, Any]:
        """Delete M-Bus group."""
        return self._client.request("DELETE", f"/mbus/groups/config/{group_id}")

    def get_mbus_groups_status_by_id(self, group_id: str) -> dict[str, Any]:
        """Returns the current value of specified M-Bus group."""
        return self._client.request("GET", f"/mbus/groups/status/{group_id}")

    def get_mbus_groups_values_config(self, group_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """List group values."""
        return self._client.request(
            "GET", f"/mbus/groups/{group_id}/values/config", params={"all_options": all_options}
        )

    def create_mbus_groups_values_config(self, group_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Create group value."""
        return self._client.request("POST", f"/mbus/groups/{group_id}/values/config", json={"data": config})

    def update_mbus_groups_values_config(self, group_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update group values."""
        return self._client.request("PUT", f"/mbus/groups/{group_id}/values/config", json={"data": config})

    def delete_mbus_groups_values_config(self, group_id: str, config: list[str]) -> dict[str, Any]:
        """Delete group values."""
        return self._client.request("DELETE", f"/mbus/groups/{group_id}/values/config", json={"data": config})

    def get_mbus_groups_values_config_by_id(
        self, group_id: str, value_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified group value."""
        return self._client.request(
            "GET", f"/mbus/groups/{group_id}/values/config/{value_id}", params={"all_options": all_options}
        )

    def update_mbus_groups_values_config_by_id(
        self, group_id: str, value_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Update group value."""
        return self._client.request("PUT", f"/mbus/groups/{group_id}/values/config/{value_id}", json={"data": config})

    def delete_mbus_groups_values_config_by_id(self, group_id: str, value_id: str) -> dict[str, Any]:
        """Delete group value."""
        return self._client.request("DELETE", f"/mbus/groups/{group_id}/values/config/{value_id}")

    def get_mbus_groups_values_status_by_id(self, group_id: str, value_id: str) -> dict[str, Any]:
        """Returns the specified current group value."""
        return self._client.request("GET", f"/mbus/groups/{group_id}/values/status/{value_id}")

    def get_mbus_records_config(self) -> dict[str, Any]:
        """List M-Bus Record configurations."""
        return self._client.request("GET", "/mbus/records/config")

    def create_mbus_records_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create M-Bus Record configuration."""
        return self._client.request("POST", "/mbus/records/config", json={"data": config})

    def update_mbus_records_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update M-Bus Record configurations."""
        return self._client.request("PUT", "/mbus/records/config", json={"data": config})

    def delete_mbus_records_config(self, config: list[str]) -> dict[str, Any]:
        """Delete M-Bus Record configurations."""
        return self._client.request("DELETE", "/mbus/records/config", json={"data": config})

    def get_mbus_records_config_by_id(self, record_id: str) -> dict[str, Any]:
        """Returns the specified M-Bus Record configuration."""
        return self._client.request("GET", f"/mbus/records/config/{record_id}")

    def update_mbus_records_config_by_id(self, record_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update M-Bus Record configuration."""
        return self._client.request("PUT", f"/mbus/records/config/{record_id}", json={"data": config})

    def delete_mbus_records_config_by_id(self, record_id: str) -> dict[str, Any]:
        """Delete M-Bus Record configuration."""
        return self._client.request("DELETE", f"/mbus/records/config/{record_id}")

    def mbus_records_requests_actions_request_test(
        self, record_id: str, config: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Test Configuration of M-Bus Request."""
        return self._client.request(
            "POST",
            f"/mbus/records/{record_id}/requests/actions/request_test",
            json=None if config is None else {"data": config},
        )

    def get_mbus_records_requests_config(self, record_id: str) -> dict[str, Any]:
        """List M-Bus Request configurations."""
        return self._client.request("GET", f"/mbus/records/{record_id}/requests/config")

    def create_mbus_records_requests_config(self, record_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Create M-Bus Request configuration."""
        return self._client.request("POST", f"/mbus/records/{record_id}/requests/config", json={"data": config})

    def update_mbus_records_requests_config(self, record_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update M-Bus Request configurations."""
        return self._client.request("PUT", f"/mbus/records/{record_id}/requests/config", json={"data": config})

    def delete_mbus_records_requests_config(self, record_id: str, config: list[str]) -> dict[str, Any]:
        """Delete M-Bus Request configurations."""
        return self._client.request("DELETE", f"/mbus/records/{record_id}/requests/config", json={"data": config})

    def get_mbus_records_requests_config_by_id(self, record_id: str, request_id: str) -> dict[str, Any]:
        """Returns the specified M-Bus Request configuration."""
        return self._client.request("GET", f"/mbus/records/{record_id}/requests/config/{request_id}")

    def update_mbus_records_requests_config_by_id(
        self, record_id: str, request_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Update M-Bus Request configuration."""
        return self._client.request(
            "PUT", f"/mbus/records/{record_id}/requests/config/{request_id}", json={"data": config}
        )

    def delete_mbus_records_requests_config_by_id(self, record_id: str, request_id: str) -> dict[str, Any]:
        """Delete M-Bus Request configuration."""
        return self._client.request("DELETE", f"/mbus/records/{record_id}/requests/config/{request_id}")

    def mbus_scan_actions_start_primary(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Start M-Bus primary scan."""
        return self._client.request(
            "POST", "/mbus/scan/actions/start_primary", json=None if config is None else {"data": config}
        )

    def mbus_scan_actions_start_secondary(self) -> dict[str, Any]:
        """Start M-Bus secondary scan."""
        return self._client.request("POST", "/mbus/scan/actions/start_secondary")

    def mbus_scan_actions_stop(self) -> dict[str, Any]:
        """Stop M-Bus primary or secondary scan."""
        return self._client.request("POST", "/mbus/scan/actions/stop")

    def get_mbus_scan_status(self) -> dict[str, Any]:
        """Get M-Bus global configuration."""
        return self._client.request("GET", "/mbus/scan/status")

    def get_mbus_status(self) -> dict[str, Any]:
        """Get M-Bus service status."""
        return self._client.request("GET", "/mbus/status")
