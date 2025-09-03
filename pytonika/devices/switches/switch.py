from ..._client import APIClient


class Switch():
    def __init__(self, base_url: str) -> None:
        self._client = APIClient(base_url)

        self._endpoints = []

    def __getattr__(self, attr: str):
        for endpoint in self._endpoints:
            if hasattr(endpoint, attr):
                return getattr(endpoint, attr)

        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{attr}'"
        )
