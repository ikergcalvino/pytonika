from typing import Any

from ._endpoint import Endpoint


class NATOffloading(Endpoint):
    def get_nat_offloading_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Firewall NAT Offloading settings."""
        return self._client.request("GET", "/nat_offloading/global", params={"all_options": all_options})

    def update_nat_offloading_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall NAT Offloading settings."""
        return self._client.request("PUT", "/nat_offloading/global", json={"data": config})
