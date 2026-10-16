from typing import Any

from ._endpoint import Endpoint


class SIMSwitchLog(Endpoint):
    def get_sim_switch_log(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns SIM switch operation log for all modems."""
        return self._client.request("GET", "/sim_switch/log", params={"all_options": all_options})

    def get_sim_switch_log_by_id(self, modem_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns SIM switch operation log for specified modem."""
        return self._client.request("GET", f"/sim_switch/log/{modem_id}", params={"all_options": all_options})
