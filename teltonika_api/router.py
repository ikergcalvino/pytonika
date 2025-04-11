#!/usr/bin/env python3

import requests
from typing import Dict, Any, Tuple, Optional, List, Union

from .endpoints.unauthorized import Unauthorized
from .endpoints.authentication import Authentication


class Router:
    """
    Central client class for interacting with Teltonika router APIs.

    This class serves as the main entry point for all API operations, managing
    the connection, authentication, and request handling. It provides access to
    all API functionality through organized endpoint groups.
    """

    def __init__(self, url: str):
        """
        Initialize a Teltonika router client.

        Args:
            url: Base URL of the router (e.g., "https://192.168.1.1").
                The "/api" path will be automatically appended.
        """
        self.api_url = url.rstrip("/") + "/api"
        self._token = None
        self._session = requests.Session()

        self.auth = Authentication(self)
        self.unauthorized = Unauthorized(self)

        self._setup_direct_methods()

    def _setup_direct_methods(self):
        """
        Setup direct access to commonly used methods from endpoints.

        Creates shortcuts to frequently used endpoint methods at the Router level.
        """
        self.get_device_info = self.unauthorized.get_status

        self.login = self.auth.login
        self.logout = self.auth.logout
        self.get_session_status = self.auth.get_session_status

    # --------------------------------------------------------------------------
    # Private HTTP request methods
    # --------------------------------------------------------------------------

    def _get_auth_headers(self) -> Dict[str, str]:
        """
        Construct the authorization headers for authenticated requests.

        Returns:
            Dictionary with headers including:
            - Content-Type: application/json
            - Authorization: Bearer token (if authenticated)
        """
        headers = {"Content-Type": "application/json"}

        if self._token:
            headers["Authorization"] = f"Bearer {self._token}"

        return headers

    def _make_request(self,
                      method: str,
                      endpoint: str,
                      data: Optional[Dict[str, Any]] = None,
                      params: Optional[Dict[str, Any]] = None) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        """
        Execute an HTTP request to the router's API.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE).
            endpoint: API endpoint path (with leading slash).
            data: JSON data for request body.
            params: URL query parameters.

        Returns:
            For successful requests:
                (True, response_data): Where response_data contains the API response.

            For failed requests:
                (False, error_list): Where error_list contains error details with:
                - source: Origin of the error (API, client, etc.)
                - error: Error message
                - code: Error code
        """
        url = f"{self.api_url}{endpoint}"

        try:
            response = self._session.request(
                method=method.upper(),
                url=url,
                json=data,
                params=params,
                headers=self._get_auth_headers(),
                timeout=10
            )

            result = response.json()

            if response.ok and result.get("success", False):
                return True, result.get("data", {})
            else:
                return False, result.get("errors", [])

        except requests.exceptions.RequestException as e:
            return False, [{"source": "client", "error": str(e), "code": 0}]
        except ValueError as e:  # JSON parsing error
            return False, [{"source": "client", "error": f"Invalid JSON response: {str(e)}", "code": 0}]

    def _get_request(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        """
        Execute a GET request to the router's API.
        """
        return self._make_request("GET", endpoint, params=params)

    def _post_request(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        """
        Execute a POST request to the router's API.
        """
        return self._make_request("POST", endpoint, data=data)

    def _put_request(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        """
        Execute a PUT request to the router's API.
        """
        return self._make_request("PUT", endpoint, data=data)

    def _delete_request(self, endpoint: str) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        """
        Execute a DELETE request to the router's API.
        """
        return self._make_request("DELETE", endpoint)
