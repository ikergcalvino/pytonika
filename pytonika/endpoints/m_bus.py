from typing import Any

from ._base import Endpoint


class MBus(Endpoint):
    def get_mbus_client_config_by_id(self, client_id: str) -> dict[str, Any]:
        """Returns the specified M-Bus Client configuration.

        .. deprecated::
        """
        endpoint = f"/mbus/client/config/{client_id}"

        return self._api_client.get(endpoint)

    def update_mbus_client_config_by_id(self, client_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update M-Bus Client configuration.

        .. deprecated::
        """
        endpoint = f"/mbus/client/config/{client_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_mbus_client_config_by_id(self, client_id: str) -> dict[str, Any]:
        """Delete M-Bus Client configuration.

        .. deprecated::
        """
        endpoint = f"/mbus/client/config/{client_id}"

        return self._api_client.delete(endpoint)

    def get_mbus_client_config(self) -> dict[str, Any]:
        """List M-Bus Client configurations.

        .. deprecated::
        """
        endpoint = "/mbus/client/config"

        return self._api_client.get(endpoint)

    def create_mbus_client_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create M-Bus Client configuration.

        .. deprecated::
        """
        endpoint = "/mbus/client/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_mbus_client_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update M-Bus Client configurations.

        .. deprecated::
        """
        endpoint = "/mbus/client/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_mbus_client_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete M-Bus Client configurations."""
        return [self.delete_mbus_client_config_by_id(client_id) for client_id in config]

    def mbus_scan_actions_start_secondary(self) -> dict[str, Any]:
        """Start M-Bus secondary scan."""
        endpoint = "/mbus/scan/actions/start_secondary"

        return self._api_client.post(endpoint)

    def mbus_scan_actions_stop(self) -> dict[str, Any]:
        """Stop M-Bus primary or secondary scan."""
        endpoint = "/mbus/scan/actions/stop"

        return self._api_client.post(endpoint)

    def mbus_scan_actions_start_primary(self, config: dict[str, Any]) -> dict[str, Any]:
        """Start M-Bus primary scan."""
        endpoint = "/mbus/scan/actions/start_primary"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def get_mbus_scan_status(self) -> dict[str, Any]:
        """Get M-Bus global configuration."""
        endpoint = "/mbus/scan/status"

        return self._api_client.get(endpoint)

    def get_mbus_found_devices_status(self) -> dict[str, Any]:
        """Get M-Bus devices found during scanning process."""
        endpoint = "/mbus/found_devices/status"

        return self._api_client.get(endpoint)

    def get_mbus_records_config(self) -> dict[str, Any]:
        """List M-Bus Record configurations.

        .. deprecated::
        """
        endpoint = "/mbus/records/config"

        return self._api_client.get(endpoint)

    def create_mbus_records_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create M-Bus Record configuration.

        .. deprecated::
        """
        endpoint = "/mbus/records/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_mbus_records_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update M-Bus Record configurations.

        .. deprecated::
        """
        endpoint = "/mbus/records/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_mbus_records_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete M-Bus Record configurations."""
        return [self.delete_mbus_records_config_by_id(record_id) for record_id in config]

    def get_mbus_records_config_by_id(self, record_id: str) -> dict[str, Any]:
        """Returns the specified M-Bus Record configuration.

        .. deprecated::
        """
        endpoint = f"/mbus/records/config/{record_id}"

        return self._api_client.get(endpoint)

    def update_mbus_records_config_by_id(self, record_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update M-Bus Record configuration.

        .. deprecated::
        """
        endpoint = f"/mbus/records/config/{record_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_mbus_records_config_by_id(self, record_id: str) -> dict[str, Any]:
        """Delete M-Bus Record configuration.

        .. deprecated::
        """
        endpoint = f"/mbus/records/config/{record_id}"

        return self._api_client.delete(endpoint)

    def mbus_devices_actions_update_address_by_id(self, device_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the primary address of saved M-Bus device."""
        endpoint = f"/mbus/devices/{device_id}/actions/update_address"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def mbus_devices_actions_test(self, config: dict[str, Any]) -> dict[str, Any]:
        """Send a test request to M-Bus device."""
        endpoint = "/mbus/devices/actions/test"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def mbus_devices_actions_reset(self, config: dict[str, Any]) -> dict[str, Any]:
        """Send reset request to M-Bus device."""
        endpoint = "/mbus/devices/actions/reset"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def get_mbus_devices_config_by_id(self, device_id: str) -> dict[str, Any]:
        """Returns the specified M-Bus device."""
        endpoint = f"/mbus/devices/config/{device_id}"

        return self._api_client.get(endpoint)

    def update_mbus_devices_config_by_id(self, device_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update M-Bus device."""
        endpoint = f"/mbus/devices/config/{device_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_mbus_devices_config_by_id(self, device_id: str) -> dict[str, Any]:
        """Delete M-Bus device."""
        endpoint = f"/mbus/devices/config/{device_id}"

        return self._api_client.delete(endpoint)

    def mbus_devices_actions_update_baudrate(self, config: dict[str, Any]) -> dict[str, Any]:
        """Update baudrate of M-Bus device."""
        endpoint = "/mbus/devices/actions/update_baudrate"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def mbus_devices_actions_get_info(self, config: dict[str, Any]) -> dict[str, Any]:
        """Get manufacturer information from M-Bus device."""
        endpoint = "/mbus/devices/actions/get_info"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def get_mbus_devices_config(self) -> dict[str, Any]:
        """List M-Bus devices."""
        endpoint = "/mbus/devices/config"

        return self._api_client.get(endpoint)

    def create_mbus_devices_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create M-Bus device."""
        endpoint = "/mbus/devices/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_mbus_devices_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update M-Bus devices."""
        endpoint = "/mbus/devices/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_mbus_devices_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete M-Bus devices."""
        return [self.delete_mbus_devices_config_by_id(device_id) for device_id in config]

    def mbus_devices_actions_ping(self, config: dict[str, Any]) -> dict[str, Any]:
        """Test if M-Bus device is reachable."""
        endpoint = "/mbus/devices/actions/ping"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def mbus_devices_actions_update_address(self, config: dict[str, Any]) -> dict[str, Any]:
        """Update primary address of M-Bus device."""
        endpoint = "/mbus/devices/actions/update_address"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def get_mbus_global(self) -> dict[str, Any]:
        """Get M-Bus global configuration."""
        endpoint = "/mbus/global"

        return self._api_client.get(endpoint)

    def update_mbus_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Update M-Bus global configuration."""
        endpoint = "/mbus/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_mbus_database_entries_status(self) -> dict[str, Any]:
        """Returns all M-Bus database entries."""
        endpoint = "/mbus/database/entries/status"

        return self._api_client.get(endpoint)

    def get_mbus_status(self) -> dict[str, Any]:
        """Get M-Bus service status."""
        endpoint = "/mbus/status"

        return self._api_client.get(endpoint)

    def get_mbus_groups_values_config(self, group_id: str) -> dict[str, Any]:
        """List group values."""
        endpoint = f"/mbus/groups/{group_id}/values/config"

        return self._api_client.get(endpoint)

    def create_mbus_groups_values_config(self, group_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Create group value."""
        endpoint = f"/mbus/groups/{group_id}/values/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_mbus_groups_values_config(self, group_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update group values."""
        endpoint = f"/mbus/groups/{group_id}/values/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_mbus_groups_values_config(self, group_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Delete group values."""
        return [self.delete_mbus_groups_values_config_by_id(group_id, value_id) for value_id in config]

    def get_mbus_groups_values_config_by_id(self, group_id: str, value_id: str) -> dict[str, Any]:
        """Returns the specified group value."""
        endpoint = f"/mbus/groups/{group_id}/values/config/{value_id}"

        return self._api_client.get(endpoint)

    def update_mbus_groups_values_config_by_id(
        self, group_id: str, value_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Update group value."""
        endpoint = f"/mbus/groups/{group_id}/values/config/{value_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_mbus_groups_values_config_by_id(self, group_id: str, value_id: str) -> dict[str, Any]:
        """Delete group value."""
        endpoint = f"/mbus/groups/{group_id}/values/config/{value_id}"

        return self._api_client.delete(endpoint)

    def get_mbus_groups_values_status_by_id(self, group_id: str, value_id: str) -> dict[str, Any]:
        """Returns the specified current group value."""
        endpoint = f"/mbus/groups/{group_id}/values/status/{value_id}"

        return self._api_client.get(endpoint)

    def get_mbus_groups_config(self) -> dict[str, Any]:
        """List M-Bus groups."""
        endpoint = "/mbus/groups/config"

        return self._api_client.get(endpoint)

    def create_mbus_groups_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create M-Bus group."""
        endpoint = "/mbus/groups/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_mbus_groups_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update M-Bus groups."""
        endpoint = "/mbus/groups/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_mbus_groups_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete M-Bus groups."""
        return [self.delete_mbus_groups_config_by_id(group_id) for group_id in config]

    def get_mbus_groups_config_by_id(self, group_id: str) -> dict[str, Any]:
        """Returns the specified M-Bus group."""
        endpoint = f"/mbus/groups/config/{group_id}"

        return self._api_client.get(endpoint)

    def update_mbus_groups_config_by_id(self, group_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update M-Bus group."""
        endpoint = f"/mbus/groups/config/{group_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_mbus_groups_config_by_id(self, group_id: str) -> dict[str, Any]:
        """Delete M-Bus group."""
        endpoint = f"/mbus/groups/config/{group_id}"

        return self._api_client.delete(endpoint)

    def mbus_groups_actions_test(self, config: dict[str, Any]) -> dict[str, Any]:
        """Test response of group."""
        endpoint = "/mbus/groups/actions/test"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def get_mbus_groups_status_by_id(self, group_id: str) -> dict[str, Any]:
        """Returns the current value of specified M-Bus group."""
        endpoint = f"/mbus/groups/status/{group_id}"

        return self._api_client.get(endpoint)

    def mbus_records_requests_actions_request_test(self, record_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Test Configuration of M-Bus Request.

        .. deprecated::
        """
        endpoint = f"/mbus/records/{record_id}/requests/actions/request_test"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def get_mbus_records_requests_config(self, record_id: str) -> dict[str, Any]:
        """List M-Bus Request configurations.

        .. deprecated::
        """
        endpoint = f"/mbus/records/{record_id}/requests/config"

        return self._api_client.get(endpoint)

    def create_mbus_records_requests_config(self, record_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Create M-Bus Request configuration.

        .. deprecated::
        """
        endpoint = f"/mbus/records/{record_id}/requests/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_mbus_records_requests_config(self, record_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update M-Bus Request configurations.

        .. deprecated::
        """
        endpoint = f"/mbus/records/{record_id}/requests/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_mbus_records_requests_config(self, record_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Delete M-Bus Request configurations."""
        return [self.delete_mbus_records_requests_config_by_id(record_id, request_id) for request_id in config]

    def get_mbus_records_requests_config_by_id(self, record_id: str, request_id: str) -> dict[str, Any]:
        """Returns the specified M-Bus Request configuration.

        .. deprecated::
        """
        endpoint = f"/mbus/records/{record_id}/requests/config/{request_id}"

        return self._api_client.get(endpoint)

    def update_mbus_records_requests_config_by_id(
        self, record_id: str, request_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Update M-Bus Request configuration.

        .. deprecated::
        """
        endpoint = f"/mbus/records/{record_id}/requests/config/{request_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_mbus_records_requests_config_by_id(self, record_id: str, request_id: str) -> dict[str, Any]:
        """Delete M-Bus Request configuration.

        .. deprecated::
        """
        endpoint = f"/mbus/records/{record_id}/requests/config/{request_id}"

        return self._api_client.delete(endpoint)
