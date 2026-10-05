from typing import Any

from ._endpoint import Endpoint


class Relayd(Endpoint):
    def get_relayd_config(self) -> dict[str, Any]:
        """Returns Relayd configurations."""
        endpoint = "/relayd/config"

        return self._client.request("GET", endpoint)

    def create_relayd_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Relayd configration."""
        endpoint = "/relayd/config"

        data = {"data": config}

        return self._client.request("POST", endpoint, json=data)

    def update_relayd_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Relayd configurations."""
        endpoint = "/relayd/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_relayd_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes Relayd configurations."""
        return [self.delete_relayd_config_by_id(config_id) for config_id in config]

    def get_relayd_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Relayd configuration."""
        endpoint = f"/relayd/config/{config_id}"

        return self._client.request("GET", endpoint)

    def update_relayd_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Relayd configuration."""
        endpoint = f"/relayd/config/{config_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_relayd_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes Relayd configuration."""
        endpoint = f"/relayd/config/{config_id}"

        return self._client.request("DELETE", endpoint)
