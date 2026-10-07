from typing import Any

from ._endpoint import Endpoint


class RoutingTables(Endpoint):
    def get_routing_tables_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns routing table configurations."""
        return self._client.request("GET", "/routing_tables/config", params={"all_options": all_options})

    def create_routing_tables_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates routing table configuration."""
        return self._client.request("POST", "/routing_tables/config", json={"data": config})

    def update_routing_tables_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates routing table configurations."""
        return self._client.request("PUT", "/routing_tables/config", json={"data": config})

    def delete_routing_tables_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes routing table configurations."""
        return self._client.request("DELETE", "/routing_tables/config", json={"data": config})

    def get_routing_tables_config_by_id(self, table_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns routing table configuration."""
        return self._client.request("GET", f"/routing_tables/config/{table_id}", params={"all_options": all_options})

    def update_routing_tables_config_by_id(self, table_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates routing table configuration."""
        return self._client.request("PUT", f"/routing_tables/config/{table_id}", json={"data": config})

    def delete_routing_tables_config_by_id(self, table_id: str) -> dict[str, Any]:
        """Deletes routing table configuration."""
        return self._client.request("DELETE", f"/routing_tables/config/{table_id}")
