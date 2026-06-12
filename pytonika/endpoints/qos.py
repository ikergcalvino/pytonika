from typing import Any

from ._base import Endpoint


class QoS(Endpoint):
    def get_qos_interfaces_config(self) -> dict[str, Any]:
        """Returns QoS interface configurations."""
        endpoint = "/qos/interfaces/config"

        return self._api_client.get(endpoint)

    def create_qos_interfaces_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates QOS interface configuration."""
        endpoint = "/qos/interfaces/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_qos_interfaces_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates QoS interface configurations."""
        endpoint = "/qos/interfaces/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_qos_interfaces_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes QoS interface configurations."""
        return [self.delete_qos_interfaces_config_by_id(interface_id) for interface_id in config]

    def get_qos_interfaces_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns QoS interface configuration."""
        endpoint = f"/qos/interfaces/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_qos_interfaces_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates QoS interface configuration."""
        endpoint = f"/qos/interfaces/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_qos_interfaces_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes QoS interface configuration."""
        endpoint = f"/qos/interfaces/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_qos_rules_config(self) -> dict[str, Any]:
        """Returns QoS classification rules."""
        endpoint = "/qos/rules/config"

        return self._api_client.get(endpoint)

    def create_qos_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates QoS classification rule."""
        endpoint = "/qos/rules/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_qos_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates QoS classification rules."""
        endpoint = "/qos/rules/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_qos_rules_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes QoS classification rules."""
        return [self.delete_qos_rules_config_by_id(rule_id) for rule_id in config]

    def get_qos_rules_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns QoS classification rule configuration."""
        endpoint = f"/qos/rules/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_qos_rules_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates QoS classification rule configuration."""
        endpoint = f"/qos/rules/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_qos_rules_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes QoS classification rule configuration."""
        endpoint = f"/qos/rules/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_qos_rules_options(self) -> dict[str, Any]:
        """Returns rules service options."""
        endpoint = "/qos/rules/options"

        return self._api_client.get(endpoint)
