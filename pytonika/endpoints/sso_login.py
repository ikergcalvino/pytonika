from typing import Any

from ._endpoint import Endpoint


class SSOLogin(Endpoint):
    def sso_login(self, config: dict[str, Any]) -> dict[str, Any]:
        """Authenticates user via SSO provider."""
        return self._client.request("POST", "/sso_login", json={"data": config})
