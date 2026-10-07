from typing import Any

from ._endpoint import Endpoint, File


class CustomScripts(Endpoint):
    def uscripts_actions_upload(self, file: File) -> dict[str, Any]:
        """Uploads a startup script file."""
        return self._client.request("POST", "/uscripts/actions/upload", files={"file": file})

    def get_uscripts_config(self) -> dict[str, Any]:
        """Returns startup script file contents."""
        return self._client.request("GET", "/uscripts/config")

    def update_uscripts_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates startup script file contents."""
        return self._client.request("PUT", "/uscripts/config", json={"data": config})
