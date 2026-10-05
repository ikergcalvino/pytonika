from typing import Any

from ._base import Endpoint


class ForwardingTable(Endpoint):
    def get_forwarding_table_status(self) -> dict[str, Any]:
        """Returns forwarding table data."""
        endpoint = "/forwarding_table/status"

        return self._client.request("GET", endpoint)
