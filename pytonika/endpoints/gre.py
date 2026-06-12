from typing import Any

from ._base import Endpoint


class GRE(Endpoint):
    def get_gre_config(self) -> dict[str, Any]:
        """Returns all GRE configuration sections."""
        endpoint = "/gre/config"

        return self._api_client.get(endpoint)

    def create_gre_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates GRE section."""
        endpoint = "/gre/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_gre_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified GRE configurations."""
        endpoint = "/gre/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_gre_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified GRE configurations."""
        return [self.delete_gre_config_by_id(gre_id) for gre_id in config]

    def get_gre_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified GRE section."""
        endpoint = f"/gre/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_gre_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified GRE configuration."""
        endpoint = f"/gre/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_gre_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified GRE configuration."""
        endpoint = f"/gre/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_gre_routes_config(self, gre_id: str) -> dict[str, Any]:
        """Returns the selected GRE section's routes."""
        endpoint = f"/gre/{gre_id}/routes/config"

        return self._api_client.get(endpoint)

    def create_gre_routes_config(self, gre_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a route for the selected GRE section."""
        endpoint = f"/gre/{gre_id}/routes/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_gre_routes_config(self, gre_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected GRE section's selected routes."""
        endpoint = f"/gre/{gre_id}/routes/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_gre_routes_config(self, gre_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected GRE section's selected routes."""
        return [self.delete_gre_routes_config_by_id(gre_id, route_id) for route_id in config]

    def get_gre_routes_config_by_id(self, gre_id: str, routes_id: str) -> dict[str, Any]:
        """Returns specified GRE IPv4 route section."""
        endpoint = f"/gre/{gre_id}/routes/config/{routes_id}"

        return self._api_client.get(endpoint)

    def update_gre_routes_config_by_id(self, gre_id: str, routes_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected GRE section's selected IPv4 route."""
        endpoint = f"/gre/{gre_id}/routes/config/{routes_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_gre_routes_config_by_id(self, gre_id: str, routes_id: str) -> dict[str, Any]:
        """Deletes the selected GRE section's selected IPv4 route."""
        endpoint = f"/gre/{gre_id}/routes/config/{routes_id}"

        return self._api_client.delete(endpoint)

    def get_gre_routes6_config_by_id(self, gre_id: str, routes_id: str) -> dict[str, Any]:
        """Returns specified GRE IPv6 route section."""
        endpoint = f"/gre/{gre_id}/routes6/config/{routes_id}"

        return self._api_client.get(endpoint)

    def update_gre_routes6_config_by_id(self, gre_id: str, routes_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected GRE section's selected IPv6 route."""
        endpoint = f"/gre/{gre_id}/routes6/config/{routes_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_gre_routes6_config_by_id(self, gre_id: str, routes_id: str) -> dict[str, Any]:
        """Deletes the selected GRE section's selected IPv6 route."""
        endpoint = f"/gre/{gre_id}/routes6/config/{routes_id}"

        return self._api_client.delete(endpoint)
