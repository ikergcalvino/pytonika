from typing import Any

from ._base import Endpoint


class DNP3(Endpoint):
    def get_dnp3_serial_requests_config(self, serial_id: str) -> dict[str, Any]:
        """Returns all DNP3 requests configuration."""
        endpoint = f"/dnp3/serial/{serial_id}/requests/config"

        return self._api_client.get(endpoint)

    def create_dnp3_serial_requests_config(self, serial_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates DNP3 request configuration."""
        endpoint = f"/dnp3/serial/{serial_id}/requests/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_dnp3_serial_requests_config(self, serial_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified DNP3 request configurations.

        Updating request options may invalidate configurations in data sources.
        """
        endpoint = f"/dnp3/serial/{serial_id}/requests/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dnp3_serial_requests_config(self, serial_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified DNP3 request configurations.

        Deleting request may cause reference loss if they are used in data sources.
        """
        return [self.delete_dnp3_serial_requests_config_by_id(serial_id, request_id) for request_id in config]

    def get_dnp3_serial_requests_config_by_id(self, serial_id: str, request_id: str) -> dict[str, Any]:
        """Returns specified DNP3 request configuration."""
        endpoint = f"/dnp3/serial/{serial_id}/requests/config/{request_id}"

        return self._api_client.get(endpoint)

    def update_dnp3_serial_requests_config_by_id(
        self, serial_id: str, request_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified DNP3 request configuration.

        Updating request options may invalidate configurations in data sources.
        """
        endpoint = f"/dnp3/serial/{serial_id}/requests/config/{request_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dnp3_serial_requests_config_by_id(self, serial_id: str, request_id: str) -> dict[str, Any]:
        """Deletes specified DNP3 request configuration.

        Deleting request may cause reference loss if they are used in data sources.
        """
        endpoint = f"/dnp3/serial/{serial_id}/requests/config/{request_id}"

        return self._api_client.delete(endpoint)

    def get_dnp3_serial_requests_status_by_id(self, serial_id: str, request_id: str) -> dict[str, Any]:
        """Returns specified DNP3 request current value."""
        endpoint = f"/dnp3/serial/{serial_id}/requests/status/{request_id}"

        return self._api_client.get(endpoint)

    def get_dnp3_serial_requests_status(self, serial_id: str) -> dict[str, Any]:
        """Returns specified DNP3 request current value."""
        endpoint = f"/dnp3/serial/{serial_id}/requests/status"

        return self._api_client.get(endpoint)

    def get_dnp3_tcp_requests_config(self, tcp_id: str) -> dict[str, Any]:
        """Returns all DNP3 requests configuration."""
        endpoint = f"/dnp3/tcp/{tcp_id}/requests/config"

        return self._api_client.get(endpoint)

    def create_dnp3_tcp_requests_config(self, tcp_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates DNP3 request configuration."""
        endpoint = f"/dnp3/tcp/{tcp_id}/requests/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_dnp3_tcp_requests_config(self, tcp_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified DNP3 request configurations.

        Updating request options may invalidate configurations in data sources.
        """
        endpoint = f"/dnp3/tcp/{tcp_id}/requests/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dnp3_tcp_requests_config(self, tcp_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified DNP3 request configurations.

        Deleting request may cause reference loss if they are used in data sources.
        """
        return [self.delete_dnp3_tcp_requests_config_by_id(tcp_id, request_id) for request_id in config]

    def get_dnp3_tcp_requests_config_by_id(self, tcp_id: str, request_id: str) -> dict[str, Any]:
        """Returns specified DNP3 request configuration."""
        endpoint = f"/dnp3/tcp/{tcp_id}/requests/config/{request_id}"

        return self._api_client.get(endpoint)

    def update_dnp3_tcp_requests_config_by_id(
        self, tcp_id: str, request_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified DNP3 request configuration.

        Updating request options may invalidate configurations in data sources.
        """
        endpoint = f"/dnp3/tcp/{tcp_id}/requests/config/{request_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dnp3_tcp_requests_config_by_id(self, tcp_id: str, request_id: str) -> dict[str, Any]:
        """Deletes specified DNP3 request configuration.

        Deleting request may cause reference loss if they are used in data sources.
        """
        endpoint = f"/dnp3/tcp/{tcp_id}/requests/config/{request_id}"

        return self._api_client.delete(endpoint)

    def get_dnp3_tcp_requests_status_by_id(self, tcp_id: str, request_id: str) -> dict[str, Any]:
        """Returns specified DNP3 request current value."""
        endpoint = f"/dnp3/tcp/{tcp_id}/requests/status/{request_id}"

        return self._api_client.get(endpoint)

    def get_dnp3_tcp_requests_status(self, tcp_id: str) -> dict[str, Any]:
        """Returns specified DNP3 request current value."""
        endpoint = f"/dnp3/tcp/{tcp_id}/requests/status"

        return self._api_client.get(endpoint)

    def get_dnp3_tcp_config(self) -> dict[str, Any]:
        """Returns all TCP Client configuration."""
        endpoint = "/dnp3/tcp/config"

        return self._api_client.get(endpoint)

    def create_dnp3_tcp_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates TCP Client configuration."""
        endpoint = "/dnp3/tcp/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_dnp3_tcp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified TCP Client configurations."""
        endpoint = "/dnp3/tcp/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dnp3_tcp_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified TCP Client configurations."""
        return [self.delete_dnp3_tcp_config_by_id(tcp_id) for tcp_id in config]

    def get_dnp3_tcp_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified TCP Client configuration."""
        endpoint = f"/dnp3/tcp/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_dnp3_tcp_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified TCP Client configuration."""
        endpoint = f"/dnp3/tcp/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dnp3_tcp_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified TCP Client configuration."""
        endpoint = f"/dnp3/tcp/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_dnp3_tcp_status(self) -> dict[str, Any]:
        """Returns TCP Client status."""
        endpoint = "/dnp3/tcp/status"

        return self._api_client.get(endpoint)

    def dnp3_tcp_actions_test_request(self, data: dict[str, Any]) -> dict[str, Any]:
        """Test request configuration."""
        endpoint = "/dnp3/tcp/actions/test_request"

        return self._api_client.post(endpoint, data={"data": data})

    def dnp3_serial_actions_test_request(self, data: dict[str, Any]) -> dict[str, Any]:
        """Test request configuration."""
        endpoint = "/dnp3/serial/actions/test_request"

        return self._api_client.post(endpoint, data={"data": data})

    def get_dnp3_serial_outstation_config(self) -> dict[str, Any]:
        """Returns specified Serial Outstation configuration."""
        endpoint = "/dnp3/serial_outstation/config"

        return self._api_client.get(endpoint)

    def update_dnp3_serial_outstation_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Serial Outstation configuration."""
        endpoint = "/dnp3/serial_outstation/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_dnp3_serial_outstation_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns all Serial Outstation configuration."""
        endpoint = f"/dnp3/serial_outstation/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_dnp3_serial_outstation_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified Serial Outstation configurations."""
        endpoint = f"/dnp3/serial_outstation/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_dnp3_serial_outstation_status(self) -> dict[str, Any]:
        """Returns Serial Outstation status."""
        endpoint = "/dnp3/serial_outstation/status"

        return self._api_client.get(endpoint)

    def get_dnp3_serial_outstation_objects_config(self) -> dict[str, Any]:
        """Returns all Serial Outstation Object configurations.

        Data sources can be found using /universal_gateway/options endpoint.
        """
        endpoint = "/dnp3/serial_outstation/objects/config"

        return self._api_client.get(endpoint)

    def create_dnp3_serial_outstation_objects_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a Serial Outstation Object configuration."""
        endpoint = "/dnp3/serial_outstation/objects/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_dnp3_serial_outstation_objects_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Serial Outstation Object configuration.

        Data sources can be found using /universal_gateway/options endpoint.
        """
        endpoint = "/dnp3/serial_outstation/objects/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dnp3_serial_outstation_objects_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Serial Outstation Object configurations."""
        return [self.delete_dnp3_serial_outstation_objects_config_by_id(obj_id) for obj_id in config]

    def get_dnp3_serial_outstation_objects_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Serial Outstation Object configuration.

        Data sources can be found using /universal_gateway/options endpoint.
        """
        endpoint = f"/dnp3/serial_outstation/objects/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_dnp3_serial_outstation_objects_config_by_id(
        self, config_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified Serial Outstation Object configuration.

        Data sources can be found using /universal_gateway/options endpoint.
        """
        endpoint = f"/dnp3/serial_outstation/objects/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dnp3_serial_outstation_objects_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified Serial Outstation Object configuration."""
        endpoint = f"/dnp3/serial_outstation/objects/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_dnp3_global(self) -> dict[str, Any]:
        """Returns all DNP3 global settings configurations."""
        endpoint = "/dnp3/global"

        return self._api_client.get(endpoint)

    def update_dnp3_global(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified DNP3 global settings configurations."""
        endpoint = "/dnp3/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_dnp3_database_entries_status(self) -> dict[str, Any]:
        """Returns all DNP3 database entries."""
        endpoint = "/dnp3/database/entries/status"

        return self._api_client.get(endpoint)

    def get_dnp3_serial_config(self) -> dict[str, Any]:
        """Returns all Serial Client configuration."""
        endpoint = "/dnp3/serial/config"

        return self._api_client.get(endpoint)

    def create_dnp3_serial_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Serial Client configuration."""
        endpoint = "/dnp3/serial/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_dnp3_serial_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Serial Client configurations."""
        endpoint = "/dnp3/serial/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dnp3_serial_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Serial Client configurations."""
        return [self.delete_dnp3_serial_config_by_id(serial_id) for serial_id in config]

    def get_dnp3_serial_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified Serial Client configuration."""
        endpoint = f"/dnp3/serial/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_dnp3_serial_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified Serial Client configuration."""
        endpoint = f"/dnp3/serial/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dnp3_serial_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified Serial Client configuration."""
        endpoint = f"/dnp3/serial/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_dnp3_serial_status(self) -> dict[str, Any]:
        """Returns Serial Client status."""
        endpoint = "/dnp3/serial/status"

        return self._api_client.get(endpoint)

    def get_dnp3_outstation_config(self) -> dict[str, Any]:
        """Returns specified TCP Outstation configuration."""
        endpoint = "/dnp3/outstation/config"

        return self._api_client.get(endpoint)

    def update_dnp3_outstation_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified TCP Outstation configuration."""
        endpoint = "/dnp3/outstation/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_dnp3_outstation_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns all TCP Outstation configuration."""
        endpoint = f"/dnp3/outstation/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_dnp3_outstation_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified TCP Outstation configurations."""
        endpoint = f"/dnp3/outstation/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_dnp3_outstation_status(self) -> dict[str, Any]:
        """Returns Outstation status."""
        endpoint = "/dnp3/outstation/status"

        return self._api_client.get(endpoint)

    def get_dnp3_outstation_objects_config(self) -> dict[str, Any]:
        """Returns all TCP Outstation Object configurations.

        Data sources can be found using /universal_gateway/options endpoint.
        """
        endpoint = "/dnp3/outstation/objects/config"

        return self._api_client.get(endpoint)

    def create_dnp3_outstation_objects_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a TCP Outstation Object configuration."""
        endpoint = "/dnp3/outstation/objects/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_dnp3_outstation_objects_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified TCP Outstation Object configuration.

        Data sources can be found using /universal_gateway/options endpoint.
        """
        endpoint = "/dnp3/outstation/objects/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dnp3_outstation_objects_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified TCP Outstation Object configurations."""
        return [self.delete_dnp3_outstation_objects_config_by_id(obj_id) for obj_id in config]

    def get_dnp3_outstation_objects_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Return TCP Outstation Object configuration.

        Data sources can be found using /universal_gateway/options endpoint.
        """
        endpoint = f"/dnp3/outstation/objects/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_dnp3_outstation_objects_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified TCP Outstation Object configuration.

        Data sources can be found using /universal_gateway/options endpoint.
        """
        endpoint = f"/dnp3/outstation/objects/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dnp3_outstation_objects_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified TCP Outstation Object configuration."""
        endpoint = f"/dnp3/outstation/objects/config/{config_id}"

        return self._api_client.delete(endpoint)
