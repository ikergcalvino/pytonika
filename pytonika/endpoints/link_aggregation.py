from typing import Any

from ._base import Endpoint


class LinkAggregation(Endpoint):
    def get_link_aggregation_config(self) -> dict[str, Any]:
        """Returns Link Aggregation configurations."""
        endpoint = "/link_aggregation/config"

        return self._client.request("GET", endpoint)

    def create_link_aggregation_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Link Aggregation configuration."""
        endpoint = "/link_aggregation/config"

        data = {"data": config}

        return self._client.request("POST", endpoint, json=data)

    def update_link_aggregation_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Link Aggregation configurations."""
        endpoint = "/link_aggregation/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_link_aggregation_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes Link Aggregation configurations."""
        return [self.delete_link_aggregation_config_by_id(link_aggregation_id) for link_aggregation_id in config]

    def get_link_aggregation_config_by_id(self, link_aggregation_id: str) -> dict[str, Any]:
        """Returns Link Aggregation configuration."""
        endpoint = f"/link_aggregation/config/{link_aggregation_id}"

        return self._client.request("GET", endpoint)

    def update_link_aggregation_config_by_id(self, link_aggregation_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Link Aggregation configuration."""
        endpoint = f"/link_aggregation/config/{link_aggregation_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_link_aggregation_config_by_id(self, link_aggregation_id: str) -> dict[str, Any]:
        """Deletes Link Aggregation configuration."""
        endpoint = f"/link_aggregation/config/{link_aggregation_id}"

        return self._client.request("DELETE", endpoint)
