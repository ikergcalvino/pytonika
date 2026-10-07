from typing import Any

from ._endpoint import Endpoint


class EthernetIP(Endpoint):
    def ethernet_ip_actions_download_eds(self) -> bytes | dict[str, Any]:
        """Download EDS file."""
        return self._client.request("POST", "/ethernet_ip/actions/download_eds", download=True)

    def get_ethernet_ip_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Ethernet/IP configurations."""
        return self._client.request("GET", "/ethernet_ip/config", params={"all_options": all_options})

    def update_ethernet_ip_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Ethernet/IP configurations."""
        return self._client.request("PUT", "/ethernet_ip/config", json={"data": config})

    def get_ethernet_ip_config_by_id(self, ethernet_ip_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Ethernet/IP configuration."""
        return self._client.request("GET", f"/ethernet_ip/config/{ethernet_ip_id}", params={"all_options": all_options})

    def update_ethernet_ip_config_by_id(self, ethernet_ip_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Ethernet/IP configuration."""
        return self._client.request("PUT", f"/ethernet_ip/config/{ethernet_ip_id}", json={"data": config})
