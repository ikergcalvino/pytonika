import ssl

from ...endpoints import *
from .gateway import Gateway


class TRB145(Gateway):
    """Teltonika TRB145 gateway, with the endpoints documented for RutOS 7.26."""

    def __init__(
        self,
        base_url: str,
        *,
        timeout: float = 10.0,
        verify: bool | ssl.SSLContext = True,
    ) -> None:
        super().__init__(base_url, timeout=timeout, verify=verify)

        self.call_utilities = CallUtilities(self._client)
        self.console = Console(self._client)
        self.dhcp_relay = DHCPRelay(self._client)
        self.greengrass_v2 = GreengrassV2(self._client)
        self.iec60870_client = IEC60870Client(self._client)
        self.iec60870_server = IEC60870Server(self._client)
        self.integrity = Integrity(self._client)
        self.ldp = LDP(self._client)
        self.lwm2m_client = LwM2MClient(self._client)
        self.modem_control = ModemControl(self._client)
        self.network_usage = NetworkUsage(self._client)
        self.ntrip = NTRIP(self._client)
        self.openconnect = OpenConnect(self._client)
        self.operator_lists = OperatorLists(self._client)
        self.ospfv3 = OSPFv3(self._client)
        self.overip = OverIP(self._client)
        self.serial = Serial(self._client)
        self.site_manager_client_status = SiteManagerClientStatus(self._client)
        self.smcroute = SMCRoute(self._client)
        self.sso = SSO(self._client)
        self.sso_login = SSOLogin(self._client)
        self.two_fa = TwoFA(self._client)
        self.two_fa_login = TwoFALogin(self._client)
        self.universal_gateway = UniversalGateway(self._client)
        self.wfq = WFQ(self._client)
        self.wireless = Wireless(self._client)
