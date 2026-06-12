from typing import Any

from ._base import Endpoint


class Users(Endpoint):
    def get_users_config(self) -> dict[str, Any]:
        """Returns all users configurations."""
        endpoint = "/users/config"

        return self._api_client.get(endpoint)

    def create_users_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates users configuration."""
        endpoint = "/users/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_users_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified users configurations."""
        endpoint = "/users/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_users_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified users configurations."""
        return [self.delete_users_config_by_id(user_id) for user_id in config]

    def get_users_config_by_id(self, user_id: str) -> dict[str, Any]:
        """Returns the specified users configuration."""
        endpoint = f"/users/config/{user_id}"

        return self._api_client.get(endpoint)

    def update_users_config_by_id(self, user_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified users configuration."""
        endpoint = f"/users/config/{user_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_users_config_by_id(self, user_id: str) -> dict[str, Any]:
        """Deletes the specified users configuration."""
        endpoint = f"/users/config/{user_id}"

        return self._api_client.delete(endpoint)

    def get_users_acls_options(self) -> dict[str, Any]:
        """Returns current user's permissions (ACL's)."""
        endpoint = "/users/acls/options"

        return self._api_client.get(endpoint)

    def get_users_groups_config(self) -> dict[str, Any]:
        """Returns all groups configurations."""
        endpoint = "/users/groups/config"

        return self._api_client.get(endpoint)

    def create_users_groups_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new group configuration."""
        endpoint = "/users/groups/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_users_groups_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified groups configurations."""
        endpoint = "/users/groups/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_users_groups_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the specified group configurations."""
        return [self.delete_users_groups_config_by_id(group_id) for group_id in config]

    def get_users_groups_config_by_id(self, group_id: str) -> dict[str, Any]:
        """Returns specified groups configuration."""
        endpoint = f"/users/groups/config/{group_id}"

        return self._api_client.get(endpoint)

    def update_users_groups_config_by_id(self, group_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified groups configuration."""
        endpoint = f"/users/groups/config/{group_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_users_groups_config_by_id(self, group_id: str) -> dict[str, Any]:
        """Deletes the specified group configuration."""
        endpoint = f"/users/groups/config/{group_id}"

        return self._api_client.delete(endpoint)
