from typing import Any

from ._endpoint import Endpoint


class DFOTA(Endpoint):
    def get_dfota_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns multiple DFOTA configurations."""
        return self._client.request("GET", "/dfota/config", params={"all_options": all_options})

    def update_dfota_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple DFOTA configurations."""
        return self._client.request("PUT", "/dfota/config", json={"data": config})

    def get_dfota_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns DFOTA configuration."""
        return self._client.request("GET", f"/dfota/config/{config_id}", params={"all_options": all_options})

    def update_dfota_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates DFOTA configuration."""
        return self._client.request("PUT", f"/dfota/config/{config_id}", json={"data": config})
