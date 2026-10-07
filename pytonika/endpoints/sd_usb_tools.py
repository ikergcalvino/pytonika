from typing import Any

from ._endpoint import Endpoint


class SDUSBTools(Endpoint):
    def usb_tools_actions_format(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Formats selected USB device."""
        return self._client.request("POST", "/usb_tools/actions/format", json=None if data is None else {"data": data})

    def usb_tools_actions_safe_remove(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Safe remove."""
        return self._client.request(
            "POST", "/usb_tools/actions/safe_remove", json=None if data is None else {"data": data}
        )

    def get_usb_tools_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all sd & usb tools configuration sections."""
        return self._client.request("GET", "/usb_tools/config", params={"all_options": all_options})

    def update_usb_tools_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update all sections options."""
        return self._client.request("PUT", "/usb_tools/config", json={"data": config})

    def get_usb_tools_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified sd & usb tools section."""
        return self._client.request("GET", f"/usb_tools/config/{config_id}", params={"all_options": all_options})

    def update_usb_tools_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update specified sections options."""
        return self._client.request("PUT", f"/usb_tools/config/{config_id}", json={"data": config})

    def usb_tools_memory_expansion_actions_disable_expansion(self) -> dict[str, Any]:
        """Disable memory expansion."""
        return self._client.request("POST", "/usb_tools/memory_expansion/actions/disable_expansion")

    def usb_tools_memory_expansion_actions_enable_expansion(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Enable memory expansion."""
        return self._client.request(
            "POST",
            "/usb_tools/memory_expansion/actions/enable_expansion",
            json=None if data is None else {"data": data},
        )

    def get_usb_tools_memory_expansion_status(self) -> dict[str, Any]:
        """Returns all status information."""
        return self._client.request("GET", "/usb_tools/memory_expansion/status")

    def get_usb_tools_mount_options(self) -> dict[str, Any]:
        """Returns mounted devices."""
        return self._client.request("GET", "/usb_tools/mount/options")

    def get_usb_tools_p910nd_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all p910nd configuration sections."""
        return self._client.request("GET", "/usb_tools/p910nd/config", params={"all_options": all_options})

    def update_usb_tools_p910nd_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update all sections options."""
        return self._client.request("PUT", "/usb_tools/p910nd/config", json={"data": config})

    def get_usb_tools_p910nd_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified p910nd section."""
        return self._client.request("GET", f"/usb_tools/p910nd/config/{config_id}", params={"all_options": all_options})

    def update_usb_tools_p910nd_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update specified sections options."""
        return self._client.request("PUT", f"/usb_tools/p910nd/config/{config_id}", json={"data": config})

    def get_usb_tools_p910nd_options(self) -> dict[str, Any]:
        """Returns available printer server device options."""
        return self._client.request("GET", "/usb_tools/p910nd/options")
