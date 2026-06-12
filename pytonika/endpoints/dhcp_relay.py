from typing import Any

from ._base import Endpoint


class DHCPRelay(Endpoint):
    def get_dhcp_relays_ipv4_config(self) -> dict[str, Any]:
        """Returns DHCP Relay configurations."""
        endpoint = "/dhcp/relays/ipv4/config"

        return self._api_client.get(endpoint)

    def create_dhcp_relays_ipv4_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates DHCP Relay configuration."""
        endpoint = "/dhcp/relays/ipv4/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_dhcp_relays_ipv4_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates DHCP Relay configurations."""
        endpoint = "/dhcp/relays/ipv4/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dhcp_relays_ipv4_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes DHCP Relay configurations."""
        return [self.delete_dhcp_relays_ipv4_config_by_id(ipv4_id) for ipv4_id in config]

    def get_dhcp_relays_ipv4_config_by_id(self, ipv4_id: str) -> dict[str, Any]:
        """Returns DHCP Relay configuration."""
        endpoint = f"/dhcp/relays/ipv4/config/{ipv4_id}"

        return self._api_client.get(endpoint)

    def update_dhcp_relays_ipv4_config_by_id(self, ipv4_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates DHCP Relay configuration."""
        endpoint = f"/dhcp/relays/ipv4/config/{ipv4_id}"

        return self._api_client.put(endpoint, data=config)

    def delete_dhcp_relays_ipv4_config_by_id(self, ipv4_id: str) -> dict[str, Any]:
        """Deletes DHCP Relay configuration."""
        endpoint = f"/dhcp/relays/ipv4/config/{ipv4_id}"

        return self._api_client.delete(endpoint)
