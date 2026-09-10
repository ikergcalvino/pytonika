from ...endpoints import *
from .gateway import Gateway


class TRB245(Gateway):
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool | str = True) -> None:
        super().__init__(base_url, timeout=timeout, verify=verify)

        self.serial = Serial(self._client)
        self.console = Console(self._client)
        self.ntrip = NTRIP(self._client)
        self.hotspot = Hotspot(self._client)
        self.gps = GPS(self._client)
        self.sim_idle_protection = SIMIdleProtection(self._client)
        self.modem_control = ModemControl(self._client)
        self.nat_offloading = NATOffloading(self._client)
        self.dot1x = Dot1X(self._client)
        self.esim = eSIM(self._client)
        self.operator_lists = OperatorLists(self._client)
        self.dfota = DFOTA(self._client)
        self.sim_switch = SIMSwitch(self._client)
        self.overip = OverIP(self._client)
        self.wake_on_lan = WakeOnLan(self._client)
        self.call_utilities = CallUtilities(self._client)
