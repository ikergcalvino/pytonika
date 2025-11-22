from ..router import Router


class RUT300(Router):
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool = True) -> None:
        super().__init__(base_url, timeout=timeout, verify=verify)

        self.serial = None
        self.input_output = None
        self.dlna = None
        self.console = None
        self.ntrip = None
        self.port_based_vlan = None
        self.sd_usb_tools = None
        self.samba = None
        self.port_mirroring = None
        self.overip = None
        self.impulse_counter = None

        self._endpoints.extend([])

    def __getattr__(self, attr: str):
        for endpoint in self._endpoints:
            if hasattr(endpoint, attr):
                return getattr(endpoint, attr)

        return super().__getattr__(attr)
