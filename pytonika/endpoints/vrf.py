from typing import Any

from ._endpoint import Endpoint


class VRF(Endpoint):
    def get_vrf_config(self) -> dict[str, Any]:
        """Returns VRF configurations."""
        endpoint = "/vrf/config"

        return self._client.request("GET", endpoint)

    def create_vrf_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates VRF configuration."""
        endpoint = "/vrf/config"

        data = {"data": config}

        return self._client.request("POST", endpoint, json=data)

    def update_vrf_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates VRF configurations."""
        endpoint = "/vrf/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_vrf_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes VRF configurations."""
        return [self.delete_vrf_config_by_id(config_id) for config_id in config]

    def get_vrf_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns VRF configuration."""
        endpoint = f"/vrf/config/{config_id}"

        return self._client.request("GET", endpoint)

    def update_vrf_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates VRF configuration."""
        endpoint = f"/vrf/config/{config_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_vrf_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes VRF configuration."""
        endpoint = f"/vrf/config/{config_id}"

        return self._client.request("DELETE", endpoint)
