import ssl

from ...endpoints import *
from .router import Router


class RUT955(Router):
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool | ssl.SSLContext = True) -> None:
        super().__init__(base_url, timeout=timeout, verify=verify)

        self.serial = Serial(self._client)
        self.usb_tools = UsbTools(self._client)
        self.apn_database = APNDatabase(self._client)
        self.data_limit = DataLimit(self._client)
        self.vrrp = VRRP(self._client)
        self.operator_lists = OperatorLists(self._client)
        self.sim_cards = SIMCards(self._client)
        self.modems = Modems(self._client)
        self.data_usage = DataUsage(self._client)
        self.sim_switch = SIMSwitch(self._client)
        self.overip = OverIP(self._client)
        self.sqm = SQM(self._client)
        self.udp_broadcast_relay = UDPBroadcastRelay(self._client)
        self.wireless = Wireless(self._client)
        self.port_mirroring = PortMirroring(self._client)
        self.input_output = InputOutput(self._client)
        self.wifi_scanner = WiFiScanner(self._client)
        self.relayd = Relayd(self._client)
        self.qos = QoS(self._client)
        self.console = Console(self._client)
        self.traffic_logging = TrafficLogging(self._client)
        self.ntrip = NTRIP(self._client)
        self.modem_control = ModemControl(self._client)
        self.sim_idle_protection = SIMIdleProtection(self._client)
        self.gps = GPS(self._client)
        self.port_based_vlan = PortBasedVlan(self._client)
        self.smpp = SMPP(self._client)
        self.bacnet = Bacnet(self._client)
        self.samba = Samba(self._client)
        self.dlna = DLNA(self._client)
        self.hotspot_2 = Hotspot2(self._client)
        self.sms_utilities = SMSUtilities(self._client)
        self.sms_gateway = SMSGateway(self._client)
        self.call_utilities = CallUtilities(self._client)
        self.messages = Messages(self._client)
