from typing import Any

from ._endpoint import Endpoint


class Starlink(Endpoint):
    def starlink_actions_reboot(self) -> dict[str, Any]:
        """Reboots the Starlink dish."""
        return self._client.request("POST", "/starlink/actions/reboot")

    def starlink_actions_stow(self) -> dict[str, Any]:
        """Stows the Starlink dish."""
        return self._client.request("POST", "/starlink/actions/stow")

    def starlink_actions_unstow(self) -> dict[str, Any]:
        """Unstows the Starlink dish."""
        return self._client.request("POST", "/starlink/actions/unstow")

    def get_starlink_status(self) -> dict[str, Any]:
        """Returns Starlink dish status."""
        return self._client.request("GET", "/starlink/status")
