from typing import Any

from ._endpoint import Endpoint


class Serial(Endpoint):
    def get_serial_options(self) -> dict[str, Any]:
        """Returns available serial options."""
        return self._client.request("GET", "/serial/options")

    def get_serial_status(self) -> dict[str, Any]:
        """Returns Serial usage status."""
        return self._client.request("GET", "/serial/status")
