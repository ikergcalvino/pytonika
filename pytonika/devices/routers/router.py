from ...api_client import ApiClient
from ...endpoints import Authentication, Firewall, Firmware, Interfaces, Unauthorized, Users, WireGuard


class Router():
    def __init__(self, base_url: str):
        self._api_client = ApiClient(base_url)

        self.authentication = Authentication(self._api_client)
        self.firewall = Firewall(self._api_client)
        self.firmware = Firmware(self._api_client)
        self.interfaces = Interfaces(self._api_client)
        self.unauthorized = Unauthorized(self._api_client)
        self.users = Users(self._api_client)
        self.wireguard = WireGuard(self._api_client)

    def __getattr__(self, attr):
        for endpoint in [self.authentication,
                         self.firewall,
                         self.firmware,
                         self.interfaces,
                         self.unauthorized,
                         self.users,
                         self.wireguard]:

            if hasattr(endpoint, attr):
                return getattr(endpoint, attr)

        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{attr}'"
        )
