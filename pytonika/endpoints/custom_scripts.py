from typing import Any

from ._endpoint import Endpoint


class CustomScripts(Endpoint):
    def get_uscripts_config(self) -> dict[str, Any]:
        """Returns startup script file contents."""
        endpoint = "/uscripts/config"

        return self._client.request("GET", endpoint)

    def upload_uscripts(self, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads a startup script file."""
        endpoint = "/uscripts/actions/upload"

        return self._client.request("POST", endpoint, json={"data": data})
