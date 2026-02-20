from .router import Router
from ...endpoints import *


class RUTM08(Router):
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool = True) -> None:
        super().__init__(base_url, timeout=timeout, verify=verify)

        self.serial = Serial(self._client)
        self.input_output = InputOutput(self._client)
        self.dlna = DLNA(self._client)
        self.console = Console(self._client)
        self.ntrip = NTRIP(self._client)
        self.bacnet = Bacnet(self._client)
        self.port_based_vlan = PortBasedVlan(self._client)
        self.sd_usb_tools = SDUSBTools(self._client)
        self.samba = Samba(self._client)
        self.tailscale = Tailscale(self._client)
        self.ports_settings = PortsSettings(self._client)
        self.port_mirroring = PortMirroring(self._client)
        self.dot1x = Dot1X(self._client)
        self.openconnect = OpenConnect(self._client)
        self.overip = OverIP(self._client)
        self.universal_gateway = UniversalGateway(self._client)
        self.impulse_counter = ImpulseCounter(self._client)
        self.network_usage = NetworkUsage(self._client)
