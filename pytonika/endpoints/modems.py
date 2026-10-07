from typing import Any

from ._endpoint import Endpoint


class Modems(Endpoint):
    def get_modems_apns_status(self) -> dict[str, Any]:
        """Returns APN values for multiple modems."""
        return self._client.request("GET", "/modems/apns/status")

    def get_modems_apns_status_by_id(self, modem_id: str) -> dict[str, Any]:
        """Returns APN values for specified modem."""
        return self._client.request("GET", f"/modems/apns/status/{modem_id}")

    def get_modems_config(self) -> dict[str, Any]:
        """Returns multiple modem configurations."""
        return self._client.request("GET", "/modems/config")

    def update_modems_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple modem configurations."""
        return self._client.request("PUT", "/modems/config", json={"data": config})

    def get_modems_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified modem configuration."""
        return self._client.request("GET", f"/modems/config/{config_id}")

    def update_modems_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified modem configuration."""
        return self._client.request("PUT", f"/modems/config/{config_id}", json={"data": config})

    def get_modems_countries_status(self) -> dict[str, Any]:
        """Returns MCC and country values."""
        return self._client.request("GET", "/modems/countries/status")

    def get_modems_scan_status(self) -> dict[str, Any]:
        """Returns last operator scan values for multiple modems."""
        return self._client.request("GET", "/modems/scan/status")

    def get_modems_scan_status_by_id(self, modem_id: str) -> dict[str, Any]:
        """Returns operator scan values for specified modem."""
        return self._client.request("GET", f"/modems/scan/status/{modem_id}")

    def get_modems_signal_status(self) -> dict[str, Any]:
        """Returns signal values for multiple modems."""
        return self._client.request("GET", "/modems/signal/status")

    def get_modems_signal_status_by_id(self, modem_id: str) -> dict[str, Any]:
        """Returns signal values for specified modem."""
        return self._client.request("GET", f"/modems/signal/status/{modem_id}")

    def get_modems_status(self) -> dict[str, Any]:
        """Returns full status for multiple modems."""
        return self._client.request("GET", "/modems/status")

    def get_modems_status_by_id(self, modem_id: str) -> dict[str, Any]:
        """Returns full status for specified modem."""
        return self._client.request("GET", f"/modems/status/{modem_id}")

    def modems_actions_change_pin(self, modem_id: str, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Changes SIM card PIN code."""
        return self._client.request(
            "POST", f"/modems/{modem_id}/actions/change_pin", json=None if data is None else {"data": data}
        )

    def modems_actions_exec_at(self, modem_id: str, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Executes AT command."""
        return self._client.request(
            "POST", f"/modems/{modem_id}/actions/exec_at", json=None if data is None else {"data": data}
        )

    def modems_actions_pin_lock(self, modem_id: str, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Changes SIM card PIN lock state."""
        return self._client.request(
            "POST", f"/modems/{modem_id}/actions/pin_lock", json=None if data is None else {"data": data}
        )

    def modems_actions_reboot(self, modem_id: str) -> dict[str, Any]:
        """Reboots specified modem."""
        return self._client.request("POST", f"/modems/{modem_id}/actions/reboot")

    def modems_actions_restart_connection(self, modem_id: str) -> dict[str, Any]:
        """Restarts connection of the specified modem."""
        return self._client.request("POST", f"/modems/{modem_id}/actions/restart_connection")

    def modems_actions_scan_network(self, modem_id: str) -> dict[str, Any]:
        """Scans mobile network and returns available operators with details."""
        return self._client.request("POST", f"/modems/{modem_id}/actions/scan_network")

    def modems_actions_send_ussd(self, modem_id: str, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Sends USSD code."""
        return self._client.request(
            "POST", f"/modems/{modem_id}/actions/send_ussd", json=None if data is None else {"data": data}
        )

    def modems_actions_sim_unblock(self, modem_id: str, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Unblocks SIM card with PUK and sets a new PIN."""
        return self._client.request(
            "POST", f"/modems/{modem_id}/actions/sim_unblock", json=None if data is None else {"data": data}
        )

    def modems_actions_sim_unlock(self, modem_id: str, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Unlocks SIM card with PIN."""
        return self._client.request(
            "POST", f"/modems/{modem_id}/actions/sim_unlock", json=None if data is None else {"data": data}
        )

    def modems_actions_switch_sim(self, modem_id: str) -> dict[str, Any]:
        """Switches to next SIM of the specified modem."""
        return self._client.request("POST", f"/modems/{modem_id}/actions/switch_sim")

    def get_modems_global(self, modem_id: str) -> dict[str, Any]:
        """Returns global modem configuration."""
        return self._client.request("GET", f"/modems/{modem_id}/global")

    def update_modems_global(self, modem_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates global modem configuration."""
        return self._client.request("PUT", f"/modems/{modem_id}/global", json={"data": config})
