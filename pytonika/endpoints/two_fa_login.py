from typing import Any

from ._endpoint import Endpoint


class TwoFALogin(Endpoint):
    def two_fa_login(self, config: dict[str, Any]) -> dict[str, Any]:
        """Verifies 2FA during login."""
        endpoint = "/2fa_login"

        data = {"data": config}

        return self._client.request("POST", endpoint, json=data)
