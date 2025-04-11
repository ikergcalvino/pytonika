"""
Endpoints that don't require authentication for Teltonika routers.

This module provides access to router functionality that can be used
without authentication, such as basic device information and public resources.
"""

from typing import Dict, Any, Tuple, Union, List


class Unauthorized:
    """
    Handles API endpoints that don't require authentication.

    These endpoints can be accessed without a valid session token and
    typically provide basic device information or public resources.
    """

    def __init__(self, router):
        """
        Initialize the unauthorized endpoints.

        Args:
            router: The Router instance to use for API requests.
        """
        self._router = router

    def get_unauthorized_status(self) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        """
        Get basic device info.

        Endpoint: GET /unauthorized/status

        Returns:
            For successful request:
                (True, data) where data contains device information including language,
                device name, model, API version, device identifier, and security banner.
        """
        endpoint = "/unauthorized/status"
        return self._router._get_request(endpoint)
