from typing import Any

from ._base import Endpoint


class DDNS(Endpoint):
    def get_ddns_config(self) -> dict[str, Any]:
        """Returns all dynamic DNS configuration sections."""
        endpoint = "/ddns/config"

        return self._api_client.get(endpoint)

    def create_ddns_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new DDNS section."""
        endpoint = "/ddns/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_ddns_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified dynamic DNS configurations."""
        endpoint = "/ddns/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ddns_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the specified dynamic DNS configurations."""
        return [self.delete_ddns_config_by_id(ddns_id) for ddns_id in config]

    def get_ddns_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified dynamic DNS section."""
        endpoint = f"/ddns/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_ddns_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified dynamic DNS configuration."""
        endpoint = f"/ddns/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ddns_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified dynamic DNS configuration."""
        endpoint = f"/ddns/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_ddns_status(self) -> dict[str, Any]:
        """Returns the status about all DDNS instances."""
        endpoint = "/ddns/status"

        return self._api_client.get(endpoint)

    def get_ddns_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns the status about the selected DDNS instance."""
        endpoint = f"/ddns/status/{status_id}"

        return self._api_client.get(endpoint)

    def get_ddns_options(self) -> dict[str, Any]:
        """Returns info needed to configure a DDNS section."""
        endpoint = "/ddns/options"

        return self._api_client.get(endpoint)
