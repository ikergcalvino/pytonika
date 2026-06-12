from typing import Any

from ._base import Endpoint


class SiteManagerClientStatus(Endpoint):
    def get_site_manager_status(self) -> dict[str, Any]:
        """Get Site Manager Client status."""
        endpoint = "/site_manager/status"

        return self._api_client.get(endpoint)
