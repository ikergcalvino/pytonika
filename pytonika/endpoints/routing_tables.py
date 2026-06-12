from typing import Any

from ._base import Endpoint


class RoutingTables(Endpoint):
    def get_routing_tables_config(self) -> dict[str, Any]:
        """Returns routing table configurations."""
        endpoint = "/routing_tables/config"

        return self._api_client.get(endpoint)

    def create_routing_tables_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates routing table configuration."""
        endpoint = "/routing_tables/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_routing_tables_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates routing table configurations."""
        endpoint = "/routing_tables/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_routing_tables_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes routing table configurations."""
        return [self.delete_routing_tables_config_by_id(table_id) for table_id in config]

    def get_routing_tables_config_by_id(self, table_id: str) -> dict[str, Any]:
        """Returns routing table configuration."""
        endpoint = f"/routing_tables/config/{table_id}"

        return self._api_client.get(endpoint)

    def update_routing_tables_config_by_id(self, table_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates routing table configuration."""
        endpoint = f"/routing_tables/config/{table_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_routing_tables_config_by_id(self, table_id: str) -> dict[str, Any]:
        """Deletes routing table configuration."""
        endpoint = f"/routing_tables/config/{table_id}"

        return self._api_client.delete(endpoint)
