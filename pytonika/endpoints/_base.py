from .._client import APIClient


class Endpoint:
    def __init__(self, api_client: APIClient) -> None:
        self._client = api_client
