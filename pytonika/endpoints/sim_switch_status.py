from typing import Any

from ._base import Endpoint


class SIMSwitchStatus(Endpoint):
    def get_sim_switch_status(self) -> dict[str, Any]:
        """Returns current SIM switch status."""
        endpoint = "/sim_switch/status"

        return self._api_client.get(endpoint)

    def get_sim_switch_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns current SIM switch status for specified modem."""
        endpoint = f"/sim_switch/status/{status_id}"

        return self._api_client.get(endpoint)
