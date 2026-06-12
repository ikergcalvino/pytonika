from typing import Any

from ._base import Endpoint


class TwoFALogin(Endpoint):
    def two_fa_login(self, config: dict[str, Any]) -> dict[str, Any]:
        """Verifies 2FA during login."""
        endpoint = "/2fa_login"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)
