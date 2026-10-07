import ssl

from ...endpoints import *
from .router import Router


class RUT300(Router):
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool | ssl.SSLContext = True) -> None:
        super().__init__(base_url, timeout=timeout, verify=verify)

        self.aws = AWS(self._client)
        self.bfd = BFD(self._client)
        self.console = Console(self._client)
        self.dlna = DLNA(self._client)
        self.eoip = EoIP(self._client)
        self.event_juggler = EventJuggler(self._client)
        self.impulse_counter = ImpulseCounter(self._client)
        self.input_output = InputOutput(self._client)
        self.internet_connection = InternetConnection(self._client)
        self.nat64 = NAT64(self._client)
        self.network = Network(self._client)
        self.ntrip = NTRIP(self._client)
        self.overip = OverIP(self._client)
        self.password_policy = PasswordPolicy(self._client)
        self.port_based_vlan = PortBasedVlan(self._client)
        self.port_mirroring = PortMirroring(self._client)
        self.qos = QoS(self._client)
        self.samba = Samba(self._client)
        self.sd_usb_tools = SDUSBTools(self._client)
        self.serial = Serial(self._client)
        self.sqm = SQM(self._client)
        self.traffic_logging = TrafficLogging(self._client)
        self.udp_broadcast_relay = UDPBroadcastRelay(self._client)
        self.vrf = VRF(self._client)
        self.vrrp = VRRP(self._client)
