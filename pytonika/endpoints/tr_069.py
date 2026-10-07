from typing import Any

from ._endpoint import Endpoint, File


class TR069(Endpoint):
    def get_tr069_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the TR-069 configuration in an array."""
        return self._client.request("GET", "/tr069/config", params={"all_options": all_options})

    def update_tr069_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the TR-069 configuration in an array."""
        return self._client.request("PUT", "/tr069/config", json={"data": config})

    def get_tr069_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the TR-069 configuration."""
        return self._client.request("GET", f"/tr069/config/{config_id}", params={"all_options": all_options})

    def upload_tr069_config_by_id(self, config_id: str, file: File, *, option: str | None = None) -> dict[str, Any]:
        """Uploads necessary files for TR-069 configuration."""
        return self._client.request("POST", f"/tr069/config/{config_id}", files={"file": file}, form={"option": option})

    def update_tr069_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the TR-069 configuration."""
        return self._client.request("PUT", f"/tr069/config/{config_id}", json={"data": config})
