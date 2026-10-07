from typing import Any

from ._endpoint import Endpoint


class SIMSwitchStatus(Endpoint):
    def get_sim_switch_status(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns current SIM switch status."""
        return self._client.request("GET", "/sim_switch/status", params={"all_options": all_options})

    def get_sim_switch_status_by_id(self, status_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns current SIM switch status for specified modem."""
        return self._client.request("GET", f"/sim_switch/status/{status_id}", params={"all_options": all_options})
