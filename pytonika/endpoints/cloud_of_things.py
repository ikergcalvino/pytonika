from typing import Any

from ._endpoint import Endpoint


class CloudOfThings(Endpoint):
    def cloud_of_things_actions_reset_auth(self) -> dict[str, Any]:
        """Resets authentication data."""
        return self._client.request("POST", "/cloud_of_things/actions/reset_auth")

    def get_cloud_of_things_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Cloud of Things configuration in an array."""
        return self._client.request("GET", "/cloud_of_things/config", params={"all_options": all_options})

    def update_cloud_of_things_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Cloud of Things configuration in an array."""
        return self._client.request("PUT", "/cloud_of_things/config", json={"data": config})

    def get_cloud_of_things_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Cloud of Things configuration."""
        return self._client.request("GET", f"/cloud_of_things/config/{config_id}", params={"all_options": all_options})

    def update_cloud_of_things_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Cloud of Things configuration."""
        return self._client.request("PUT", f"/cloud_of_things/config/{config_id}", json={"data": config})

    def get_cloud_of_things_status(self) -> dict[str, Any]:
        """Returns Cloud of Things status."""
        return self._client.request("GET", "/cloud_of_things/status")
