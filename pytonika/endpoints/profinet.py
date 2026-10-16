from typing import Any

from ._endpoint import Endpoint


class Profinet(Endpoint):
    def profinet_actions_download_gsdml(self) -> bytes | dict[str, Any]:
        """Download GSDML file."""
        return self._client.request("POST", "/profinet/actions/download_gsdml", download=True)

    def get_profinet_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Profinet configurations."""
        return self._client.request("GET", "/profinet/config", params={"all_options": all_options})

    def update_profinet_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Profinet configurations."""
        return self._client.request("PUT", "/profinet/config", json={"data": config})

    def get_profinet_config_by_id(self, profinet_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Profinet configuration."""
        return self._client.request("GET", f"/profinet/config/{profinet_id}", params={"all_options": all_options})

    def update_profinet_config_by_id(self, profinet_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Profinet configuration."""
        return self._client.request("PUT", f"/profinet/config/{profinet_id}", json={"data": config})

    def get_profinet_status(self) -> dict[str, Any]:
        """Returns all backup information."""
        return self._client.request("GET", "/profinet/status")
