from typing import Any

from ._base import Endpoint


class SIMSwitchLog(Endpoint):
    def get_sim_switch_log(self) -> dict[str, Any]:
        """Returns SIM switch operation log for all modems."""
        endpoint = "/sim_switch/log"

        return self._api_client.get(endpoint)

    def get_sim_switch_log_by_modem_id(self, modem_id: str) -> dict[str, Any]:
        """Returns SIM switch operation log for specified modem."""
        endpoint = f"/sim_switch/log/{modem_id}"

        return self._api_client.get(endpoint)
