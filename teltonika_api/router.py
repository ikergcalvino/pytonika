#!/usr/bin/env python3

import requests
from typing import Dict, Any, Tuple, Optional, List, Union


class Router:
    """
    API client for Teltonika routers.
    """

    def __init__(self, url: str):
        """
        Initialize a Teltonika router client.

        Args:
            url (str): The base URL of the router (e.g., "https://192.168.1.1").
                       The "/api" path will be automatically appended.
        """
        self.api_url = url.rstrip("/") + "/api"
        self._token = None
        self._session = requests.Session()

    # --------------------------------------------------------------------------
    # Private HTTP request methods
    # --------------------------------------------------------------------------

    def _get_auth_headers(self) -> Dict[str, str]:
        """
        Returns the authorization headers for authenticated requests.

        Returns:
            Dict[str, str]: Dictionary containing headers with authorization token if available.
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
            method (str): HTTP method (GET, POST, PUT, DELETE).
            endpoint (str): API endpoint path (with leading slash, e.g., "/login").
            data (Optional[Dict[str, Any]]): JSON data for request body.
            params (Optional[Dict[str, Any]]): URL query parameters.

        Returns:
            Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]: 
                A tuple containing (success, data / errors) where:
                - success (bool): True if the request was successful, False otherwise.
                - data / errors: Either the response data on success, or error details on failure.
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
