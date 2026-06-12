from typing import Any

from ._base import Endpoint


class Diagnostics(Endpoint):
    def ping(self, data: dict[str, Any]) -> dict[str, Any]:
        """Send ping command."""
        endpoint = "/diagnostics/actions/ping"

        return self._api_client.post(endpoint, data={"data": data})

    def traceroute(self, data: dict[str, Any]) -> dict[str, Any]:
        """Send traceroute command."""
        endpoint = "/diagnostics/actions/traceroute"

        return self._api_client.post(endpoint, data={"data": data})

    def nslookup(self, data: dict[str, Any]) -> dict[str, Any]:
        """Send nslookup command."""
        endpoint = "/diagnostics/actions/nslookup"

        return self._api_client.post(endpoint, data={"data": data})
