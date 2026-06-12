from typing import Any

from ._base import Endpoint


class Profinet(Endpoint):
    def get_profinet_config(self) -> dict[str, Any]:
        """Returns all Profinet configurations."""
        endpoint = "/profinet/config"

        return self._api_client.get(endpoint)

    def update_profinet_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Profinet configurations."""
        endpoint = "/profinet/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_profinet_config_by_id(self, profinet_id: str) -> dict[str, Any]:
        """Returns the specified Profinet configuration."""
        endpoint = f"/profinet/config/{profinet_id}"

        return self._api_client.get(endpoint)

    def update_profinet_config_by_id(self, profinet_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Profinet configuration."""
        endpoint = f"/profinet/config/{profinet_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_profinet_status(self) -> dict[str, Any]:
        """Returns all status information."""
        endpoint = "/profinet/status"

        return self._api_client.get(endpoint)

    def profinet_actions_download_gsdml(self) -> dict[str, Any]:
        """Download GSDML file."""
        endpoint = "/profinet/actions/download_gsdml"

        return self._api_client.post(endpoint)
