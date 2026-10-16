from typing import Any

from ._endpoint import Endpoint


class DDNS(Endpoint):
    def get_ddns_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all dynamic DNS configuration sections."""
        return self._client.request("GET", "/ddns/config", params={"all_options": all_options})

    def create_ddns_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new DDNS section."""
        return self._client.request("POST", "/ddns/config", json={"data": config})

    def update_ddns_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified dynamic DNS configurations."""
        return self._client.request("PUT", "/ddns/config", json={"data": config})

    def delete_ddns_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the specified dynamic DNS configurations."""
        return self._client.request("DELETE", "/ddns/config", json={"data": config})

    def get_ddns_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified dynamic DNS section."""
        return self._client.request("GET", f"/ddns/config/{config_id}", params={"all_options": all_options})

    def update_ddns_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified dynamic DNS configuration."""
        return self._client.request("PUT", f"/ddns/config/{config_id}", json={"data": config})

    def delete_ddns_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified dynamic DNS configuration."""
        return self._client.request("DELETE", f"/ddns/config/{config_id}")

    def get_ddns_options(self) -> dict[str, Any]:
        """Returns info needed to configure a DDNS section."""
        return self._client.request("GET", "/ddns/options")

    def get_ddns_status(self) -> dict[str, Any]:
        """Returns the status about all DDNS instances."""
        return self._client.request("GET", "/ddns/status")

    def get_ddns_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns the status about the selected DDNS instance."""
        return self._client.request("GET", f"/ddns/status/{status_id}")
