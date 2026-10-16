from typing import Any

from ._endpoint import Endpoint


class SMSUtilities(Endpoint):
    def get_sms_utilities_rules_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all SMS Rules configurations."""
        return self._client.request("GET", "/sms_utilities/rules/config", params={"all_options": all_options})

    def create_sms_utilities_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new SMS rule configuration."""
        return self._client.request("POST", "/sms_utilities/rules/config", json={"data": config})

    def update_sms_utilities_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected SMS Rules configurations."""
        return self._client.request("PUT", "/sms_utilities/rules/config", json={"data": config})

    def delete_sms_utilities_rules_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the selected SMS Rules configurations."""
        return self._client.request("DELETE", "/sms_utilities/rules/config", json={"data": config})

    def get_sms_utilities_rules_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the selected SMS rule configuration."""
        return self._client.request(
            "GET", f"/sms_utilities/rules/config/{config_id}", params={"all_options": all_options}
        )

    def update_sms_utilities_rules_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected SMS rule configuration."""
        return self._client.request("PUT", f"/sms_utilities/rules/config/{config_id}", json={"data": config})

    def delete_sms_utilities_rules_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the selected SMS rule configuration."""
        return self._client.request("DELETE", f"/sms_utilities/rules/config/{config_id}")

    def get_sms_utilities_rules_options(self) -> dict[str, Any]:
        """Returns SMS Rules options."""
        return self._client.request("GET", "/sms_utilities/rules/options")
