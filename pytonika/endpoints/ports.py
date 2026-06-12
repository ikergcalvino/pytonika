from typing import Any

from ._base import Endpoint


class Ports(Endpoint):
    def get_ports_traffic_errors_status(self) -> dict[str, Any]:
        """Returns port status."""
        endpoint = "/ports/traffic/errors/status"

        return self._api_client.get(endpoint)
