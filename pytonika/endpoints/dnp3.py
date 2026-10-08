from typing import Any, Literal

from ._endpoint import Endpoint


class DNP3(Endpoint):
    def get_dnp3_database_entries_status(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        db_location: Literal["flash", "ram"] | None = None,
        id: str | None = None,
        data_type: str | None = None,
        client_id: str | None = None,
        client_name: str | None = None,
        request_id: str | None = None,
        name: str | None = None,
        ip_address: str | None = None,
        port: int | None = None,
    ) -> dict[str, Any]:
        """Returns all DNP3 database entries."""
        return self._client.request(
            "GET",
            "/dnp3/database/entries/status",
            params={
                "limit": limit,
                "offset": offset,
                "db_location": db_location,
                "id": id,
                "data_type": data_type,
                "client_id": client_id,
                "client_name": client_name,
                "request_id": request_id,
                "name": name,
                "ip_address": ip_address,
                "port": port,
            },
        )

    def get_dnp3_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all DNP3 global settings configurations."""
        return self._client.request("GET", "/dnp3/global", params={"all_options": all_options})

    def update_dnp3_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified DNP3 global settings configurations."""
        return self._client.request("PUT", "/dnp3/global", json={"data": config})

    def get_dnp3_outstation_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified TCP Outstation configuration."""
        return self._client.request("GET", "/dnp3/outstation/config", params={"all_options": all_options})

    def update_dnp3_outstation_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified TCP Outstation configuration."""
        return self._client.request("PUT", "/dnp3/outstation/config", json={"data": config})

    def get_dnp3_outstation_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all TCP Outstation configuration."""
        return self._client.request("GET", f"/dnp3/outstation/config/{config_id}", params={"all_options": all_options})

    def update_dnp3_outstation_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified TCP Outstation configurations."""
        return self._client.request("PUT", f"/dnp3/outstation/config/{config_id}", json={"data": config})

    def get_dnp3_outstation_objects_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all TCP Outstation Object configurations. Data sources can be found using
        /universal_gateway/options endpoint.
        """
        return self._client.request("GET", "/dnp3/outstation/objects/config", params={"all_options": all_options})

    def create_dnp3_outstation_objects_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a TCP Outstation Object configuration."""
        return self._client.request("POST", "/dnp3/outstation/objects/config", json={"data": config})

    def update_dnp3_outstation_objects_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified TCP Outstation Object configuration. Data sources can be found using
        /universal_gateway/options endpoint.
        """
        return self._client.request("PUT", "/dnp3/outstation/objects/config", json={"data": config})

    def delete_dnp3_outstation_objects_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified TCP Outstation Object configurations."""
        return self._client.request("DELETE", "/dnp3/outstation/objects/config", json={"data": config})

    def get_dnp3_outstation_objects_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Return TCP Outstation Object configuration. Data sources can be found using /universal_gateway/options
        endpoint.
        """
        return self._client.request(
            "GET", f"/dnp3/outstation/objects/config/{config_id}", params={"all_options": all_options}
        )

    def update_dnp3_outstation_objects_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified TCP Outstation Object configuration. Data sources can be found using
        /universal_gateway/options endpoint.
        """
        return self._client.request("PUT", f"/dnp3/outstation/objects/config/{config_id}", json={"data": config})

    def delete_dnp3_outstation_objects_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified TCP Outstation Object configuration."""
        return self._client.request("DELETE", f"/dnp3/outstation/objects/config/{config_id}")

    def get_dnp3_outstation_status(self) -> dict[str, Any]:
        """Returns Outstation status."""
        return self._client.request("GET", "/dnp3/outstation/status")

    def dnp3_serial_actions_test_request(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Test request configuration."""
        return self._client.request(
            "POST", "/dnp3/serial/actions/test_request", json=None if data is None else {"data": data}
        )

    def get_dnp3_serial_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Serial Client configuration."""
        return self._client.request("GET", "/dnp3/serial/config", params={"all_options": all_options})

    def create_dnp3_serial_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Serial Client configuration."""
        return self._client.request("POST", "/dnp3/serial/config", json={"data": config})

    def update_dnp3_serial_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Serial Client configurations."""
        return self._client.request("PUT", "/dnp3/serial/config", json={"data": config})

    def delete_dnp3_serial_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Serial Client configurations."""
        return self._client.request("DELETE", "/dnp3/serial/config", json={"data": config})

    def get_dnp3_serial_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified Serial Client configuration."""
        return self._client.request("GET", f"/dnp3/serial/config/{config_id}", params={"all_options": all_options})

    def update_dnp3_serial_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified Serial Client configuration."""
        return self._client.request("PUT", f"/dnp3/serial/config/{config_id}", json={"data": config})

    def delete_dnp3_serial_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified Serial Client configuration."""
        return self._client.request("DELETE", f"/dnp3/serial/config/{config_id}")

    def get_dnp3_serial_status(self) -> dict[str, Any]:
        """Returns Serial Client status."""
        return self._client.request("GET", "/dnp3/serial/status")

    def get_dnp3_serial_requests_config(self, serial_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all DNP3 requests configuration."""
        return self._client.request(
            "GET", f"/dnp3/serial/{serial_id}/requests/config", params={"all_options": all_options}
        )

    def create_dnp3_serial_requests_config(self, serial_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates DNP3 request configuration."""
        return self._client.request("POST", f"/dnp3/serial/{serial_id}/requests/config", json={"data": config})

    def update_dnp3_serial_requests_config(self, serial_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified DNP3 request configurations. Updating request options may invalidate configurations in
        data sources.
        """
        return self._client.request("PUT", f"/dnp3/serial/{serial_id}/requests/config", json={"data": config})

    def delete_dnp3_serial_requests_config(self, serial_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes specified DNP3 request configurations. Deleting request may cause reference loss if they are used
        in data sources.
        """
        return self._client.request("DELETE", f"/dnp3/serial/{serial_id}/requests/config", json={"data": config})

    def get_dnp3_serial_requests_config_by_id(
        self, serial_id: str, request_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns specified DNP3 request configuration."""
        return self._client.request(
            "GET", f"/dnp3/serial/{serial_id}/requests/config/{request_id}", params={"all_options": all_options}
        )

    def update_dnp3_serial_requests_config_by_id(
        self, serial_id: str, request_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified DNP3 request configuration. Updating request options may invalidate configurations in
        data sources.
        """
        return self._client.request(
            "PUT", f"/dnp3/serial/{serial_id}/requests/config/{request_id}", json={"data": config}
        )

    def delete_dnp3_serial_requests_config_by_id(self, serial_id: str, request_id: str) -> dict[str, Any]:
        """Deletes specified DNP3 request configuration. Deleting request may cause reference loss if they are used
        in data sources.
        """
        return self._client.request("DELETE", f"/dnp3/serial/{serial_id}/requests/config/{request_id}")

    def get_dnp3_serial_requests_status(self, serial_id: str) -> dict[str, Any]:
        """Returns specified DNP3 request current value."""
        return self._client.request("GET", f"/dnp3/serial/{serial_id}/requests/status")

    def get_dnp3_serial_requests_status_by_id(self, serial_id: str, request_id: str) -> dict[str, Any]:
        """Returns specified DNP3 request current value."""
        return self._client.request("GET", f"/dnp3/serial/{serial_id}/requests/status/{request_id}")

    def get_dnp3_serial_outstation_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Serial Outstation configurations."""
        return self._client.request("GET", "/dnp3/serial_outstation/config", params={"all_options": all_options})

    def create_dnp3_serial_outstation_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Serial Outstation configuration."""
        return self._client.request("POST", "/dnp3/serial_outstation/config", json={"data": config})

    def update_dnp3_serial_outstation_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Serial Outstation configurations."""
        return self._client.request("PUT", "/dnp3/serial_outstation/config", json={"data": config})

    def delete_dnp3_serial_outstation_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Serial Outstation configurations."""
        return self._client.request("DELETE", "/dnp3/serial_outstation/config", json={"data": config})

    def get_dnp3_serial_outstation_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Serial Outstation configuration."""
        return self._client.request(
            "GET", f"/dnp3/serial_outstation/config/{config_id}", params={"all_options": all_options}
        )

    def update_dnp3_serial_outstation_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Serial Outstation configuration."""
        return self._client.request("PUT", f"/dnp3/serial_outstation/config/{config_id}", json={"data": config})

    def delete_dnp3_serial_outstation_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Serial Outstation configuration."""
        return self._client.request("DELETE", f"/dnp3/serial_outstation/config/{config_id}")

    def get_dnp3_serial_outstation_objects_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Serial Outstation Object configurations. Data sources can be found using
        /universal_gateway/options endpoint.
        """
        return self._client.request(
            "GET", "/dnp3/serial_outstation/objects/config", params={"all_options": all_options}
        )

    def create_dnp3_serial_outstation_objects_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a Serial Outstation Object configuration."""
        return self._client.request("POST", "/dnp3/serial_outstation/objects/config", json={"data": config})

    def update_dnp3_serial_outstation_objects_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Serial Outstation Object configuration. Data sources can be found using
        /universal_gateway/options endpoint.
        """
        return self._client.request("PUT", "/dnp3/serial_outstation/objects/config", json={"data": config})

    def delete_dnp3_serial_outstation_objects_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Serial Outstation Object configurations."""
        return self._client.request("DELETE", "/dnp3/serial_outstation/objects/config", json={"data": config})

    def get_dnp3_serial_outstation_objects_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns Serial Outstation Object configuration. Data sources can be found using /universal_gateway/options
        endpoint.
        """
        return self._client.request(
            "GET", f"/dnp3/serial_outstation/objects/config/{config_id}", params={"all_options": all_options}
        )

    def update_dnp3_serial_outstation_objects_config_by_id(
        self, config_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified Serial Outstation Object configuration. Data sources can be found using
        /universal_gateway/options endpoint.
        """
        return self._client.request("PUT", f"/dnp3/serial_outstation/objects/config/{config_id}", json={"data": config})

    def delete_dnp3_serial_outstation_objects_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified Serial Outstation Object configuration."""
        return self._client.request("DELETE", f"/dnp3/serial_outstation/objects/config/{config_id}")

    def get_dnp3_serial_outstation_status(self) -> dict[str, Any]:
        """Returns Serial Outstation status."""
        return self._client.request("GET", "/dnp3/serial_outstation/status")

    def dnp3_tcp_actions_test_request(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Test request configuration."""
        return self._client.request(
            "POST", "/dnp3/tcp/actions/test_request", json=None if data is None else {"data": data}
        )

    def get_dnp3_tcp_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all TCP Client configuration."""
        return self._client.request("GET", "/dnp3/tcp/config", params={"all_options": all_options})

    def create_dnp3_tcp_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates TCP Client configuration."""
        return self._client.request("POST", "/dnp3/tcp/config", json={"data": config})

    def update_dnp3_tcp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified TCP Client configurations."""
        return self._client.request("PUT", "/dnp3/tcp/config", json={"data": config})

    def delete_dnp3_tcp_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified TCP Client configurations."""
        return self._client.request("DELETE", "/dnp3/tcp/config", json={"data": config})

    def get_dnp3_tcp_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified TCP Client configuration."""
        return self._client.request("GET", f"/dnp3/tcp/config/{config_id}", params={"all_options": all_options})

    def update_dnp3_tcp_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified TCP Client configuration."""
        return self._client.request("PUT", f"/dnp3/tcp/config/{config_id}", json={"data": config})

    def delete_dnp3_tcp_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified TCP Client configuration."""
        return self._client.request("DELETE", f"/dnp3/tcp/config/{config_id}")

    def get_dnp3_tcp_status(self) -> dict[str, Any]:
        """Returns TCP Client status."""
        return self._client.request("GET", "/dnp3/tcp/status")

    def get_dnp3_tcp_requests_config(self, tcp_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all DNP3 requests configuration."""
        return self._client.request("GET", f"/dnp3/tcp/{tcp_id}/requests/config", params={"all_options": all_options})

    def create_dnp3_tcp_requests_config(self, tcp_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates DNP3 request configuration."""
        return self._client.request("POST", f"/dnp3/tcp/{tcp_id}/requests/config", json={"data": config})

    def update_dnp3_tcp_requests_config(self, tcp_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified DNP3 request configurations. Updating request options may invalidate configurations in
        data sources.
        """
        return self._client.request("PUT", f"/dnp3/tcp/{tcp_id}/requests/config", json={"data": config})

    def delete_dnp3_tcp_requests_config(self, tcp_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes specified DNP3 request configurations. Deleting request may cause reference loss if they are used
        in data sources.
        """
        return self._client.request("DELETE", f"/dnp3/tcp/{tcp_id}/requests/config", json={"data": config})

    def get_dnp3_tcp_requests_config_by_id(
        self, tcp_id: str, request_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns specified DNP3 request configuration."""
        return self._client.request(
            "GET", f"/dnp3/tcp/{tcp_id}/requests/config/{request_id}", params={"all_options": all_options}
        )

    def update_dnp3_tcp_requests_config_by_id(
        self, tcp_id: str, request_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified DNP3 request configuration. Updating request options may invalidate configurations in
        data sources.
        """
        return self._client.request("PUT", f"/dnp3/tcp/{tcp_id}/requests/config/{request_id}", json={"data": config})

    def delete_dnp3_tcp_requests_config_by_id(self, tcp_id: str, request_id: str) -> dict[str, Any]:
        """Deletes specified DNP3 request configuration. Deleting request may cause reference loss if they are used
        in data sources.
        """
        return self._client.request("DELETE", f"/dnp3/tcp/{tcp_id}/requests/config/{request_id}")

    def get_dnp3_tcp_requests_status(self, tcp_id: str) -> dict[str, Any]:
        """Returns specified DNP3 request current value."""
        return self._client.request("GET", f"/dnp3/tcp/{tcp_id}/requests/status")

    def get_dnp3_tcp_requests_status_by_id(self, tcp_id: str, request_id: str) -> dict[str, Any]:
        """Returns specified DNP3 request current value."""
        return self._client.request("GET", f"/dnp3/tcp/{tcp_id}/requests/status/{request_id}")
