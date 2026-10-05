from typing import Any

from ._base import Endpoint


class PortMirroring(Endpoint):
    def get_port_mirroring_config(self) -> dict[str, Any]:
        """Returns Port Mirroring configuration."""
        endpoint = "/port_mirroring/config"

        return self._client.request("GET", endpoint)

    def update_port_mirroring_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Port Mirroring configuration."""
        endpoint = "/port_mirroring/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def get_port_mirroring_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Port Mirroring configuration."""
        endpoint = f"/port_mirroring/config/{config_id}"

        return self._client.request("GET", endpoint)

    def update_port_mirroring_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Port Mirroring configuration."""
        endpoint = f"/port_mirroring/config/{config_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)
