from typing import Any

from ._endpoint import Endpoint


class MACFilter(Endpoint):
    def get_macfilter_config(self) -> dict[str, Any]:
        """Returns all Macfilter configurations."""
        return self._client.request("GET", "/macfilter/config")

    def update_macfilter_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Macfilter configurations."""
        return self._client.request("PUT", "/macfilter/config", json={"data": config})

    def get_macfilter_config_by_id(self, macfilter_id: str) -> dict[str, Any]:
        """Returns the specified Macfilter configuration."""
        return self._client.request("GET", f"/macfilter/config/{macfilter_id}")

    def update_macfilter_config_by_id(self, macfilter_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Macfilter configuration."""
        return self._client.request("PUT", f"/macfilter/config/{macfilter_id}", json={"data": config})
