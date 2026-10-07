from typing import Any

from ._endpoint import Endpoint


class Thingworx(Endpoint):
    def get_thingworx_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the ThingWorx configuration in an array."""
        return self._client.request("GET", "/thingworx/config", params={"all_options": all_options})

    def update_thingworx_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the ThingWorx configuration in an array."""
        return self._client.request("PUT", "/thingworx/config", json={"data": config})

    def get_thingworx_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the ThingWorx configuration."""
        return self._client.request("GET", f"/thingworx/config/{config_id}", params={"all_options": all_options})

    def update_thingworx_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the ThingWorx configuration."""
        return self._client.request("PUT", f"/thingworx/config/{config_id}", json={"data": config})
