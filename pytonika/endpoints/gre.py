from typing import Any

from ._endpoint import Endpoint


class GRE(Endpoint):
    def get_gre_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all GRE configuration sections."""
        return self._client.request("GET", "/gre/config", params={"all_options": all_options})

    def create_gre_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates GRE section."""
        return self._client.request("POST", "/gre/config", json={"data": config})

    def update_gre_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified GRE configurations."""
        return self._client.request("PUT", "/gre/config", json={"data": config})

    def delete_gre_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified GRE configurations."""
        return self._client.request("DELETE", "/gre/config", json={"data": config})

    def get_gre_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified GRE section."""
        return self._client.request("GET", f"/gre/config/{config_id}", params={"all_options": all_options})

    def update_gre_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified GRE configuration."""
        return self._client.request("PUT", f"/gre/config/{config_id}", json={"data": config})

    def delete_gre_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified GRE configuration."""
        return self._client.request("DELETE", f"/gre/config/{config_id}")

    def get_gre_routes_config(self, gre_id: str) -> dict[str, Any]:
        """Returns the selected GRE section's routes."""
        return self._client.request("GET", f"/gre/{gre_id}/routes/config")

    def create_gre_routes_config(self, gre_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a route for the selected GRE section."""
        return self._client.request("POST", f"/gre/{gre_id}/routes/config", json={"data": config})

    def update_gre_routes_config(self, gre_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected GRE section's selected routes."""
        return self._client.request("PUT", f"/gre/{gre_id}/routes/config", json={"data": config})

    def delete_gre_routes_config(self, gre_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes the selected GRE section's selected routes."""
        return self._client.request("DELETE", f"/gre/{gre_id}/routes/config", json={"data": config})

    def get_gre_routes_config_by_id(self, gre_id: str, routes_id: str) -> dict[str, Any]:
        """Returns specified GRE IPv4 route section."""
        return self._client.request("GET", f"/gre/{gre_id}/routes/config/{routes_id}")

    def update_gre_routes_config_by_id(self, gre_id: str, routes_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected GRE section's selected IPv4 route."""
        return self._client.request("PUT", f"/gre/{gre_id}/routes/config/{routes_id}", json={"data": config})

    def delete_gre_routes_config_by_id(self, gre_id: str, routes_id: str) -> dict[str, Any]:
        """Deletes the selected GRE section's selected IPv4 route."""
        return self._client.request("DELETE", f"/gre/{gre_id}/routes/config/{routes_id}")

    def get_gre_routes6_config(self, gre_id: str) -> dict[str, Any]:
        """Returns the selected GRE section's IPv6 routes."""
        return self._client.request("GET", f"/gre/{gre_id}/routes6/config")

    def create_gre_routes6_config(self, gre_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates an IPv6 route for the selected GRE section."""
        return self._client.request("POST", f"/gre/{gre_id}/routes6/config", json={"data": config})

    def update_gre_routes6_config(self, gre_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected GRE section's selected IPv6 routes."""
        return self._client.request("PUT", f"/gre/{gre_id}/routes6/config", json={"data": config})

    def delete_gre_routes6_config(self, gre_id: str, config: list[str]) -> dict[str, Any]:
        """Deletes the selected GRE section's selected IPv6 routes."""
        return self._client.request("DELETE", f"/gre/{gre_id}/routes6/config", json={"data": config})

    def get_gre_routes6_config_by_id(self, gre_id: str, routes_id: str) -> dict[str, Any]:
        """Returns specified GRE IPv6 route section."""
        return self._client.request("GET", f"/gre/{gre_id}/routes6/config/{routes_id}")

    def update_gre_routes6_config_by_id(self, gre_id: str, routes_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected GRE section's selected IPv6 route."""
        return self._client.request("PUT", f"/gre/{gre_id}/routes6/config/{routes_id}", json={"data": config})

    def delete_gre_routes6_config_by_id(self, gre_id: str, routes_id: str) -> dict[str, Any]:
        """Deletes the selected GRE section's selected IPv6 route."""
        return self._client.request("DELETE", f"/gre/{gre_id}/routes6/config/{routes_id}")
