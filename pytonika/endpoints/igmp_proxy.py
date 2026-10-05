from typing import Any

from ._endpoint import Endpoint


class IGMPProxy(Endpoint):
    def get_igmp_proxy_global(self) -> dict[str, Any]:
        """Returns IGMP Proxy global configuration."""
        endpoint = "/igmp_proxy/global"

        return self._client.request("GET", endpoint)

    def update_igmp_proxy_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates IGMP Proxy global configuration."""
        endpoint = "/igmp_proxy/global"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def get_igmp_proxy_routes_config(self) -> dict[str, Any]:
        """Returns IGMP Proxy routes."""
        endpoint = "/igmp_proxy/routes/config"

        return self._client.request("GET", endpoint)

    def create_igmp_proxy_routes_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates IGMP Proxy routes."""
        endpoint = "/igmp_proxy/routes/config"

        data = {"data": config}

        return self._client.request("POST", endpoint, json=data)

    def update_igmp_proxy_routes_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates IGMP Proxy routes."""
        endpoint = "/igmp_proxy/routes/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_igmp_proxy_routes_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes IGMP Proxy routes."""
        return [self.delete_igmp_proxy_routes_config_by_id(route_id) for route_id in config]

    def get_igmp_proxy_routes_config_by_id(self, route_id: str) -> dict[str, Any]:
        """Returns IGMP Proxy route."""
        endpoint = f"/igmp_proxy/routes/config/{route_id}"

        return self._client.request("GET", endpoint)

    def update_igmp_proxy_routes_config_by_id(self, route_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates IGMP Proxy route."""
        endpoint = f"/igmp_proxy/routes/config/{route_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_igmp_proxy_routes_config_by_id(self, route_id: str) -> dict[str, Any]:
        """Deletes IGMP Proxy routes."""
        endpoint = f"/igmp_proxy/routes/config/{route_id}"

        return self._client.request("DELETE", endpoint)
