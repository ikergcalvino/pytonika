from typing import Any

from ._endpoint import Endpoint


class CANopenSDOClient(Endpoint):
    def canopen_client_actions_test_group(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Test CANopen SDO Client Value Group."""
        return self._client.request(
            "POST", "/canopen/client/actions/test_group", json=None if data is None else {"data": data}
        )

    def canopen_client_actions_test_group_value(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Test CANopen SDO Client value configuration."""
        return self._client.request(
            "POST", "/canopen/client/actions/test_group_value", json=None if data is None else {"data": data}
        )

    def get_canopen_client_database_entries_status(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        id: int | None = None,
        group_name: str | None = None,
    ) -> dict[str, Any]:
        """Returns CANopen SDO Client database entries."""
        return self._client.request(
            "GET",
            "/canopen/client/database/entries/status",
            params={"limit": limit, "offset": offset, "id": id, "group_name": group_name},
        )

    def get_canopen_client_global(self) -> dict[str, Any]:
        """Returns CANopen SDO Client global configuration."""
        return self._client.request("GET", "/canopen/client/global")

    def update_canopen_client_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates CANopen SDO Client global configuration."""
        return self._client.request("PUT", "/canopen/client/global", json={"data": config})

    def get_canopen_client_groups_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all CANopen SDO Client Value Group configurations."""
        return self._client.request("GET", "/canopen/client/groups/config", params={"all_options": all_options})

    def create_canopen_client_groups_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates CANopen SDO Client Value Group configuration."""
        return self._client.request("POST", "/canopen/client/groups/config", json={"data": config})

    def update_canopen_client_groups_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified CANopen SDO Client Value Group configurations."""
        return self._client.request("PUT", "/canopen/client/groups/config", json={"data": config})

    def delete_canopen_client_groups_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified CANopen SDO Client Value Group configurations."""
        return self._client.request("DELETE", "/canopen/client/groups/config", json={"data": config})

    def get_canopen_client_groups_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified CANopen SDO Client Value Group configuration."""
        return self._client.request(
            "GET", f"/canopen/client/groups/config/{config_id}", params={"all_options": all_options}
        )

    def update_canopen_client_groups_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified CANopen SDO Client Value Group configuration."""
        return self._client.request("PUT", f"/canopen/client/groups/config/{config_id}", json={"data": config})

    def delete_canopen_client_groups_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified CANopen SDO Client Value Group configuration."""
        return self._client.request("DELETE", f"/canopen/client/groups/config/{config_id}")

    def get_canopen_client_groups_values_config(
        self, groups_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns all CANopen SDO Client Value configurations."""
        return self._client.request(
            "GET", f"/canopen/client/groups/{groups_id}/values/config", params={"all_options": all_options}
        )

    def create_canopen_client_groups_values_config(self, groups_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates CANopen SDO Client Value configuration."""
        return self._client.request("POST", f"/canopen/client/groups/{groups_id}/values/config", json={"data": config})

    def update_canopen_client_groups_values_config(
        self, groups_id: str, config: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """Updates specified CANopen SDO Client Value configurations."""
        return self._client.request("PUT", f"/canopen/client/groups/{groups_id}/values/config", json={"data": config})

    def delete_canopen_client_groups_values_config(self, groups_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes specified CANopen SDO Client Value configurations."""
        return self._client.request(
            "DELETE", f"/canopen/client/groups/{groups_id}/values/config", json={"data": config}
        )

    def get_canopen_client_groups_values_config_by_id(
        self, groups_id: str, value_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified CANopen SDO Client Value configuration."""
        return self._client.request(
            "GET", f"/canopen/client/groups/{groups_id}/values/config/{value_id}", params={"all_options": all_options}
        )

    def update_canopen_client_groups_values_config_by_id(
        self, groups_id: str, value_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified CANopen SDO Client Value configuration."""
        return self._client.request(
            "PUT", f"/canopen/client/groups/{groups_id}/values/config/{value_id}", json={"data": config}
        )

    def delete_canopen_client_groups_values_config_by_id(self, groups_id: str, value_id: str) -> dict[str, Any]:
        """Deletes the specified CANopen SDO Client value configuration."""
        return self._client.request("DELETE", f"/canopen/client/groups/{groups_id}/values/config/{value_id}")

    def get_canopen_client_status(self) -> dict[str, Any]:
        """Returns CANopen SDO Client service status."""
        return self._client.request("GET", "/canopen/client/status")
