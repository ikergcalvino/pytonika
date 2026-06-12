from typing import Any

from ._base import Endpoint


class EthernetIP(Endpoint):
    def get_ethernet_ip_config(self) -> dict[str, Any]:
        """Returns all Ethernet/IP configurations."""
        endpoint = "/ethernet_ip/config"

        return self._api_client.get(endpoint)

    def update_ethernet_ip_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Ethernet/IP configurations."""
        endpoint = "/ethernet_ip/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_ethernet_ip_config_by_id(self, ethernet_ip_id: str) -> dict[str, Any]:
        """Returns the specified Ethernet/IP configuration."""
        endpoint = f"/ethernet_ip/config/{ethernet_ip_id}"

        return self._api_client.get(endpoint)

    def update_ethernet_ip_config_by_id(self, ethernet_ip_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Ethernet/IP configuration."""
        endpoint = f"/ethernet_ip/config/{ethernet_ip_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def ethernet_ip_actions_download_eds(self) -> dict[str, Any]:
        """Download EDS file."""
        endpoint = "/ethernet_ip/actions/download_eds"

        return self._api_client.post(endpoint)
