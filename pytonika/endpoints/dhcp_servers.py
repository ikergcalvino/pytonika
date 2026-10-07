from typing import Any

from ._endpoint import Endpoint


class DHCPServers(Endpoint):
    def get_dhcp_leases_ipv4_status(self) -> dict[str, Any]:
        """Returns active DHCPv4 servers leases."""
        return self._client.request("GET", "/dhcp/leases/ipv4/status")

    def get_dhcp_leases_ipv6_status(self) -> dict[str, Any]:
        """Returns active DHCPv6 servers leases."""
        return self._client.request("GET", "/dhcp/leases/ipv6/status")

    def dhcp_servers_ipv4_actions_restart(self) -> dict[str, Any]:
        """Restarts all DHCPv4 servers."""
        return self._client.request("POST", "/dhcp/servers/ipv4/actions/restart")

    def get_dhcp_servers_ipv4_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns DHCP IPv4 servers."""
        return self._client.request("GET", "/dhcp/servers/ipv4/config", params={"all_options": all_options})

    def create_dhcp_servers_ipv4_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates DHCP IPv4 server."""
        return self._client.request("POST", "/dhcp/servers/ipv4/config", json={"data": config})

    def update_dhcp_servers_ipv4_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates DHCP IPv4 servers."""
        return self._client.request("PUT", "/dhcp/servers/ipv4/config", json={"data": config})

    def delete_dhcp_servers_ipv4_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes DHCP IPv4 servers."""
        return self._client.request("DELETE", "/dhcp/servers/ipv4/config", json={"data": config})

    def get_dhcp_servers_ipv4_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns DHCP IPv4 server."""
        return self._client.request(
            "GET", f"/dhcp/servers/ipv4/config/{config_id}", params={"all_options": all_options}
        )

    def update_dhcp_servers_ipv4_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates DHCP IPv4 server."""
        return self._client.request("PUT", f"/dhcp/servers/ipv4/config/{config_id}", json={"data": config})

    def delete_dhcp_servers_ipv4_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes DHCP IPv4 server."""
        return self._client.request("DELETE", f"/dhcp/servers/ipv4/config/{config_id}")

    def get_dhcp_servers_ipv4_status(self) -> dict[str, Any]:
        """Returns status of DHCPv4 servers."""
        return self._client.request("GET", "/dhcp/servers/ipv4/status")

    def get_dhcp_servers_ipv6_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns DHCP IPv6 servers."""
        return self._client.request("GET", "/dhcp/servers/ipv6/config", params={"all_options": all_options})

    def create_dhcp_servers_ipv6_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates DHCP IPv6 server."""
        return self._client.request("POST", "/dhcp/servers/ipv6/config", json={"data": config})

    def update_dhcp_servers_ipv6_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates DHCP IPv6 servers."""
        return self._client.request("PUT", "/dhcp/servers/ipv6/config", json={"data": config})

    def delete_dhcp_servers_ipv6_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes DHCP IPv6 servers."""
        return self._client.request("DELETE", "/dhcp/servers/ipv6/config", json={"data": config})

    def get_dhcp_servers_ipv6_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns DHCP IPv6 server."""
        return self._client.request(
            "GET", f"/dhcp/servers/ipv6/config/{config_id}", params={"all_options": all_options}
        )

    def update_dhcp_servers_ipv6_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates DHCP IPv6 server."""
        return self._client.request("PUT", f"/dhcp/servers/ipv6/config/{config_id}", json={"data": config})

    def delete_dhcp_servers_ipv6_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes DHCP IPv6 server."""
        return self._client.request("DELETE", f"/dhcp/servers/ipv6/config/{config_id}")

    def get_dhcp_servers_ipv6_status(self) -> dict[str, Any]:
        """Returns status of DHCPv6 servers."""
        return self._client.request("GET", "/dhcp/servers/ipv6/status")

    def get_dhcp_static_leases_ipv4_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns static IPv4 leases."""
        return self._client.request("GET", "/dhcp/static_leases/ipv4/config", params={"all_options": all_options})

    def create_dhcp_static_leases_ipv4_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates static IPv4 lease."""
        return self._client.request("POST", "/dhcp/static_leases/ipv4/config", json={"data": config})

    def update_dhcp_static_leases_ipv4_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates static IPv4 leases."""
        return self._client.request("PUT", "/dhcp/static_leases/ipv4/config", json={"data": config})

    def delete_dhcp_static_leases_ipv4_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes static IPv4 leases."""
        return self._client.request("DELETE", "/dhcp/static_leases/ipv4/config", json={"data": config})

    def get_dhcp_static_leases_ipv4_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns static IPv4 lease."""
        return self._client.request(
            "GET", f"/dhcp/static_leases/ipv4/config/{config_id}", params={"all_options": all_options}
        )

    def update_dhcp_static_leases_ipv4_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates static IPv4 lease."""
        return self._client.request("PUT", f"/dhcp/static_leases/ipv4/config/{config_id}", json={"data": config})

    def delete_dhcp_static_leases_ipv4_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes static IPv4 lease."""
        return self._client.request("DELETE", f"/dhcp/static_leases/ipv4/config/{config_id}")

    def get_dhcp_static_leases_ipv6_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns static IPv6 leases."""
        return self._client.request("GET", "/dhcp/static_leases/ipv6/config", params={"all_options": all_options})

    def create_dhcp_static_leases_ipv6_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates static IPv6 lease."""
        return self._client.request("POST", "/dhcp/static_leases/ipv6/config", json={"data": config})

    def update_dhcp_static_leases_ipv6_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates static IPv6 leases."""
        return self._client.request("PUT", "/dhcp/static_leases/ipv6/config", json={"data": config})

    def delete_dhcp_static_leases_ipv6_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes static IPv6 leases."""
        return self._client.request("DELETE", "/dhcp/static_leases/ipv6/config", json={"data": config})

    def get_dhcp_static_leases_ipv6_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns static lease."""
        return self._client.request(
            "GET", f"/dhcp/static_leases/ipv6/config/{config_id}", params={"all_options": all_options}
        )

    def update_dhcp_static_leases_ipv6_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates static lease."""
        return self._client.request("PUT", f"/dhcp/static_leases/ipv6/config/{config_id}", json={"data": config})

    def delete_dhcp_static_leases_ipv6_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes static lease."""
        return self._client.request("DELETE", f"/dhcp/static_leases/ipv6/config/{config_id}")
