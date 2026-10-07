from typing import Any

from ._endpoint import Endpoint, File


class OPCUA(Endpoint):
    def opcua_actions_test_group(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Test OPC UA Group."""
        return self._client.request("POST", "/opcua/actions/test_group", json=None if data is None else {"data": data})

    def opcua_actions_test_group_value(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Test OPC UA Group Value."""
        return self._client.request(
            "POST", "/opcua/actions/test_group_value", json=None if data is None else {"data": data}
        )

    def opcua_actions_test_server(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Test OPC UA Server."""
        return self._client.request("POST", "/opcua/actions/test_server", json=None if data is None else {"data": data})

    def opcua_actions_test_server_node(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Test OPC UA Server Node."""
        return self._client.request(
            "POST", "/opcua/actions/test_server_node", json=None if data is None else {"data": data}
        )

    def get_opcua_database_entries_status(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        id: str | None = None,
        group_name: str | None = None,
        group_id: str | None = None,
    ) -> dict[str, Any]:
        """Returns all OPC UA Client database entries."""
        return self._client.request(
            "GET",
            "/opcua/database/entries/status",
            params={"limit": limit, "offset": offset, "id": id, "group_name": group_name, "group_id": group_id},
        )

    def get_opcua_destination_server_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all OPC UA server configurations."""
        return self._client.request("GET", "/opcua/destination_server/config", params={"all_options": all_options})

    def update_opcua_destination_server_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OPC UA server configurations."""
        return self._client.request("PUT", "/opcua/destination_server/config", json={"data": config})

    def get_opcua_destination_server_config_by_id(
        self, server_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified OPC UA server configuration."""
        return self._client.request(
            "GET", f"/opcua/destination_server/config/{server_id}", params={"all_options": all_options}
        )

    def upload_opcua_destination_server_config_by_id(
        self, server_id: str, file: File, *, option: str | None = None
    ) -> dict[str, Any]:
        """Uploads the specified OPC UA server configuration certificate files."""
        return self._client.request(
            "POST", f"/opcua/destination_server/config/{server_id}", files={"file": file}, form={"option": option}
        )

    def update_opcua_destination_server_config_by_id(self, server_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified OPC UA server configuration."""
        return self._client.request("PUT", f"/opcua/destination_server/config/{server_id}", json={"data": config})

    def get_opcua_destination_server_nodes_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all OPC UA server node configurations."""
        return self._client.request(
            "GET", "/opcua/destination_server/nodes/config", params={"all_options": all_options}
        )

    def create_opcua_destination_server_nodes_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a OPC UA server node configuration. Data sources can be found using /universal_gateway/options
        endpoint.
        """
        return self._client.request("POST", "/opcua/destination_server/nodes/config", json={"data": config})

    def update_opcua_destination_server_nodes_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OPC UA server node configurations. Data sources can be found using
        /universal_gateway/options endpoint.
        """
        return self._client.request("PUT", "/opcua/destination_server/nodes/config", json={"data": config})

    def delete_opcua_destination_server_nodes_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified OPC UA server node configurations."""
        return self._client.request("DELETE", "/opcua/destination_server/nodes/config", json={"data": config})

    def get_opcua_destination_server_nodes_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified OPC UA server node configuration."""
        return self._client.request(
            "GET", f"/opcua/destination_server/nodes/config/{config_id}", params={"all_options": all_options}
        )

    def update_opcua_destination_server_nodes_config_by_id(
        self, config_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified OPC UA server node configuration. Data sources can be found using
        /universal_gateway/options endpoint.
        """
        return self._client.request("PUT", f"/opcua/destination_server/nodes/config/{config_id}", json={"data": config})

    def delete_opcua_destination_server_nodes_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified OPC UA server node configuration."""
        return self._client.request("DELETE", f"/opcua/destination_server/nodes/config/{config_id}")

    def get_opcua_destination_server_status(self) -> dict[str, Any]:
        """Returns OPC UA server status."""
        return self._client.request("GET", "/opcua/destination_server/status")

    def get_opcua_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all OPC UA Client Global Settings configurations."""
        return self._client.request("GET", "/opcua/global", params={"all_options": all_options})

    def update_opcua_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified OPC UA Client Global Settings configurations."""
        return self._client.request("PUT", "/opcua/global", json={"data": config})

    def opcua_group_actions_test(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Test OPC UA Value Group."""
        return self._client.request("POST", "/opcua/group/actions/test", json=None if data is None else {"data": data})

    def get_opcua_group_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all OPC UA Value Group configurations."""
        return self._client.request("GET", "/opcua/group/config", params={"all_options": all_options})

    def create_opcua_group_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates OPC UA Value Group configuration."""
        return self._client.request("POST", "/opcua/group/config", json={"data": config})

    def update_opcua_group_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OPC UA Value Group configurations."""
        return self._client.request("PUT", "/opcua/group/config", json={"data": config})

    def delete_opcua_group_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified OPC UA Value Group configurations."""
        return self._client.request("DELETE", "/opcua/group/config", json={"data": config})

    def get_opcua_group_config_by_id(self, group_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified OPC UA Value Group configuration."""
        return self._client.request("GET", f"/opcua/group/config/{group_id}", params={"all_options": all_options})

    def update_opcua_group_config_by_id(self, group_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified OPC UA Value Group configuration."""
        return self._client.request("PUT", f"/opcua/group/config/{group_id}", json={"data": config})

    def delete_opcua_group_config_by_id(self, group_id: str) -> dict[str, Any]:
        """Deletes the specified OPC UA Value Group configuration."""
        return self._client.request("DELETE", f"/opcua/group/config/{group_id}")

    def get_opcua_group_status(self) -> dict[str, Any]:
        """Returns OPC UA Value Group status."""
        return self._client.request("GET", "/opcua/group/status")

    def get_opcua_group_status_by_id(self, group_id: str) -> dict[str, Any]:
        """Returns the specified OPC UA Value Group configuration."""
        return self._client.request("GET", f"/opcua/group/status/{group_id}")

    def opcua_group_values_actions_test(self, group_id: str, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Test OPC UA Value."""
        return self._client.request(
            "POST", f"/opcua/group/{group_id}/values/actions/test", json=None if data is None else {"data": data}
        )

    def get_opcua_group_values_config(self, group_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all OPC UA Value configurations."""
        return self._client.request(
            "GET", f"/opcua/group/{group_id}/values/config", params={"all_options": all_options}
        )

    def create_opcua_group_values_config(self, group_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates OPC UA Value configuration."""
        return self._client.request("POST", f"/opcua/group/{group_id}/values/config", json={"data": config})

    def update_opcua_group_values_config(self, group_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OPC UA Value configurations."""
        return self._client.request("PUT", f"/opcua/group/{group_id}/values/config", json={"data": config})

    def delete_opcua_group_values_config(self, group_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes specified OPC UA Value configurations."""
        return self._client.request("DELETE", f"/opcua/group/{group_id}/values/config", json={"data": config})

    def get_opcua_group_values_config_by_id(
        self, group_id: str, value_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified OPC UA Value configuration."""
        return self._client.request(
            "GET", f"/opcua/group/{group_id}/values/config/{value_id}", params={"all_options": all_options}
        )

    def update_opcua_group_values_config_by_id(
        self, group_id: str, value_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified OPC UA Value configuration."""
        return self._client.request("PUT", f"/opcua/group/{group_id}/values/config/{value_id}", json={"data": config})

    def delete_opcua_group_values_config_by_id(self, group_id: str, value_id: str) -> dict[str, Any]:
        """Deletes the specified OPC UA Value configuration."""
        return self._client.request("DELETE", f"/opcua/group/{group_id}/values/config/{value_id}")

    def get_opcua_group_values_status_by_id(self, group_id: str, value_id: str) -> dict[str, Any]:
        """Returns the specified OPC UA Value configuration."""
        return self._client.request("GET", f"/opcua/group/{group_id}/values/status/{value_id}")

    def opcua_server_actions_test(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Test OPC UA Server."""
        return self._client.request("POST", "/opcua/server/actions/test", json=None if data is None else {"data": data})

    def get_opcua_server_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all OPC UA Server configurations."""
        return self._client.request("GET", "/opcua/server/config", params={"all_options": all_options})

    def create_opcua_server_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates OPC UA Server configuration."""
        return self._client.request("POST", "/opcua/server/config", json={"data": config})

    def update_opcua_server_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OPC UA Server configurations."""
        return self._client.request("PUT", "/opcua/server/config", json={"data": config})

    def delete_opcua_server_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified OPC UA Server configurations."""
        return self._client.request("DELETE", "/opcua/server/config", json={"data": config})

    def get_opcua_server_config_by_id(self, server_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified OPC UA Server configuration."""
        return self._client.request("GET", f"/opcua/server/config/{server_id}", params={"all_options": all_options})

    def upload_opcua_server_config_by_id(
        self, server_id: str, file: File, *, option: str | None = None
    ) -> dict[str, Any]:
        """Uploads the specified OPC UA Server configuration certificate files."""
        return self._client.request(
            "POST", f"/opcua/server/config/{server_id}", files={"file": file}, form={"option": option}
        )

    def update_opcua_server_config_by_id(self, server_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified OPC UA Server configuration."""
        return self._client.request("PUT", f"/opcua/server/config/{server_id}", json={"data": config})

    def delete_opcua_server_config_by_id(self, server_id: str) -> dict[str, Any]:
        """Deletes the specified OPC UA Server configuration."""
        return self._client.request("DELETE", f"/opcua/server/config/{server_id}")

    def get_opcua_server_status(self) -> dict[str, Any]:
        """Returns OPC UA Server status."""
        return self._client.request("GET", "/opcua/server/status")

    def opcua_server_nodes_actions_test(self, server_id: str, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Test OPC UA Server Node."""
        return self._client.request(
            "POST", f"/opcua/server/{server_id}/nodes/actions/test", json=None if data is None else {"data": data}
        )

    def get_opcua_server_nodes_config(self, server_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all OPC UA Server Node configurations."""
        return self._client.request(
            "GET", f"/opcua/server/{server_id}/nodes/config", params={"all_options": all_options}
        )

    def create_opcua_server_nodes_config(self, server_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates OPC UA Server Node configuration."""
        return self._client.request("POST", f"/opcua/server/{server_id}/nodes/config", json={"data": config})

    def update_opcua_server_nodes_config(self, server_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OPC UA Server Node configurations."""
        return self._client.request("PUT", f"/opcua/server/{server_id}/nodes/config", json={"data": config})

    def delete_opcua_server_nodes_config(self, server_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes specified OPC UA Server Node configurations."""
        return self._client.request("DELETE", f"/opcua/server/{server_id}/nodes/config", json={"data": config})

    def get_opcua_server_nodes_config_by_id(
        self, server_id: str, node_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified OPC UA Server Node configuration."""
        return self._client.request(
            "GET", f"/opcua/server/{server_id}/nodes/config/{node_id}", params={"all_options": all_options}
        )

    def update_opcua_server_nodes_config_by_id(
        self, server_id: str, node_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified OPC UA Server Node configuration."""
        return self._client.request("PUT", f"/opcua/server/{server_id}/nodes/config/{node_id}", json={"data": config})

    def delete_opcua_server_nodes_config_by_id(self, server_id: str, node_id: str) -> dict[str, Any]:
        """Deletes the specified OPC UA Server Node configuration."""
        return self._client.request("DELETE", f"/opcua/server/{server_id}/nodes/config/{node_id}")

    def get_opcua_server_nodes_status_by_id(self, server_id: str, node_id: str) -> dict[str, Any]:
        """Returns the specified OPC UA Server Node configuration."""
        return self._client.request("GET", f"/opcua/server/{server_id}/nodes/status/{node_id}")
