from typing import Any

from ._endpoint import Endpoint


class STP(Endpoint):
    def get_rstp_status(self) -> dict[str, Any]:
        """Returns rapid spanning tree status."""
        return self._client.request("GET", "/rstp/status")

    def get_stp_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns spanning tree configuration."""
        return self._client.request("GET", "/stp/global", params={"all_options": all_options})

    def update_stp_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates spanning tree configuration."""
        return self._client.request("PUT", "/stp/global", json={"data": config})

    def get_stp_status(self) -> dict[str, Any]:
        """Returns spanning tree status."""
        return self._client.request("GET", "/stp/status")
