from typing import Any

from ._base import Endpoint


class Stunnel(Endpoint):
    def get_stunnel_global(self) -> dict[str, Any]:
        """Returns specified stunnel global section."""
        endpoint = "/stunnel/global"

        return self._api_client.get(endpoint)

    def update_stunnel_global(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified stunnel global configuration."""
        endpoint = "/stunnel/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_stunnel_config(self) -> dict[str, Any]:
        """Returns all stunnel configuration sections."""
        endpoint = "/stunnel/config"

        return self._api_client.get(endpoint)

    def create_stunnel_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates stunnel section."""
        endpoint = "/stunnel/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_stunnel_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Update all section options."""
        endpoint = "/stunnel/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_stunnel_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified stunnel configurations."""
        return [self.delete_stunnel_config_by_id(stunnel_id) for stunnel_id in config]

    def get_stunnel_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified stunnel section."""
        endpoint = f"/stunnel/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_stunnel_certificates(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads certificates."""
        endpoint = f"/stunnel/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_stunnel_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified stunnel configuration."""
        endpoint = f"/stunnel/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_stunnel_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified stunnel configuration."""
        endpoint = f"/stunnel/config/{config_id}"

        return self._api_client.delete(endpoint)
