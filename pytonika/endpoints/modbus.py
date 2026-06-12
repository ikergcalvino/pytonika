from typing import Any

from ._base import Endpoint


class Modbus(Endpoint):
    def get_modbus_client_tcp_config(self) -> dict[str, Any]:
        """Returns all Modbus TCP Client configurations."""
        endpoint = "/modbus/client/tcp/config"

        return self._api_client.get(endpoint)

    def create_modbus_client_tcp_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Modbus TCP Client configuration."""
        endpoint = "/modbus/client/tcp/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_modbus_client_tcp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Modbus TCP Client configurations."""
        endpoint = "/modbus/client/tcp/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_modbus_client_tcp_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Modbus TCP Client configurations."""
        return [self.delete_modbus_client_tcp_config_by_id(client_id) for client_id in config]

    def get_modbus_client_tcp_config_by_id(self, client_id: str) -> dict[str, Any]:
        """Returns the specified Modbus TCP Client configuration."""
        endpoint = f"/modbus/client/tcp/config/{client_id}"

        return self._api_client.get(endpoint)

    def update_modbus_client_tcp_config_by_id(self, client_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Modbus TCP Client configuration."""
        endpoint = f"/modbus/client/tcp/config/{client_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_modbus_client_tcp_config_by_id(self, client_id: str) -> dict[str, Any]:
        """Deletes the specified Modbus TCP Client configuration."""
        endpoint = f"/modbus/client/tcp/config/{client_id}"

        return self._api_client.delete(endpoint)

    def get_modbus_client_tcp_status(self) -> dict[str, Any]:
        """Returns Modbus TCP Client status."""
        endpoint = "/modbus/client/tcp/status"

        return self._api_client.get(endpoint)

    def get_modbus_client_tcp_requests_config(self, client_id: str) -> dict[str, Any]:
        """Returns all Modbus TCP Client Requests configurations."""
        endpoint = f"/modbus/client/tcp/{client_id}/requests/config"

        return self._api_client.get(endpoint)

    def create_modbus_client_tcp_requests_config(self, client_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Modbus TCP Client Request configuration."""
        endpoint = f"/modbus/client/tcp/{client_id}/requests/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_modbus_client_tcp_requests_config(self, client_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Modbus TCP Client Requests configurations."""
        endpoint = f"/modbus/client/tcp/{client_id}/requests/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_modbus_client_tcp_requests_config(self, client_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Modbus TCP Client Requests configurations."""
        return [self.delete_modbus_client_tcp_requests_config_by_id(client_id, request_id) for request_id in config]

    def get_modbus_client_tcp_requests_config_by_id(self, client_id: str, request_id: str) -> dict[str, Any]:
        """Returns the specified Modbus TCP Client Request configuration."""
        endpoint = f"/modbus/client/tcp/{client_id}/requests/config/{request_id}"

        return self._api_client.get(endpoint)

    def update_modbus_client_tcp_requests_config_by_id(
        self, client_id: str, request_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified Modbus TCP Client Request configuration."""
        endpoint = f"/modbus/client/tcp/{client_id}/requests/config/{request_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_modbus_client_tcp_requests_config_by_id(self, client_id: str, request_id: str) -> dict[str, Any]:
        """Deletes the specified Modbus TCP Client Request configuration."""
        endpoint = f"/modbus/client/tcp/{client_id}/requests/config/{request_id}"

        return self._api_client.delete(endpoint)

    def modbus_client_tcp_requests_actions_test_request(self, client_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Test Modbus TCP Client Request configuration."""
        endpoint = f"/modbus/client/tcp/{client_id}/requests/actions/test_request"

        return self._api_client.post(endpoint, data={"data": data})

    def get_modbus_client_tcp_requests_status(self, client_id: str) -> dict[str, Any]:
        """Get the current value of all enabled requests."""
        endpoint = f"/modbus/client/tcp/{client_id}/requests/status"

        return self._api_client.get(endpoint)

    def get_modbus_client_tcp_requests_status_by_name(self, client_id: str, name: str) -> dict[str, Any]:
        """Get the current value of request."""
        endpoint = f"/modbus/client/tcp/{client_id}/requests/status/{name}"

        return self._api_client.get(endpoint)

    def get_modbus_client_tcp_alarms_config(self, client_id: str) -> dict[str, Any]:
        """Returns all Modbus TCP Client Alarms configurations."""
        endpoint = f"/modbus/client/tcp/{client_id}/alarms/config"

        return self._api_client.get(endpoint)

    def create_modbus_client_tcp_alarms_config(self, client_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Modbus TCP Client Alarm configuration."""
        endpoint = f"/modbus/client/tcp/{client_id}/alarms/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_modbus_client_tcp_alarms_config(self, client_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Modbus TCP Client Alarms configurations."""
        endpoint = f"/modbus/client/tcp/{client_id}/alarms/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_modbus_client_tcp_alarms_config(self, client_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Modbus TCP Client Alarms configurations."""
        return [self.delete_modbus_client_tcp_alarms_config_by_id(client_id, alarm_id) for alarm_id in config]

    def get_modbus_client_tcp_alarms_config_by_id(self, client_id: str, alarm_id: str) -> dict[str, Any]:
        """Returns the specified Modbus TCP Client Alarm configuration."""
        endpoint = f"/modbus/client/tcp/{client_id}/alarms/config/{alarm_id}"

        return self._api_client.get(endpoint)

    def upload_modbus_client_tcp_alarms_config_by_id(
        self, client_id: str, alarm_id: str, data: dict[str, Any]
    ) -> dict[str, Any]:
        """Uploads the specified Modbus TCP Client Alarm certificate files."""
        endpoint = f"/modbus/client/tcp/{client_id}/alarms/config/{alarm_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_modbus_client_tcp_alarms_config_by_id(
        self, client_id: str, alarm_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified Modbus TCP Client Alarm configuration."""
        endpoint = f"/modbus/client/tcp/{client_id}/alarms/config/{alarm_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_modbus_client_tcp_alarms_config_by_id(self, client_id: str, alarm_id: str) -> dict[str, Any]:
        """Deletes the specified Modbus TCP Client Alarm configuration."""
        endpoint = f"/modbus/client/tcp/{client_id}/alarms/config/{alarm_id}"

        return self._api_client.delete(endpoint)

    def get_modbus_client_global(self) -> dict[str, Any]:
        """Returns all Modbus client global settings configurations."""
        endpoint = "/modbus/client/global"

        return self._api_client.get(endpoint)

    def update_modbus_client_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Modbus client global settings configurations."""
        endpoint = "/modbus/client/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_modbus_server_serial_registers_config(self) -> dict[str, Any]:
        """Returns all Modbus Serial Server Register configurations."""
        endpoint = "/modbus/server/serial/registers/config"

        return self._api_client.get(endpoint)

    def create_modbus_server_serial_registers_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a Modbus Serial Server Register configuration."""
        endpoint = "/modbus/server/serial/registers/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_modbus_server_serial_registers_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Modbus Serial Server Register configurations."""
        endpoint = "/modbus/server/serial/registers/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_modbus_server_serial_registers_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Modbus Serial Server Register configurations."""
        return [self.delete_modbus_server_serial_registers_config_by_id(register_id) for register_id in config]

    def get_modbus_server_serial_registers_config_by_id(self, register_id: str) -> dict[str, Any]:
        """Returns the specified Modbus Serial Server Register configuration."""
        endpoint = f"/modbus/server/serial/registers/config/{register_id}"

        return self._api_client.get(endpoint)

    def update_modbus_server_serial_registers_config_by_id(
        self, register_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified Modbus Serial Server Register configuration."""
        endpoint = f"/modbus/server/serial/registers/config/{register_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_modbus_server_serial_registers_config_by_id(self, register_id: str) -> dict[str, Any]:
        """Deletes the specified Modbus Serial Server Register configuration."""
        endpoint = f"/modbus/server/serial/registers/config/{register_id}"

        return self._api_client.delete(endpoint)

    def get_modbus_server_tcp_registers_config(self) -> dict[str, Any]:
        """Returns all Modbus TCP Server Register configurations."""
        endpoint = "/modbus/server/tcp/registers/config"

        return self._api_client.get(endpoint)

    def create_modbus_server_tcp_registers_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a Modbus TCP Server Register configuration."""
        endpoint = "/modbus/server/tcp/registers/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_modbus_server_tcp_registers_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Modbus TCP Server Register configurations."""
        endpoint = "/modbus/server/tcp/registers/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_modbus_server_tcp_registers_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Modbus TCP Server Register configurations."""
        return [self.delete_modbus_server_tcp_registers_config_by_id(register_id) for register_id in config]

    def get_modbus_server_tcp_registers_config_by_id(self, register_id: str) -> dict[str, Any]:
        """Returns the specified Modbus TCP Server Register configuration."""
        endpoint = f"/modbus/server/tcp/registers/config/{register_id}"

        return self._api_client.get(endpoint)

    def update_modbus_server_tcp_registers_config_by_id(
        self, register_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified Modbus TCP Server Register configuration."""
        endpoint = f"/modbus/server/tcp/registers/config/{register_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_modbus_server_tcp_registers_config_by_id(self, register_id: str) -> dict[str, Any]:
        """Deletes specified Modbus TCP Server Register configuration."""
        endpoint = f"/modbus/server/tcp/registers/config/{register_id}"

        return self._api_client.delete(endpoint)

    def get_modbus_tcp_over_serial_config(self) -> dict[str, Any]:
        """Returns all Modbus TCP over Serial Gateway configurations."""
        endpoint = "/modbus/tcp_over_serial/config"

        return self._api_client.get(endpoint)

    def create_modbus_tcp_over_serial_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Modbus TCP over Serial Gateway configuration."""
        endpoint = "/modbus/tcp_over_serial/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_modbus_tcp_over_serial_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Modbus TCP over Serial Gateway configurations."""
        endpoint = "/modbus/tcp_over_serial/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_modbus_tcp_over_serial_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Modbus TCP over Serial Gateway configurations."""
        return [self.delete_modbus_tcp_over_serial_config_by_id(gateway_id) for gateway_id in config]

    def get_modbus_tcp_over_serial_config_by_id(self, gateway_id: str) -> dict[str, Any]:
        """Returns the specified Modbus TCP over Serial Gateway configuration."""
        endpoint = f"/modbus/tcp_over_serial/config/{gateway_id}"

        return self._api_client.get(endpoint)

    def update_modbus_tcp_over_serial_config_by_id(self, gateway_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Modbus TCP over Serial Gateway configuration."""
        endpoint = f"/modbus/tcp_over_serial/config/{gateway_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_modbus_tcp_over_serial_config_by_id(self, gateway_id: str) -> dict[str, Any]:
        """Deletes the specified Modbus TCP over Serial Gateway configuration."""
        endpoint = f"/modbus/tcp_over_serial/config/{gateway_id}"

        return self._api_client.delete(endpoint)

    def get_modbus_tcp_over_serial_status(self) -> dict[str, Any]:
        """Returns Modbus TCP over Serial Gateway status."""
        endpoint = "/modbus/tcp_over_serial/status"

        return self._api_client.get(endpoint)

    def get_modbus_tcp_over_serial_filters_config(self, gateway_id: str) -> dict[str, Any]:
        """Returns all Modbus TCP over Serial Gateway IP Filter rules."""
        endpoint = f"/modbus/tcp_over_serial/{gateway_id}/filters/config"

        return self._api_client.get(endpoint)

    def create_modbus_tcp_over_serial_filters_config(self, gateway_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Modbus TCP over Serial Gateway IP Filter rule."""
        endpoint = f"/modbus/tcp_over_serial/{gateway_id}/filters/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_modbus_tcp_over_serial_filters_config(
        self, gateway_id: str, config: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """Updates specified Modbus TCP over Serial Gateway IP Filter rules."""
        endpoint = f"/modbus/tcp_over_serial/{gateway_id}/filters/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_modbus_tcp_over_serial_filters_config(self, gateway_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Modbus TCP over Serial Gateway IP Filter rules."""
        return [self.delete_modbus_tcp_over_serial_filters_config_by_id(gateway_id, filter_id) for filter_id in config]

    def get_modbus_tcp_over_serial_filters_config_by_id(self, gateway_id: str, filter_id: str) -> dict[str, Any]:
        """Returns the specified Modbus TCP over Serial Gateway IP Filter rule."""
        endpoint = f"/modbus/tcp_over_serial/{gateway_id}/filters/config/{filter_id}"

        return self._api_client.get(endpoint)

    def update_modbus_tcp_over_serial_filters_config_by_id(
        self, gateway_id: str, filter_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified Modbus TCP over Serial Gateway IP Filter rule."""
        endpoint = f"/modbus/tcp_over_serial/{gateway_id}/filters/config/{filter_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_modbus_tcp_over_serial_filters_config_by_id(self, gateway_id: str, filter_id: str) -> dict[str, Any]:
        """Deletes the specified Modbus TCP over Serial Gateway IP Filter rule."""
        endpoint = f"/modbus/tcp_over_serial/{gateway_id}/filters/config/{filter_id}"

        return self._api_client.delete(endpoint)
