from typing import Any

from ._base import Endpoint


class DataUsage(Endpoint):
    def get_data_usage_status(self, interval: str) -> dict[str, Any]:
        """Returns SIM card usage data for specified interval."""
        endpoint = f"/data_usage/{interval}/status"

        return self._api_client.get(endpoint)

    def get_data_usage_modem_status(self, interval: str, modem_id: str) -> dict[str, Any]:
        """Returns SIM card usage data for specified interval and modem."""
        endpoint = f"/data_usage/{interval}/modem/{modem_id}/status"

        return self._api_client.get(endpoint)

    def get_data_usage_modem_sim_status(self, interval: str, modem_id: str, sim_id: str) -> dict[str, Any]:
        """Returns SIM card usage data for specified interval, modem and SIM card."""
        endpoint = f"/data_usage/{interval}/modem/{modem_id}/sim/{sim_id}/status"

        return self._api_client.get(endpoint)

    def get_data_usage_modem_esim_status(self, interval: str, modem_id: str, esim_id: str) -> dict[str, Any]:
        """Returns eSIM card usage data for specified interval, modem and eSIM card."""
        endpoint = f"/data_usage/{interval}/modem/{modem_id}/esim/{esim_id}/status"

        return self._api_client.get(endpoint)
