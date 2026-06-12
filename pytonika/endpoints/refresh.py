from typing import Any

from ._base import Endpoint


class Refresh(Endpoint):
    def refresh(self, config: dict[str, Any]) -> dict[str, Any]:
        """Refresh endpoint.

        .. deprecated::
        """
        endpoint = "/refresh"

        return self._api_client.post(endpoint, data=config)
