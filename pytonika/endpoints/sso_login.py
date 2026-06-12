from typing import Any

from ._base import Endpoint


class SSOLogin(Endpoint):
    def sso_login(self, config: dict[str, Any]) -> dict[str, Any]:
        """Authenticates user via SSO provider."""
        endpoint = "/sso_login"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)
