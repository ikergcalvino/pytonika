from typing import Any

from ._endpoint import Endpoint


class NAT64(Endpoint):
    def get_jool_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns NAT64 global configuration."""
        return self._client.request("GET", "/jool/global", params={"all_options": all_options})

    def update_jool_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates NAT64 global configuration."""
        return self._client.request("PUT", "/jool/global", json={"data": config})

    def get_jool_rules_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns NAT64 rule configurations."""
        return self._client.request("GET", "/jool/rules/config", params={"all_options": all_options})

    def create_jool_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates NAT64 rule configuration."""
        return self._client.request("POST", "/jool/rules/config", json={"data": config})

    def update_jool_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates NAT64 rule configurations."""
        return self._client.request("PUT", "/jool/rules/config", json={"data": config})

    def delete_jool_rules_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes NAT64 rule configurations."""
        return self._client.request("DELETE", "/jool/rules/config", json={"data": config})

    def get_jool_rules_config_by_id(self, rule_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns NAT64 rule configuration."""
        return self._client.request("GET", f"/jool/rules/config/{rule_id}", params={"all_options": all_options})

    def update_jool_rules_config_by_id(self, rule_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates NAT64 rule configuration."""
        return self._client.request("PUT", f"/jool/rules/config/{rule_id}", json=config)

    def delete_jool_rules_config_by_id(self, rule_id: str) -> dict[str, Any]:
        """Deletes NAT64 rule configuration."""
        return self._client.request("DELETE", f"/jool/rules/config/{rule_id}")
