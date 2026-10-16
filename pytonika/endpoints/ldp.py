from typing import Any

from ._endpoint import Endpoint


class LDP(Endpoint):
    def get_mpls_ldp_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns LDP global configuration."""
        return self._client.request("GET", "/mpls/ldp/global", params={"all_options": all_options})

    def update_mpls_ldp_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates LDP global configuration."""
        return self._client.request("PUT", "/mpls/ldp/global", json={"data": config})
