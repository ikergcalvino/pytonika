"""
Authentication-related API endpoints for Teltonika routers.

This module provides interfaces for user authentication, session management,
and secure access to the router's API. It handles user login, session validation,
and proper logout procedures.
"""

from typing import Dict, Any, Tuple, Union, List


class Authentication:
    """
    Handles authentication and session management for Teltonika routers.

    This class provides methods for authenticating users, managing API sessions, 
    and maintaining security credentials. It is responsible for obtaining and
    storing authentication tokens required for accessing protected endpoints.
    """

    def __init__(self, router):
        """
        Initialize the authentication endpoints.

        Args:
            router: The Router instance to use for API requests.
        """
        self._router = router

    def login(self, username: str, password: str) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        """
        Authenticate user for API access.

        Endpoint: POST /login

        Args:
            username: Username for authentication.
            password: Password for authentication.

        Returns:
            For successful authentication:
                (True, data) where data contains username, token and expiration time.

            For authentication failure:
                (False, errors) where errors contains error details.
        """
        endpoint = "/login"
        login_data = {"username": username, "password": password}

        success, response = self._router._post_request(endpoint, login_data)

        if success and "token" in response:
            self._router._token = response.get("token")

        return success, response

    def logout(self) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        """
        Logs out user from API.

        Endpoint: POST /logout

        Returns:
            For successful logout:
                (True, data) where data contains a confirmation message.
        """
        endpoint = "/logout"
        success, response = self._router._post_request(endpoint)

        if success:
            self._router._token = None
            self._router._session.cookies.clear()

        return success, response

    def get_session_status(self) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        """
        Returns if API session is alive and resets session's timer.

        Endpoint: GET /session/status

        Returns:
            For successful request:
                (True, data) where data indicates if the session is active.
        """
        endpoint = "/session/status"
        return self._router._get_request(endpoint)
