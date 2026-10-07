from typing import Any

from ._endpoint import Endpoint


class PortMirroring(Endpoint):
    def get_port_mirroring_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Port Mirroring configuration."""
        return self._client.request("GET", "/port_mirroring/config", params={"all_options": all_options})

    def update_port_mirroring_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Port Mirroring configuration."""
        return self._client.request("PUT", "/port_mirroring/config", json={"data": config})

    def get_port_mirroring_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Port Mirroring configuration."""
        return self._client.request("GET", f"/port_mirroring/config/{config_id}", params={"all_options": all_options})

    def update_port_mirroring_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Port Mirroring configuration."""
        return self._client.request("PUT", f"/port_mirroring/config/{config_id}", json={"data": config})
