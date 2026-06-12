from typing import Any

from ._base import Endpoint


class Failover(Endpoint):
    def get_failover_mode_config(self) -> dict[str, Any]:
        """Returns failover configurations."""
        endpoint = "/failover/mode/config"

        return self._api_client.get(endpoint)

    def update_failover_mode_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates failover configurations."""
        endpoint = "/failover/mode/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_failover_mode_config_by_id(self, mode_id: str) -> dict[str, Any]:
        """Returns failover configuration."""
        endpoint = f"/failover/mode/config/{mode_id}"

        return self._api_client.get(endpoint)

    def update_failover_mode_config_by_id(self, mode_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates failover configuration."""
        endpoint = f"/failover/mode/config/{mode_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_failover_status(self) -> dict[str, Any]:
        """Returns failover status."""
        endpoint = "/failover/status"

        return self._api_client.get(endpoint)

    def get_failover_interfaces_config(self) -> dict[str, Any]:
        """Returns failover interfaces."""
        endpoint = "/failover/interfaces/config"

        return self._api_client.get(endpoint)

    def create_failover_interfaces_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates failover interface."""
        endpoint = "/failover/interfaces/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_failover_interfaces_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates failover interfaces."""
        endpoint = "/failover/interfaces/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_failover_interfaces_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes failover interfaces."""
        return [self.delete_failover_interfaces_config_by_id(interface_id) for interface_id in config]

    def get_failover_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Returns failover interface."""
        endpoint = f"/failover/interfaces/config/{interface_id}"

        return self._api_client.get(endpoint)

    def update_failover_interfaces_config_by_id(self, interface_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates failover interface."""
        endpoint = f"/failover/interfaces/config/{interface_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_failover_interfaces_config_by_id(self, interface_id: str) -> dict[str, Any]:
        """Deletes failover interface."""
        endpoint = f"/failover/interfaces/config/{interface_id}"

        return self._api_client.delete(endpoint)

    def get_failover_policies_config(self) -> dict[str, Any]:
        """Returns failover policies."""
        endpoint = "/failover/policies/config"

        return self._api_client.get(endpoint)

    def create_failover_policies_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates failover policies."""
        endpoint = "/failover/policies/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_failover_policies_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates failover policies."""
        endpoint = "/failover/policies/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_failover_policies_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes failover policies."""
        return [self.delete_failover_policies_config_by_id(policy_id) for policy_id in config]

    def get_failover_policies_config_by_id(self, policy_id: str) -> dict[str, Any]:
        """Returns failover policy."""
        endpoint = f"/failover/policies/config/{policy_id}"

        return self._api_client.get(endpoint)

    def update_failover_policies_config_by_id(self, policy_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates failover policy."""
        endpoint = f"/failover/policies/config/{policy_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_failover_policies_config_by_id(self, policy_id: str) -> dict[str, Any]:
        """Deletes failover policy."""
        endpoint = f"/failover/policies/config/{policy_id}"

        return self._api_client.delete(endpoint)

    def get_failover_rules_config(self) -> dict[str, Any]:
        """Returns failover rules."""
        endpoint = "/failover/rules/config"

        return self._api_client.get(endpoint)

    def create_failover_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates failover rules."""
        endpoint = "/failover/rules/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_failover_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates failover rules."""
        endpoint = "/failover/rules/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_failover_rules_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes failover rules."""
        return [self.delete_failover_rules_config_by_id(rule_id) for rule_id in config]

    def get_failover_rules_config_by_id(self, rule_id: str) -> dict[str, Any]:
        """Returns failover rule."""
        endpoint = f"/failover/rules/config/{rule_id}"

        return self._api_client.get(endpoint)

    def update_failover_rules_config_by_id(self, rule_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates failover rule."""
        endpoint = f"/failover/rules/config/{rule_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_failover_rules_config_by_id(self, rule_id: str) -> dict[str, Any]:
        """Deletes failover rule."""
        endpoint = f"/failover/rules/config/{rule_id}"

        return self._api_client.delete(endpoint)

    def get_failover_members_config(self) -> dict[str, Any]:
        """Returns failover member configurations."""
        endpoint = "/failover/members/config"

        return self._api_client.get(endpoint)

    def create_failover_members_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates failover member."""
        endpoint = "/failover/members/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_failover_members_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates failover member configurations."""
        endpoint = "/failover/members/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_failover_members_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes failover members."""
        return [self.delete_failover_members_config_by_id(member_id) for member_id in config]

    def get_failover_members_config_by_id(self, member_id: str) -> dict[str, Any]:
        """Returns failover member configuration."""
        endpoint = f"/failover/members/config/{member_id}"

        return self._api_client.get(endpoint)

    def update_failover_members_config_by_id(self, member_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates failover member."""
        endpoint = f"/failover/members/config/{member_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_failover_members_config_by_id(self, member_id: str) -> dict[str, Any]:
        """Deletes failover member."""
        endpoint = f"/failover/members/config/{member_id}"

        return self._api_client.delete(endpoint)
