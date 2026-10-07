from typing import Any

from ._endpoint import Endpoint


class DMZ(Endpoint):
    def get_dmz_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns DMZ configuration settings."""
        return self._client.request("GET", "/dmz/config", params={"all_options": all_options})

    def update_dmz_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates DMZ configration settings."""
        return self._client.request("PUT", "/dmz/config", json={"data": config})

    def get_dmz_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns DMZ configuration settings."""
        return self._client.request("GET", f"/dmz/config/{config_id}", params={"all_options": all_options})

    def update_dmz_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates DMZ configration settings."""
        return self._client.request("PUT", f"/dmz/config/{config_id}", json={"data": config})
