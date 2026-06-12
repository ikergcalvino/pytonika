from typing import Any

from ._base import Endpoint


class IPRoutes(Endpoint):
    def get_ip_routes_ipv4_status(self) -> dict[str, Any]:
        """Returns IPv4 routes."""
        endpoint = "/ip_routes/ipv4/status"

        return self._api_client.get(endpoint)

    def get_ip_routes_ipv4_config(self) -> dict[str, Any]:
        """Returns static IPv4 route configurations."""
        endpoint = "/ip_routes/ipv4/config"

        return self._api_client.get(endpoint)

    def create_ip_routes_ipv4_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates static IPv4 route configuration."""
        endpoint = "/ip_routes/ipv4/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_ip_routes_ipv4_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates static IPv4 route configurations."""
        endpoint = "/ip_routes/ipv4/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ip_routes_ipv4_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes static IPv4 route configurations."""
        return [self.delete_ip_routes_ipv4_config_by_id(route_id) for route_id in config]

    def get_ip_routes_ipv4_config_by_id(self, route_id: str) -> dict[str, Any]:
        """Returns static IPv4 route configuration."""
        endpoint = f"/ip_routes/ipv4/config/{route_id}"

        return self._api_client.get(endpoint)

    def update_ip_routes_ipv4_config_by_id(self, route_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates static IPv4 route configuration."""
        endpoint = f"/ip_routes/ipv4/config/{route_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ip_routes_ipv4_config_by_id(self, route_id: str) -> dict[str, Any]:
        """Deletes static IPv4 route configuration."""
        endpoint = f"/ip_routes/ipv4/config/{route_id}"

        return self._api_client.delete(endpoint)

    def get_ip_routes_ipv6_status(self) -> dict[str, Any]:
        """Returns IPv6 routes."""
        endpoint = "/ip_routes/ipv6/status"

        return self._api_client.get(endpoint)

    def get_ip_routes_ipv6_config(self) -> dict[str, Any]:
        """Returns static IPv6 route configurations."""
        endpoint = "/ip_routes/ipv6/config"

        return self._api_client.get(endpoint)

    def create_ip_routes_ipv6_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates static IPv6 route configuration."""
        endpoint = "/ip_routes/ipv6/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_ip_routes_ipv6_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates static IPv6 route configurations."""
        endpoint = "/ip_routes/ipv6/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ip_routes_ipv6_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes static IPv6 route configurations."""
        return [self.delete_ip_routes_ipv6_config_by_id(route_id) for route_id in config]

    def get_ip_routes_ipv6_config_by_id(self, route_id: str) -> dict[str, Any]:
        """Returns static IPv6 route configuration."""
        endpoint = f"/ip_routes/ipv6/config/{route_id}"

        return self._api_client.get(endpoint)

    def update_ip_routes_ipv6_config_by_id(self, route_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates static IPv6 route configuration."""
        endpoint = f"/ip_routes/ipv6/config/{route_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ip_routes_ipv6_config_by_id(self, route_id: str) -> dict[str, Any]:
        """Deletes static IPv6 route configuration."""
        endpoint = f"/ip_routes/ipv6/config/{route_id}"

        return self._api_client.delete(endpoint)
