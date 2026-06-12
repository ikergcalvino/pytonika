from typing import Any

from ._base import Endpoint


class Firewall(Endpoint):
    def get_firewall_traffic_rules_config(self) -> dict[str, Any]:
        """Returns Firewall Traffic Rules."""
        endpoint = "/firewall/traffic_rules/config"

        return self._api_client.get(endpoint)

    def create_firewall_traffic_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Firewall Traffic Rule."""
        endpoint = "/firewall/traffic_rules/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_firewall_traffic_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall Traffic Rules."""
        endpoint = "/firewall/traffic_rules/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_firewall_traffic_rules_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes Firewall Traffic Rules."""
        return [self.delete_firewall_traffic_rules_config_by_id(rule_id) for rule_id in config]

    def get_firewall_traffic_rules_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Firewall Traffic Rule."""
        endpoint = f"/firewall/traffic_rules/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_firewall_traffic_rules_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall Traffic Rule."""
        endpoint = f"/firewall/traffic_rules/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_firewall_traffic_rules_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes Firewall Traffic Rule."""
        endpoint = f"/firewall/traffic_rules/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_firewall_custom_rules_config(self) -> dict[str, Any]:
        """Returns Firewall Custom Rules."""
        endpoint = "/firewall/custom_rules/config"

        return self._api_client.get(endpoint)

    def update_firewall_custom_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall Custom Rules."""
        endpoint = "/firewall/custom_rules/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_firewall_custom_rules_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Firewall Custom Rules."""
        endpoint = f"/firewall/custom_rules/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_firewall_custom_rules_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall Custom Rules."""
        endpoint = f"/firewall/custom_rules/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def firewall_custom_rules_actions_reset(self) -> dict[str, Any]:
        """Resets Firewall Custom Rules."""
        endpoint = "/firewall/custom_rules/actions/reset"

        return self._api_client.post(endpoint)

    def get_firewall_port_forwards_config(self) -> dict[str, Any]:
        """Returns Firewall Port Forwards."""
        endpoint = "/firewall/port_forwards/config"

        return self._api_client.get(endpoint)

    def create_firewall_port_forwards_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Firewall Port Forward."""
        endpoint = "/firewall/port_forwards/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_firewall_port_forwards_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall Port Forwards."""
        endpoint = "/firewall/port_forwards/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_firewall_port_forwards_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes Firewall Port Forwards."""
        return [self.delete_firewall_port_forwards_config_by_id(fwd_id) for fwd_id in config]

    def get_firewall_port_forwards_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Firewall Port Forward."""
        endpoint = f"/firewall/port_forwards/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_firewall_port_forwards_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall Port Forward."""
        endpoint = f"/firewall/port_forwards/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_firewall_port_forwards_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes Firewall Port Forward."""
        endpoint = f"/firewall/port_forwards/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_firewall_iptables_ipv4_status(self) -> dict[str, Any]:
        """Returns all parsed chains and their rules from `iptables` command."""
        endpoint = "/firewall/iptables/ipv4/status"

        return self._api_client.get(endpoint)

    def get_firewall_iptables_ipv6_status(self) -> dict[str, Any]:
        """Returns all parsed chains and their rules from `ip6tables` command."""
        endpoint = "/firewall/iptables/ipv6/status"

        return self._api_client.get(endpoint)

    def firewall_iptables_ipv4_actions_reset(self) -> dict[str, Any]:
        """Resets `iptables` chains counters."""
        endpoint = "/firewall/iptables/ipv4/actions/reset"

        return self._api_client.post(endpoint)

    def firewall_iptables_ipv6_actions_reset(self) -> dict[str, Any]:
        """Resets `ip6tables` chains counters."""
        endpoint = "/firewall/iptables/ipv6/actions/reset"

        return self._api_client.post(endpoint)

    def get_firewall_nat_rules_config(self) -> dict[str, Any]:
        """Returns Firewall NAT Rules."""
        endpoint = "/firewall/nat_rules/config"

        return self._api_client.get(endpoint)

    def create_firewall_nat_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Firewall NAT Rule."""
        endpoint = "/firewall/nat_rules/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_firewall_nat_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall NAT Rules."""
        endpoint = "/firewall/nat_rules/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_firewall_nat_rules_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes Firewall NAT Rules."""
        return [self.delete_firewall_nat_rules_config_by_id(rule_id) for rule_id in config]

    def get_firewall_nat_rules_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Firewall NAT Rule."""
        endpoint = f"/firewall/nat_rules/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_firewall_nat_rules_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall NAT Rule."""
        endpoint = f"/firewall/nat_rules/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_firewall_nat_rules_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes Firewall NAT Rule."""
        endpoint = f"/firewall/nat_rules/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_firewall_zones_config(self) -> dict[str, Any]:
        """Returns Firewall Zones."""
        endpoint = "/firewall/zones/config"

        return self._api_client.get(endpoint)

    def create_firewall_zones_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Firewall Zones."""
        endpoint = "/firewall/zones/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_firewall_zones_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall Zones."""
        endpoint = "/firewall/zones/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_firewall_zones_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes Firewall Zones."""
        return [self.delete_firewall_zones_config_by_id(zone_id) for zone_id in config]

    def get_firewall_zones_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Firewall Zone."""
        endpoint = f"/firewall/zones/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_firewall_zones_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall Zone."""
        endpoint = f"/firewall/zones/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_firewall_zones_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes Firewall Zone."""
        endpoint = f"/firewall/zones/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_firewall_global(self) -> dict[str, Any]:
        """Returns Firewall Global Settings."""
        endpoint = "/firewall/global"

        return self._api_client.get(endpoint)

    def update_firewall_global(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall Global Settings."""
        endpoint = "/firewall/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_firewall_connections_status(self) -> dict[str, Any]:
        """Returns current network connections."""
        endpoint = "/firewall/connections/status"

        return self._api_client.get(endpoint)
