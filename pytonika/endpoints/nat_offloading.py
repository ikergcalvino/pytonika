from typing import Any

from ._base import Endpoint


class NATOffloading(Endpoint):
    def get_nat_offloading_global(self) -> dict[str, Any]:
        """Returns Firewall NAT Offloading settings."""
        endpoint = "/nat_offloading/global"

        return self._client.request("GET", endpoint)

    def update_nat_offloading_global(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall NAT Offloading settings."""
        endpoint = "/nat_offloading/global"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)
