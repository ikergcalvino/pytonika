from typing import Any

from ._endpoint import Endpoint


class Cumulocity(Endpoint):
    def cumulocity_actions_reset_auth(self) -> dict[str, Any]:
        """Resets authentication data."""
        return self._client.request("POST", "/cumulocity/actions/reset_auth")

    def get_cumulocity_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Cumulocity configuration in an array."""
        return self._client.request("GET", "/cumulocity/config", params={"all_options": all_options})

    def update_cumulocity_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Cumulocity configuration in an array."""
        return self._client.request("PUT", "/cumulocity/config", json={"data": config})

    def get_cumulocity_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Cumulocity configuration."""
        return self._client.request("GET", f"/cumulocity/config/{config_id}", params={"all_options": all_options})

    def update_cumulocity_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Cumulocity configuration."""
        return self._client.request("PUT", f"/cumulocity/config/{config_id}", json={"data": config})

    def get_cumulocity_status(self) -> dict[str, Any]:
        """Returns Cumulocity status."""
        return self._client.request("GET", "/cumulocity/status")
