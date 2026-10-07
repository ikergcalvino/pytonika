from typing import Any

from ._endpoint import Endpoint


class Console(Endpoint):
    def get_console_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Console over Serial configurations."""
        return self._client.request("GET", "/console/config", params={"all_options": all_options})

    def create_console_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Console over Serial configuration."""
        return self._client.request("POST", "/console/config", json={"data": config})

    def update_console_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Console over Serial configurations."""
        return self._client.request("PUT", "/console/config", json={"data": config})

    def delete_console_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes Console over Serial configurations."""
        return self._client.request("DELETE", "/console/config", json={"data": config})

    def get_console_config_by_id(self, console_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Console over Serial configuration."""
        return self._client.request("GET", f"/console/config/{console_id}", params={"all_options": all_options})

    def update_console_config_by_id(self, console_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Console over Serial configuration."""
        return self._client.request("PUT", f"/console/config/{console_id}", json={"data": config})

    def delete_console_config_by_id(self, console_id: str) -> dict[str, Any]:
        """Deletes Console over Serial configuration."""
        return self._client.request("DELETE", f"/console/config/{console_id}")

    def get_console_status(self) -> dict[str, Any]:
        """Returns Console over Serial status."""
        return self._client.request("GET", "/console/status")
