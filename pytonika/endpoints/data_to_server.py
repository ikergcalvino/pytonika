from typing import Any

from ._base import Endpoint


class DataToServer(Endpoint):
    def get_data_to_server_format_options(self) -> dict[str, Any]:
        """Returns Data to Server all available format plugin names."""
        endpoint = "/data_to_server/format/options"

        return self._api_client.get(endpoint)

    def data_to_server_format_actions_download_example_format_lua(
        self,
    ) -> dict[str, Any]:
        """Downloads Lua format script example file."""
        endpoint = "/data_to_server/format/actions/download_example_format_lua"

        return self._api_client.post(endpoint)

    def get_data_to_server_data_options(self) -> dict[str, Any]:
        """Returns Data to Server all available Data Plugin names, description and tags."""
        endpoint = "/data_to_server/data/options"

        return self._api_client.get(endpoint)

    def create_data_to_server_collections_data_config(
        self, collection_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Creates a new Data to Server Data Plugin configuration."""
        endpoint = f"/data_to_server/collections/{collection_id}/data/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def get_data_to_server_data_config(self) -> dict[str, Any]:
        """Returns all Data to Server Data Plugins configuration."""
        endpoint = "/data_to_server/data/config"

        return self._api_client.get(endpoint)

    def update_data_to_server_data_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Data to Server Data Plugins configurations."""
        endpoint = "/data_to_server/data/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_data_to_server_data_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected Data to Server Plugins configurations."""
        return [self.delete_data_to_server_data_config_by_id(config_id) for config_id in config]

    def get_data_to_server_data_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified Data to Server Data Plugin configuration."""
        endpoint = f"/data_to_server/data/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_data_to_server_data_config_by_id(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads the Data Plugin necessary files."""
        endpoint = f"/data_to_server/data/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_data_to_server_data_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected Data to Server Data Plugins configurations."""
        endpoint = f"/data_to_server/data/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_data_to_server_data_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Data to Server Data Plugins configurations."""
        endpoint = f"/data_to_server/data/config/{config_id}"

        return self._api_client.delete(endpoint)

    def data_to_server_data_actions_download_example_input_lua(
        self,
    ) -> dict[str, Any]:
        """Downloads Lua script example file."""
        endpoint = "/data_to_server/data/actions/download_example_input_lua"

        return self._api_client.post(endpoint)

    def get_data_to_server_servers_options(self) -> dict[str, Any]:
        """Returns Data to Server all available Server Plugin names, description and tags."""
        endpoint = "/data_to_server/servers/options"

        return self._api_client.get(endpoint)

    def get_data_to_server_servers_config(self) -> dict[str, Any]:
        """Returns all Data to Server Server Plugins configuration."""
        endpoint = "/data_to_server/servers/config"

        return self._api_client.get(endpoint)

    def update_data_to_server_servers_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Data to Server Server Plugins configurations."""
        endpoint = "/data_to_server/servers/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_data_to_server_servers_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified Data to Server Server Plugin configuration."""
        endpoint = f"/data_to_server/servers/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_data_to_server_servers_config_by_id(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads the Server Plugin necessary files."""
        endpoint = f"/data_to_server/servers/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_data_to_server_servers_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Data to Server Server Plugin configuration."""
        endpoint = f"/data_to_server/servers/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def data_to_server_servers_actions_download_example_output_lua(
        self,
    ) -> dict[str, Any]:
        """Downloads Lua output script example file."""
        endpoint = "/data_to_server/servers/actions/download_example_output_lua"

        return self._api_client.post(endpoint)

    def get_data_to_server_collections_config(self) -> dict[str, Any]:
        """Returns all Data to Server Collections configurations."""
        endpoint = "/data_to_server/collections/config"

        return self._api_client.get(endpoint)

    def create_data_to_server_collections_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Data to Server Collection configuration."""
        endpoint = "/data_to_server/collections/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_data_to_server_collections_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Data to Server Collections configurations."""
        endpoint = "/data_to_server/collections/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_data_to_server_collections_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected Data to Server Collections configurations."""
        return [self.delete_data_to_server_collections_config_by_id(config_id) for config_id in config]

    def get_data_to_server_collections_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified Data to Server Collection configuration."""
        endpoint = f"/data_to_server/collections/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_data_to_server_collections_config_by_id(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads the Data to Server Collection necessary files."""
        endpoint = f"/data_to_server/collections/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_data_to_server_collections_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Data to Server Collection configuration."""
        endpoint = f"/data_to_server/collections/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_data_to_server_collections_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Data to Server configuration."""
        endpoint = f"/data_to_server/collections/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_data_to_server_encoder_options(self) -> dict[str, Any]:
        """Returns Data to Server all available encoder plugin names."""
        endpoint = "/data_to_server/encoder/options"

        return self._api_client.get(endpoint)
