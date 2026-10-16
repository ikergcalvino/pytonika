import ssl

from ...endpoints import *
from .access_point import AccessPoint


class TAP200(AccessPoint):
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool | ssl.SSLContext = True) -> None:
        super().__init__(base_url, timeout=timeout, verify=verify)

        self.openvpn = OpenVPN(self._client)
