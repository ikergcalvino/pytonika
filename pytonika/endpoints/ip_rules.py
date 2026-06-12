from typing import Any

from ._base import Endpoint


class IPRules(Endpoint):
    def get_ip_rules_ipv4_config(self) -> dict[str, Any]:
        """Returns routing rule configurations."""
        endpoint = "/ip_rules/ipv4/config"

        return self._api_client.get(endpoint)

    def create_ip_rules_ipv4_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates routing rule configuration."""
        endpoint = "/ip_rules/ipv4/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_ip_rules_ipv4_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates routing rule configurations."""
        endpoint = "/ip_rules/ipv4/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ip_rules_ipv4_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified routing rule configurations."""
        return [self.delete_ip_rules_ipv4_config_by_id(rule_id) for rule_id in config]

    def get_ip_rules_ipv4_config_by_id(self, rule_id: str) -> dict[str, Any]:
        """Returns routing rule configuration."""
        endpoint = f"/ip_rules/ipv4/config/{rule_id}"

        return self._api_client.get(endpoint)

    def update_ip_rules_ipv4_config_by_id(self, rule_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates routing rule configuration."""
        endpoint = f"/ip_rules/ipv4/config/{rule_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ip_rules_ipv4_config_by_id(self, rule_id: str) -> dict[str, Any]:
        """Deletes specified routing rule configuration."""
        endpoint = f"/ip_rules/ipv4/config/{rule_id}"

        return self._api_client.delete(endpoint)
