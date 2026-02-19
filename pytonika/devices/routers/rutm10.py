from .router import Router


class RUTM10(Router):
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool = True) -> None:
        super().__init__(base_url, timeout=timeout, verify=verify)

        self.serial = None
        self.input_output = None
        self.dlna = None
        self.console = None
        self.wireless = None
        self.ntrip = None
        self.bacnet = None
        self.port_based_vlan = None
        self.sd_usb_tools = None
        self.samba = None
        self.hotspot_2 = None
        self.tailscale = None
        self.ports_settings = None
        self.wifi_scanner = None
        self.port_mirroring = None
        self.dot1x = None
        self.openconnect = None
        self.overip = None
        self.universal_gateway = None
        self.impulse_counter = None
        self.relayd = None
        self.network_usage = None
