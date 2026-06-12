from typing import Any

from ._base import Endpoint


class WebFilter(Endpoint):
    def get_webfilter_global(self) -> dict[str, Any]:
        """Returns Site Blocking configuration."""
        endpoint = "/webfilter/global"

        return self._api_client.get(endpoint)

    def update_webfilter_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Site Blocking configuration."""
        endpoint = "/webfilter/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_webfilter_config(self) -> dict[str, Any]:
        """Returns all Site Blocking rules."""
        endpoint = "/webfilter/config"

        return self._api_client.get(endpoint)

    def create_webfilter_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Site Blocking rule."""
        endpoint = "/webfilter/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_webfilter_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Site Blocking rules."""
        endpoint = "/webfilter/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_webfilter_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Site Blocking rules."""
        return [self.delete_webfilter_config_by_id(rule_id) for rule_id in config]

    def get_webfilter_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified Site Blocking rule."""
        endpoint = f"/webfilter/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_webfilter_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Site Blocking rule."""
        endpoint = f"/webfilter/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_webfilter_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Site Blocking rule."""
        endpoint = f"/webfilter/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_webfilter_privoxy_config(self) -> dict[str, Any]:
        """Returns all Proxy Based URL Content Blocker configurations."""
        endpoint = "/webfilter/privoxy/config"

        return self._api_client.get(endpoint)

    def update_webfilter_privoxy_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Proxy Based URL Content Blocker configurations."""
        endpoint = "/webfilter/privoxy/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_webfilter_privoxy_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified Proxy Based URL Content Blocker configuration."""
        endpoint = f"/webfilter/privoxy/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_webfilter_privoxy_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Proxy Based URL Content Blocker configuration."""
        endpoint = f"/webfilter/privoxy/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
