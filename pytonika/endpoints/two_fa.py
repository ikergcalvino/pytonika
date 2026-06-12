from typing import Any

from ._base import Endpoint


class TwoFA(Endpoint):
    def get_two_fa_config(self) -> dict[str, Any]:
        """Returns 2FA configuration."""
        endpoint = "/2fa/config"

        return self._api_client.get(endpoint)

    def update_two_fa_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates 2FA configuration."""
        endpoint = "/2fa/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_two_fa_config_by_id(self, two_fa_id: str) -> dict[str, Any]:
        """Returns 2FA configuration."""
        endpoint = f"/2fa/config/{two_fa_id}"

        return self._api_client.get(endpoint)

    def update_two_fa_config_by_id(self, two_fa_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates 2FA configuration."""
        endpoint = f"/2fa/config/{two_fa_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def two_fa_actions_setup(self, config: dict[str, Any]) -> dict[str, Any]:
        """Setup 2FA for user."""
        endpoint = "/2fa/actions/setup"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def two_fa_actions_verify(self, config: dict[str, Any]) -> dict[str, Any]:
        """Verify 2FA code for user."""
        endpoint = "/2fa/actions/verify"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def two_fa_actions_remove(self, config: dict[str, Any]) -> dict[str, Any]:
        """Remove 2FA for user."""
        endpoint = "/2fa/actions/remove"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)
