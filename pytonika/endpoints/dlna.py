from typing import Any

from ._endpoint import Endpoint


class DLNA(Endpoint):
    def get_minidlna_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the minidlna configuration."""
        return self._client.request("GET", "/minidlna/config", params={"all_options": all_options})

    def update_minidlna_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the minidlna configuration."""
        return self._client.request("PUT", "/minidlna/config", json={"data": config})

    def get_minidlna_config_by_id(self, dlna_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the minidlna configuration."""
        return self._client.request("GET", f"/minidlna/config/{dlna_id}", params={"all_options": all_options})

    def update_minidlna_config_by_id(self, dlna_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the minidlna configuration."""
        return self._client.request("PUT", f"/minidlna/config/{dlna_id}", json={"data": config})

    def get_minidlna_options(self) -> dict[str, Any]:
        """Get available dlna interfaces."""
        return self._client.request("GET", "/minidlna/options")

    def get_minidlna_status(self) -> dict[str, Any]:
        """Get minidlna status."""
        return self._client.request("GET", "/minidlna/status")
