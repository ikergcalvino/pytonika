from .._client import APIClient


class Firewall:
    def __init__(self, api_client: APIClient) -> None:
        self._api_client = api_client

    def get_firewall_connections_status(self) -> dict[str, object]:
        endpoint = "/firewall/connections/status"

        return self._api_client.get(endpoint)

    def get_firewall_port_forwards_config(self) -> dict[str, object]:
        endpoint = "/firewall/port_forwards/config"

        return self._api_client.get(endpoint)

    def create_firewall_port_forwards_config(self, config: dict[str, object]) -> dict[str, object]:
        endpoint = "/firewall/port_forwards/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_firewall_port_forwards_config(self, config: list[dict[str, object]]) -> dict[str, object]:
        endpoint = "/firewall/port_forwards/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_firewall_port_forwards_config(self, config: list[str]) -> dict[str, object]:
        endpoint = "/firewall/port_forwards/config"

        data = {"data": config}

        return self._api_client.delete(endpoint, data=data)

    def get_firewall_port_forwards_config_by_id(self, port_forward_id: str) -> dict[str, object]:
        endpoint = f"/firewall/port_forwards/config/{port_forward_id}"

        return self._api_client.get(endpoint)

    def update_firewall_port_forwards_config_by_id(self, port_forward_id: str, config: dict[str, object]) -> dict[str, object]:
        endpoint = f"/firewall/port_forwards/config/{port_forward_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_firewall_port_forwards_config_by_id(self, port_forward_id: str) -> dict[str, object]:
        endpoint = f"/firewall/port_forwards/config/{port_forward_id}"

        return self._api_client.delete(endpoint)
