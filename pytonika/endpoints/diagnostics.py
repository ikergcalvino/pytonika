from typing import Any

from ._endpoint import Endpoint


class Diagnostics(Endpoint):
    def diagnostics_actions_nslookup(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Send nslookup command."""
        return self._client.request(
            "POST", "/diagnostics/actions/nslookup", json=None if data is None else {"data": data}
        )

    def diagnostics_actions_ping(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Send ping command."""
        return self._client.request("POST", "/diagnostics/actions/ping", json=None if data is None else {"data": data})

    def diagnostics_actions_traceroute(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Send traceroute command."""
        return self._client.request(
            "POST", "/diagnostics/actions/traceroute", json=None if data is None else {"data": data}
        )
