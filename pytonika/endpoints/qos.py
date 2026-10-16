from typing import Any

from ._endpoint import Endpoint


class QoS(Endpoint):
    def get_qos_bandwidth_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns QoS bandwidth configuration."""
        return self._client.request("GET", "/qos/bandwidth/global", params={"all_options": all_options})

    def update_qos_bandwidth_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates QoS bandwidth configurations."""
        return self._client.request("PUT", "/qos/bandwidth/global", json={"data": config})

    def get_qos_dscp_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns QoS DSCP priority configurations."""
        return self._client.request("GET", "/qos/dscp/config", params={"all_options": all_options})

    def update_qos_dscp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates QoS DSCP priority configurations."""
        return self._client.request("PUT", "/qos/dscp/config", json={"data": config})

    def get_qos_dscp_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns QoS DSCP priority configuration."""
        return self._client.request("GET", f"/qos/dscp/config/{config_id}", params={"all_options": all_options})

    def update_qos_dscp_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates QoS DSCP priority configuration."""
        return self._client.request("PUT", f"/qos/dscp/config/{config_id}", json={"data": config})

    def get_qos_interfaces_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns QoS interface configurations."""
        return self._client.request("GET", "/qos/interfaces/config", params={"all_options": all_options})

    def create_qos_interfaces_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates QOS interface configuration."""
        return self._client.request("POST", "/qos/interfaces/config", json={"data": config})

    def update_qos_interfaces_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates QoS interface configurations."""
        return self._client.request("PUT", "/qos/interfaces/config", json={"data": config})

    def delete_qos_interfaces_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes QoS interface configurations."""
        return self._client.request("DELETE", "/qos/interfaces/config", json={"data": config})

    def get_qos_interfaces_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns QoS interface configuration."""
        return self._client.request("GET", f"/qos/interfaces/config/{config_id}", params={"all_options": all_options})

    def update_qos_interfaces_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates QoS interface configuration."""
        return self._client.request("PUT", f"/qos/interfaces/config/{config_id}", json={"data": config})

    def delete_qos_interfaces_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes QoS interface configuration."""
        return self._client.request("DELETE", f"/qos/interfaces/config/{config_id}")

    def get_qos_priority_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns QoS queue priority configurations."""
        return self._client.request("GET", "/qos/priority/config", params={"all_options": all_options})

    def update_qos_priority_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates QoS queue priority configurations."""
        return self._client.request("PUT", "/qos/priority/config", json={"data": config})

    def get_qos_priority_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns QoS queue priority configuration."""
        return self._client.request("GET", f"/qos/priority/config/{config_id}", params={"all_options": all_options})

    def update_qos_priority_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates QoS queue priority configuration."""
        return self._client.request("PUT", f"/qos/priority/config/{config_id}", json={"data": config})

    def get_qos_rules_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns QoS classification rules."""
        return self._client.request("GET", "/qos/rules/config", params={"all_options": all_options})

    def create_qos_rules_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates QoS classification rule."""
        return self._client.request("POST", "/qos/rules/config", json={"data": config})

    def update_qos_rules_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates QoS classification rules."""
        return self._client.request("PUT", "/qos/rules/config", json={"data": config})

    def delete_qos_rules_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes QoS classification rules."""
        return self._client.request("DELETE", "/qos/rules/config", json={"data": config})

    def get_qos_rules_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns QoS classification rule configuration."""
        return self._client.request("GET", f"/qos/rules/config/{config_id}", params={"all_options": all_options})

    def update_qos_rules_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates QoS classification rule configuration."""
        return self._client.request("PUT", f"/qos/rules/config/{config_id}", json={"data": config})

    def delete_qos_rules_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes QoS classification rule configuration."""
        return self._client.request("DELETE", f"/qos/rules/config/{config_id}")

    def get_qos_rules_options(self) -> dict[str, Any]:
        """Returns rules service options."""
        return self._client.request("GET", "/qos/rules/options")

    def get_qos_scheduling_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns QoS scheduling weights configurations."""
        return self._client.request("GET", "/qos/scheduling/config", params={"all_options": all_options})

    def update_qos_scheduling_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates QoS scheduling weights configurations."""
        return self._client.request("PUT", "/qos/scheduling/config", json={"data": config})

    def get_qos_scheduling_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns QoS scheduling weights configuration."""
        return self._client.request("GET", f"/qos/scheduling/config/{config_id}", params={"all_options": all_options})

    def update_qos_scheduling_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates QoS scheduling weights configuration."""
        return self._client.request("PUT", f"/qos/scheduling/config/{config_id}", json={"data": config})

    def get_qos_scheduling_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns QoS scheduling general configuration."""
        return self._client.request("GET", "/qos/scheduling/global", params={"all_options": all_options})

    def update_qos_scheduling_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates QoS scheduling general configuration."""
        return self._client.request("PUT", "/qos/scheduling/global", json={"data": config})
