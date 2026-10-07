from typing import Any

from ._endpoint import Endpoint


class IPRoutes(Endpoint):
    def get_ip_routes_ipv4_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns static IPv4 route configurations."""
        return self._client.request("GET", "/ip_routes/ipv4/config", params={"all_options": all_options})

    def create_ip_routes_ipv4_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates static IPv4 route configuration."""
        return self._client.request("POST", "/ip_routes/ipv4/config", json={"data": config})

    def update_ip_routes_ipv4_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates static IPv4 route configurations."""
        return self._client.request("PUT", "/ip_routes/ipv4/config", json={"data": config})

    def delete_ip_routes_ipv4_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes static IPv4 route configurations."""
        return self._client.request("DELETE", "/ip_routes/ipv4/config", json={"data": config})

    def get_ip_routes_ipv4_config_by_id(self, route_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns static IPv4 route configuration."""
        return self._client.request("GET", f"/ip_routes/ipv4/config/{route_id}", params={"all_options": all_options})

    def update_ip_routes_ipv4_config_by_id(self, route_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates static IPv4 route configuration."""
        return self._client.request("PUT", f"/ip_routes/ipv4/config/{route_id}", json={"data": config})

    def delete_ip_routes_ipv4_config_by_id(self, route_id: str) -> dict[str, Any]:
        """Deletes static IPv4 route configuration."""
        return self._client.request("DELETE", f"/ip_routes/ipv4/config/{route_id}")

    def get_ip_routes_ipv4_status(self) -> dict[str, Any]:
        """Returns IPv4 routes."""
        return self._client.request("GET", "/ip_routes/ipv4/status")

    def get_ip_routes_ipv6_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns static IPv6 route configurations."""
        return self._client.request("GET", "/ip_routes/ipv6/config", params={"all_options": all_options})

    def create_ip_routes_ipv6_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates static IPv6 route configuration."""
        return self._client.request("POST", "/ip_routes/ipv6/config", json={"data": config})

    def update_ip_routes_ipv6_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates static IPv6 route configurations."""
        return self._client.request("PUT", "/ip_routes/ipv6/config", json={"data": config})

    def delete_ip_routes_ipv6_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes static IPv6 route configurations."""
        return self._client.request("DELETE", "/ip_routes/ipv6/config", json={"data": config})

    def get_ip_routes_ipv6_config_by_id(self, route_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns static IPv6 route configuration."""
        return self._client.request("GET", f"/ip_routes/ipv6/config/{route_id}", params={"all_options": all_options})

    def update_ip_routes_ipv6_config_by_id(self, route_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates static IPv6 route configuration."""
        return self._client.request("PUT", f"/ip_routes/ipv6/config/{route_id}", json={"data": config})

    def delete_ip_routes_ipv6_config_by_id(self, route_id: str) -> dict[str, Any]:
        """Deletes static IPv6 route configuration."""
        return self._client.request("DELETE", f"/ip_routes/ipv6/config/{route_id}")

    def get_ip_routes_ipv6_status(self) -> dict[str, Any]:
        """Returns IPv6 routes."""
        return self._client.request("GET", "/ip_routes/ipv6/status")
