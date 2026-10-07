from typing import Any

from ._endpoint import Endpoint


class Firewall(Endpoint):
    def get_firewall_connections_status(self) -> dict[str, Any]:
        """Returns current network connections."""
        return self._client.request("GET", "/firewall/connections/status")

    def firewall_custom_rules_actions_reset(self) -> dict[str, Any]:
        """Resets Firewall Custom Rules."""
        return self._client.request("POST", "/firewall/custom_rules/actions/reset")

    def get_firewall_custom_rules_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Firewall Custom Rules."""
        return self._client.request("GET", "/firewall/custom_rules/config", params={"all_options": all_options})

    def update_firewall_custom_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall Custom Rules."""
        return self._client.request("PUT", "/firewall/custom_rules/config", json={"data": config})

    def get_firewall_custom_rules_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns Firewall Custom Rules."""
        return self._client.request(
            "GET", f"/firewall/custom_rules/config/{config_id}", params={"all_options": all_options}
        )

    def update_firewall_custom_rules_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall Custom Rules."""
        return self._client.request("PUT", f"/firewall/custom_rules/config/{config_id}", json={"data": config})

    def get_firewall_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Firewall Global Settings."""
        return self._client.request("GET", "/firewall/global", params={"all_options": all_options})

    def update_firewall_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall Global Settings."""
        return self._client.request("PUT", "/firewall/global", json={"data": config})

    def firewall_iptables_ipv4_actions_reset(self) -> dict[str, Any]:
        """Resets `iptables` chains counters."""
        return self._client.request("POST", "/firewall/iptables/ipv4/actions/reset")

    def get_firewall_iptables_ipv4_status(self) -> dict[str, Any]:
        """Returns all parsed chains and their rules from `iptables` command."""
        return self._client.request("GET", "/firewall/iptables/ipv4/status")

    def firewall_iptables_ipv6_actions_reset(self) -> dict[str, Any]:
        """Resets `ip6tables` chains counters."""
        return self._client.request("POST", "/firewall/iptables/ipv6/actions/reset")

    def get_firewall_iptables_ipv6_status(self) -> dict[str, Any]:
        """Returns all parsed chains and their rules from `ip6tables` command."""
        return self._client.request("GET", "/firewall/iptables/ipv6/status")

    def get_firewall_limits_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Connection Limits configurations."""
        return self._client.request("GET", "/firewall/limits/config", params={"all_options": all_options})

    def create_firewall_limits_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Connection Limits configuration."""
        return self._client.request("POST", "/firewall/limits/config", json={"data": config})

    def update_firewall_limits_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Connection Limits configurations."""
        return self._client.request("PUT", "/firewall/limits/config", json={"data": config})

    def delete_firewall_limits_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes Connection Limits configurations."""
        return self._client.request("DELETE", "/firewall/limits/config", json={"data": config})

    def get_firewall_limits_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Connection Limits configuration."""
        return self._client.request("GET", f"/firewall/limits/config/{config_id}", params={"all_options": all_options})

    def update_firewall_limits_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Connection Limits configuration."""
        return self._client.request("PUT", f"/firewall/limits/config/{config_id}", json={"data": config})

    def delete_firewall_limits_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes Connection Limits configuration."""
        return self._client.request("DELETE", f"/firewall/limits/config/{config_id}")

    def get_firewall_nat_rules_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Firewall NAT Rules."""
        return self._client.request("GET", "/firewall/nat_rules/config", params={"all_options": all_options})

    def create_firewall_nat_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Firewall NAT Rule."""
        return self._client.request("POST", "/firewall/nat_rules/config", json={"data": config})

    def update_firewall_nat_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall NAT Rules."""
        return self._client.request("PUT", "/firewall/nat_rules/config", json={"data": config})

    def delete_firewall_nat_rules_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes Firewall NAT Rules."""
        return self._client.request("DELETE", "/firewall/nat_rules/config", json={"data": config})

    def get_firewall_nat_rules_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Firewall NAT Rule."""
        return self._client.request(
            "GET", f"/firewall/nat_rules/config/{config_id}", params={"all_options": all_options}
        )

    def update_firewall_nat_rules_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall NAT Rule."""
        return self._client.request("PUT", f"/firewall/nat_rules/config/{config_id}", json={"data": config})

    def delete_firewall_nat_rules_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes Firewall NAT Rule."""
        return self._client.request("DELETE", f"/firewall/nat_rules/config/{config_id}")

    def get_firewall_port_forwards_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Firewall Port Forwards."""
        return self._client.request("GET", "/firewall/port_forwards/config", params={"all_options": all_options})

    def create_firewall_port_forwards_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Firewall Port Forward."""
        return self._client.request("POST", "/firewall/port_forwards/config", json={"data": config})

    def update_firewall_port_forwards_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall Port Forwards."""
        return self._client.request("PUT", "/firewall/port_forwards/config", json={"data": config})

    def delete_firewall_port_forwards_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes Firewall Port Forwards."""
        return self._client.request("DELETE", "/firewall/port_forwards/config", json={"data": config})

    def get_firewall_port_forwards_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns Firewall Port Forward."""
        return self._client.request(
            "GET", f"/firewall/port_forwards/config/{config_id}", params={"all_options": all_options}
        )

    def update_firewall_port_forwards_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall Port Forward."""
        return self._client.request("PUT", f"/firewall/port_forwards/config/{config_id}", json={"data": config})

    def delete_firewall_port_forwards_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes Firewall Port Forward."""
        return self._client.request("DELETE", f"/firewall/port_forwards/config/{config_id}")

    def get_firewall_traffic_rules_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Firewall Traffic Rules."""
        return self._client.request("GET", "/firewall/traffic_rules/config", params={"all_options": all_options})

    def create_firewall_traffic_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Firewall Traffic Rule."""
        return self._client.request("POST", "/firewall/traffic_rules/config", json={"data": config})

    def update_firewall_traffic_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall Traffic Rules."""
        return self._client.request("PUT", "/firewall/traffic_rules/config", json={"data": config})

    def delete_firewall_traffic_rules_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes Firewall Traffic Rules."""
        return self._client.request("DELETE", "/firewall/traffic_rules/config", json={"data": config})

    def get_firewall_traffic_rules_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns Firewall Traffic Rule."""
        return self._client.request(
            "GET", f"/firewall/traffic_rules/config/{config_id}", params={"all_options": all_options}
        )

    def update_firewall_traffic_rules_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall Traffic Rule."""
        return self._client.request("PUT", f"/firewall/traffic_rules/config/{config_id}", json={"data": config})

    def delete_firewall_traffic_rules_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes Firewall Traffic Rule."""
        return self._client.request("DELETE", f"/firewall/traffic_rules/config/{config_id}")

    def get_firewall_zones_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Firewall Zones."""
        return self._client.request("GET", "/firewall/zones/config", params={"all_options": all_options})

    def create_firewall_zones_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Firewall Zones."""
        return self._client.request("POST", "/firewall/zones/config", json={"data": config})

    def update_firewall_zones_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall Zones."""
        return self._client.request("PUT", "/firewall/zones/config", json={"data": config})

    def delete_firewall_zones_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes Firewall Zones."""
        return self._client.request("DELETE", "/firewall/zones/config", json={"data": config})

    def get_firewall_zones_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Firewall Zone."""
        return self._client.request("GET", f"/firewall/zones/config/{config_id}", params={"all_options": all_options})

    def update_firewall_zones_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall Zone."""
        return self._client.request("PUT", f"/firewall/zones/config/{config_id}", json={"data": config})

    def delete_firewall_zones_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes Firewall Zone."""
        return self._client.request("DELETE", f"/firewall/zones/config/{config_id}")
