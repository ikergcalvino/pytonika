from typing import Any

from ._endpoint import Endpoint


class Users(Endpoint):
    def get_users_acls_options(self) -> dict[str, Any]:
        """Returns current user's permissions (ACL's)."""
        return self._client.request("GET", "/users/acls/options")

    def get_users_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all users configurations."""
        return self._client.request("GET", "/users/config", params={"all_options": all_options})

    def create_users_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates users configuration."""
        return self._client.request("POST", "/users/config", json={"data": config})

    def update_users_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified users configurations."""
        return self._client.request("PUT", "/users/config", json={"data": config})

    def delete_users_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified users configurations."""
        return self._client.request("DELETE", "/users/config", json={"data": config})

    def get_users_config_by_id(self, user_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified users configuration."""
        return self._client.request("GET", f"/users/config/{user_id}", params={"all_options": all_options})

    def update_users_config_by_id(self, user_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified users configuration."""
        return self._client.request("PUT", f"/users/config/{user_id}", json={"data": config})

    def delete_users_config_by_id(self, user_id: str) -> dict[str, Any]:
        """Deletes the specified users configuration."""
        return self._client.request("DELETE", f"/users/config/{user_id}")

    def get_users_groups_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all groups configurations."""
        return self._client.request("GET", "/users/groups/config", params={"all_options": all_options})

    def create_users_groups_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new group configuration."""
        return self._client.request("POST", "/users/groups/config", json={"data": config})

    def update_users_groups_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified groups configurations."""
        return self._client.request("PUT", "/users/groups/config", json={"data": config})

    def delete_users_groups_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the specified group configurations."""
        return self._client.request("DELETE", "/users/groups/config", json={"data": config})

    def get_users_groups_config_by_id(self, group_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified groups configuration."""
        return self._client.request("GET", f"/users/groups/config/{group_id}", params={"all_options": all_options})

    def update_users_groups_config_by_id(self, group_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified groups configuration."""
        return self._client.request("PUT", f"/users/groups/config/{group_id}", json={"data": config})

    def delete_users_groups_config_by_id(self, group_id: str) -> dict[str, Any]:
        """Deletes the specified group configuration."""
        return self._client.request("DELETE", f"/users/groups/config/{group_id}")
