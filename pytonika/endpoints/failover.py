from typing import Any

from ._endpoint import Endpoint


class Failover(Endpoint):
    def get_failover_interfaces_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns failover interfaces."""
        return self._client.request("GET", "/failover/interfaces/config", params={"all_options": all_options})

    def create_failover_interfaces_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates failover interface."""
        return self._client.request("POST", "/failover/interfaces/config", json={"data": config})

    def update_failover_interfaces_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates failover interfaces."""
        return self._client.request("PUT", "/failover/interfaces/config", json={"data": config})

    def delete_failover_interfaces_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes failover interfaces."""
        return self._client.request("DELETE", "/failover/interfaces/config", json={"data": config})

    def get_failover_interfaces_config_by_id(
        self, interface_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns failover interface."""
        return self._client.request(
            "GET", f"/failover/interfaces/config/{interface_id}", params={"all_options": all_options}
        )

    def update_failover_interfaces_config_by_id(self, interface_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates failover interface."""
        return self._client.request("PUT", f"/failover/interfaces/config/{interface_id}", json={"data": config})

    def delete_failover_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Deletes failover interface."""
        return self._client.request("DELETE", f"/failover/interfaces/config/{interface_id}")

    def get_failover_members_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns failover member configurations."""
        return self._client.request("GET", "/failover/members/config", params={"all_options": all_options})

    def create_failover_members_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates failover member."""
        return self._client.request("POST", "/failover/members/config", json={"data": config})

    def update_failover_members_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates failover member configurations."""
        return self._client.request("PUT", "/failover/members/config", json={"data": config})

    def delete_failover_members_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes failover members."""
        return self._client.request("DELETE", "/failover/members/config", json={"data": config})

    def get_failover_members_config_by_id(self, member_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns failover member configuration."""
        return self._client.request("GET", f"/failover/members/config/{member_id}", params={"all_options": all_options})

    def update_failover_members_config_by_id(self, member_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates failover member."""
        return self._client.request("PUT", f"/failover/members/config/{member_id}", json={"data": config})

    def delete_failover_members_config_by_id(self, member_id: str) -> dict[str, Any]:
        """Deletes failover member."""
        return self._client.request("DELETE", f"/failover/members/config/{member_id}")

    def get_failover_mode_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns failover configurations."""
        return self._client.request("GET", "/failover/mode/config", params={"all_options": all_options})

    def update_failover_mode_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates failover configurations."""
        return self._client.request("PUT", "/failover/mode/config", json={"data": config})

    def get_failover_mode_config_by_id(self, mode_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns failover configuration."""
        return self._client.request("GET", f"/failover/mode/config/{mode_id}", params={"all_options": all_options})

    def update_failover_mode_config_by_id(self, mode_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates failover configuration."""
        return self._client.request("PUT", f"/failover/mode/config/{mode_id}", json={"data": config})

    def get_failover_policies_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns failover policies."""
        return self._client.request("GET", "/failover/policies/config", params={"all_options": all_options})

    def create_failover_policies_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates failover policies."""
        return self._client.request("POST", "/failover/policies/config", json={"data": config})

    def update_failover_policies_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates failover policies."""
        return self._client.request("PUT", "/failover/policies/config", json={"data": config})

    def delete_failover_policies_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes failover policies."""
        return self._client.request("DELETE", "/failover/policies/config", json={"data": config})

    def get_failover_policies_config_by_id(self, policy_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns failover policy."""
        return self._client.request(
            "GET", f"/failover/policies/config/{policy_id}", params={"all_options": all_options}
        )

    def update_failover_policies_config_by_id(self, policy_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates failover policy."""
        return self._client.request("PUT", f"/failover/policies/config/{policy_id}", json={"data": config})

    def delete_failover_policies_config_by_id(self, policy_id: str) -> dict[str, Any]:
        """Deletes failover policy."""
        return self._client.request("DELETE", f"/failover/policies/config/{policy_id}")

    def get_failover_rules_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns failover rules."""
        return self._client.request("GET", "/failover/rules/config", params={"all_options": all_options})

    def create_failover_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates failover rules."""
        return self._client.request("POST", "/failover/rules/config", json={"data": config})

    def update_failover_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates failover rules."""
        return self._client.request("PUT", "/failover/rules/config", json={"data": config})

    def delete_failover_rules_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes failover rules."""
        return self._client.request("DELETE", "/failover/rules/config", json={"data": config})

    def get_failover_rules_config_by_id(self, rule_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns failover rule."""
        return self._client.request("GET", f"/failover/rules/config/{rule_id}", params={"all_options": all_options})

    def update_failover_rules_config_by_id(self, rule_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates failover rule."""
        return self._client.request("PUT", f"/failover/rules/config/{rule_id}", json={"data": config})

    def delete_failover_rules_config_by_id(self, rule_id: str) -> dict[str, Any]:
        """Deletes failover rule."""
        return self._client.request("DELETE", f"/failover/rules/config/{rule_id}")

    def get_failover_status(self) -> dict[str, Any]:
        """Returns failover status."""
        return self._client.request("GET", "/failover/status")
