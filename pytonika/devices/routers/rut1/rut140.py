from ..router import Router


class RUT140(Router):
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool = True) -> None:
        super().__init__(base_url, timeout=timeout, verify=verify)

        self.wireless = None
        self.bacnet = None
        self.port_based_vlan = None
        self.hotspot_2 = None
        self.ports_settings = None
        self.wifi_scanner = None
        self.dot1x = None
        self.universal_gateway = None
        self.relayd = None

        self._endpoints.extend([])

    def __getattr__(self, attr: str):
        for endpoint in self._endpoints:
            if hasattr(endpoint, attr):
                return getattr(endpoint, attr)

        return super().__getattr__(attr)
