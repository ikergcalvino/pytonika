from typing import Any

from ._endpoint import Endpoint


class Relayd(Endpoint):
    def get_relayd_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Relayd configurations."""
        return self._client.request("GET", "/relayd/config", params={"all_options": all_options})

    def create_relayd_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Relayd configration."""
        return self._client.request("POST", "/relayd/config", json={"data": config})

    def update_relayd_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Relayd configurations."""
        return self._client.request("PUT", "/relayd/config", json={"data": config})

    def delete_relayd_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes Relayd configurations."""
        return self._client.request("DELETE", "/relayd/config", json={"data": config})

    def get_relayd_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Relayd configuration."""
        return self._client.request("GET", f"/relayd/config/{config_id}", params={"all_options": all_options})

    def update_relayd_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Relayd configuration."""
        return self._client.request("PUT", f"/relayd/config/{config_id}", json={"data": config})

    def delete_relayd_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes Relayd configuration."""
        return self._client.request("DELETE", f"/relayd/config/{config_id}")
