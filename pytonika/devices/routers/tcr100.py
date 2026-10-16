import ssl

from ...endpoints import *
from .router import Router


class TCR100(Router):
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool | ssl.SSLContext = True) -> None:
        super().__init__(base_url, timeout=timeout, verify=verify)

        self.apn_database = APNDatabase(self._client)
        self.aws = AWS(self._client)
        self.bfd = BFD(self._client)
        self.call_utilities = CallUtilities(self._client)
        self.data_limit = DataLimit(self._client)
        self.data_usage = DataUsage(self._client)
        self.dfota = DFOTA(self._client)
        self.eoip = EoIP(self._client)
        self.esim = eSIM(self._client)
        self.event_juggler = EventJuggler(self._client)
        self.hotspot_2 = Hotspot2(self._client)
        self.internet_connection = InternetConnection(self._client)
        self.messages = Messages(self._client)
        self.modems = Modems(self._client)
        self.nat64 = NAT64(self._client)
        self.network = Network(self._client)
        self.operator_lists = OperatorLists(self._client)
        self.password_policy = PasswordPolicy(self._client)
        self.qos = QoS(self._client)
        self.relayd = Relayd(self._client)
        self.sim_cards = SIMCards(self._client)
        self.smpp = SMPP(self._client)
        self.sms_gateway = SMSGateway(self._client)
        self.sms_utilities = SMSUtilities(self._client)
        self.sqm = SQM(self._client)
        self.traffic_logging = TrafficLogging(self._client)
        self.udp_broadcast_relay = UDPBroadcastRelay(self._client)
        self.vrf = VRF(self._client)
        self.vrrp = VRRP(self._client)
        self.wifi_scanner = WiFiScanner(self._client)
        self.wireless = Wireless(self._client)
