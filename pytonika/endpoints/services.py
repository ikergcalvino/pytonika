from typing import Any

from ._endpoint import Endpoint


class Services(Endpoint):
    """Endpoints of the "Services" page of the Teltonika Web API reference."""

    def get_services_status(self) -> dict[str, Any]:
        """Returns information about installed services on the device."""
        return self._client.request("GET", "/services/status")
