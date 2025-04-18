from ..api_client import ApiClient
from ..endpoints import Authentication, Users, Firmware, Interfaces


class RUT200:
    def __init__(self, base_url: str):
        self._api_client = ApiClient(base_url)

        self.auth = Authentication(self._api_client)
        self.users = Users(self._api_client)
        self.firmware = Firmware(self._api_client)
        self.interfaces = Interfaces(self._api_client)

    def __getattr__(self, attr):
        for endpoint in [self.auth, self.users, self.firmware, self.interfaces]:
            if hasattr(endpoint, attr):
                return getattr(endpoint, attr)

        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{attr}'"
        )
