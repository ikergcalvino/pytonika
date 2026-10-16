from typing import Any

from ._endpoint import Endpoint


class TwoFA(Endpoint):
    def two_fa_actions_remove(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Remove 2FA for user."""
        return self._client.request("POST", "/2fa/actions/remove", json=None if config is None else {"data": config})

    def two_fa_actions_setup(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Setup 2FA for user."""
        return self._client.request("POST", "/2fa/actions/setup", json=None if config is None else {"data": config})

    def two_fa_actions_verify(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Verify 2FA code for user."""
        return self._client.request("POST", "/2fa/actions/verify", json=None if config is None else {"data": config})

    def get_two_fa_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns 2FA configuration."""
        return self._client.request("GET", "/2fa/config", params={"all_options": all_options})

    def update_two_fa_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates 2FA configuration."""
        return self._client.request("PUT", "/2fa/config", json={"data": config})

    def get_two_fa_config_by_id(self, two_fa_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns 2FA configuration."""
        return self._client.request("GET", f"/2fa/config/{two_fa_id}", params={"all_options": all_options})

    def update_two_fa_config_by_id(self, two_fa_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates 2FA configuration."""
        return self._client.request("PUT", f"/2fa/config/{two_fa_id}", json={"data": config})
