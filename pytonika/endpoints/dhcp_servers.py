from typing import Any

from ._base import Endpoint


class DHCPServers(Endpoint):
    def get_dhcp_static_leases_ipv4_config(self) -> dict[str, Any]:
        """Returns static IPv4 leases."""
        endpoint = "/dhcp/static_leases/ipv4/config"

        return self._api_client.get(endpoint)

    def create_dhcp_static_leases_ipv4_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates static IPv4 lease."""
        endpoint = "/dhcp/static_leases/ipv4/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_dhcp_static_leases_ipv4_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates static IPv4 leases."""
        endpoint = "/dhcp/static_leases/ipv4/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dhcp_static_leases_ipv4_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes static IPv4 leases."""
        return [self.delete_dhcp_static_leases_ipv4_config_by_id(lease_id) for lease_id in config]

    def get_dhcp_static_leases_ipv4_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns static IPv4 lease."""
        endpoint = f"/dhcp/static_leases/ipv4/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_dhcp_static_leases_ipv4_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates static IPv4 lease."""
        endpoint = f"/dhcp/static_leases/ipv4/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dhcp_static_leases_ipv4_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes static IPv4 lease."""
        endpoint = f"/dhcp/static_leases/ipv4/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_dhcp_static_leases_ipv6_config(self) -> dict[str, Any]:
        """Returns static IPv6 leases."""
        endpoint = "/dhcp/static_leases/ipv6/config"

        return self._api_client.get(endpoint)

    def create_dhcp_static_leases_ipv6_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates static IPv6 lease."""
        endpoint = "/dhcp/static_leases/ipv6/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_dhcp_static_leases_ipv6_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates static IPv6 leases."""
        endpoint = "/dhcp/static_leases/ipv6/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dhcp_static_leases_ipv6_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes static IPv6 leases."""
        return [self.delete_dhcp_static_leases_ipv6_config_by_id(lease_id) for lease_id in config]

    def get_dhcp_static_leases_ipv6_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns static lease."""
        endpoint = f"/dhcp/static_leases/ipv6/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_dhcp_static_leases_ipv6_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates static lease."""
        endpoint = f"/dhcp/static_leases/ipv6/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dhcp_static_leases_ipv6_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes static lease."""
        endpoint = f"/dhcp/static_leases/ipv6/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_dhcp_servers_ipv4_config(self) -> dict[str, Any]:
        """Returns DHCP IPv4 servers."""
        endpoint = "/dhcp/servers/ipv4/config"

        return self._api_client.get(endpoint)

    def create_dhcp_servers_ipv4_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates DHCP IPv4 server."""
        endpoint = "/dhcp/servers/ipv4/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_dhcp_servers_ipv4_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates DHCP IPv4 servers."""
        endpoint = "/dhcp/servers/ipv4/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dhcp_servers_ipv4_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes DHCP IPv4 servers."""
        return [self.delete_dhcp_servers_ipv4_config_by_id(server_id) for server_id in config]

    def get_dhcp_servers_ipv4_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns DHCP IPv4 server."""
        endpoint = f"/dhcp/servers/ipv4/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_dhcp_servers_ipv4_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates DHCP IPv4 server."""
        endpoint = f"/dhcp/servers/ipv4/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dhcp_servers_ipv4_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes DHCP IPv4 server."""
        endpoint = f"/dhcp/servers/ipv4/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_dhcp_servers_ipv4_status(self) -> dict[str, Any]:
        """Returns status of DHCPv4 servers."""
        endpoint = "/dhcp/servers/ipv4/status"

        return self._api_client.get(endpoint)

    def dhcp_servers_ipv4_actions_restart(self) -> dict[str, Any]:
        """Restarts all DHCPv4 servers."""
        endpoint = "/dhcp/servers/ipv4/actions/restart"

        return self._api_client.post(endpoint)

    def get_dhcp_servers_ipv6_config(self) -> dict[str, Any]:
        """Returns DHCP IPv6 servers."""
        endpoint = "/dhcp/servers/ipv6/config"

        return self._api_client.get(endpoint)

    def create_dhcp_servers_ipv6_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates DHCP IPv6 server."""
        endpoint = "/dhcp/servers/ipv6/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_dhcp_servers_ipv6_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates DHCP IPv6 servers."""
        endpoint = "/dhcp/servers/ipv6/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dhcp_servers_ipv6_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes DHCP IPv6 servers."""
        return [self.delete_dhcp_servers_ipv6_config_by_id(server_id) for server_id in config]

    def get_dhcp_servers_ipv6_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns DHCP IPv6 server."""
        endpoint = f"/dhcp/servers/ipv6/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_dhcp_servers_ipv6_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates DHCP IPv6 server."""
        endpoint = f"/dhcp/servers/ipv6/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dhcp_servers_ipv6_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes DHCP IPv6 server."""
        endpoint = f"/dhcp/servers/ipv6/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_dhcp_servers_ipv6_status(self) -> dict[str, Any]:
        """Returns status of DHCPv6 servers."""
        endpoint = "/dhcp/servers/ipv6/status"

        return self._api_client.get(endpoint)

    def get_dhcp_leases_ipv4_status(self) -> dict[str, Any]:
        """Returns active DHCPv4 servers leases."""
        endpoint = "/dhcp/leases/ipv4/status"

        return self._api_client.get(endpoint)

    def get_dhcp_leases_ipv6_status(self) -> dict[str, Any]:
        """Returns active DHCPv6 servers leases."""
        endpoint = "/dhcp/leases/ipv6/status"

        return self._api_client.get(endpoint)
