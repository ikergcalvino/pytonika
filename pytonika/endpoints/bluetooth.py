from typing import Any

from ._endpoint import Endpoint


class Bluetooth(Endpoint):
    def bluetooth_actions_pair(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Pair bluetooth devices."""
        return self._client.request(
            "POST", "/bluetooth/actions/pair", json=None if config is None else {"data": config}
        )

    def bluetooth_actions_scan(self) -> dict[str, Any]:
        """Start bluetooth scan."""
        return self._client.request("POST", "/bluetooth/actions/scan")

    def bluetooth_actions_unpair(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Unpair bluetooth devices."""
        return self._client.request(
            "POST", "/bluetooth/actions/unpair", json=None if config is None else {"data": config}
        )

    def get_bluetooth_autopair_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all bluetooth auto pair rule configurations."""
        return self._client.request("GET", "/bluetooth/autopair/config", params={"all_options": all_options})

    def create_bluetooth_autopair_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates auto pair rule configuration."""
        return self._client.request("POST", "/bluetooth/autopair/config", json={"data": config})

    def update_bluetooth_autopair_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified bluetooth auto pair rule configurations."""
        return self._client.request("PUT", "/bluetooth/autopair/config", json={"data": config})

    def delete_bluetooth_autopair_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified bluetooth auto pair rule configurations."""
        return self._client.request("DELETE", "/bluetooth/autopair/config", json={"data": config})

    def get_bluetooth_autopair_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified bluetooth auto pair rule configuration."""
        return self._client.request(
            "GET", f"/bluetooth/autopair/config/{config_id}", params={"all_options": all_options}
        )

    def update_bluetooth_autopair_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified bluetooth auto pair rule configuration."""
        return self._client.request("PUT", f"/bluetooth/autopair/config/{config_id}", json=config)

    def delete_bluetooth_autopair_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified bluetooth auto pair rule configuration."""
        return self._client.request("DELETE", f"/bluetooth/autopair/config/{config_id}")

    def get_bluetooth_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get bluetooth configurations."""
        return self._client.request("GET", "/bluetooth/config", params={"all_options": all_options})

    def update_bluetooth_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update bluetooth configurations."""
        return self._client.request("PUT", "/bluetooth/config", json={"data": config})

    def get_bluetooth_config_by_id(self, bluetooth_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get bluetooth configuration."""
        return self._client.request("GET", f"/bluetooth/config/{bluetooth_id}", params={"all_options": all_options})

    def update_bluetooth_config_by_id(self, bluetooth_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update bluetooth configuration."""
        return self._client.request("PUT", f"/bluetooth/config/{bluetooth_id}", json={"data": config})

    def get_bluetooth_database_entries_status(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        name: str | None = None,
        id: str | None = None,
        mac_address: str | None = None,
    ) -> dict[str, Any]:
        """List bluetooth database entries."""
        return self._client.request(
            "GET",
            "/bluetooth/database/entries/status",
            params={"limit": limit, "offset": offset, "name": name, "id": id, "mac_address": mac_address},
        )

    def get_bluetooth_paired_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get paired devices."""
        return self._client.request("GET", "/bluetooth/paired/config", params={"all_options": all_options})

    def update_bluetooth_paired_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update paired devices configurations."""
        return self._client.request("PUT", "/bluetooth/paired/config", json={"data": config})

    def get_bluetooth_paired_config_by_id(self, paired_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get paired device."""
        return self._client.request("GET", f"/bluetooth/paired/config/{paired_id}", params={"all_options": all_options})

    def update_bluetooth_paired_config_by_id(self, paired_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update paired device configuration."""
        return self._client.request("PUT", f"/bluetooth/paired/config/{paired_id}", json={"data": config})

    def get_bluetooth_result_status(self) -> dict[str, Any]:
        """Get bluetooth scanned devices."""
        return self._client.request("GET", "/bluetooth/result/status")

    def get_bluetooth_scanning_status(self) -> dict[str, Any]:
        """Get bluetooth current scan job status."""
        return self._client.request("GET", "/bluetooth/scanning/status")

    def get_bluetooth_status(self) -> dict[str, Any]:
        """Gets bluetooth service status."""
        return self._client.request("GET", "/bluetooth/status")
