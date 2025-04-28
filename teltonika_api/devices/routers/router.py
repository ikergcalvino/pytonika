from ...api_client import ApiClient
from ...endpoints import Unauthorized


class Router:
    def __init__(self, base_url: str):
        self._api_client = ApiClient(base_url)

        self.unauthorized = Unauthorized(self._api_client)

    def __getattr__(self, attr):
        for endpoint in [self.unauthorized]:
            if hasattr(endpoint, attr):
                return getattr(endpoint, attr)

        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{attr}'"
        )
