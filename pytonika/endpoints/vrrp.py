from typing import Any

from ._endpoint import Endpoint


class VRRP(Endpoint):
    def get_vrrp_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns VRRP configurations."""
        return self._client.request("GET", "/vrrp/config", params={"all_options": all_options})

    def create_vrrp_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates VRRP configurations."""
        return self._client.request("POST", "/vrrp/config", json={"data": config})

    def update_vrrp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates VRRP configurations."""
        return self._client.request("PUT", "/vrrp/config", json={"data": config})

    def delete_vrrp_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes VRRP configurations."""
        return self._client.request("DELETE", "/vrrp/config", json={"data": config})

    def get_vrrp_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns VRRP configuration."""
        return self._client.request("GET", f"/vrrp/config/{config_id}", params={"all_options": all_options})

    def update_vrrp_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates VRRP configuration."""
        return self._client.request("PUT", f"/vrrp/config/{config_id}", json={"data": config})

    def delete_vrrp_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes VRRP configuration."""
        return self._client.request("DELETE", f"/vrrp/config/{config_id}")

    def get_vrrp_status(self) -> dict[str, Any]:
        """Returns VRRP status."""
        return self._client.request("GET", "/vrrp/status")
