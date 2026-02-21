from typing import Any

from ._base import Endpoint


class Interfaces(Endpoint):
    def get_interfaces_config(self) -> dict[str, Any]:
        endpoint = "/interfaces/config"

        return self._api_client.get(endpoint)

    def create_interfaces_config(self, config: dict[str, Any]) -> dict[str, Any]:
        endpoint = "/interfaces/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_interfaces_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        endpoint = "/interfaces/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_interfaces_config(self, config: list[str]) -> list[dict[str, Any]]:
        return [
            self.delete_interfaces_config_by_id(interface_id)
            for interface_id in config
        ]

    def get_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        endpoint = f"/interfaces/config/{interface_id}"

        return self._api_client.get(endpoint)

    def update_interfaces_config_by_id(self, interface_id: str, config: dict[str, Any]) -> dict[str, Any]:
        endpoint = f"/interfaces/config/{interface_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        endpoint = f"/interfaces/config/{interface_id}"

        return self._api_client.delete(endpoint)

    def get_interfaces_status(self) -> dict[str, Any]:
        endpoint = "/interfaces/status"

        return self._api_client.get(endpoint)

    def get_interfaces_status_by_id(self, interface_id: str) -> dict[str, Any]:
        endpoint = f"/interfaces/status/{interface_id}"

        return self._api_client.get(endpoint)
