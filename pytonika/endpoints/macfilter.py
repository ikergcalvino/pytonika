from typing import Any

from ._base import Endpoint


class MACFilter(Endpoint):
    def get_macfilter_config(self) -> dict[str, Any]:
        """Returns all Macfilter configurations."""
        endpoint = "/macfilter/config"

        return self._api_client.get(endpoint)

    def update_macfilter_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Macfilter configurations."""
        endpoint = "/macfilter/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_macfilter_config_by_id(self, macfilter_id: str) -> dict[str, Any]:
        """Returns the specified Macfilter configuration."""
        endpoint = f"/macfilter/config/{macfilter_id}"

        return self._api_client.get(endpoint)

    def update_macfilter_config_by_id(self, macfilter_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Macfilter configuration."""
        endpoint = f"/macfilter/config/{macfilter_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
