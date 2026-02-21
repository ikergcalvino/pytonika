from typing import Any

from ._base import Endpoint


class Unauthorized(Endpoint):

    def get_unauthorized_status(self) -> dict[str, Any]:
        endpoint = "/unauthorized/status"

        return self._api_client.get(endpoint)
