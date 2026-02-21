from typing import Any

from ._base import Endpoint


class Users(Endpoint):
    def get_users_config(self) -> dict[str, Any]:
        endpoint = "/users/config"

        return self._api_client.get(endpoint)

    def create_users_config(self, config: dict[str, Any]) -> dict[str, Any]:
        endpoint = "/users/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_users_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        endpoint = "/users/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_users_config(self, config: list[str]) -> list[dict[str, Any]]:
        return [self.delete_users_config_by_id(user_id) for user_id in config]

    def get_users_config_by_id(self, user_id: str) -> dict[str, Any]:
        endpoint = f"/users/config/{user_id}"

        return self._api_client.get(endpoint)

    def update_users_config_by_id(self, user_id: str, config: dict[str, Any]) -> dict[str, Any]:
        endpoint = f"/users/config/{user_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_users_config_by_id(self, user_id: str) -> dict[str, Any]:
        endpoint = f"/users/config/{user_id}"

        return self._api_client.delete(endpoint)
