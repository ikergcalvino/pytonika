from typing import Any

from ._base import Endpoint


class Services(Endpoint):
    def get_services_status(self) -> dict[str, Any]:
        """Returns information about installed services on the device."""
        endpoint = "/services/status"

        return self._api_client.get(endpoint)
