from typing import Any

from ._base import Endpoint


class SDUSBTools(Endpoint):
    def get_usb_tools_p910nd_config(self) -> dict[str, Any]:
        """Returns all p910nd configuration sections."""
        endpoint = "/usb_tools/p910nd/config"

        return self._api_client.get(endpoint)

    def update_usb_tools_p910nd_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update all sections options."""
        endpoint = "/usb_tools/p910nd/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_usb_tools_p910nd_options(self) -> dict[str, Any]:
        """Returns available printer server device options."""
        endpoint = "/usb_tools/p910nd/options"

        return self._api_client.get(endpoint)

    def get_usb_tools_p910nd_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified p910nd section."""
        endpoint = f"/usb_tools/p910nd/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_usb_tools_p910nd_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update specified sections options."""
        endpoint = f"/usb_tools/p910nd/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_usb_tools_config(self) -> dict[str, Any]:
        """Returns all sd & usb tools configuration sections."""
        endpoint = "/usb_tools/config"

        return self._api_client.get(endpoint)

    def update_usb_tools_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update all sections options."""
        endpoint = "/usb_tools/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_usb_tools_mount_options(self) -> dict[str, Any]:
        """Returns mounted devices."""
        endpoint = "/usb_tools/mount/options"

        return self._api_client.get(endpoint)

    def get_usb_tools_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified sd & usb tools section."""
        endpoint = f"/usb_tools/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_usb_tools_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update specified sections options."""
        endpoint = f"/usb_tools/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def usb_tools_format(self, data: dict[str, Any]) -> dict[str, Any]:
        """Formats selected USB device."""
        endpoint = "/usb_tools/actions/format"

        return self._api_client.post(endpoint, data={"data": data})

    def usb_tools_safe_remove(self, data: dict[str, Any]) -> dict[str, Any]:
        """Safe remove."""
        endpoint = "/usb_tools/actions/safe_remove"

        return self._api_client.post(endpoint, data={"data": data})

    def get_usb_tools_memory_expansion_status(self) -> dict[str, Any]:
        """Returns all status information."""
        endpoint = "/usb_tools/memory_expansion/status"

        return self._api_client.get(endpoint)

    def usb_tools_memory_expansion_enable(self, data: dict[str, Any]) -> dict[str, Any]:
        """Enable memory expansion."""
        endpoint = "/usb_tools/memory_expansion/actions/enable_expansion"

        return self._api_client.post(endpoint, data={"data": data})

    def usb_tools_memory_expansion_disable(self, data: dict[str, Any]) -> dict[str, Any]:
        """Disable memory expansion."""
        endpoint = "/usb_tools/memory_expansion/actions/disable_expansion"

        return self._api_client.post(endpoint, data={"data": data})
