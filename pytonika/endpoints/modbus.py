from typing import Any, Literal

from ._endpoint import Endpoint, File


class Modbus(Endpoint):
    def get_modbus_client_database_entries_status(
        self,
        *,
        db_path: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        id: str | None = None,
        request_id: str | None = None,
        request_name: str | None = None,
        server_id: str | None = None,
        server_name: str | None = None,
        ip_address: str | None = None,
    ) -> dict[str, Any]:
        """Returns all Modbus client database entries."""
        return self._client.request(
            "GET",
            "/modbus/client/database/entries/status",
            params={
                "db_path": db_path,
                "limit": limit,
                "offset": offset,
                "id": id,
                "request_id": request_id,
                "request_name": request_name,
                "server_id": server_id,
                "server_name": server_name,
                "ip_address": ip_address,
            },
        )

    def get_modbus_client_database_status(self, *, db_path: str | None = None) -> dict[str, Any]:
        """Returns Modbus client database statistics."""
        return self._client.request("GET", "/modbus/client/database/status", params={"db_path": db_path})

    def get_modbus_client_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Modbus client global settings configurations."""
        return self._client.request("GET", "/modbus/client/global", params={"all_options": all_options})

    def update_modbus_client_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified Modbus client global settings configurations."""
        return self._client.request("PUT", "/modbus/client/global", json={"data": config})

    def get_modbus_client_serial_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Modbus Serial Client configurations."""
        return self._client.request("GET", "/modbus/client/serial/config", params={"all_options": all_options})

    def create_modbus_client_serial_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Modbus Serial Client configuration."""
        return self._client.request("POST", "/modbus/client/serial/config", json={"data": config})

    def update_modbus_client_serial_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Modbus Serial Client configurations."""
        return self._client.request("PUT", "/modbus/client/serial/config", json={"data": config})

    def delete_modbus_client_serial_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Modbus Serial Client configurations."""
        return self._client.request("DELETE", "/modbus/client/serial/config", json={"data": config})

    def get_modbus_client_serial_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Modbus Serial Client configuration."""
        return self._client.request(
            "GET", f"/modbus/client/serial/config/{config_id}", params={"all_options": all_options}
        )

    def update_modbus_client_serial_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Modbus Serial Client configuration."""
        return self._client.request("PUT", f"/modbus/client/serial/config/{config_id}", json={"data": config})

    def delete_modbus_client_serial_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Modbus Serial Client configuration."""
        return self._client.request("DELETE", f"/modbus/client/serial/config/{config_id}")

    def get_modbus_client_serial_servers_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Modbus Serial Client Server configurations."""
        return self._client.request("GET", "/modbus/client/serial/servers/config", params={"all_options": all_options})

    def create_modbus_client_serial_servers_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Modbus Serial Client Server configuration."""
        return self._client.request("POST", "/modbus/client/serial/servers/config", json={"data": config})

    def update_modbus_client_serial_servers_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Modbus Serial Client Server configurations."""
        return self._client.request("PUT", "/modbus/client/serial/servers/config", json={"data": config})

    def delete_modbus_client_serial_servers_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Modbus Serial Client Server configurations."""
        return self._client.request("DELETE", "/modbus/client/serial/servers/config", json={"data": config})

    def get_modbus_client_serial_servers_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Modbus Serial Client Server configuration."""
        return self._client.request(
            "GET", f"/modbus/client/serial/servers/config/{config_id}", params={"all_options": all_options}
        )

    def update_modbus_client_serial_servers_config_by_id(
        self, config_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified Modbus Serial Client Server configuration."""
        return self._client.request("PUT", f"/modbus/client/serial/servers/config/{config_id}", json={"data": config})

    def delete_modbus_client_serial_servers_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Modbus Serial Client Server configuration."""
        return self._client.request("DELETE", f"/modbus/client/serial/servers/config/{config_id}")

    def get_modbus_client_serial_servers_status(self) -> dict[str, Any]:
        """Returns Modbus Serial Client Server status."""
        return self._client.request("GET", "/modbus/client/serial/servers/status")

    def get_modbus_client_serial_servers_alarms_config(
        self, servers_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns all Modbus Serial Client Server Alarms configurations."""
        return self._client.request(
            "GET", f"/modbus/client/serial/servers/{servers_id}/alarms/config", params={"all_options": all_options}
        )

    def create_modbus_client_serial_servers_alarms_config(
        self, servers_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Creates Modbus Serial Client Server Alarm configuration."""
        return self._client.request(
            "POST", f"/modbus/client/serial/servers/{servers_id}/alarms/config", json={"data": config}
        )

    def update_modbus_client_serial_servers_alarms_config(
        self, servers_id: str, config: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """Updates specified Modbus Serial Client Server Alarms configurations."""
        return self._client.request(
            "PUT", f"/modbus/client/serial/servers/{servers_id}/alarms/config", json={"data": config}
        )

    def delete_modbus_client_serial_servers_alarms_config(self, servers_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes specified Modbus Serial Client Server Alarms configurations."""
        return self._client.request(
            "DELETE", f"/modbus/client/serial/servers/{servers_id}/alarms/config", json={"data": config}
        )

    def get_modbus_client_serial_servers_alarms_config_by_id(
        self, servers_id: str, alarm_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Modbus Serial Client Server Alarm configuration."""
        return self._client.request(
            "GET",
            f"/modbus/client/serial/servers/{servers_id}/alarms/config/{alarm_id}",
            params={"all_options": all_options},
        )

    def upload_modbus_client_serial_servers_alarms_config_by_id(
        self,
        servers_id: str,
        alarm_id: str,
        file: File,
        *,
        option: Literal["ca_file", "cert_file", "key_file"] | None = None,
    ) -> dict[str, Any]:
        """Uploads the specified Modbus Serial Client Server Alarm certificate files."""
        return self._client.request(
            "POST",
            f"/modbus/client/serial/servers/{servers_id}/alarms/config/{alarm_id}",
            files={"file": file},
            form={"option": option},
        )

    def update_modbus_client_serial_servers_alarms_config_by_id(
        self, servers_id: str, alarm_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified Modbus Serial Client Server Alarm configuration."""
        return self._client.request(
            "PUT", f"/modbus/client/serial/servers/{servers_id}/alarms/config/{alarm_id}", json={"data": config}
        )

    def delete_modbus_client_serial_servers_alarms_config_by_id(self, servers_id: str, alarm_id: str) -> dict[str, Any]:
        """Deletes the specified Modbus Serial Client Server Alarm configuration."""
        return self._client.request("DELETE", f"/modbus/client/serial/servers/{servers_id}/alarms/config/{alarm_id}")

    def modbus_client_serial_servers_requests_actions_test_request(
        self, servers_id: str, data: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Test Modbus Serial Client Server Request configuration."""
        return self._client.request(
            "POST",
            f"/modbus/client/serial/servers/{servers_id}/requests/actions/test_request",
            json=None if data is None else {"data": data},
        )

    def get_modbus_client_serial_servers_requests_config(
        self, servers_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns all Modbus Serial Client Server Requests configurations."""
        return self._client.request(
            "GET", f"/modbus/client/serial/servers/{servers_id}/requests/config", params={"all_options": all_options}
        )

    def create_modbus_client_serial_servers_requests_config(
        self, servers_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Creates Modbus Serial Client Server Request configuration."""
        return self._client.request(
            "POST", f"/modbus/client/serial/servers/{servers_id}/requests/config", json={"data": config}
        )

    def update_modbus_client_serial_servers_requests_config(
        self, servers_id: str, config: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """Updates specified Modbus Serial Client Server Requests configurations. Updating request options may
        invalidate configurations in data sources.
        """
        return self._client.request(
            "PUT", f"/modbus/client/serial/servers/{servers_id}/requests/config", json={"data": config}
        )

    def delete_modbus_client_serial_servers_requests_config(self, servers_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes specified Modbus Serial Client Server Requests configurations. Deleting request may cause
        reference loss if they are used in data sources.
        """
        return self._client.request(
            "DELETE", f"/modbus/client/serial/servers/{servers_id}/requests/config", json={"data": config}
        )

    def get_modbus_client_serial_servers_requests_config_by_id(
        self, servers_id: str, request_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Modbus Serial Client Server Request configuration."""
        return self._client.request(
            "GET",
            f"/modbus/client/serial/servers/{servers_id}/requests/config/{request_id}",
            params={"all_options": all_options},
        )

    def update_modbus_client_serial_servers_requests_config_by_id(
        self, servers_id: str, request_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified Modbus Serial Client Server Request configuration. Updating request options may
        invalidate configurations in data sources.
        """
        return self._client.request(
            "PUT", f"/modbus/client/serial/servers/{servers_id}/requests/config/{request_id}", json={"data": config}
        )

    def delete_modbus_client_serial_servers_requests_config_by_id(
        self, servers_id: str, request_id: str
    ) -> dict[str, Any]:
        """Deletes the specified Modbus Serial Client Server Request configuration. Deleting request may cause
        reference loss if they are used in data sources.
        """
        return self._client.request(
            "DELETE", f"/modbus/client/serial/servers/{servers_id}/requests/config/{request_id}"
        )

    def get_modbus_client_serial_servers_requests_status(self, servers_id: str) -> dict[str, Any]:
        """Get the current value of all enabled requests."""
        return self._client.request("GET", f"/modbus/client/serial/servers/{servers_id}/requests/status")

    def get_modbus_client_serial_servers_requests_status_by_name(self, servers_id: str, name: str) -> dict[str, Any]:
        """Get the current value of a single request."""
        return self._client.request("GET", f"/modbus/client/serial/servers/{servers_id}/requests/status/{name}")

    def get_modbus_client_tcp_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Modbus TCP Client configurations."""
        return self._client.request("GET", "/modbus/client/tcp/config", params={"all_options": all_options})

    def create_modbus_client_tcp_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Modbus TCP Client configuration."""
        return self._client.request("POST", "/modbus/client/tcp/config", json={"data": config})

    def update_modbus_client_tcp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Modbus TCP Client configurations."""
        return self._client.request("PUT", "/modbus/client/tcp/config", json={"data": config})

    def delete_modbus_client_tcp_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Modbus TCP Client configurations."""
        return self._client.request("DELETE", "/modbus/client/tcp/config", json={"data": config})

    def get_modbus_client_tcp_config_by_id(self, client_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Modbus TCP Client configuration."""
        return self._client.request(
            "GET", f"/modbus/client/tcp/config/{client_id}", params={"all_options": all_options}
        )

    def update_modbus_client_tcp_config_by_id(self, client_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Modbus TCP Client configuration."""
        return self._client.request("PUT", f"/modbus/client/tcp/config/{client_id}", json={"data": config})

    def delete_modbus_client_tcp_config_by_id(self, client_id: str) -> dict[str, Any]:
        """Deletes the specified Modbus TCP Client configuration."""
        return self._client.request("DELETE", f"/modbus/client/tcp/config/{client_id}")

    def get_modbus_client_tcp_config_alarms_by_id(self, config_id: str, alarm_id: str) -> dict[str, Any]:
        """Returns the specified Modbus TCP Client Alarm configuration."""
        return self._client.request("GET", f"/modbus/client/tcp/config/{config_id}/alarms/{alarm_id}")

    def upload_modbus_client_tcp_config_alarms_by_id(
        self,
        config_id: str,
        alarm_id: str,
        file: File,
        *,
        option: Literal["ca_file", "cert_file", "key_file"] | None = None,
    ) -> dict[str, Any]:
        """Upload Modbus alarm certificates."""
        return self._client.request(
            "POST",
            f"/modbus/client/tcp/config/{config_id}/alarms/{alarm_id}",
            files={"file": file},
            form={"option": option},
        )

    def update_modbus_client_tcp_config_alarms_by_id(
        self, config_id: str, alarm_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified Modbus TCP Client Alarm configuration."""
        return self._client.request(
            "PUT", f"/modbus/client/tcp/config/{config_id}/alarms/{alarm_id}", json={"data": config}
        )

    def delete_modbus_client_tcp_config_alarms_by_id(self, config_id: str, alarm_id: str) -> dict[str, Any]:
        """Deletes the specified Modbus TCP Client Alarm configuration."""
        return self._client.request("DELETE", f"/modbus/client/tcp/config/{config_id}/alarms/{alarm_id}")

    def get_modbus_client_tcp_status(self) -> dict[str, Any]:
        """Returns Modbus TCP Client status."""
        return self._client.request("GET", "/modbus/client/tcp/status")

    def get_modbus_client_tcp_alarms_config(self, client_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Modbus TCP Client Alarms configurations."""
        return self._client.request(
            "GET", f"/modbus/client/tcp/{client_id}/alarms/config", params={"all_options": all_options}
        )

    def create_modbus_client_tcp_alarms_config(self, client_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Modbus TCP Client Alarm configuration."""
        return self._client.request("POST", f"/modbus/client/tcp/{client_id}/alarms/config", json={"data": config})

    def update_modbus_client_tcp_alarms_config(self, client_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Modbus TCP Client Alarms configurations."""
        return self._client.request("PUT", f"/modbus/client/tcp/{client_id}/alarms/config", json={"data": config})

    def delete_modbus_client_tcp_alarms_config(self, client_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes specified Modbus TCP Client Alarms configurations."""
        return self._client.request("DELETE", f"/modbus/client/tcp/{client_id}/alarms/config", json={"data": config})

    def get_modbus_client_tcp_alarms_config_by_id(
        self, client_id: str, alarm_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Modbus TCP Client Alarm configuration."""
        return self._client.request(
            "GET", f"/modbus/client/tcp/{client_id}/alarms/config/{alarm_id}", params={"all_options": all_options}
        )

    def upload_modbus_client_tcp_alarms_config_by_id(
        self,
        client_id: str,
        alarm_id: str,
        file: File,
        *,
        option: Literal["ca_file", "cert_file", "key_file"] | None = None,
    ) -> dict[str, Any]:
        """Uploads the specified Modbus TCP Client Alarm certificate files."""
        return self._client.request(
            "POST",
            f"/modbus/client/tcp/{client_id}/alarms/config/{alarm_id}",
            files={"file": file},
            form={"option": option},
        )

    def update_modbus_client_tcp_alarms_config_by_id(
        self, client_id: str, alarm_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified Modbus TCP Client Alarm configuration."""
        return self._client.request(
            "PUT", f"/modbus/client/tcp/{client_id}/alarms/config/{alarm_id}", json={"data": config}
        )

    def delete_modbus_client_tcp_alarms_config_by_id(self, client_id: str, alarm_id: str) -> dict[str, Any]:
        """Deletes the specified Modbus TCP Client Alarm configuration."""
        return self._client.request("DELETE", f"/modbus/client/tcp/{client_id}/alarms/config/{alarm_id}")

    def modbus_client_tcp_requests_actions_test_request(
        self, client_id: str, data: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Test Modbus TCP Client Request configuration."""
        return self._client.request(
            "POST",
            f"/modbus/client/tcp/{client_id}/requests/actions/test_request",
            json=None if data is None else {"data": data},
        )

    def get_modbus_client_tcp_requests_config(
        self, client_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns all Modbus TCP Client Requests configurations."""
        return self._client.request(
            "GET", f"/modbus/client/tcp/{client_id}/requests/config", params={"all_options": all_options}
        )

    def create_modbus_client_tcp_requests_config(self, client_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Modbus TCP Client Request configuration."""
        return self._client.request("POST", f"/modbus/client/tcp/{client_id}/requests/config", json={"data": config})

    def update_modbus_client_tcp_requests_config(self, client_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Modbus TCP Client Requests configurations. Updating request options may invalidate
        configurations in data sources.
        """
        return self._client.request("PUT", f"/modbus/client/tcp/{client_id}/requests/config", json={"data": config})

    def delete_modbus_client_tcp_requests_config(self, client_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes specified Modbus TCP Client Requests configurations. Deleting request may cause reference loss if
        they are used in data sources.
        """
        return self._client.request("DELETE", f"/modbus/client/tcp/{client_id}/requests/config", json={"data": config})

    def get_modbus_client_tcp_requests_config_by_id(
        self, client_id: str, request_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Modbus TCP Client Request configuration."""
        return self._client.request(
            "GET", f"/modbus/client/tcp/{client_id}/requests/config/{request_id}", params={"all_options": all_options}
        )

    def update_modbus_client_tcp_requests_config_by_id(
        self, client_id: str, request_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified Modbus TCP Client Request configuration. Updating request options may invalidate
        configurations in data sources.
        """
        return self._client.request(
            "PUT", f"/modbus/client/tcp/{client_id}/requests/config/{request_id}", json={"data": config}
        )

    def delete_modbus_client_tcp_requests_config_by_id(self, client_id: str, request_id: str) -> dict[str, Any]:
        """Deletes the specified Modbus TCP Client Request configuration. Deleting request may cause reference loss
        if they are used in data sources.
        """
        return self._client.request("DELETE", f"/modbus/client/tcp/{client_id}/requests/config/{request_id}")

    def get_modbus_client_tcp_requests_status(self, client_id: str) -> dict[str, Any]:
        """Get the current value of all enabled requests."""
        return self._client.request("GET", f"/modbus/client/tcp/{client_id}/requests/status")

    def get_modbus_client_tcp_requests_status_by_name(self, client_id: str, name: str) -> dict[str, Any]:
        """Get the current value of request."""
        return self._client.request("GET", f"/modbus/client/tcp/{client_id}/requests/status/{name}")

    def get_modbus_gateway_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all MQTT Modbus Gateway configurations."""
        return self._client.request("GET", "/modbus/gateway/config", params={"all_options": all_options})

    def update_modbus_gateway_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified MQTT Modbus Gateway configurations."""
        return self._client.request("PUT", "/modbus/gateway/config", json={"data": config})

    def get_modbus_gateway_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified MQTT Modbus Gateway configuration."""
        return self._client.request("GET", f"/modbus/gateway/config/{config_id}", params={"all_options": all_options})

    def upload_modbus_gateway_config_by_id(
        self, config_id: str, file: File, *, option: Literal["cafile", "certfile", "keyfile"] | None = None
    ) -> dict[str, Any]:
        """Uploads the specified MQTT Modbus Gateway certificate files."""
        return self._client.request(
            "POST", f"/modbus/gateway/config/{config_id}", files={"file": file}, form={"option": option}
        )

    def update_modbus_gateway_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified MQTT Modbus Gateway configuration."""
        return self._client.request("PUT", f"/modbus/gateway/config/{config_id}", json={"data": config})

    def get_modbus_gateway_status(self) -> dict[str, Any]:
        """Returns MQTT Modbus Gateway status."""
        return self._client.request("GET", "/modbus/gateway/status")

    def get_modbus_serial_gateway_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all MQTT Modbus Serial Gateway configurations."""
        return self._client.request("GET", "/modbus/serial_gateway/config", params={"all_options": all_options})

    def create_modbus_serial_gateway_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates MQTT Modbus Serial Gateway configuration."""
        return self._client.request("POST", "/modbus/serial_gateway/config", json={"data": config})

    def update_modbus_serial_gateway_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified MQTT Modbus Serial Gateway configurations."""
        return self._client.request("PUT", "/modbus/serial_gateway/config", json={"data": config})

    def delete_modbus_serial_gateway_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified MQTT Modbus Serial Gateway configurations."""
        return self._client.request("DELETE", "/modbus/serial_gateway/config", json={"data": config})

    def get_modbus_serial_gateway_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified MQTT Modbus Serial Gateway configuration."""
        return self._client.request(
            "GET", f"/modbus/serial_gateway/config/{config_id}", params={"all_options": all_options}
        )

    def update_modbus_serial_gateway_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified MQTT Modbus Serial Gateway configuration."""
        return self._client.request("PUT", f"/modbus/serial_gateway/config/{config_id}", json={"data": config})

    def delete_modbus_serial_gateway_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified MQTT Modbus Serial Gateway configuration."""
        return self._client.request("DELETE", f"/modbus/serial_gateway/config/{config_id}")

    def get_modbus_server_serial_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Modbus Serial Server configurations."""
        return self._client.request("GET", "/modbus/server/serial/config", params={"all_options": all_options})

    def create_modbus_server_serial_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a Modbus Serial Server configuration."""
        return self._client.request("POST", "/modbus/server/serial/config", json={"data": config})

    def update_modbus_server_serial_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Modbus Serial Server configurations."""
        return self._client.request("PUT", "/modbus/server/serial/config", json={"data": config})

    def delete_modbus_server_serial_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Modbus Serial Server configurations."""
        return self._client.request("DELETE", "/modbus/server/serial/config", json={"data": config})

    def get_modbus_server_serial_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Modbus Serial Server configuration."""
        return self._client.request(
            "GET", f"/modbus/server/serial/config/{config_id}", params={"all_options": all_options}
        )

    def update_modbus_server_serial_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Modbus Serial Server configuration."""
        return self._client.request("PUT", f"/modbus/server/serial/config/{config_id}", json={"data": config})

    def delete_modbus_server_serial_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Modbus Serial Server configuration."""
        return self._client.request("DELETE", f"/modbus/server/serial/config/{config_id}")

    def get_modbus_server_serial_registers_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Modbus Serial Server Register configurations."""
        return self._client.request(
            "GET", "/modbus/server/serial/registers/config", params={"all_options": all_options}
        )

    def create_modbus_server_serial_registers_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a Modbus Serial Server Register configuration. Data sources can be found using
        /universal_gateway/options endpoint.
        """
        return self._client.request("POST", "/modbus/server/serial/registers/config", json={"data": config})

    def update_modbus_server_serial_registers_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Modbus Serial Server Register configurations. Data sources can be found using
        /universal_gateway/options endpoint.
        """
        return self._client.request("PUT", "/modbus/server/serial/registers/config", json={"data": config})

    def delete_modbus_server_serial_registers_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Modbus Serial Server Register configurations."""
        return self._client.request("DELETE", "/modbus/server/serial/registers/config", json={"data": config})

    def get_modbus_server_serial_registers_config_by_id(
        self, register_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Modbus Serial Server Register configuration."""
        return self._client.request(
            "GET", f"/modbus/server/serial/registers/config/{register_id}", params={"all_options": all_options}
        )

    def update_modbus_server_serial_registers_config_by_id(
        self, register_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified Modbus Serial Server Register configuration. Data sources can be found using
        /universal_gateway/options endpoint.
        """
        return self._client.request(
            "PUT", f"/modbus/server/serial/registers/config/{register_id}", json={"data": config}
        )

    def delete_modbus_server_serial_registers_config_by_id(self, register_id: str) -> dict[str, Any]:
        """Deletes the specified Modbus Serial Server Register configuration."""
        return self._client.request("DELETE", f"/modbus/server/serial/registers/config/{register_id}")

    def get_modbus_server_serial_status(self) -> dict[str, Any]:
        """Returns Modbus Serial Server status."""
        return self._client.request("GET", "/modbus/server/serial/status")

    def get_modbus_server_tcp_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Modbus TCP Server configurations."""
        return self._client.request("GET", "/modbus/server/tcp/config", params={"all_options": all_options})

    def update_modbus_server_tcp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Modbus TCP Server configurations."""
        return self._client.request("PUT", "/modbus/server/tcp/config", json={"data": config})

    def get_modbus_server_tcp_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Modbus TCP Server configuration."""
        return self._client.request(
            "GET", f"/modbus/server/tcp/config/{config_id}", params={"all_options": all_options}
        )

    def update_modbus_server_tcp_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Modbus TCP Server configuration."""
        return self._client.request("PUT", f"/modbus/server/tcp/config/{config_id}", json={"data": config})

    def get_modbus_server_tcp_registers_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Modbus TCP Server Register configurations."""
        return self._client.request("GET", "/modbus/server/tcp/registers/config", params={"all_options": all_options})

    def create_modbus_server_tcp_registers_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a Modbus TCP Server Register configuration. Data sources can be found using
        /universal_gateway/options endpoint.
        """
        return self._client.request("POST", "/modbus/server/tcp/registers/config", json={"data": config})

    def update_modbus_server_tcp_registers_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Modbus TCP Server Register configurations. Data sources can be found using
        /universal_gateway/options endpoint.
        """
        return self._client.request("PUT", "/modbus/server/tcp/registers/config", json={"data": config})

    def delete_modbus_server_tcp_registers_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Modbus TCP Server Register configurations."""
        return self._client.request("DELETE", "/modbus/server/tcp/registers/config", json={"data": config})

    def get_modbus_server_tcp_registers_config_by_id(
        self, register_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Modbus TCP Server Register configuration."""
        return self._client.request(
            "GET", f"/modbus/server/tcp/registers/config/{register_id}", params={"all_options": all_options}
        )

    def update_modbus_server_tcp_registers_config_by_id(
        self, register_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified Modbus TCP Server Register configuration. Data sources can be found using
        /universal_gateway/options endpoint.
        """
        return self._client.request("PUT", f"/modbus/server/tcp/registers/config/{register_id}", json={"data": config})

    def delete_modbus_server_tcp_registers_config_by_id(self, register_id: str) -> dict[str, Any]:
        """Deletes specified Modbus TCP Server Register configuration."""
        return self._client.request("DELETE", f"/modbus/server/tcp/registers/config/{register_id}")

    def get_modbus_server_tcp_status(self) -> dict[str, Any]:
        """Returns Modbus TCP Server status."""
        return self._client.request("GET", "/modbus/server/tcp/status")

    def get_modbus_tcp_over_serial_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Modbus TCP over Serial Gateway configurations."""
        return self._client.request("GET", "/modbus/tcp_over_serial/config", params={"all_options": all_options})

    def create_modbus_tcp_over_serial_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Modbus TCP over Serial Gateway configuration."""
        return self._client.request("POST", "/modbus/tcp_over_serial/config", json={"data": config})

    def update_modbus_tcp_over_serial_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Modbus TCP over Serial Gateway configurations."""
        return self._client.request("PUT", "/modbus/tcp_over_serial/config", json={"data": config})

    def delete_modbus_tcp_over_serial_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Modbus TCP over Serial Gateway configurations."""
        return self._client.request("DELETE", "/modbus/tcp_over_serial/config", json={"data": config})

    def get_modbus_tcp_over_serial_config_by_id(
        self, gateway_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Modbus TCP over Serial Gateway configuration."""
        return self._client.request(
            "GET", f"/modbus/tcp_over_serial/config/{gateway_id}", params={"all_options": all_options}
        )

    def update_modbus_tcp_over_serial_config_by_id(self, gateway_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Modbus TCP over Serial Gateway configuration."""
        return self._client.request("PUT", f"/modbus/tcp_over_serial/config/{gateway_id}", json={"data": config})

    def delete_modbus_tcp_over_serial_config_by_id(self, gateway_id: str) -> dict[str, Any]:
        """Deletes the specified Modbus TCP over Serial Gateway configuration."""
        return self._client.request("DELETE", f"/modbus/tcp_over_serial/config/{gateway_id}")

    def get_modbus_tcp_over_serial_status(self) -> dict[str, Any]:
        """Returns Modbus TCP over Serial Gateway status."""
        return self._client.request("GET", "/modbus/tcp_over_serial/status")

    def get_modbus_tcp_over_serial_filters_config(
        self, gateway_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns all Modbus TCP over Serial Gateway IP Filter rules."""
        return self._client.request(
            "GET", f"/modbus/tcp_over_serial/{gateway_id}/filters/config", params={"all_options": all_options}
        )

    def create_modbus_tcp_over_serial_filters_config(self, gateway_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Modbus TCP over Serial Gateway IP Filter rule."""
        return self._client.request(
            "POST", f"/modbus/tcp_over_serial/{gateway_id}/filters/config", json={"data": config}
        )

    def update_modbus_tcp_over_serial_filters_config(
        self, gateway_id: str, config: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """Updates specified Modbus TCP over Serial Gateway IP Filter rules."""
        return self._client.request(
            "PUT", f"/modbus/tcp_over_serial/{gateway_id}/filters/config", json={"data": config}
        )

    def delete_modbus_tcp_over_serial_filters_config(self, gateway_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes specified Modbus TCP over Serial Gateway IP Filter rules."""
        return self._client.request(
            "DELETE", f"/modbus/tcp_over_serial/{gateway_id}/filters/config", json={"data": config}
        )

    def get_modbus_tcp_over_serial_filters_config_by_id(
        self, gateway_id: str, filter_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Modbus TCP over Serial Gateway IP Filter rule."""
        return self._client.request(
            "GET",
            f"/modbus/tcp_over_serial/{gateway_id}/filters/config/{filter_id}",
            params={"all_options": all_options},
        )

    def update_modbus_tcp_over_serial_filters_config_by_id(
        self, gateway_id: str, filter_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified Modbus TCP over Serial Gateway IP Filter rule."""
        return self._client.request(
            "PUT", f"/modbus/tcp_over_serial/{gateway_id}/filters/config/{filter_id}", json={"data": config}
        )

    def delete_modbus_tcp_over_serial_filters_config_by_id(self, gateway_id: str, filter_id: str) -> dict[str, Any]:
        """Deletes the specified Modbus TCP over Serial Gateway IP Filter rule."""
        return self._client.request("DELETE", f"/modbus/tcp_over_serial/{gateway_id}/filters/config/{filter_id}")
