from typing import Any

from ._base import Endpoint


class VRRP(Endpoint):
    def get_vrrp_config(self) -> dict[str, Any]:
        """Returns VRRP configurations."""
        endpoint = "/vrrp/config"

        return self._client.request("GET", endpoint)

    def create_vrrp_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates VRRP configurations."""
        endpoint = "/vrrp/config"

        data = {"data": config}

        return self._client.request("POST", endpoint, json=data)

    def update_vrrp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates VRRP configurations."""
        endpoint = "/vrrp/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_vrrp_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes VRRP configurations."""
        return [self.delete_vrrp_config_by_id(config_id) for config_id in config]

    def get_vrrp_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns VRRP configuration."""
        endpoint = f"/vrrp/config/{config_id}"

        return self._client.request("GET", endpoint)

    def update_vrrp_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates VRRP configuration."""
        endpoint = f"/vrrp/config/{config_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_vrrp_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes VRRP configuration."""
        endpoint = f"/vrrp/config/{config_id}"

        return self._client.request("DELETE", endpoint)

    def get_vrrp_status(self) -> dict[str, Any]:
        """Returns VRRP status."""
        endpoint = "/vrrp/status"

        return self._client.request("GET", endpoint)
