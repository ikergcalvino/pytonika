from typing import Any

from ._endpoint import Endpoint


class PasswordPolicy(Endpoint):
    def get_password_policy_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns password policy configuration."""
        return self._client.request("GET", "/password_policy/config", params={"all_options": all_options})

    def update_password_policy_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates password policy configuration."""
        return self._client.request("PUT", "/password_policy/config", json={"data": config})

    def get_password_policy_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns password policy configuration."""
        return self._client.request("GET", f"/password_policy/config/{config_id}", params={"all_options": all_options})

    def update_password_policy_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates password policy configuration."""
        return self._client.request("PUT", f"/password_policy/config/{config_id}", json={"data": config})
