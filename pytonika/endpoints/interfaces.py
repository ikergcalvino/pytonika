from .._client import APIClient


class Interfaces:
    def __init__(self, api_client: APIClient) -> None:
        self._api_client = api_client

    def get_interfaces_config(self) -> dict[str, object]:
        endpoint = "/interfaces/config"

        return self._api_client.get(endpoint)

    def create_interfaces_config(self, config: dict[str, object]) -> dict[str, object]:
        endpoint = "/interfaces/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_interfaces_config(self, config: list[dict[str, object]]) -> dict[str, object]:
        endpoint = "/interfaces/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_interfaces_config(self, config: list[str]) -> dict[str, object]:
        endpoint = "/interfaces/config"

        data = {"data": config}

        return self._api_client.delete(endpoint, data=data)

    def get_interfaces_config_by_id(self, interface_id: str) -> dict[str, object]:
        endpoint = f"/interfaces/config/{interface_id}"

        return self._api_client.get(endpoint)

    def update_interfaces_config_by_id(self, interface_id: str, config: dict[str, object]) -> dict[str, object]:
        endpoint = f"/interfaces/config/{interface_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_interfaces_config_by_id(self, interface_id: str) -> dict[str, object]:
        endpoint = f"/interfaces/config/{interface_id}"

        return self._api_client.delete(endpoint)

    def get_interfaces_status(self) -> dict[str, object]:
        endpoint = "/interfaces/status"

        return self._api_client.get(endpoint)

    def get_interfaces_status_by_id(self, interface_id: str) -> dict[str, object]:
        endpoint = f"/interfaces/status/{interface_id}"

        return self._api_client.get(endpoint)
