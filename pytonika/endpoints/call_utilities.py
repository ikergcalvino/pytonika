from typing import Any

from ._endpoint import Endpoint


class CallUtilities(Endpoint):
    def get_call_utilities_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the Call Utilities Global Configuration."""
        return self._client.request("GET", "/call_utilities/global", params={"all_options": all_options})

    def update_call_utilities_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the Call Utilities Global configuration."""
        return self._client.request("PUT", "/call_utilities/global", json={"data": config})

    def get_call_utilities_rules_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Call Utilities Rules configurations."""
        return self._client.request("GET", "/call_utilities/rules/config", params={"all_options": all_options})

    def create_call_utilities_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Call Utilities rule configuration."""
        return self._client.request("POST", "/call_utilities/rules/config", json={"data": config})

    def update_call_utilities_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Call Utilities Rules configurations."""
        return self._client.request("PUT", "/call_utilities/rules/config", json={"data": config})

    def delete_call_utilities_rules_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the selected Call Utilities Rules configurations."""
        return self._client.request("DELETE", "/call_utilities/rules/config", json={"data": config})

    def get_call_utilities_rules_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the selected Call Utilities rule configuration."""
        return self._client.request(
            "GET", f"/call_utilities/rules/config/{config_id}", params={"all_options": all_options}
        )

    def update_call_utilities_rules_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected Call Utilities rule configuration."""
        return self._client.request("PUT", f"/call_utilities/rules/config/{config_id}", json={"data": config})

    def delete_call_utilities_rules_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the selected Call Utilities rule configuration."""
        return self._client.request("DELETE", f"/call_utilities/rules/config/{config_id}")

    def get_call_utilities_rules_options(self) -> dict[str, Any]:
        """Returns Call Utilities options."""
        return self._client.request("GET", "/call_utilities/rules/options")
