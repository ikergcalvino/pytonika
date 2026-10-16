from typing import Any

from ._endpoint import Endpoint


class WebFilter(Endpoint):
    def get_webfilter_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Site Blocking rules."""
        return self._client.request("GET", "/webfilter/config", params={"all_options": all_options})

    def create_webfilter_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Site Blocking rule."""
        return self._client.request("POST", "/webfilter/config", json={"data": config})

    def update_webfilter_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Site Blocking rules."""
        return self._client.request("PUT", "/webfilter/config", json={"data": config})

    def delete_webfilter_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Site Blocking rules."""
        return self._client.request("DELETE", "/webfilter/config", json={"data": config})

    def get_webfilter_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Site Blocking rule."""
        return self._client.request("GET", f"/webfilter/config/{config_id}", params={"all_options": all_options})

    def update_webfilter_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Site Blocking rule."""
        return self._client.request("PUT", f"/webfilter/config/{config_id}", json={"data": config})

    def delete_webfilter_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Site Blocking rule."""
        return self._client.request("DELETE", f"/webfilter/config/{config_id}")

    def get_webfilter_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Site Blocking configuration."""
        return self._client.request("GET", "/webfilter/global", params={"all_options": all_options})

    def update_webfilter_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Site Blocking configuration."""
        return self._client.request("PUT", "/webfilter/global", json={"data": config})

    def get_webfilter_privoxy_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Proxy Based URL Content Blocker configurations."""
        return self._client.request("GET", "/webfilter/privoxy/config", params={"all_options": all_options})

    def update_webfilter_privoxy_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Proxy Based URL Content Blocker configurations."""
        return self._client.request("PUT", "/webfilter/privoxy/config", json={"data": config})

    def get_webfilter_privoxy_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Proxy Based URL Content Blocker configuration."""
        return self._client.request(
            "GET", f"/webfilter/privoxy/config/{config_id}", params={"all_options": all_options}
        )

    def update_webfilter_privoxy_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Proxy Based URL Content Blocker configuration."""
        return self._client.request("PUT", f"/webfilter/privoxy/config/{config_id}", json={"data": config})
