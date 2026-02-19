from .router import Router


class RUT301(Router):
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool = True) -> None:
        super().__init__(base_url, timeout=timeout, verify=verify)

        self.serial = None
        self.input_output = None
        self.dlna = None
        self.console = None
        self.ntrip = None
        self.bacnet = None
        self.port_based_vlan = None
        self.sd_usb_tools = None
        self.samba = None
        self.dot1x = None
        self.overip = None
        self.universal_gateway = None
        self.impulse_counter = None
