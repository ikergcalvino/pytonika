from typing import Any

from ._endpoint import Endpoint


class Troubleshoot(Endpoint):
    def troubleshoot_actions_download(self, data: dict[str, Any] | None = None) -> bytes | dict[str, Any]:
        """Downloads generated troubleshoot/tcpdump archive."""
        return self._client.request(
            "POST", "/troubleshoot/actions/download", json=None if data is None else {"data": data}, download=True
        )

    def troubleshoot_actions_generate(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Generates troubleshoot archive."""
        return self._client.request(
            "POST", "/troubleshoot/actions/generate", json=None if data is None else {"data": data}
        )

    def get_troubleshoot_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Troubleshoot configuration."""
        return self._client.request("GET", "/troubleshoot/config", params={"all_options": all_options})

    def update_troubleshoot_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Troubleshoot configuration."""
        return self._client.request("PUT", "/troubleshoot/config", json={"data": config})

    def get_troubleshoot_config_by_id(self, troubleshoot_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Troubleshoot configuration."""
        return self._client.request(
            "GET", f"/troubleshoot/config/{troubleshoot_id}", params={"all_options": all_options}
        )

    def update_troubleshoot_config_by_id(self, troubleshoot_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Troubleshoot configuration."""
        return self._client.request("PUT", f"/troubleshoot/config/{troubleshoot_id}", json={"data": config})

    def get_troubleshoot_kernel_status(self) -> dict[str, Any]:
        """Returns kernel log contents."""
        return self._client.request("GET", "/troubleshoot/kernel/status")

    def get_troubleshoot_system_status(self) -> dict[str, Any]:
        """Returns system log contents."""
        return self._client.request("GET", "/troubleshoot/system/status")
