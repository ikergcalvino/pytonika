from typing import Any

from ._endpoint import Endpoint


class DataUsage(Endpoint):
    def get_data_usage_modem_esim_status(
        self, interval: str, modem_id: str, esim_id: str, *, to: int | None = None
    ) -> dict[str, Any]:
        """Returns eSIM card usage data for specified interval, modem and eSIM card."""
        return self._client.request(
            "GET", f"/data_usage/{interval}/modem/{modem_id}/esim/{esim_id}/status", params={"to": to}
        )

    def get_data_usage_modem_sim_status(
        self, interval: str, modem_id: str, sim_id: str, *, to: int | None = None
    ) -> dict[str, Any]:
        """Returns SIM card usage data for specified interval, modem and SIM card."""
        return self._client.request(
            "GET", f"/data_usage/{interval}/modem/{modem_id}/sim/{sim_id}/status", params={"to": to}
        )

    def get_data_usage_modem_status(self, interval: str, modem_id: str, *, to: int | None = None) -> dict[str, Any]:
        """Returns SIM card usage data for specified interval and modem."""
        return self._client.request("GET", f"/data_usage/{interval}/modem/{modem_id}/status", params={"to": to})

    def get_data_usage_status(self, interval: str, *, to: int | None = None) -> dict[str, Any]:
        """Returns SIM card usage data for specified interval."""
        return self._client.request("GET", f"/data_usage/{interval}/status", params={"to": to})
