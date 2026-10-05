from typing import Any

from ._base import Endpoint


class Console(Endpoint):
    def get_console_config(self) -> dict[str, Any]:
        """Returns Console over Serial configurations."""
        endpoint = "/console/config"

        return self._client.request("GET", endpoint)

    def create_console_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Console over Serial configuration."""
        endpoint = "/console/config"

        data = {"data": config}

        return self._client.request("POST", endpoint, json=data)

    def update_console_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Console over Serial configurations."""
        endpoint = "/console/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_console_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes Console over Serial configurations."""
        return [self.delete_console_config_by_id(console_id) for console_id in config]

    def get_console_config_by_id(self, console_id: str) -> dict[str, Any]:
        """Returns the specified Console over Serial configuration."""
        endpoint = f"/console/config/{console_id}"

        return self._client.request("GET", endpoint)

    def update_console_config_by_id(self, console_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Console over Serial configuration."""
        endpoint = f"/console/config/{console_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_console_config_by_id(self, console_id: str) -> dict[str, Any]:
        """Deletes Console over Serial configuration."""
        endpoint = f"/console/config/{console_id}"

        return self._client.request("DELETE", endpoint)

    def get_console_status(self) -> dict[str, Any]:
        """Returns Console over Serial status."""
        endpoint = "/console/status"

        return self._client.request("GET", endpoint)
