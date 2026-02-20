from .router import Router
from ...endpoints import *


class RUT300(Router):
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool = True) -> None:
        super().__init__(base_url, timeout=timeout, verify=verify)

        self.serial = Serial(self._client)
        self.input_output = InputOutput(self._client)
        self.dlna = DLNA(self._client)
        self.console = Console(self._client)
        self.ntrip = NTRIP(self._client)
        self.port_based_vlan = PortBasedVlan(self._client)
        self.sd_usb_tools = SDUSBTools(self._client)
        self.samba = Samba(self._client)
        self.port_mirroring = PortMirroring(self._client)
        self.overip = OverIP(self._client)
        self.impulse_counter = ImpulseCounter(self._client)
