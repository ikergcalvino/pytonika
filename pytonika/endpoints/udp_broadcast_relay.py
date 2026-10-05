from typing import Any

from ._endpoint import Endpoint


class UDPBroadcastRelay(Endpoint):
    def get_udprelay_config(self) -> dict[str, Any]:
        """Returns UDP Broadcast Relay configurations."""
        endpoint = "/udprelay/config"

        return self._client.request("GET", endpoint)

    def create_udprelay_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates UDP Broadcast Relay configuration."""
        endpoint = "/udprelay/config"

        data = {"data": config}

        return self._client.request("POST", endpoint, json=data)

    def update_udprelay_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates UDP Broadcast Relay configurations.

        .. deprecated::
        """
        endpoint = "/udprelay/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_udprelay_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes UDP Broadcast Relay configurations."""
        return [self.delete_udprelay_config_by_id(config_id) for config_id in config]

    def get_udprelay_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns UDP Broadcast Relay configuration."""
        endpoint = f"/udprelay/config/{config_id}"

        return self._client.request("GET", endpoint)

    def update_udprelay_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates UDP Broadcast Relay configuration."""
        endpoint = f"/udprelay/config/{config_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_udprelay_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes UDP Broadcast Relay configuration."""
        endpoint = f"/udprelay/config/{config_id}"

        return self._client.request("DELETE", endpoint)
