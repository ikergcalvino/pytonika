from typing import Any

from ._endpoint import Endpoint


class JWTLogin(Endpoint):
    """Endpoints of the "Jwt Login" page of the Teltonika Web API reference."""

    def jwt_login(
        self,
        config: dict[str, Any],
    ) -> bytes | dict[str, Any]:
        """JWT authentication endpoint."""
        return self._client.request(
            "POST",
            "/jwt_login",
            json=config,
            download=True,
        )
