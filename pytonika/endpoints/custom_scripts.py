from typing import Any

from ._base import Endpoint


class CustomScripts(Endpoint):
    def get_uscripts_config(self) -> dict[str, Any]:
        """Returns startup script file contents."""
        endpoint = "/uscripts/config"

        return self._api_client.get(endpoint)

    def upload_uscripts(self, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads a startup script file."""
        endpoint = "/uscripts/actions/upload"

        return self._api_client.post(endpoint, data={"data": data})
