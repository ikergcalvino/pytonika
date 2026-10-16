from typing import Any

from ._endpoint import Endpoint


class JWTLogin(Endpoint):
    def jwt_login(self, config: dict[str, Any]) -> bytes | dict[str, Any]:
        """JWT authentication endpoint."""
        return self._client.request("POST", "/jwt_login", json=config, download=True)
