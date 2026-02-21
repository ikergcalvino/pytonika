from typing import Any

from ._base import Endpoint


class Firewall(Endpoint):
    def get_firewall_connections_status(self) -> dict[str, Any]:
        endpoint = "/firewall/connections/status"

        return self._api_client.get(endpoint)

    def get_firewall_port_forwards_config(self) -> dict[str, Any]:
        endpoint = "/firewall/port_forwards/config"

        return self._api_client.get(endpoint)

    def create_firewall_port_forwards_config(self, config: dict[str, Any]) -> dict[str, Any]:
        endpoint = "/firewall/port_forwards/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_firewall_port_forwards_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        endpoint = "/firewall/port_forwards/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_firewall_port_forwards_config(self, config: list[str]) -> list[dict[str, Any]]:
        return [
            self.delete_firewall_port_forwards_config_by_id(port_forward_id)
            for port_forward_id in config
        ]

    def get_firewall_port_forwards_config_by_id(self, port_forward_id: str) -> dict[str, Any]:
        endpoint = f"/firewall/port_forwards/config/{port_forward_id}"

        return self._api_client.get(endpoint)

    def update_firewall_port_forwards_config_by_id(
        self, port_forward_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        endpoint = f"/firewall/port_forwards/config/{port_forward_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_firewall_port_forwards_config_by_id(self, port_forward_id: str) -> dict[str, Any]:
        endpoint = f"/firewall/port_forwards/config/{port_forward_id}"

        return self._api_client.delete(endpoint)
