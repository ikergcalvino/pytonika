import ssl

from ...endpoints import *
from .access_point import AccessPoint


class TAP400(AccessPoint):
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool | ssl.SSLContext = True) -> None:
        super().__init__(base_url, timeout=timeout, verify=verify)

        self.hotspot = Hotspot(self._client)
