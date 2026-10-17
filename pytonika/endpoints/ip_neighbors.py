from typing import Any

from ._endpoint import Endpoint


class IPNeighbors(Endpoint):
    """Endpoints of the "IP Neighbors" page of the Teltonika Web API reference."""

    def get_ip_neighbors_ipv4_status(self) -> dict[str, Any]:
        """Returns ARP tables."""
        return self._client.request("GET", "/ip_neighbors/ipv4/status")

    def get_ip_neighbors_ipv6_status(self) -> dict[str, Any]:
        """Returns IPv6 neighbors."""
        return self._client.request("GET", "/ip_neighbors/ipv6/status")
