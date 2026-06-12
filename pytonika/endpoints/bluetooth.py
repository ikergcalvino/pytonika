from typing import Any

from ._base import Endpoint


class Bluetooth(Endpoint):
    def get_bluetooth_config(self) -> dict[str, Any]:
        """Get bluetooth configurations."""
        endpoint = "/bluetooth/config"

        return self._api_client.get(endpoint)

    def update_bluetooth_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update bluetooth configurations."""
        endpoint = "/bluetooth/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_bluetooth_config_by_id(self, bluetooth_id: str) -> dict[str, Any]:
        """Get bluetooth configuration."""
        endpoint = f"/bluetooth/config/{bluetooth_id}"

        return self._api_client.get(endpoint)

    def update_bluetooth_config_by_id(self, bluetooth_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update bluetooth configuration."""
        endpoint = f"/bluetooth/config/{bluetooth_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def bluetooth_actions_scan(self) -> dict[str, Any]:
        """Start bluetooth scan."""
        endpoint = "/bluetooth/actions/scan"

        return self._api_client.post(endpoint)

    def get_bluetooth_scanning_status(self) -> dict[str, Any]:
        """Get bluetooth current scan job status."""
        endpoint = "/bluetooth/scanning/status"

        return self._api_client.get(endpoint)

    def get_bluetooth_result_status(self) -> dict[str, Any]:
        """Get bluetooth scanned devices."""
        endpoint = "/bluetooth/result/status"

        return self._api_client.get(endpoint)

    def bluetooth_actions_pair(self, config: dict[str, Any]) -> dict[str, Any]:
        """Pair bluetooth devices."""
        endpoint = "/bluetooth/actions/pair"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def bluetooth_actions_unpair(self, config: dict[str, Any]) -> dict[str, Any]:
        """Unpair bluetooth devices."""
        endpoint = "/bluetooth/actions/unpair"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def get_bluetooth_paired_config(self) -> dict[str, Any]:
        """Get paired devices."""
        endpoint = "/bluetooth/paired/config"

        return self._api_client.get(endpoint)

    def update_bluetooth_paired_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update paired devices configurations."""
        endpoint = "/bluetooth/paired/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_bluetooth_paired_config_by_id(self, paired_id: str) -> dict[str, Any]:
        """Get paired device."""
        endpoint = f"/bluetooth/paired/config/{paired_id}"

        return self._api_client.get(endpoint)

    def update_bluetooth_paired_config_by_id(self, paired_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update paired device configuration."""
        endpoint = f"/bluetooth/paired/config/{paired_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_bluetooth_status(self) -> dict[str, Any]:
        """Gets bluetooth service status."""
        endpoint = "/bluetooth/status"

        return self._api_client.get(endpoint)

    def get_bluetooth_database_entries_status(self) -> dict[str, Any]:
        """List bluetooth database entries."""
        endpoint = "/bluetooth/database/entries/status"

        return self._api_client.get(endpoint)
