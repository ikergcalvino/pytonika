from typing import Any

from ._base import Endpoint


class STP(Endpoint):
    def get_stp_global(self) -> dict[str, Any]:
        """Returns spanning tree configuration."""
        endpoint = "/stp/global"

        return self._api_client.get(endpoint)

    def update_stp_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates spanning tree configuration."""
        endpoint = "/stp/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_stp_status(self) -> dict[str, Any]:
        """Returns spanning tree status."""
        endpoint = "/stp/status"

        return self._api_client.get(endpoint)

    def get_rstp_status(self) -> dict[str, Any]:
        """Returns rapid spanning tree status."""
        endpoint = "/rstp/status"

        return self._api_client.get(endpoint)
