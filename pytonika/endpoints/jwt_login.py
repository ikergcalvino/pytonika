from typing import Any

from ._base import Endpoint


class JWTLogin(Endpoint):
    def jwt_login(self, config: dict[str, Any]) -> dict[str, Any]:
        """JWT authentication endpoint.

        .. deprecated::
        """
        endpoint = "/jwt_login"

        return self._api_client.post(endpoint, data=config)
