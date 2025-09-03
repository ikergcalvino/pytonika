from ..._client import APIClient
from ...endpoints import Authentication, Firewall, Firmware, Interfaces, Unauthorized, Users, WireGuard


class Router():
    def __init__(self, base_url: str) -> None:
        self._client = APIClient(base_url)

        self.authentication = Authentication(self._client)
        self.firewall = Firewall(self._client)
        self.firmware = Firmware(self._client)
        self.interfaces = Interfaces(self._client)
        self.unauthorized = Unauthorized(self._client)
        self.users = Users(self._client)
        self.wireguard = WireGuard(self._client)

        self._endpoints = [
            self.authentication,
            self.firewall,
            self.firmware,
            self.interfaces,
            self.unauthorized,
            self.users,
            self.wireguard
        ]

    def __getattr__(self, attr: str):
        for endpoint in self._endpoints:
            if hasattr(endpoint, attr):
                return getattr(endpoint, attr)

        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{attr}'"
        )
