from typing import Any

from ._endpoint import Endpoint


class RMS(Endpoint):
    def rms_actions_connect(self) -> dict[str, Any]:
        """Connect to RMS."""
        return self._client.request("POST", "/rms/actions/connect")

    def rms_actions_unregister(self) -> dict[str, Any]:
        """Unregister from RMS."""
        return self._client.request("POST", "/rms/actions/unregister")

    def get_rms_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns RMS configuration in an array."""
        return self._client.request("GET", "/rms/config", params={"all_options": all_options})

    def update_rms_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates RMS configuration in an array."""
        return self._client.request("PUT", "/rms/config", json={"data": config})

    def get_rms_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns RMS configuration."""
        return self._client.request("GET", f"/rms/config/{config_id}", params={"all_options": all_options})

    def update_rms_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates RMS configuration."""
        return self._client.request("PUT", f"/rms/config/{config_id}", json={"data": config})

    def get_rms_proxy_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns RMS proxy configuration in an array."""
        return self._client.request("GET", "/rms/proxy/config", params={"all_options": all_options})

    def update_rms_proxy_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates RMS proxy configuration in an array."""
        return self._client.request("PUT", "/rms/proxy/config", json={"data": config})

    def get_rms_proxy_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns RMS proxy configuration."""
        return self._client.request("GET", f"/rms/proxy/config/{config_id}", params={"all_options": all_options})

    def update_rms_proxy_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates RMS proxy configuration."""
        return self._client.request("PUT", f"/rms/proxy/config/{config_id}", json={"data": config})

    def get_rms_status(self) -> dict[str, Any]:
        """Returns RMS Status."""
        return self._client.request("GET", "/rms/status")
