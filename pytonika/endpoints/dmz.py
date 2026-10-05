from typing import Any

from ._base import Endpoint


class DMZ(Endpoint):
    def get_dmz_config(self) -> dict[str, Any]:
        """Returns DMZ configuration settings."""
        endpoint = "/dmz/config"

        return self._client.request("GET", endpoint)

    def update_dmz_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates DMZ configration settings."""
        endpoint = "/dmz/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def get_dmz_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns DMZ configuration settings."""
        endpoint = f"/dmz/config/{config_id}"

        return self._client.request("GET", endpoint)

    def update_dmz_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates DMZ configration settings."""
        endpoint = f"/dmz/config/{config_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)
