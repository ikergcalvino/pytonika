import ssl

from ...endpoints import *
from .router import Router


class RUT140(Router):
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool | ssl.SSLContext = True) -> None:
        super().__init__(base_url, timeout=timeout, verify=verify)

        self.internet_connection = InternetConnection(self._client)
        self.nat64 = NAT64(self._client)
        self.ldp = LDP(self._client)
        self.integrity = Integrity(self._client)
        self.two_fa_login = TwoFALogin(self._client)
        self.two_fa = TwoFA(self._client)
        self.wireless = Wireless(self._client)
        self.sso_login = SSOLogin(self._client)
        self.sso = SSO(self._client)
        self.wireless_reboot = WirelessReboot(self._client)
        self.bacnet = Bacnet(self._client)
        self.port_based_vlan = PortBasedVlan(self._client)
        self.hotspot_2 = Hotspot2(self._client)
        self.event_juggler = EventJuggler(self._client)
        self.iec_60870_5_client = IEC608705Client(self._client)
        self.network = Network(self._client)
        self.sqm = SQM(self._client)
        self.iec_60870_5_server = IEC608705Server(self._client)
        self.bfd = BFD(self._client)
        self.qos = QoS(self._client)
        self.ports_settings = PortsSettings(self._client)
        self.smcroute = SMCRoute(self._client)
        self.password_policy = PasswordPolicy(self._client)
        self.dhcp_relay = DHCPRelay(self._client)
        self.wifi_scanner = WiFiScanner(self._client)
        self.eoip = EoIP(self._client)
        self.dot1x = Dot1X(self._client)
        self.site_manager_client_status = SiteManagerClientStatus(self._client)
        self.traffic_logging = TrafficLogging(self._client)
        self.universal_gateway = UniversalGateway(self._client)
        self.vrrp = VRRP(self._client)
        self.relayd = Relayd(self._client)
        self.aws = AWS(self._client)
        self.udp_broadcast_relay = UDPBroadcastRelay(self._client)
        self.vrf = VRF(self._client)
