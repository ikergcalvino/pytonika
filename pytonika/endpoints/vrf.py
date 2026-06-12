from typing import Any

from ._base import Endpoint


class VRF(Endpoint):
    def get_vrf_config(self) -> dict[str, Any]:
        """Returns VRF configurations."""
        endpoint = "/vrf/config"

        return self._api_client.get(endpoint)

    def create_vrf_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates VRF configuration."""
        endpoint = "/vrf/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_vrf_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates VRF configurations."""
        endpoint = "/vrf/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_vrf_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes VRF configurations."""
        return [self.delete_vrf_config_by_id(config_id) for config_id in config]

    def get_vrf_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns VRF configuration."""
        endpoint = f"/vrf/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_vrf_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates VRF configuration."""
        endpoint = f"/vrf/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_vrf_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes VRF configuration."""
        endpoint = f"/vrf/config/{config_id}"

        return self._api_client.delete(endpoint)
