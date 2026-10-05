from typing import Any

from ._endpoint import Endpoint


class Unauthorized(Endpoint):
    def get_unauthorized_status(self) -> dict[str, Any]:
        """Get basic device info."""
        endpoint = "/unauthorized/status"

        return self._client.request("GET", endpoint)
