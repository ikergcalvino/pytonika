from typing import Any

from ._endpoint import Endpoint


class Starlink(Endpoint):
    def get_starlink_status(self) -> dict[str, Any]:
        """Returns Starlink dish status."""
        endpoint = "/starlink/status"

        return self._client.request("GET", endpoint)

    def starlink_actions_stow(self) -> dict[str, Any]:
        """Stows the Starlink dish."""
        endpoint = "/starlink/actions/stow"

        return self._client.request("POST", endpoint)

    def starlink_actions_unstow(self) -> dict[str, Any]:
        """Unstows the Starlink dish."""
        endpoint = "/starlink/actions/unstow"

        return self._client.request("POST", endpoint)

    def starlink_actions_reboot(self) -> dict[str, Any]:
        """Reboots the Starlink dish."""
        endpoint = "/starlink/actions/reboot"

        return self._client.request("POST", endpoint)
