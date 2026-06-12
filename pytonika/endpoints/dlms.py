from typing import Any

from ._base import Endpoint


class DLMS(Endpoint):
    def dlms_scan_actions_start(self, data: dict[str, Any]) -> dict[str, Any]:
        """Starts DLMS scan."""
        endpoint = "/dlms/scan/actions/start"

        return self._api_client.post(endpoint, data={"data": data})

    def dlms_scan_actions_stop(self, data: dict[str, Any]) -> dict[str, Any]:
        """Stops DLMS scan."""
        endpoint = "/dlms/scan/actions/stop"

        return self._api_client.post(endpoint, data={"data": data})

    def get_dlms_scan_status(self) -> dict[str, Any]:
        """Returns DLMS scan status."""
        endpoint = "/dlms/scan/status"

        return self._api_client.get(endpoint)

    def get_dlms_found_parameters_status(self) -> dict[str, Any]:
        """Returns DLMS scan results."""
        endpoint = "/dlms/found_parameters/status"

        return self._api_client.get(endpoint)

    def get_dlms_cosem_group_config(self) -> dict[str, Any]:
        """Returns all COSEM group configurations."""
        endpoint = "/dlms/cosem_group/config"

        return self._api_client.get(endpoint)

    def create_dlms_cosem_group_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates COSEM group configuration."""
        endpoint = "/dlms/cosem_group/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_dlms_cosem_group_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified COSEM group configurations."""
        endpoint = "/dlms/cosem_group/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dlms_cosem_group_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified COSEM group configurations."""
        return [self.delete_dlms_cosem_group_config_by_id(group_id) for group_id in config]

    def get_dlms_cosem_group_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified COSEM group configuration."""
        endpoint = f"/dlms/cosem_group/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_dlms_cosem_group_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified COSEM group configuration."""
        endpoint = f"/dlms/cosem_group/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dlms_cosem_group_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified COSEM group configuration."""
        endpoint = f"/dlms/cosem_group/config/{config_id}"

        return self._api_client.delete(endpoint)

    def dlms_cosem_group_actions_test(self, data: dict[str, Any]) -> dict[str, Any]:
        """Test COSEM group configuration."""
        endpoint = "/dlms/cosem_group/actions/test"

        return self._api_client.post(endpoint, data={"data": data})

    def get_dlms_cosem_group_status(self) -> dict[str, Any]:
        """Returns DLMS status."""
        endpoint = "/dlms/cosem_group/status"

        return self._api_client.get(endpoint)

    def get_dlms_cosem_group_status_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns cosem group current value."""
        endpoint = f"/dlms/cosem_group/status/{config_id}"

        return self._api_client.get(endpoint)

    def get_dlms_global(self) -> dict[str, Any]:
        """Returns all DLMS global settings configurations."""
        endpoint = "/dlms/global"

        return self._api_client.get(endpoint)

    def update_dlms_global(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified DLMS global settings configurations."""
        endpoint = "/dlms/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_dlms_database_entries_status(self) -> dict[str, Any]:
        """Returns all DLMS database entries."""
        endpoint = "/dlms/database/entries/status"

        return self._api_client.get(endpoint)

    def get_dlms_cosem_config(self, cosem_group_id: str) -> dict[str, Any]:
        """Returns all DLMS COSEM configurations."""
        endpoint = f"/dlms/cosem_group/{cosem_group_id}/cosem/config"

        return self._api_client.get(endpoint)

    def create_dlms_cosem_config(self, cosem_group_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates DLMS COSEM configuration."""
        endpoint = f"/dlms/cosem_group/{cosem_group_id}/cosem/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_dlms_cosem_config(self, cosem_group_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified DLMS COSEM configurations."""
        endpoint = f"/dlms/cosem_group/{cosem_group_id}/cosem/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dlms_cosem_config(self, cosem_group_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified DLMS COSEM configurations."""
        return [self.delete_dlms_cosem_config_by_id(cosem_group_id, cosem_id) for cosem_id in config]

    def get_dlms_cosem_config_by_id(self, cosem_group_id: str, cosem_id: str) -> dict[str, Any]:
        """Returns the specified DLMS COSEM configuration."""
        endpoint = f"/dlms/cosem_group/{cosem_group_id}/cosem/config/{cosem_id}"

        return self._api_client.get(endpoint)

    def update_dlms_cosem_config_by_id(
        self, cosem_group_id: str, cosem_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified DLMS COSEM configuration."""
        endpoint = f"/dlms/cosem_group/{cosem_group_id}/cosem/config/{cosem_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dlms_cosem_config_by_id(self, cosem_group_id: str, cosem_id: str) -> dict[str, Any]:
        """Deletes the specified DLMS COSEM configuration."""
        endpoint = f"/dlms/cosem_group/{cosem_group_id}/cosem/config/{cosem_id}"

        return self._api_client.delete(endpoint)

    def get_dlms_cosem_status_by_id(self, cosem_group_id: str, cosem_id: str) -> dict[str, Any]:
        """Returns the specified DLMS COSEM configuration."""
        endpoint = f"/dlms/cosem_group/{cosem_group_id}/cosem/status/{cosem_id}"

        return self._api_client.get(endpoint)

    def get_dlms_devices_config(self) -> dict[str, Any]:
        """Returns all Devices configurations."""
        endpoint = "/dlms/devices/config"

        return self._api_client.get(endpoint)

    def create_dlms_devices_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Devices configuration."""
        endpoint = "/dlms/devices/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_dlms_devices_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Devices configurations."""
        endpoint = "/dlms/devices/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dlms_devices_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Devices configurations."""
        return [self.delete_dlms_devices_config_by_id(device_id) for device_id in config]

    def get_dlms_devices_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified Devices configuration."""
        endpoint = f"/dlms/devices/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_dlms_devices_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Devices configuration."""
        endpoint = f"/dlms/devices/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dlms_devices_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Devices configuration."""
        endpoint = f"/dlms/devices/config/{config_id}"

        return self._api_client.delete(endpoint)

    def dlms_devices_actions_test(self, data: dict[str, Any]) -> dict[str, Any]:
        """Test DLMS physDevices configuration."""
        endpoint = "/dlms/devices/actions/test"

        return self._api_client.post(endpoint, data={"data": data})

    def get_dlms_connections_config(self) -> dict[str, Any]:
        """Returns all Connections configurations."""
        endpoint = "/dlms/connections/config"

        return self._api_client.get(endpoint)

    def create_dlms_connections_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Connections configuration."""
        endpoint = "/dlms/connections/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_dlms_connections_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Connections configurations."""
        endpoint = "/dlms/connections/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dlms_connections_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Connections configurations."""
        return [self.delete_dlms_connections_config_by_id(conn_id) for conn_id in config]

    def get_dlms_connections_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified Connections configuration."""
        endpoint = f"/dlms/connections/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_dlms_connections_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Connections configuration."""
        endpoint = f"/dlms/connections/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dlms_connections_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Connections configuration."""
        endpoint = f"/dlms/connections/config/{config_id}"

        return self._api_client.delete(endpoint)
