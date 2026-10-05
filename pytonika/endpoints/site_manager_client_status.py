from typing import Any

from ._endpoint import Endpoint


class SiteManagerClientStatus(Endpoint):
    def get_site_manager_status(self) -> dict[str, Any]:
        """Get Site Manager Client status."""
        endpoint = "/site_manager/status"

        return self._client.request("GET", endpoint)
