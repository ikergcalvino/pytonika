from typing import Any

from ._endpoint import Endpoint


class SMCRoute(Endpoint):
    def get_smcroutes_interfaces_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns SMCRoute interface configurations."""
        return self._client.request("GET", "/smcroutes/interfaces/config", params={"all_options": all_options})

    def create_smcroutes_interfaces_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates SMCRoute interface configuration."""
        return self._client.request("POST", "/smcroutes/interfaces/config", json={"data": config})

    def update_smcroutes_interfaces_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SMCRoute interface configurations."""
        return self._client.request("PUT", "/smcroutes/interfaces/config", json={"data": config})

    def delete_smcroutes_interfaces_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes SMCRoute interface configurations."""
        return self._client.request("DELETE", "/smcroutes/interfaces/config", json={"data": config})

    def get_smcroutes_interfaces_config_by_id(
        self, interface_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns SMCRoute interface configuration."""
        return self._client.request(
            "GET", f"/smcroutes/interfaces/config/{interface_id}", params={"all_options": all_options}
        )

    def update_smcroutes_interfaces_config_by_id(self, interface_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates SMCRoute interface configuration."""
        return self._client.request("PUT", f"/smcroutes/interfaces/config/{interface_id}", json=config)

    def delete_smcroutes_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Deletes SMCRoute interface configuration."""
        return self._client.request("DELETE", f"/smcroutes/interfaces/config/{interface_id}")

    def get_smcroutes_routes_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns SMCRoute route configurations."""
        return self._client.request("GET", "/smcroutes/routes/config", params={"all_options": all_options})

    def create_smcroutes_routes_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates SMCRoute route configuration."""
        return self._client.request("POST", "/smcroutes/routes/config", json={"data": config})

    def update_smcroutes_routes_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SMCRoute route configurations."""
        return self._client.request("PUT", "/smcroutes/routes/config", json={"data": config})

    def delete_smcroutes_routes_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes SMCRoute route configurations."""
        return self._client.request("DELETE", "/smcroutes/routes/config", json={"data": config})

    def get_smcroutes_routes_config_by_id(self, route_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns SMCRoute route configuration."""
        return self._client.request("GET", f"/smcroutes/routes/config/{route_id}", params={"all_options": all_options})

    def update_smcroutes_routes_config_by_id(self, route_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates SMCRoute route configuration."""
        return self._client.request("PUT", f"/smcroutes/routes/config/{route_id}", json=config)

    def delete_smcroutes_routes_config_by_id(self, route_id: str) -> dict[str, Any]:
        """Deletes SMCRoute route configuration."""
        return self._client.request("DELETE", f"/smcroutes/routes/config/{route_id}")
