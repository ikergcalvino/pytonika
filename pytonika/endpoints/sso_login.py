from typing import Any

from ._endpoint import Endpoint


class SSOLogin(Endpoint):
    """Endpoints of the "Sso Login" page of the Teltonika Web API reference."""

    def sso_login(
        self,
        config: dict[str, Any],
    ) -> dict[str, Any]:
        """Authenticates user via SSO provider."""
        return self._client.request(
            "POST",
            "/sso_login",
            json={"data": config},
        )
