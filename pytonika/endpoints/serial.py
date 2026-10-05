from typing import Any

from ._base import Endpoint


class Serial(Endpoint):
    def get_serial_status(self) -> dict[str, Any]:
        """Returns Serial usage status."""
        endpoint = "/serial/status"

        return self._client.request("GET", endpoint)

    def get_serial_options(self) -> dict[str, Any]:
        """Returns available serial options."""
        endpoint = "/serial/options"

        return self._client.request("GET", endpoint)
