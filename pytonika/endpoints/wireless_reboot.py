from typing import Any

from ._endpoint import Endpoint


class WirelessReboot(Endpoint):
    def get_auto_reboot_wireless_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Wireless Reboot configurations."""
        return self._client.request("GET", "/auto_reboot/wireless/config", params={"all_options": all_options})

    def update_auto_reboot_wireless_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Wireless Reboot configurations."""
        return self._client.request("PUT", "/auto_reboot/wireless/config", json={"data": config})

    def get_auto_reboot_wireless_config_by_id(
        self, wireless_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the selected Wireless Reboot configuration."""
        return self._client.request(
            "GET", f"/auto_reboot/wireless/config/{wireless_id}", params={"all_options": all_options}
        )

    def update_auto_reboot_wireless_config_by_id(self, wireless_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected Wireless Reboot configuration."""
        return self._client.request("PUT", f"/auto_reboot/wireless/config/{wireless_id}", json={"data": config})
