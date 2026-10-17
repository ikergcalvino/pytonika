from typing import Any

from ._endpoint import Endpoint


class Unauthorized(Endpoint):
    """Endpoints of the "Unauthorized" page of the Teltonika Web API reference."""

    def get_unauthorized_status(self) -> dict[str, Any]:
        """Get basic device info."""
        return self._client.request("GET", "/unauthorized/status")
