from typing import Any

from ._base import Endpoint


class NetworkUsage(Endpoint):
    def get_network_usage_global(self) -> dict[str, Any]:
        """Returns Network Usage global configuration."""
        endpoint = "/network_usage/global"

        return self._api_client.get(endpoint)

    def update_network_usage_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Network Usage global configuration."""
        endpoint = "/network_usage/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def network_usage_actions_delete_data(self, data: dict[str, Any]) -> dict[str, Any]:
        """Delete specified data."""
        endpoint = "/network_usage/actions/delete_data"

        return self._api_client.post(endpoint, data={"data": data})

    def get_network_usage_transfers_day_status(self) -> dict[str, Any]:
        """Get single day transfer information."""
        endpoint = "/network_usage/transfers/day/status"

        return self._api_client.get(endpoint)

    def get_network_usage_metrics_day_status(self) -> dict[str, Any]:
        """Get single day metrics information."""
        endpoint = "/network_usage/metrics/day/status"

        return self._api_client.get(endpoint)

    def get_network_usage_metrics_week_status(self) -> dict[str, Any]:
        """Get single week metrics information."""
        endpoint = "/network_usage/metrics/week/status"

        return self._api_client.get(endpoint)

    def get_network_usage_metrics_month_status(self) -> dict[str, Any]:
        """Get single month metrics information."""
        endpoint = "/network_usage/metrics/month/status"

        return self._api_client.get(endpoint)

    def get_network_usage_metrics_total_status(self) -> dict[str, Any]:
        """Get total metrics information."""
        endpoint = "/network_usage/metrics/total/status"

        return self._api_client.get(endpoint)
