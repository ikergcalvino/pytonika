from typing import Any

from ._endpoint import Endpoint


class EIGRP(Endpoint):
    def get_eigrp_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns EIGRP global configurations."""
        return self._client.request("GET", "/eigrp/config", params={"all_options": all_options})

    def update_eigrp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates EIGRP global configurations."""
        return self._client.request("PUT", "/eigrp/config", json={"data": config})

    def get_eigrp_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns EIGRP global configuration."""
        return self._client.request("GET", f"/eigrp/config/{config_id}", params={"all_options": all_options})

    def update_eigrp_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates EIGRP global configuration."""
        return self._client.request("PUT", f"/eigrp/config/{config_id}", json={"data": config})

    def get_eigrp_status(self) -> dict[str, Any]:
        """Fetches data about EIGRP neighbors."""
        return self._client.request("GET", "/eigrp/status")
