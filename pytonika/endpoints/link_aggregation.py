from typing import Any

from ._endpoint import Endpoint


class LinkAggregation(Endpoint):
    def get_link_aggregation_config(self) -> dict[str, Any]:
        """Returns Link Aggregation configurations."""
        return self._client.request("GET", "/link_aggregation/config")

    def create_link_aggregation_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Link Aggregation configuration."""
        return self._client.request("POST", "/link_aggregation/config", json={"data": config})

    def update_link_aggregation_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Link Aggregation configurations."""
        return self._client.request("PUT", "/link_aggregation/config", json={"data": config})

    def delete_link_aggregation_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes Link Aggregation configurations."""
        return self._client.request("DELETE", "/link_aggregation/config", json={"data": config})

    def get_link_aggregation_config_by_id(self, link_aggregation_id: str) -> dict[str, Any]:
        """Returns Link Aggregation configuration."""
        return self._client.request("GET", f"/link_aggregation/config/{link_aggregation_id}")

    def update_link_aggregation_config_by_id(self, link_aggregation_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Link Aggregation configuration."""
        return self._client.request("PUT", f"/link_aggregation/config/{link_aggregation_id}", json={"data": config})

    def delete_link_aggregation_config_by_id(self, link_aggregation_id: str) -> dict[str, Any]:
        """Deletes Link Aggregation configuration."""
        return self._client.request("DELETE", f"/link_aggregation/config/{link_aggregation_id}")
