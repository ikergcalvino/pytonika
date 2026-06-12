from typing import Any

from ._base import Endpoint


class PhoneSettings(Endpoint):
    def get_phone_settings_config(self) -> dict[str, Any]:
        """Returns Phone Settings configuration in an array."""
        endpoint = "/phone_settings/config"

        return self._api_client.get(endpoint)

    def update_phone_settings_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Phone Settings configuration in an array."""
        endpoint = "/phone_settings/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_phone_settings_config_by_id(self, phone_setting_id: str) -> dict[str, Any]:
        """Returns Phone Settings configuration."""
        endpoint = f"/phone_settings/config/{phone_setting_id}"

        return self._api_client.get(endpoint)

    def update_phone_settings_config_by_id(self, phone_setting_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Phone Settings configuration."""
        endpoint = f"/phone_settings/config/{phone_setting_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
