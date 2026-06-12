from typing import Any

from ._base import Endpoint


class IPNeighbors(Endpoint):
    def get_ip_neighbors_ipv4_status(self) -> dict[str, Any]:
        """Returns ARP tables."""
        endpoint = "/ip_neighbors/ipv4/status"

        return self._api_client.get(endpoint)

    def get_ip_neighbors_ipv6_status(self) -> dict[str, Any]:
        """Returns IPv6 neighbors."""
        endpoint = "/ip_neighbors/ipv6/status"

        return self._api_client.get(endpoint)
