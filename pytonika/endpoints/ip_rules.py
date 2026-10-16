from typing import Any

from ._endpoint import Endpoint


class IPRules(Endpoint):
    def get_ip_rules_ipv4_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns routing rule configurations."""
        return self._client.request("GET", "/ip_rules/ipv4/config", params={"all_options": all_options})

    def create_ip_rules_ipv4_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates routing rule configuration."""
        return self._client.request("POST", "/ip_rules/ipv4/config", json={"data": config})

    def update_ip_rules_ipv4_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates routing rule configurations."""
        return self._client.request("PUT", "/ip_rules/ipv4/config", json={"data": config})

    def delete_ip_rules_ipv4_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified routing rule configurations."""
        return self._client.request("DELETE", "/ip_rules/ipv4/config", json={"data": config})

    def get_ip_rules_ipv4_config_by_id(self, rule_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns routing rule configuration."""
        return self._client.request("GET", f"/ip_rules/ipv4/config/{rule_id}", params={"all_options": all_options})

    def update_ip_rules_ipv4_config_by_id(self, rule_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates routing rule configuration."""
        return self._client.request("PUT", f"/ip_rules/ipv4/config/{rule_id}", json={"data": config})

    def delete_ip_rules_ipv4_config_by_id(self, rule_id: str) -> dict[str, Any]:
        """Deletes specified routing rule configuration."""
        return self._client.request("DELETE", f"/ip_rules/ipv4/config/{rule_id}")
