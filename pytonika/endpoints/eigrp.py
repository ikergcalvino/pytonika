from typing import Any

from ._base import Endpoint


class EIGRP(Endpoint):
    def get_eigrp_config(self) -> dict[str, Any]:
        """Returns EIGRP global configurations."""
        endpoint = "/eigrp/config"

        return self._api_client.get(endpoint)

    def update_eigrp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates EIGRP global configurations."""
        endpoint = "/eigrp/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_eigrp_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns EIGRP global configuration."""
        endpoint = f"/eigrp/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_eigrp_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates EIGRP global configuration."""
        endpoint = f"/eigrp/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_eigrp_status(self) -> dict[str, Any]:
        """Fetches data about EIGRP neighbors."""
        endpoint = "/eigrp/status"

        return self._api_client.get(endpoint)
