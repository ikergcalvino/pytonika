from typing import Any

from ._endpoint import Endpoint


class PortsSettings(Endpoint):
    def ports_settings_actions_bounce_link(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Restarts the link of the specified ports."""
        return self._client.request(
            "POST", "/ports_settings/actions/bounce_link", json=None if data is None else {"data": data}
        )

    def ports_settings_actions_bounce_poe(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Restarts the PoE of the specified ports."""
        return self._client.request(
            "POST", "/ports_settings/actions/bounce_poe", json=None if data is None else {"data": data}
        )

    def get_ports_settings_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns port configurations."""
        return self._client.request("GET", "/ports_settings/config", params={"all_options": all_options})

    def update_ports_settings_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates port configurations."""
        return self._client.request("PUT", "/ports_settings/config", json={"data": config})

    def get_ports_settings_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns port configuration."""
        return self._client.request("GET", f"/ports_settings/config/{config_id}", params={"all_options": all_options})

    def update_ports_settings_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates port configuration."""
        return self._client.request("PUT", f"/ports_settings/config/{config_id}", json={"data": config})

    def get_ports_settings_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns ports general configuration."""
        return self._client.request("GET", "/ports_settings/global", params={"all_options": all_options})

    def update_ports_settings_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates ports general configuration."""
        return self._client.request("PUT", "/ports_settings/global", json={"data": config})

    def get_ports_settings_status(self, *, sfp_stats: bool | None = None) -> dict[str, Any]:
        """Returns port status."""
        return self._client.request("GET", "/ports_settings/status", params={"sfp_stats": sfp_stats})
