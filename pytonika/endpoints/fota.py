from typing import Any

from ._endpoint import Endpoint


class FOTA(Endpoint):
    def get_fota_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Fota configuration."""
        return self._client.request("GET", "/fota/config", params={"all_options": all_options})

    def update_fota_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Fota configuration."""
        return self._client.request("PUT", "/fota/config", json={"data": config})

    def get_fota_config_by_id(self, fota_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Fota configuration."""
        return self._client.request("GET", f"/fota/config/{fota_id}", params={"all_options": all_options})

    def update_fota_config_by_id(self, fota_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Fota configuration."""
        return self._client.request("PUT", f"/fota/config/{fota_id}", json={"data": config})
