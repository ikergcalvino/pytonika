from typing import Any

from ._endpoint import Endpoint


class UDPBroadcastRelay(Endpoint):
    def get_udprelay_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns UDP Broadcast Relay configurations."""
        return self._client.request("GET", "/udprelay/config", params={"all_options": all_options})

    def create_udprelay_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates UDP Broadcast Relay configuration."""
        return self._client.request("POST", "/udprelay/config", json={"data": config})

    def update_udprelay_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates UDP Broadcast Relay configurations."""
        return self._client.request("PUT", "/udprelay/config", json={"data": config})

    def delete_udprelay_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes UDP Broadcast Relay configurations."""
        return self._client.request("DELETE", "/udprelay/config", json={"data": config})

    def get_udprelay_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns UDP Broadcast Relay configuration."""
        return self._client.request("GET", f"/udprelay/config/{config_id}", params={"all_options": all_options})

    def update_udprelay_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates UDP Broadcast Relay configuration."""
        return self._client.request("PUT", f"/udprelay/config/{config_id}", json={"data": config})

    def delete_udprelay_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes UDP Broadcast Relay configuration."""
        return self._client.request("DELETE", f"/udprelay/config/{config_id}")
