from ._base import Endpoint


class Unauthorized(Endpoint):

    def get_unauthorized_status(self) -> dict[str, object]:
        endpoint = "/unauthorized/status"

        return self._api_client.get(endpoint)
