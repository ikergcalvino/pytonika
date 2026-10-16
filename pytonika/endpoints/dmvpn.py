from typing import Any

from ._endpoint import Endpoint


class DMVPN(Endpoint):
    def get_dmvpn_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all DMVPN instances."""
        return self._client.request("GET", "/dmvpn/config", params={"all_options": all_options})

    def create_dmvpn_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates DMVPN configuration."""
        return self._client.request("POST", "/dmvpn/config", json={"data": config})

    def update_dmvpn_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified DMVPN configurations."""
        return self._client.request("PUT", "/dmvpn/config", json={"data": config})

    def delete_dmvpn_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified DMVPN configurations."""
        return self._client.request("DELETE", "/dmvpn/config", json={"data": config})

    def get_dmvpn_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified DMVPN configuration."""
        return self._client.request("GET", f"/dmvpn/config/{config_id}", params={"all_options": all_options})

    def update_dmvpn_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified DMVPN configuration."""
        return self._client.request("PUT", f"/dmvpn/config/{config_id}", json={"data": config})

    def delete_dmvpn_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified DMVPN configuration."""
        return self._client.request("DELETE", f"/dmvpn/config/{config_id}")
