from ...endpoints import *
from .gateway import Gateway


class TRB143(Gateway):
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool | str = True) -> None:
        super().__init__(base_url, timeout=timeout, verify=verify)

        self.ldp = LDP(self._client)
        self.integrity = Integrity(self._client)
        self.two_fa_login = TwoFALogin(self._client)
        self.two_fa = TwoFA(self._client)
        self.sso_login = SSOLogin(self._client)
        self.sso = SSO(self._client)
        self.iec_60870_5_client = IEC608705Client(self._client)
        self.hotspot = Hotspot(self._client)
        self.iec_60870_5_server = IEC608705Server(self._client)
        self.ports_settings = PortsSettings(self._client)
        self.smcroute = SMCRoute(self._client)
        self.m_bus = MBus(self._client)
        self.dhcp_relay = DHCPRelay(self._client)
        self.dot1x = Dot1X(self._client)
        self.site_manager_client_status = SiteManagerClientStatus(self._client)
        self.openconnect = OpenConnect(self._client)
        self.operator_lists = OperatorLists(self._client)
        self.overip = OverIP(self._client)
        self.universal_gateway = UniversalGateway(self._client)
        self.wake_on_lan = WakeOnLan(self._client)
        self.call_utilities = CallUtilities(self._client)
        self.network_usage = NetworkUsage(self._client)
        self.serial = Serial(self._client)
