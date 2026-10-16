from typing import Any

from ._endpoint import Endpoint


class IGMPProxy(Endpoint):
    def get_igmp_proxy_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns IGMP Proxy global configuration."""
        return self._client.request("GET", "/igmp_proxy/global", params={"all_options": all_options})

    def update_igmp_proxy_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates IGMP Proxy global configuration."""
        return self._client.request("PUT", "/igmp_proxy/global", json={"data": config})

    def get_igmp_proxy_routes_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns IGMP Proxy routes."""
        return self._client.request("GET", "/igmp_proxy/routes/config", params={"all_options": all_options})

    def create_igmp_proxy_routes_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates IGMP Proxy routes."""
        return self._client.request("POST", "/igmp_proxy/routes/config", json={"data": config})

    def update_igmp_proxy_routes_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates IGMP Proxy routes."""
        return self._client.request("PUT", "/igmp_proxy/routes/config", json={"data": config})

    def delete_igmp_proxy_routes_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes IGMP Proxy routes."""
        return self._client.request("DELETE", "/igmp_proxy/routes/config", json={"data": config})

    def get_igmp_proxy_routes_config_by_id(self, route_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns IGMP Proxy route."""
        return self._client.request("GET", f"/igmp_proxy/routes/config/{route_id}", params={"all_options": all_options})

    def update_igmp_proxy_routes_config_by_id(self, route_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates IGMP Proxy route."""
        return self._client.request("PUT", f"/igmp_proxy/routes/config/{route_id}", json=config)

    def delete_igmp_proxy_routes_config_by_id(self, route_id: str) -> dict[str, Any]:
        """Deletes IGMP Proxy routes."""
        return self._client.request("DELETE", f"/igmp_proxy/routes/config/{route_id}")
