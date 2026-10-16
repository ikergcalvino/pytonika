from typing import Any

from ._endpoint import Endpoint


class VRF(Endpoint):
    def get_vrf_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns VRF configurations."""
        return self._client.request("GET", "/vrf/config", params={"all_options": all_options})

    def create_vrf_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates VRF configuration."""
        return self._client.request("POST", "/vrf/config", json={"data": config})

    def update_vrf_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates VRF configurations."""
        return self._client.request("PUT", "/vrf/config", json={"data": config})

    def delete_vrf_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes VRF configurations."""
        return self._client.request("DELETE", "/vrf/config", json={"data": config})

    def get_vrf_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns VRF configuration."""
        return self._client.request("GET", f"/vrf/config/{config_id}", params={"all_options": all_options})

    def update_vrf_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates VRF configuration."""
        return self._client.request("PUT", f"/vrf/config/{config_id}", json={"data": config})

    def delete_vrf_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes VRF configuration."""
        return self._client.request("DELETE", f"/vrf/config/{config_id}")

    def get_vrf_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns global VRF configuration."""
        return self._client.request("GET", "/vrf/global", params={"all_options": all_options})

    def update_vrf_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates global VRF configuration."""
        return self._client.request("PUT", "/vrf/global", json={"data": config})
