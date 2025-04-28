from .router import Router
from ...endpoints import Authentication, Users, Firmware, Interfaces


class RUTX08(Router):
    def __init__(self, base_url: str):
        super().__init__(base_url)

        self.auth = Authentication(self._api_client)
        self.users = Users(self._api_client)
        self.firmware = Firmware(self._api_client)
        self.interfaces = Interfaces(self._api_client)

    def __getattr__(self, attr):
        for endpoint in [self.auth, self.users, self.firmware, self.interfaces]:
            if hasattr(endpoint, attr):
                return getattr(endpoint, attr)

        return super().__getattr__(attr)
