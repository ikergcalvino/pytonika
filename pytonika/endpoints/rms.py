from typing import Any

from ._base import Endpoint


class RMS(Endpoint):
    def get_rms_status(self) -> dict[str, Any]:
        """Returns RMS Status."""
        endpoint = "/rms/status"

        return self._api_client.get(endpoint)

    def get_rms_config(self) -> dict[str, Any]:
        """Returns RMS configuration in an array."""
        endpoint = "/rms/config"

        return self._api_client.get(endpoint)

    def update_rms_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates RMS configuration in an array."""
        endpoint = "/rms/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_rms_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns RMS configuration."""
        endpoint = f"/rms/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_rms_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates RMS configuration."""
        endpoint = f"/rms/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def rms_connect(self, data: dict[str, Any]) -> dict[str, Any]:
        """Connect to RMS."""
        endpoint = "/rms/actions/connect"

        return self._api_client.post(endpoint, data={"data": data})

    def rms_unregister(self, data: dict[str, Any]) -> dict[str, Any]:
        """Unregister from RMS."""
        endpoint = "/rms/actions/unregister"

        return self._api_client.post(endpoint, data={"data": data})

    def get_rms_proxy_config(self) -> dict[str, Any]:
        """Returns RMS proxy configuration in an array."""
        endpoint = "/rms/proxy/config"

        return self._api_client.get(endpoint)

    def update_rms_proxy_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates RMS proxy configuration in an array."""
        endpoint = "/rms/proxy/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_rms_proxy_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns RMS proxy configuration."""
        endpoint = f"/rms/proxy/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_rms_proxy_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates RMS proxy configuration."""
        endpoint = f"/rms/proxy/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
