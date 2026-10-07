from typing import Any

from ._endpoint import Endpoint


class Interfaces(Endpoint):
    def get_interfaces_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns network interface configurations."""
        return self._client.request("GET", "/interfaces/config", params={"all_options": all_options})

    def create_interfaces_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates network interface configuration."""
        return self._client.request("POST", "/interfaces/config", json={"data": config})

    def update_interfaces_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates network interface configurations."""
        return self._client.request("PUT", "/interfaces/config", json={"data": config})

    def delete_interfaces_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes network interface configurations."""
        return self._client.request("DELETE", "/interfaces/config", json={"data": config})

    def get_interfaces_config_by_id(self, interface_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns network interface configuration."""
        return self._client.request("GET", f"/interfaces/config/{interface_id}", params={"all_options": all_options})

    def update_interfaces_config_by_id(self, interface_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates network interface configuration."""
        return self._client.request("PUT", f"/interfaces/config/{interface_id}", json={"data": config})

    def delete_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Deletes network interface configuration."""
        return self._client.request("DELETE", f"/interfaces/config/{interface_id}")

    def get_interfaces_status(self) -> dict[str, Any]:
        """Returns network interfaces status."""
        return self._client.request("GET", "/interfaces/status")

    def get_interfaces_status_by_id(self, interface_id: str) -> dict[str, Any]:
        """Returns network interface status."""
        return self._client.request("GET", f"/interfaces/status/{interface_id}")
