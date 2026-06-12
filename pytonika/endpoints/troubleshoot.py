from typing import Any

from ._base import Endpoint


class Troubleshoot(Endpoint):
    def get_troubleshoot_config(self) -> dict[str, Any]:
        """Returns Troubleshoot configuration."""
        endpoint = "/troubleshoot/config"

        return self._api_client.get(endpoint)

    def create_troubleshoot_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Troubleshoot configuration."""
        endpoint = "/troubleshoot/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_troubleshoot_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Troubleshoot configuration."""
        endpoint = "/troubleshoot/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_troubleshoot_config_by_id(self, troubleshoot_id: str) -> dict[str, Any]:
        """Returns Troubleshoot configuration."""
        endpoint = f"/troubleshoot/config/{troubleshoot_id}"

        return self._api_client.get(endpoint)

    def update_troubleshoot_config_by_id(self, troubleshoot_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Troubleshoot configuration."""
        endpoint = f"/troubleshoot/config/{troubleshoot_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_troubleshoot_system_status(self) -> dict[str, Any]:
        """Returns system log contents."""
        endpoint = "/troubleshoot/system/status"

        return self._api_client.get(endpoint)

    def get_troubleshoot_kernel_status(self) -> dict[str, Any]:
        """Returns kernel log contents."""
        endpoint = "/troubleshoot/kernel/status"

        return self._api_client.get(endpoint)

    def download_troubleshoot(self) -> dict[str, Any]:
        """Downloads generated troubleshoot/tcpdump archive."""
        endpoint = "/troubleshoot/actions/download"

        return self._api_client.post(endpoint)

    def generate_troubleshoot(self) -> dict[str, Any]:
        """Generates troubleshoot archive."""
        endpoint = "/troubleshoot/actions/generate"

        return self._api_client.post(endpoint)
