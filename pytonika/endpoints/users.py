from .._client import APIClient


class Users:
    def __init__(self, api_client: APIClient) -> None:
        self._api_client = api_client

    def get_users_config(self) -> dict[str, object]:
        endpoint = "/users/config"

        return self._api_client.get(endpoint)

    def create_users_config(self, config: dict[str, object]) -> dict[str, object]:
        endpoint = "/users/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_users_config(self, config: list[dict[str, object]]) -> dict[str, object]:
        endpoint = "/users/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_users_config(self, config: list[str]) -> dict[str, object]:
        endpoint = "/users/config"

        data = {"data": config}

        return self._api_client.delete(endpoint, data=data)

    def get_users_config_by_id(self, user_id: str) -> dict[str, object]:
        endpoint = f"/users/config/{user_id}"

        return self._api_client.get(endpoint)

    def update_users_config_by_id(self, user_id: str, config: dict[str, object]) -> dict[str, object]:
        endpoint = f"/users/config/{user_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_users_config_by_id(self, user_id: str) -> dict[str, object]:
        endpoint = f"/users/config/{user_id}"

        return self._api_client.delete(endpoint)
