from typing import Any

from ._base import Endpoint


class CallUtilities(Endpoint):
    def get_call_utilities_global(self) -> dict[str, Any]:
        """Returns the Call Utilities Global Configuration."""
        endpoint = "/call_utilities/global"

        return self._api_client.get(endpoint)

    def update_call_utilities_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the Call Utilities Global configuration."""
        endpoint = "/call_utilities/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_call_utilities_rules_options(self) -> dict[str, Any]:
        """Returns Call Utilities options."""
        endpoint = "/call_utilities/rules/options"

        return self._api_client.get(endpoint)

    def get_call_utilities_rules_config(self) -> dict[str, Any]:
        """Returns all Call Utilities Rules configurations."""
        endpoint = "/call_utilities/rules/config"

        return self._api_client.get(endpoint)

    def create_call_utilities_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Call Utilities rule configuration."""
        endpoint = "/call_utilities/rules/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_call_utilities_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Call Utilities Rules configurations."""
        endpoint = "/call_utilities/rules/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_call_utilities_rules_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected Call Utilities Rules configurations."""
        return [self.delete_call_utilities_rules_config_by_id(config_id) for config_id in config]

    def get_call_utilities_rules_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the selected Call Utilities rule configuration."""
        endpoint = f"/call_utilities/rules/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_call_utilities_rules_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected Call Utilities rule configuration."""
        endpoint = f"/call_utilities/rules/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_call_utilities_rules_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the selected Call Utilities rule configuration."""
        endpoint = f"/call_utilities/rules/config/{config_id}"

        return self._api_client.delete(endpoint)
