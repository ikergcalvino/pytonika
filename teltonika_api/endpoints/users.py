"""
User management endpoints for Teltonika routers.

This module provides functionality to manage user accounts on the router,
including creating, retrieving, updating and deleting user configurations.
"""

from typing import Dict, Any, Tuple, Union, List


class Users:
    """
    Handles user management operations for Teltonika routers.

    Provides functionality to create, read, update and delete user configurations,
    manage user permissions, passwords, and SSH access settings.
    """

    def __init__(self, router):
        """
        Initialize the users endpoints.

        Args:
            router: The Router instance to use for API requests.
        """
        self._router = router

    def get_users_config(self) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        """
        Returns all users configurations.

        Endpoint: GET /users/config

        Returns:
            For successful request (200):
                (True, data) where data is a list of user configurations including
                id, username, group, and SSH access settings.
        """
        endpoint = "/users/config"
        return self._router._get_request(endpoint)

    def create_users_config(self, config: Dict[str, Any]) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        """
        Creates a user configuration.

        Endpoint: POST /users/config

        Args:
            config: User configuration including required fields:
                   - username: User login name
                   - password: User password
                   - group: User permission group
                   - ssh_enable: SSH access setting

        Returns:
            For successful creation (201):
                (True, data) where data contains the created user information
                including generated ID.

            For validation errors (422):
                (False, errors) where errors contains validation error details.
        """
        endpoint = "/users/config"
        return self._router._post_request(endpoint, data={"data": config})

    def update_users_config(self, configs: List[Dict[str, Any]]) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        """
        Updates specified users configurations.

        Endpoint: PUT /users/config

        Args:
            configs: List of user configurations to update. Each should include:
                    - id: User ID (required)
                    - group: User permission group (optional)
                    - current_password: Current password for verification (when changing password)
                    - password: New password (optional)
                    - password_confirm: Password confirmation (required with password)
                    - ssh_enable: SSH access setting (optional)

        Returns:
            For successful update (200):
                (True, data) where data is a list of updated user configurations.

            For not found (404):
                (False, errors) with information about users not found.

            For validation errors (422):
                (False, errors) where errors contains validation error details.
        """
        endpoint = "/users/config"
        return self._router._put_request(endpoint, data={"data": configs})

    def delete_users_config(self, user_ids: List[str]) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        """
        Deletes specified users configurations.

        Endpoint: DELETE /users/config

        Args:
            user_ids: List of user IDs to delete.

        Returns:
            For successful deletion (200):
                (True, data) where data is a list of deleted user IDs.

            For not found (404):
                (False, errors) with information about users not found.

            For validation errors (422):
                (False, errors) where errors contains validation error details.
        """
        endpoint = "/users/config"
        return self._router._delete_request(endpoint, data={"data": user_ids})

    def get_users_config_by_id(self, user_id: str) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        """
        Returns the specified user configuration.

        Endpoint: GET /users/config/{id}

        Args:
            user_id: ID of the user to retrieve.

        Returns:
            For successful request (200):
                (True, data) where data contains user configuration details.

            For not found (404):
                (False, errors) where errors contains information about the not found user.
        """
        endpoint = f"/users/config/{user_id}"
        return self._router._get_request(endpoint)

    def update_users_config_by_id(self, user_id: str, config: Dict[str, Any]) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        """
        Updates the specified user configuration.

        Endpoint: PUT /users/config/{id}

        Args:
            user_id: ID of the user to update.
            config: Updated user configuration which may include:
                   - group: User permission group
                   - current_password: Current password (for verification)
                   - password: New password
                   - password_confirm: Password confirmation
                   - ssh_enable: SSH access setting

        Returns:
            For successful update (200):
                (True, data) where data contains the updated user configuration.

            For not found (404):
                (False, errors) where errors contains information about the not found user.

            For validation errors (422):
                (False, errors) where errors contains validation error details.
        """
        endpoint = f"/users/config/{user_id}"
        return self._router._put_request(endpoint, data={"data": config})

    def delete_users_config_by_id(self, user_id: str) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        """
        Deletes the specified user configuration.

        Endpoint: DELETE /users/config/{id}

        Args:
            user_id: ID of the user to delete.

        Returns:
            For successful deletion (200):
                (True, data) where data contains the deleted user ID.

            For not found (404):
                (False, errors) where errors contains information about the not found user.

            For validation errors (422):
                (False, errors) where errors contains validation error details.
        """
        endpoint = f"/users/config/{user_id}"
        return self._router._delete_request(endpoint)
