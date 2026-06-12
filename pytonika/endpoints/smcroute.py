from typing import Any

from ._base import Endpoint


class SMCRoute(Endpoint):
    def get_smcroutes_routes_config(self) -> dict[str, Any]:
        """Returns SMCRoute route configurations."""
        endpoint = "/smcroutes/routes/config"

        return self._api_client.get(endpoint)

    def create_smcroutes_routes_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates SMCRoute route configuration."""
        endpoint = "/smcroutes/routes/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_smcroutes_routes_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SMCRoute route configurations."""
        endpoint = "/smcroutes/routes/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_smcroutes_routes_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes SMCRoute route configurations."""
        return [self.delete_smcroutes_routes_config_by_id(route_id) for route_id in config]

    def get_smcroutes_routes_config_by_id(self, route_id: str) -> dict[str, Any]:
        """Returns SMCRoute route configuration."""
        endpoint = f"/smcroutes/routes/config/{route_id}"

        return self._api_client.get(endpoint)

    def update_smcroutes_routes_config_by_id(self, route_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates SMCRoute route configuration."""
        endpoint = f"/smcroutes/routes/config/{route_id}"

        return self._api_client.put(endpoint, data=config)

    def delete_smcroutes_routes_config_by_id(self, route_id: str) -> dict[str, Any]:
        """Deletes SMCRoute route configuration."""
        endpoint = f"/smcroutes/routes/config/{route_id}"

        return self._api_client.delete(endpoint)

    def get_smcroutes_interfaces_config(self) -> dict[str, Any]:
        """Returns SMCRoute interface configurations."""
        endpoint = "/smcroutes/interfaces/config"

        return self._api_client.get(endpoint)

    def create_smcroutes_interfaces_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates SMCRoute interface configuration."""
        endpoint = "/smcroutes/interfaces/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_smcroutes_interfaces_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SMCRoute interface configurations."""
        endpoint = "/smcroutes/interfaces/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_smcroutes_interfaces_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes SMCRoute interface configurations."""
        return [self.delete_smcroutes_interfaces_config_by_id(interface_id) for interface_id in config]

    def get_smcroutes_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Returns SMCRoute interface configuration."""
        endpoint = f"/smcroutes/interfaces/config/{interface_id}"

        return self._api_client.get(endpoint)

    def update_smcroutes_interfaces_config_by_id(self, interface_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates SMCRoute interface configuration."""
        endpoint = f"/smcroutes/interfaces/config/{interface_id}"

        return self._api_client.put(endpoint, data=config)

    def delete_smcroutes_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Deletes SMCRoute interface configuration."""
        endpoint = f"/smcroutes/interfaces/config/{interface_id}"

        return self._api_client.delete(endpoint)
