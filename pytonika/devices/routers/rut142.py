from .router import Router
from ...endpoints import *


class RUT142(Router):
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool = True) -> None:
        super().__init__(base_url, timeout=timeout, verify=verify)

        self.serial = Serial(self._client)
        self.console = Console(self._client)
        self.wireless = Wireless(self._client)
        self.ntrip = NTRIP(self._client)
        self.bacnet = Bacnet(self._client)
        self.port_based_vlan = PortBasedVlan(self._client)
        self.hotspot_2 = Hotspot2(self._client)
        self.ports_settings = PortsSettings(self._client)
        self.wifi_scanner = WiFiScanner(self._client)
        self.dot1x = Dot1X(self._client)
        self.overip = OverIP(self._client)
        self.universal_gateway = UniversalGateway(self._client)
        self.relayd = Relayd(self._client)
