from typing import Any

from ._endpoint import Endpoint


class LDP(Endpoint):
    def get_mpls_ldp_global(self) -> dict[str, Any]:
        """Returns LDP global configuration."""
        endpoint = "/mpls/ldp/global"

        return self._client.request("GET", endpoint)

    def update_mpls_ldp_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates LDP global configuration."""
        endpoint = "/mpls/ldp/global"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def get_mpls_ldp_status(self) -> dict[str, Any]:
        """Returns LDP status information."""
        endpoint = "/mpls/ldp/status"

        return self._client.request("GET", endpoint)
