from typing import Any

from ._base import Endpoint


class WirelessReboot(Endpoint):
    def get_auto_reboot_wireless_config(self) -> dict[str, Any]:
        """Returns all Wireless Reboot configurations."""
        endpoint = "/auto_reboot/wireless/config"

        return self._api_client.get(endpoint)

    def update_auto_reboot_wireless_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Wireless Reboot configurations."""
        endpoint = "/auto_reboot/wireless/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_auto_reboot_wireless_config_by_id(self, wireless_id: str) -> dict[str, Any]:
        """Returns the selected Wireless Reboot configuration."""
        endpoint = f"/auto_reboot/wireless/config/{wireless_id}"

        return self._api_client.get(endpoint)

    def update_auto_reboot_wireless_config_by_id(self, wireless_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected Wireless Reboot configuration."""
        endpoint = f"/auto_reboot/wireless/config/{wireless_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
