from .router import Router


class RUT951(Router):
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool = True) -> None:
        super().__init__(base_url, timeout=timeout, verify=verify)

        self.sms_gateway = None
        self.input_output = None
        self.wireless = None
        self.bacnet = None
        self.port_based_vlan = None
        self.hotspot_2 = None
        self.data_limit = None
        self.ports_settings = None
        self.smpp = None
        self.sms_utilities = None
        self.messages = None
        self.sim_idle_protection = None
        self.wifi_scanner = None
        self.port_mirroring = None
        self.dot1x = None
        self.apn_database = None
        self.esim = None
        self.operator_lists = None
        self.sim_cards = None
        self.modems = None
        self.dfota = None
        self.data_usage = None
        self.sim_switch = None
        self.universal_gateway = None
        self.impulse_counter = None
        self.relayd = None
        self.call_utilities = None
