from typing import Any

from ._base import Endpoint


class Modems(Endpoint):
    def get_modems_status(self) -> dict[str, Any]:
        """Returns full status for multiple modems."""
        endpoint = "/modems/status"

        return self._api_client.get(endpoint)

    def get_modems_status_by_id(self, modem_id: str) -> dict[str, Any]:
        """Returns full status for specified modem."""
        endpoint = f"/modems/status/{modem_id}"

        return self._api_client.get(endpoint)

    def get_modems_apns_status(self) -> dict[str, Any]:
        """Returns APN values for multiple modems."""
        endpoint = "/modems/apns/status"

        return self._api_client.get(endpoint)

    def get_modems_apns_status_by_id(self, modem_id: str) -> dict[str, Any]:
        """Returns APN values for specified modem."""
        endpoint = f"/modems/apns/status/{modem_id}"

        return self._api_client.get(endpoint)

    def get_modems_signal_status(self) -> dict[str, Any]:
        """Returns signal values for multiple modems."""
        endpoint = "/modems/signal/status"

        return self._api_client.get(endpoint)

    def get_modems_signal_status_by_id(self, modem_id: str) -> dict[str, Any]:
        """Returns signal values for specified modem."""
        endpoint = f"/modems/signal/status/{modem_id}"

        return self._api_client.get(endpoint)

    def get_modems_scan_status(self) -> dict[str, Any]:
        """Returns last operator scan values for multiple modems."""
        endpoint = "/modems/scan/status"

        return self._api_client.get(endpoint)

    def get_modems_scan_status_by_id(self, modem_id: str) -> dict[str, Any]:
        """Returns operator scan values for specified modem."""
        endpoint = f"/modems/scan/status/{modem_id}"

        return self._api_client.get(endpoint)

    def get_modems_countries_status(self) -> dict[str, Any]:
        """Returns MCC and country values."""
        endpoint = "/modems/countries/status"

        return self._api_client.get(endpoint)

    def get_modems_global(self, modem_id: str) -> dict[str, Any]:
        """Returns global modem configuration."""
        endpoint = f"/modems/{modem_id}/global"

        return self._api_client.get(endpoint)

    def update_modems_global(self, modem_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates global modem configuration."""
        endpoint = f"/modems/{modem_id}/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def modems_actions_send_ussd(self, modem_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Sends USSD code."""
        endpoint = f"/modems/{modem_id}/actions/send_ussd"

        return self._api_client.post(endpoint, data={"data": data})

    def modems_actions_scan_network(self, modem_id: str) -> dict[str, Any]:
        """Scans mobile network and returns available operators with details."""
        endpoint = f"/modems/{modem_id}/actions/scan_network"

        return self._api_client.post(endpoint)

    def modems_actions_reboot(self, modem_id: str) -> dict[str, Any]:
        """Reboots specified modem."""
        endpoint = f"/modems/{modem_id}/actions/reboot"

        return self._api_client.post(endpoint)

    def modems_actions_exec_at(self, modem_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Executes AT command."""
        endpoint = f"/modems/{modem_id}/actions/exec_at"

        return self._api_client.post(endpoint, data={"data": data})

    def modems_actions_restart_connection(self, modem_id: str) -> dict[str, Any]:
        """Restarts connection of the specified modem."""
        endpoint = f"/modems/{modem_id}/actions/restart_connection"

        return self._api_client.post(endpoint)

    def modems_actions_switch_sim(self, modem_id: str) -> dict[str, Any]:
        """Switches to next SIM of the specified modem."""
        endpoint = f"/modems/{modem_id}/actions/switch_sim"

        return self._api_client.post(endpoint)

    def modems_actions_sim_unblock(self, modem_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Unblocks SIM card with PUK and sets a new PIN."""
        endpoint = f"/modems/{modem_id}/actions/sim_unblock"

        return self._api_client.post(endpoint, data={"data": data})

    def modems_actions_sim_unlock(self, modem_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Unlocks SIM card with PIN."""
        endpoint = f"/modems/{modem_id}/actions/sim_unlock"

        return self._api_client.post(endpoint, data={"data": data})

    def modems_actions_change_pin(self, modem_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Changes SIM card PIN code."""
        endpoint = f"/modems/{modem_id}/actions/change_pin"

        return self._api_client.post(endpoint, data={"data": data})

    def modems_actions_pin_lock(self, modem_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Changes SIM card PIN lock state."""
        endpoint = f"/modems/{modem_id}/actions/pin_lock"

        return self._api_client.post(endpoint, data={"data": data})
