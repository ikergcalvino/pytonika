from typing import Any

from ._endpoint import Endpoint


class Services(Endpoint):
    def get_services_status(self) -> dict[str, Any]:
        """Returns information about installed services on the device."""
        endpoint = "/services/status"

        return self._client.request("GET", endpoint)
