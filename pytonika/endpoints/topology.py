from typing import Any

from ._base import Endpoint


class Topology(Endpoint):
    def get_topology_status(self) -> dict[str, Any]:
        """Get interfaces information for devices scanning."""
        endpoint = "/topology/status"

        return self._api_client.get(endpoint)

    def get_topology_scan_status(self) -> dict[str, Any]:
        """Get history of started scans."""
        endpoint = "/topology/scan/status"

        return self._api_client.get(endpoint)

    def topology_start_scan(self, data: dict[str, Any]) -> dict[str, Any]:
        """Start topology scan."""
        endpoint = "/topology/actions/start_scan"

        return self._api_client.post(endpoint, data={"data": data})

    def topology_devices_scan(self, data: dict[str, Any]) -> dict[str, Any]:
        """Get devices information.

        .. deprecated::
            This endpoint is deprecated.
        """
        endpoint = "/topology/actions/devices_scan"

        return self._api_client.post(endpoint, data={"data": data})
