from typing import Any

from ._endpoint import Endpoint


class AttackPrevention(Endpoint):
    def get_attack_prevention_http_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Firewall HTTP Attack Prevention Settings."""
        return self._client.request("GET", "/attack_prevention/http/config", params={"all_options": all_options})

    def update_attack_prevention_http_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall HTTP Attack Prevention Settings."""
        return self._client.request("PUT", "/attack_prevention/http/config", json={"data": config})

    def get_attack_prevention_http_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns Firewall HTTP Attack Prevention Settings."""
        return self._client.request(
            "GET", f"/attack_prevention/http/config/{config_id}", params={"all_options": all_options}
        )

    def update_attack_prevention_http_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall HTTP Attack Prevention Settings."""
        return self._client.request("PUT", f"/attack_prevention/http/config/{config_id}", json={"data": config})

    def get_attack_prevention_https_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Firewall HTTPS Attack Prevention Settings."""
        return self._client.request("GET", "/attack_prevention/https/config", params={"all_options": all_options})

    def update_attack_prevention_https_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall HTTPS Attack Prevention Settings."""
        return self._client.request("PUT", "/attack_prevention/https/config", json={"data": config})

    def get_attack_prevention_https_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns Firewall HTTPS Attack Prevention Settings."""
        return self._client.request(
            "GET", f"/attack_prevention/https/config/{config_id}", params={"all_options": all_options}
        )

    def update_attack_prevention_https_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall HTTPS Attack Prevention Settings."""
        return self._client.request("PUT", f"/attack_prevention/https/config/{config_id}", json={"data": config})

    def get_attack_prevention_icmp_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Firewall Remote ICMP Request Settings."""
        return self._client.request("GET", "/attack_prevention/icmp/config", params={"all_options": all_options})

    def update_attack_prevention_icmp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall Remote ICMP Request Settings."""
        return self._client.request("PUT", "/attack_prevention/icmp/config", json={"data": config})

    def get_attack_prevention_icmp_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns Firewall Remote ICMP Request Settings."""
        return self._client.request(
            "GET", f"/attack_prevention/icmp/config/{config_id}", params={"all_options": all_options}
        )

    def update_attack_prevention_icmp_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall Remote ICMP Request Settings."""
        return self._client.request("PUT", f"/attack_prevention/icmp/config/{config_id}", json={"data": config})

    def get_attack_prevention_port_scan_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Firewall Port Scan Settings."""
        return self._client.request("GET", "/attack_prevention/port_scan/config", params={"all_options": all_options})

    def update_attack_prevention_port_scan_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall Port Scan Settings."""
        return self._client.request("PUT", "/attack_prevention/port_scan/config", json={"data": config})

    def get_attack_prevention_port_scan_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns Firewall Port Scan Settings."""
        return self._client.request(
            "GET", f"/attack_prevention/port_scan/config/{config_id}", params={"all_options": all_options}
        )

    def update_attack_prevention_port_scan_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall Port Scan Settings."""
        return self._client.request("PUT", f"/attack_prevention/port_scan/config/{config_id}", json={"data": config})

    def get_attack_prevention_ssh_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Firewall SSH Attack Prevention Settings."""
        return self._client.request("GET", "/attack_prevention/ssh/config", params={"all_options": all_options})

    def update_attack_prevention_ssh_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall SSH Attack Prevention Settings."""
        return self._client.request("PUT", "/attack_prevention/ssh/config", json={"data": config})

    def get_attack_prevention_ssh_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns Firewall SSH Attack Prevention Settings."""
        return self._client.request(
            "GET", f"/attack_prevention/ssh/config/{config_id}", params={"all_options": all_options}
        )

    def update_attack_prevention_ssh_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall SSH Attack Prevention Settings."""
        return self._client.request("PUT", f"/attack_prevention/ssh/config/{config_id}", json={"data": config})

    def get_attack_prevention_syn_flood_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Firewall SYN Flood Protection Settings."""
        return self._client.request("GET", "/attack_prevention/syn_flood/config", params={"all_options": all_options})

    def update_attack_prevention_syn_flood_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Firewall SYN Flood Protection Settings."""
        return self._client.request("PUT", "/attack_prevention/syn_flood/config", json={"data": config})

    def get_attack_prevention_syn_flood_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns Firewall SYN Flood Protection Settings."""
        return self._client.request(
            "GET", f"/attack_prevention/syn_flood/config/{config_id}", params={"all_options": all_options}
        )

    def update_attack_prevention_syn_flood_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Firewall SYN Flood Protection Settings."""
        return self._client.request("PUT", f"/attack_prevention/syn_flood/config/{config_id}", json={"data": config})
