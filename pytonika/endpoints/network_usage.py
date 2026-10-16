from typing import Any

from ._endpoint import Endpoint


class NetworkUsage(Endpoint):
    def network_usage_actions_delete_data(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Delete specified data."""
        return self._client.request(
            "POST", "/network_usage/actions/delete_data", json=None if data is None else {"data": data}
        )

    def get_network_usage_global(self) -> dict[str, Any]:
        """Returns Network Usage global configuration."""
        return self._client.request("GET", "/network_usage/global")

    def update_network_usage_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Network Usage global configuration."""
        return self._client.request("PUT", "/network_usage/global", json={"data": config})

    def get_network_usage_metrics_day_status(self) -> dict[str, Any]:
        """Get single day metrics information."""
        return self._client.request("GET", "/network_usage/metrics/day/status")

    def get_network_usage_metrics_month_status(self) -> dict[str, Any]:
        """Get single month metrics information."""
        return self._client.request("GET", "/network_usage/metrics/month/status")

    def get_network_usage_metrics_total_status(self) -> dict[str, Any]:
        """Get total metrics information."""
        return self._client.request("GET", "/network_usage/metrics/total/status")

    def get_network_usage_metrics_week_status(self) -> dict[str, Any]:
        """Get single week metrics information."""
        return self._client.request("GET", "/network_usage/metrics/week/status")

    def get_network_usage_transfers_day_status(self) -> dict[str, Any]:
        """Get single day transfer information."""
        return self._client.request("GET", "/network_usage/transfers/day/status")
