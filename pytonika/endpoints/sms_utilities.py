from typing import Any

from ._base import Endpoint


class SMSUtilities(Endpoint):
    def get_sms_utilities_rules_config(self) -> dict[str, Any]:
        """Returns all SMS Rules configurations."""
        endpoint = "/sms_utilities/rules/config"

        return self._api_client.get(endpoint)

    def create_sms_utilities_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new SMS rule configuration."""
        endpoint = "/sms_utilities/rules/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_sms_utilities_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected SMS Rules configurations."""
        endpoint = "/sms_utilities/rules/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_sms_utilities_rules_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected SMS Rules configurations."""
        return [self.delete_sms_utilities_rules_config_by_id(rule_id) for rule_id in config]

    def get_sms_utilities_rules_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the selected SMS rule configuration."""
        endpoint = f"/sms_utilities/rules/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_sms_utilities_rules_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected SMS rule configuration."""
        endpoint = f"/sms_utilities/rules/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_sms_utilities_rules_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the selected SMS rule configuration."""
        endpoint = f"/sms_utilities/rules/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_sms_utilities_rules_options(self) -> dict[str, Any]:
        """Returns SMS Rules options."""
        endpoint = "/sms_utilities/rules/options"

        return self._api_client.get(endpoint)
