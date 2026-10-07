from typing import Any

from ._endpoint import Endpoint


class Topology(Endpoint):
    def topology_actions_devices_scan(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Get devices information."""
        return self._client.request(
            "POST", "/topology/actions/devices_scan", json=None if data is None else {"data": data}
        )

    def topology_actions_start_scan(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Start topology scan."""
        return self._client.request(
            "POST", "/topology/actions/start_scan", json=None if data is None else {"data": data}
        )

    def get_topology_scan_status(self, *, vendor: bool | None = None) -> dict[str, Any]:
        """Get history of started scans."""
        return self._client.request("GET", "/topology/scan/status", params={"vendor": vendor})

    def get_topology_status(self) -> dict[str, Any]:
        """Get interfaces information for devices scanning."""
        return self._client.request("GET", "/topology/status")
