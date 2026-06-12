from typing import Any

from ._base import Endpoint


class OPCUA(Endpoint):
    def get_opcua_destination_server_config(self) -> dict[str, Any]:
        """Returns all OPC UA server configurations."""
        endpoint = "/opcua/destination_server/config"

        return self._api_client.get(endpoint)

    def update_opcua_destination_server_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OPC UA server configurations."""
        endpoint = "/opcua/destination_server/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_opcua_destination_server_config_by_id(self, server_id: str) -> dict[str, Any]:
        """Returns the specified OPC UA server configuration."""
        endpoint = f"/opcua/destination_server/config/{server_id}"

        return self._api_client.get(endpoint)

    def upload_opcua_destination_server_config_by_id(self, server_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads the specified OPC UA server configuration certificate files."""
        endpoint = f"/opcua/destination_server/config/{server_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_opcua_destination_server_config_by_id(self, server_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified OPC UA server configuration."""
        endpoint = f"/opcua/destination_server/config/{server_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_opcua_destination_server_status(self) -> dict[str, Any]:
        """Returns OPC UA server status."""
        endpoint = "/opcua/destination_server/status"

        return self._api_client.get(endpoint)

    def upload_opcua_server_config_certificates(self, server_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads the specified OPC UA Server configuration certificate files."""
        endpoint = f"/opcua/server/config/{server_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def get_opcua_global(self) -> dict[str, Any]:
        """Returns all OPC UA Client Global Settings configurations."""
        endpoint = "/opcua/global"

        return self._api_client.get(endpoint)

    def update_opcua_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified OPC UA Client Global Settings configurations."""
        endpoint = "/opcua/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_opcua_database_entries_status(self) -> dict[str, Any]:
        """Returns all OPC UA Client database entries."""
        endpoint = "/opcua/database/entries/status"

        return self._api_client.get(endpoint)

    def opcua_actions_test_server(self, data: dict[str, Any]) -> dict[str, Any]:
        """Test OPC UA Server."""
        endpoint = "/opcua/actions/test_server"

        return self._api_client.post(endpoint, data={"data": data})

    def opcua_actions_test_server_node(self, data: dict[str, Any]) -> dict[str, Any]:
        """Test OPC UA Server Node."""
        endpoint = "/opcua/actions/test_server_node"

        return self._api_client.post(endpoint, data={"data": data})

    def opcua_actions_test_group_value(self, data: dict[str, Any]) -> dict[str, Any]:
        """Test OPC UA Group Value."""
        endpoint = "/opcua/actions/test_group_value"

        return self._api_client.post(endpoint, data={"data": data})

    def opcua_actions_test_group(self, data: dict[str, Any]) -> dict[str, Any]:
        """Test OPC UA Group."""
        endpoint = "/opcua/actions/test_group"

        return self._api_client.post(endpoint, data={"data": data})

    def get_opcua_server_config(self) -> dict[str, Any]:
        """Returns all OPC UA Server configurations."""
        endpoint = "/opcua/server/config"

        return self._api_client.get(endpoint)

    def create_opcua_server_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates OPC UA Server configuration."""
        endpoint = "/opcua/server/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_opcua_server_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OPC UA Server configurations."""
        endpoint = "/opcua/server/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_opcua_server_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified OPC UA Server configurations."""
        return [self.delete_opcua_server_config_by_id(server_id) for server_id in config]

    def get_opcua_server_config_by_id(self, server_id: str) -> dict[str, Any]:
        """Returns the specified OPC UA Server configuration."""
        endpoint = f"/opcua/server/config/{server_id}"

        return self._api_client.get(endpoint)

    def update_opcua_server_config_by_id(self, server_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified OPC UA Server configuration."""
        endpoint = f"/opcua/server/config/{server_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_opcua_server_config_by_id(self, server_id: str) -> dict[str, Any]:
        """Deletes the specified OPC UA Server configuration."""
        endpoint = f"/opcua/server/config/{server_id}"

        return self._api_client.delete(endpoint)

    def opcua_server_actions_test(self, data: dict[str, Any]) -> dict[str, Any]:
        """Deprecated. Test OPC UA Server."""
        endpoint = "/opcua/server/actions/test"

        return self._api_client.post(endpoint, data={"data": data})

    def get_opcua_server_status(self) -> dict[str, Any]:
        """Returns OPC UA Server status."""
        endpoint = "/opcua/server/status"

        return self._api_client.get(endpoint)

    def get_opcua_server_nodes_config(self, server_id: str) -> dict[str, Any]:
        """Returns all OPC UA Server Node configurations."""
        endpoint = f"/opcua/server/{server_id}/nodes/config"

        return self._api_client.get(endpoint)

    def create_opcua_server_nodes_config(self, server_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates OPC UA Server Node configuration."""
        endpoint = f"/opcua/server/{server_id}/nodes/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_opcua_server_nodes_config(self, server_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OPC UA Server Node configurations."""
        endpoint = f"/opcua/server/{server_id}/nodes/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_opcua_server_nodes_config(self, server_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified OPC UA Server Node configurations."""
        return [self.delete_opcua_server_nodes_config_by_id(server_id, node_id) for node_id in config]

    def get_opcua_server_nodes_config_by_id(self, server_id: str, node_id: str) -> dict[str, Any]:
        """Returns the specified OPC UA Server Node configuration."""
        endpoint = f"/opcua/server/{server_id}/nodes/config/{node_id}"

        return self._api_client.get(endpoint)

    def update_opcua_server_nodes_config_by_id(
        self, server_id: str, node_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified OPC UA Server Node configuration."""
        endpoint = f"/opcua/server/{server_id}/nodes/config/{node_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_opcua_server_nodes_config_by_id(self, server_id: str, node_id: str) -> dict[str, Any]:
        """Deletes the specified OPC UA Server Node configuration."""
        endpoint = f"/opcua/server/{server_id}/nodes/config/{node_id}"

        return self._api_client.delete(endpoint)

    def opcua_server_nodes_actions_test(self, server_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Deprecated. Test OPC UA Server Node."""
        endpoint = f"/opcua/server/{server_id}/nodes/actions/test"

        return self._api_client.post(endpoint, data={"data": data})

    def get_opcua_server_nodes_status_by_id(self, server_id: str, node_id: str) -> dict[str, Any]:
        """Returns the specified OPC UA Server Node configuration."""
        endpoint = f"/opcua/server/{server_id}/nodes/status/{node_id}"

        return self._api_client.get(endpoint)

    def get_opcua_group_values_config(self, group_id: str) -> dict[str, Any]:
        """Returns all OPC UA Value configurations."""
        endpoint = f"/opcua/group/{group_id}/values/config"

        return self._api_client.get(endpoint)

    def create_opcua_group_values_config(self, group_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates OPC UA Value configuration."""
        endpoint = f"/opcua/group/{group_id}/values/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_opcua_group_values_config(self, group_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OPC UA Value configurations."""
        endpoint = f"/opcua/group/{group_id}/values/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_opcua_group_values_config(self, group_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified OPC UA Value configurations."""
        return [self.delete_opcua_group_values_config_by_id(group_id, value_id) for value_id in config]

    def get_opcua_group_values_config_by_id(self, group_id: str, value_id: str) -> dict[str, Any]:
        """Returns the specified OPC UA Value configuration."""
        endpoint = f"/opcua/group/{group_id}/values/config/{value_id}"

        return self._api_client.get(endpoint)

    def update_opcua_group_values_config_by_id(
        self, group_id: str, value_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified OPC UA Value configuration."""
        endpoint = f"/opcua/group/{group_id}/values/config/{value_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_opcua_group_values_config_by_id(self, group_id: str, value_id: str) -> dict[str, Any]:
        """Deletes the specified OPC UA Value configuration."""
        endpoint = f"/opcua/group/{group_id}/values/config/{value_id}"

        return self._api_client.delete(endpoint)

    def opcua_group_values_actions_test(self, group_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Deprecated. Test OPC UA Value."""
        endpoint = f"/opcua/group/{group_id}/values/actions/test"

        return self._api_client.post(endpoint, data={"data": data})

    def get_opcua_group_values_status_by_id(self, group_id: str, value_id: str) -> dict[str, Any]:
        """Returns the specified OPC UA Value configuration."""
        endpoint = f"/opcua/group/{group_id}/values/status/{value_id}"

        return self._api_client.get(endpoint)

    def get_opcua_group_config(self) -> dict[str, Any]:
        """Returns all OPC UA Value Group configurations."""
        endpoint = "/opcua/group/config"

        return self._api_client.get(endpoint)

    def create_opcua_group_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates OPC UA Value Group configuration."""
        endpoint = "/opcua/group/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_opcua_group_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OPC UA Value Group configurations."""
        endpoint = "/opcua/group/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_opcua_group_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified OPC UA Value Group configurations."""
        return [self.delete_opcua_group_config_by_id(group_id) for group_id in config]

    def get_opcua_group_config_by_id(self, group_id: str) -> dict[str, Any]:
        """Returns the specified OPC UA Value Group configuration."""
        endpoint = f"/opcua/group/config/{group_id}"

        return self._api_client.get(endpoint)

    def update_opcua_group_config_by_id(self, group_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified OPC UA Value Group configuration."""
        endpoint = f"/opcua/group/config/{group_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_opcua_group_config_by_id(self, group_id: str) -> dict[str, Any]:
        """Deletes the specified OPC UA Value Group configuration."""
        endpoint = f"/opcua/group/config/{group_id}"

        return self._api_client.delete(endpoint)

    def opcua_group_actions_test(self, data: dict[str, Any]) -> dict[str, Any]:
        """Deprecated. Test OPC UA Value Group."""
        endpoint = "/opcua/group/actions/test"

        return self._api_client.post(endpoint, data={"data": data})

    def get_opcua_group_status(self) -> dict[str, Any]:
        """Returns OPC UA Value Group status."""
        endpoint = "/opcua/group/status"

        return self._api_client.get(endpoint)

    def get_opcua_group_status_by_id(self, group_id: str) -> dict[str, Any]:
        """Returns the specified OPC UA Value Group configuration."""
        endpoint = f"/opcua/group/status/{group_id}"

        return self._api_client.get(endpoint)
