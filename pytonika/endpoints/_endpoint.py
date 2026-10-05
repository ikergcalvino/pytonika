from .._client import APIClient


class Endpoint:
    def __init__(self, client: APIClient) -> None:
        self._client = client
