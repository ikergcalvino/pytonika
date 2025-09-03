from .._client import APIClient


class Unauthorized:
    def __init__(self, api_client: APIClient) -> None:
        self._api_client = api_client

    def get_unauthorized_status(self) -> dict[str, object]:
        endpoint = "/unauthorized/status"

        return self._api_client.get(endpoint)
