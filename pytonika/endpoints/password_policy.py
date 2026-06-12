from typing import Any

from ._base import Endpoint


class PasswordPolicy(Endpoint):
    def get_password_policy_config(self) -> dict[str, Any]:
        """Returns password policy configuration."""
        endpoint = "/password_policy/config"

        return self._api_client.get(endpoint)

    def update_password_policy_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates password policy configuration."""
        endpoint = "/password_policy/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_password_policy_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns password policy configuration."""
        endpoint = f"/password_policy/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_password_policy_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates password policy configuration."""
        endpoint = f"/password_policy/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
