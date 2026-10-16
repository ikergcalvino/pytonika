from typing import Any

from ._endpoint import Endpoint


class ForwardingTable(Endpoint):
    def get_forwarding_table_status(self) -> dict[str, Any]:
        """Get forwarding table data."""
        return self._client.request("GET", "/forwarding_table/status")
