from typing import Any

from ._endpoint import Endpoint


class WFQ(Endpoint):
    def get_wfq_interfaces_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns WFQ interface configurations."""
        return self._client.request("GET", "/wfq/interfaces/config", params={"all_options": all_options})

    def create_wfq_interfaces_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates WFQ interface configuration."""
        return self._client.request("POST", "/wfq/interfaces/config", json={"data": config})

    def update_wfq_interfaces_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates WFQ interface configurations."""
        return self._client.request("PUT", "/wfq/interfaces/config", json={"data": config})

    def delete_wfq_interfaces_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes WFQ interface configurations."""
        return self._client.request("DELETE", "/wfq/interfaces/config", json={"data": config})

    def get_wfq_interfaces_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns WFQ interface configuration."""
        return self._client.request("GET", f"/wfq/interfaces/config/{config_id}", params={"all_options": all_options})

    def update_wfq_interfaces_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates WFQ interface configuration."""
        return self._client.request("PUT", f"/wfq/interfaces/config/{config_id}", json={"data": config})

    def delete_wfq_interfaces_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes WFQ interface configuration."""
        return self._client.request("DELETE", f"/wfq/interfaces/config/{config_id}")

    def get_wfq_rules_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns WFQ classification rules."""
        return self._client.request("GET", "/wfq/rules/config", params={"all_options": all_options})

    def create_wfq_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates WFQ classification rule."""
        return self._client.request("POST", "/wfq/rules/config", json={"data": config})

    def update_wfq_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates WFQ classification rules."""
        return self._client.request("PUT", "/wfq/rules/config", json={"data": config})

    def delete_wfq_rules_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes WFQ classification rules."""
        return self._client.request("DELETE", "/wfq/rules/config", json={"data": config})

    def get_wfq_rules_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns WFQ classification rule configuration."""
        return self._client.request("GET", f"/wfq/rules/config/{config_id}", params={"all_options": all_options})

    def update_wfq_rules_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates WFQ classification rule configuration."""
        return self._client.request("PUT", f"/wfq/rules/config/{config_id}", json={"data": config})

    def delete_wfq_rules_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes WFQ classification rule configuration."""
        return self._client.request("DELETE", f"/wfq/rules/config/{config_id}")

    def get_wfq_rules_options(self) -> dict[str, Any]:
        """Returns rules service options."""
        return self._client.request("GET", "/wfq/rules/options")
