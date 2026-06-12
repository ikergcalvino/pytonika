from typing import Any

from ._base import Endpoint


class AttackPrevention(Endpoint):
    def get_attack_prevention_port_scan_config(self) -> dict[str, Any]:
        """Returns Firewall Port Scan Settings."""
        endpoint = "/attack_prevention/port_scan/config"

        return self._api_client.get(endpoint)

    def update_attack_prevention_port_scan_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall Port Scan Settings."""
        endpoint = "/attack_prevention/port_scan/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_attack_prevention_port_scan_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Firewall Port Scan Settings."""
        endpoint = f"/attack_prevention/port_scan/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_attack_prevention_port_scan_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall Port Scan Settings."""
        endpoint = f"/attack_prevention/port_scan/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_attack_prevention_syn_flood_config(self) -> dict[str, Any]:
        """Returns Firewall SYN Flood Protection Settings."""
        endpoint = "/attack_prevention/syn_flood/config"

        return self._api_client.get(endpoint)

    def update_attack_prevention_syn_flood_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall SYN Flood Protection Settings."""
        endpoint = "/attack_prevention/syn_flood/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_attack_prevention_syn_flood_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Firewall SYN Flood Protection Settings."""
        endpoint = f"/attack_prevention/syn_flood/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_attack_prevention_syn_flood_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall SYN Flood Protection Settings."""
        endpoint = f"/attack_prevention/syn_flood/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_attack_prevention_icmp_config(self) -> dict[str, Any]:
        """Returns Firewall Remote ICMP Request Settings."""
        endpoint = "/attack_prevention/icmp/config"

        return self._api_client.get(endpoint)

    def update_attack_prevention_icmp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall Remote ICMP Request Settings."""
        endpoint = "/attack_prevention/icmp/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_attack_prevention_icmp_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Firewall Remote ICMP Request Settings."""
        endpoint = f"/attack_prevention/icmp/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_attack_prevention_icmp_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall Remote ICMP Request Settings."""
        endpoint = f"/attack_prevention/icmp/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_attack_prevention_https_config(self) -> dict[str, Any]:
        """Returns Firewall HTTPS Attack Prevention Settings."""
        endpoint = "/attack_prevention/https/config"

        return self._api_client.get(endpoint)

    def update_attack_prevention_https_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall HTTPS Attack Prevention Settings."""
        endpoint = "/attack_prevention/https/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_attack_prevention_https_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Firewall HTTPS Attack Prevention Settings."""
        endpoint = f"/attack_prevention/https/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_attack_prevention_https_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall HTTPS Attack Prevention Settings."""
        endpoint = f"/attack_prevention/https/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_attack_prevention_http_config(self) -> dict[str, Any]:
        """Returns Firewall HTTP Attack Prevention Settings."""
        endpoint = "/attack_prevention/http/config"

        return self._api_client.get(endpoint)

    def update_attack_prevention_http_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall HTTP Attack Prevention Settings."""
        endpoint = "/attack_prevention/http/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_attack_prevention_http_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Firewall HTTP Attack Prevention Settings."""
        endpoint = f"/attack_prevention/http/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_attack_prevention_http_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall HTTP Attack Prevention Settings."""
        endpoint = f"/attack_prevention/http/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_attack_prevention_ssh_config(self) -> dict[str, Any]:
        """Returns Firewall SSH Attack Prevention Settings."""
        endpoint = "/attack_prevention/ssh/config"

        return self._api_client.get(endpoint)

    def update_attack_prevention_ssh_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall SSH Attack Prevention Settings."""
        endpoint = "/attack_prevention/ssh/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_attack_prevention_ssh_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Firewall SSH Attack Prevention Settings."""
        endpoint = f"/attack_prevention/ssh/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_attack_prevention_ssh_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall SSH Attack Prevention Settings."""
        endpoint = f"/attack_prevention/ssh/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
