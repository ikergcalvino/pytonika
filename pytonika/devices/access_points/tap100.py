import ssl

from ...endpoints import *
from .access_point import AccessPoint


class TAP100(AccessPoint):
    """Teltonika TAP100 access point, with the endpoints documented for RutOS 7.26."""

    def __init__(
        self,
        base_url: str,
        *,
        timeout: float = 10.0,
        verify: bool | ssl.SSLContext = True,
    ) -> None:
        super().__init__(base_url, timeout=timeout, verify=verify)

        self.wireless_reboot = WirelessReboot(self._client)
