from typing import Any

from ._endpoint import Endpoint


class DHCPRelay(Endpoint):
    def get_dhcp_relays_ipv4_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns DHCP Relay configurations."""
        return self._client.request("GET", "/dhcp/relays/ipv4/config", params={"all_options": all_options})

    def create_dhcp_relays_ipv4_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates DHCP Relay configuration."""
        return self._client.request("POST", "/dhcp/relays/ipv4/config", json={"data": config})

    def update_dhcp_relays_ipv4_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates DHCP Relay configurations."""
        return self._client.request("PUT", "/dhcp/relays/ipv4/config", json={"data": config})

    def delete_dhcp_relays_ipv4_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes DHCP Relay configurations."""
        return self._client.request("DELETE", "/dhcp/relays/ipv4/config", json={"data": config})

    def get_dhcp_relays_ipv4_config_by_id(self, ipv4_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns DHCP Relay configuration."""
        return self._client.request("GET", f"/dhcp/relays/ipv4/config/{ipv4_id}", params={"all_options": all_options})

    def update_dhcp_relays_ipv4_config_by_id(self, ipv4_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates DHCP Relay configuration."""
        return self._client.request("PUT", f"/dhcp/relays/ipv4/config/{ipv4_id}", json=config)

    def delete_dhcp_relays_ipv4_config_by_id(self, ipv4_id: str) -> dict[str, Any]:
        """Deletes DHCP Relay configuration."""
        return self._client.request("DELETE", f"/dhcp/relays/ipv4/config/{ipv4_id}")
