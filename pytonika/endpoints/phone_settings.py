from typing import Any

from ._endpoint import Endpoint


class PhoneSettings(Endpoint):
    def get_phone_settings_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Phone Settings configuration in an array."""
        return self._client.request("GET", "/phone_settings/config", params={"all_options": all_options})

    def update_phone_settings_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Phone Settings configuration in an array."""
        return self._client.request("PUT", "/phone_settings/config", json={"data": config})

    def get_phone_settings_config_by_id(
        self, phone_setting_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns Phone Settings configuration."""
        return self._client.request(
            "GET", f"/phone_settings/config/{phone_setting_id}", params={"all_options": all_options}
        )

    def update_phone_settings_config_by_id(self, phone_setting_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Phone Settings configuration."""
        return self._client.request("PUT", f"/phone_settings/config/{phone_setting_id}", json={"data": config})
