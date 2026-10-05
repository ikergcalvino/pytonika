from typing import Any

from ._endpoint import Endpoint


class NAT64(Endpoint):
    def get_jool_global(self) -> dict[str, Any]:
        """Returns NAT64 global configuration."""
        endpoint = "/jool/global"

        return self._client.request("GET", endpoint)

    def update_jool_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates NAT64 global configuration."""
        endpoint = "/jool/global"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def get_jool_rules_config(self) -> dict[str, Any]:
        """Returns NAT64 rule configurations."""
        endpoint = "/jool/rules/config"

        return self._client.request("GET", endpoint)

    def create_jool_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates NAT64 rule configuration."""
        endpoint = "/jool/rules/config"

        data = {"data": config}

        return self._client.request("POST", endpoint, json=data)

    def update_jool_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates NAT64 rule configurations."""
        endpoint = "/jool/rules/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_jool_rules_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes NAT64 rule configurations."""
        return [self.delete_jool_rules_config_by_id(rule_id) for rule_id in config]

    def get_jool_rules_config_by_id(self, rule_id: str) -> dict[str, Any]:
        """Returns NAT64 rule configuration."""
        endpoint = f"/jool/rules/config/{rule_id}"

        return self._client.request("GET", endpoint)

    def update_jool_rules_config_by_id(self, rule_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates NAT64 rule configuration."""
        endpoint = f"/jool/rules/config/{rule_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_jool_rules_config_by_id(self, rule_id: str) -> dict[str, Any]:
        """Deletes NAT64 rule configuration."""
        endpoint = f"/jool/rules/config/{rule_id}"

        return self._client.request("DELETE", endpoint)
