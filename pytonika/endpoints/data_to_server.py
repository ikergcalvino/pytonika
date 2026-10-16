from typing import Any, Literal

from ._endpoint import Endpoint, File


class DataToServer(Endpoint):
    def get_data_to_server_collections_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Data to Server Collections configurations."""
        return self._client.request("GET", "/data_to_server/collections/config", params={"all_options": all_options})

    def create_data_to_server_collections_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Data to Server Collection configuration."""
        return self._client.request("POST", "/data_to_server/collections/config", json={"data": config})

    def update_data_to_server_collections_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Data to Server Collections configurations."""
        return self._client.request("PUT", "/data_to_server/collections/config", json={"data": config})

    def delete_data_to_server_collections_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the selected Data to Server Collections configurations."""
        return self._client.request("DELETE", "/data_to_server/collections/config", json={"data": config})

    def get_data_to_server_collections_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Data to Server Collection configuration."""
        return self._client.request(
            "GET", f"/data_to_server/collections/config/{config_id}", params={"all_options": all_options}
        )

    def upload_data_to_server_collections_config_by_id(
        self, config_id: str, file: File, *, option: Literal["format_script"] | None = None
    ) -> dict[str, Any]:
        """Uploads the Data to Server Collection necessary files."""
        return self._client.request(
            "POST", f"/data_to_server/collections/config/{config_id}", files={"file": file}, form={"option": option}
        )

    def update_data_to_server_collections_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Data to Server Collection configuration."""
        return self._client.request("PUT", f"/data_to_server/collections/config/{config_id}", json={"data": config})

    def delete_data_to_server_collections_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Data to Server configuration."""
        return self._client.request("DELETE", f"/data_to_server/collections/config/{config_id}")

    def get_data_to_server_collections_status(self) -> dict[str, Any]:
        """Returns status for all Data to Server collections."""
        return self._client.request("GET", "/data_to_server/collections/status")

    def get_data_to_server_collections_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns status for the specified Data to Server collection."""
        return self._client.request("GET", f"/data_to_server/collections/status/{status_id}")

    def data_to_server_collections_actions_trigger(self, collections_id: str) -> dict[str, Any]:
        """Triggers an immediate data send for the specified collection."""
        return self._client.request("POST", f"/data_to_server/collections/{collections_id}/actions/trigger")

    def get_data_to_server_collections_data_config(
        self, collections_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns all Data to Server Data Plugins configuration."""
        return self._client.request(
            "GET", f"/data_to_server/collections/{collections_id}/data/config", params={"all_options": all_options}
        )

    def create_data_to_server_collections_data_config(
        self, collection_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Creates a new Data to Server Data Plugin configuration."""
        return self._client.request(
            "POST", f"/data_to_server/collections/{collection_id}/data/config", json={"data": config}
        )

    def update_data_to_server_collections_data_config(
        self, collections_id: str, config: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """Updates the selected Data to Server Data Plugins configurations."""
        return self._client.request(
            "PUT", f"/data_to_server/collections/{collections_id}/data/config", json={"data": config}
        )

    def delete_data_to_server_collections_data_config(self, collections_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes the selected Data to Server Data Plugins configurations."""
        return self._client.request(
            "DELETE", f"/data_to_server/collections/{collections_id}/data/config", json={"data": config}
        )

    def get_data_to_server_compression_options(self) -> dict[str, Any]:
        """Returns Data to Server all available compression plugin names."""
        return self._client.request("GET", "/data_to_server/compression/options")

    def data_to_server_data_actions_download_example_input_lua(self) -> bytes | dict[str, Any]:
        """Downloads Lua script example file."""
        return self._client.request("POST", "/data_to_server/data/actions/download_example_input_lua", download=True)

    def get_data_to_server_data_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Data to Server Data Plugins configuration."""
        return self._client.request("GET", "/data_to_server/data/config", params={"all_options": all_options})

    def update_data_to_server_data_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Data to Server Data Plugins configurations."""
        return self._client.request("PUT", "/data_to_server/data/config", json={"data": config})

    def delete_data_to_server_data_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the selected Data to Server Plugins configurations."""
        return self._client.request("DELETE", "/data_to_server/data/config", json={"data": config})

    def get_data_to_server_data_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Data to Server Data Plugin configuration."""
        return self._client.request(
            "GET", f"/data_to_server/data/config/{config_id}", params={"all_options": all_options}
        )

    def upload_data_to_server_data_config_by_id(
        self,
        config_id: str,
        file: File,
        *,
        option: Literal["format_script", "lua_script", "mqtt_in_cafile", "mqtt_in_certfile", "mqtt_in_keyfile"]
        | None = None,
    ) -> dict[str, Any]:
        """Uploads the Data Plugin necessary files."""
        return self._client.request(
            "POST", f"/data_to_server/data/config/{config_id}", files={"file": file}, form={"option": option}
        )

    def update_data_to_server_data_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected Data to Server Data Plugins configurations."""
        return self._client.request("PUT", f"/data_to_server/data/config/{config_id}", json={"data": config})

    def delete_data_to_server_data_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Data to Server Data Plugins configurations."""
        return self._client.request("DELETE", f"/data_to_server/data/config/{config_id}")

    def get_data_to_server_data_options(self) -> dict[str, Any]:
        """Returns Data to Server all available Data Plugin names, description and tags."""
        return self._client.request("GET", "/data_to_server/data/options")

    def get_data_to_server_encoder_options(self) -> dict[str, Any]:
        """Returns Data to Server all available encoder plugin names."""
        return self._client.request("GET", "/data_to_server/encoder/options")

    def data_to_server_format_actions_download_example_format_lua(self) -> bytes | dict[str, Any]:
        """Downloads Lua format script example file."""
        return self._client.request("POST", "/data_to_server/format/actions/download_example_format_lua", download=True)

    def get_data_to_server_format_options(self) -> dict[str, Any]:
        """Returns Data to Server all available format plugin names."""
        return self._client.request("GET", "/data_to_server/format/options")

    def data_to_server_servers_actions_download_example_output_lua(self) -> bytes | dict[str, Any]:
        """Downloads Lua output script example file."""
        return self._client.request(
            "POST", "/data_to_server/servers/actions/download_example_output_lua", download=True
        )

    def data_to_server_servers_actions_scan_key(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Scan SFTP server's public key."""
        return self._client.request(
            "POST", "/data_to_server/servers/actions/scan_key", json=None if data is None else data
        )

    def get_data_to_server_servers_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Data to Server Server Plugins configuration."""
        return self._client.request("GET", "/data_to_server/servers/config", params={"all_options": all_options})

    def update_data_to_server_servers_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Data to Server Server Plugins configurations."""
        return self._client.request("PUT", "/data_to_server/servers/config", json={"data": config})

    def get_data_to_server_servers_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Data to Server Server Plugin configuration."""
        return self._client.request(
            "GET", f"/data_to_server/servers/config/{config_id}", params={"all_options": all_options}
        )

    def upload_data_to_server_servers_config_by_id(
        self,
        config_id: str,
        file: File,
        *,
        option: Literal[
            "azure_x509certificate",
            "azure_x509privatekey",
            "ftp_cafile",
            "ftp_certfile",
            "ftp_keyfile",
            "ftp_private_key",
            "http_cafile",
            "http_certfile",
            "http_keyfile",
            "mqtt_cafile",
            "mqtt_certfile",
            "mqtt_keyfile",
        ]
        | None = None,
    ) -> dict[str, Any]:
        """Uploads the Server Plugin necessary files."""
        return self._client.request(
            "POST", f"/data_to_server/servers/config/{config_id}", files={"file": file}, form={"option": option}
        )

    def update_data_to_server_servers_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Data to Server Server Plugin configuration."""
        return self._client.request("PUT", f"/data_to_server/servers/config/{config_id}", json={"data": config})

    def get_data_to_server_servers_options(self) -> dict[str, Any]:
        """Returns Data to Server all available Server Plugin names, description and tags."""
        return self._client.request("GET", "/data_to_server/servers/options")
