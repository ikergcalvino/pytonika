from typing import Any

from ._base import Endpoint


class EmailRelay(Endpoint):
    def get_email_relay_config(self) -> dict[str, Any]:
        """Returns all Email Relay configurations."""
        endpoint = "/email_relay/config"

        return self._api_client.get(endpoint)

    def create_email_relay_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Email Relay configuration."""
        endpoint = "/email_relay/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_email_relay_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Email Relay configurations."""
        endpoint = "/email_relay/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_email_relay_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Email Relay configurations."""
        return [self.delete_email_relay_config_by_id(config_id) for config_id in config]

    def get_email_relay_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified Email Relay configuration."""
        endpoint = f"/email_relay/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_email_relay_config_by_id(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads TLS certificate."""
        endpoint = f"/email_relay/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_email_relay_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Email Relay configuration."""
        endpoint = f"/email_relay/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_email_relay_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Email Relay configuration."""
        endpoint = f"/email_relay/config/{config_id}"

        return self._api_client.delete(endpoint)
