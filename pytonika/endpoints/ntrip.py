from typing import Any

from ._base import Endpoint


class NTRIP(Endpoint):
    def get_ntrip_config(self) -> dict[str, Any]:
        """Returns all NTRIP configurations."""
        endpoint = "/ntrip/config"

        return self._api_client.get(endpoint)

    def create_ntrip_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates NTRIP configuration."""
        endpoint = "/ntrip/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_ntrip_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified NTRIP configurations."""
        endpoint = "/ntrip/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ntrip_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified NTRIP configurations."""
        return [self.delete_ntrip_config_by_id(ntrip_id) for ntrip_id in config]

    def get_ntrip_config_by_id(self, ntrip_id: str) -> dict[str, Any]:
        """Returns the specified NTRIP configuration."""
        endpoint = f"/ntrip/config/{ntrip_id}"

        return self._api_client.get(endpoint)

    def update_ntrip_config_by_id(self, ntrip_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified NTRIP configuration."""
        endpoint = f"/ntrip/config/{ntrip_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ntrip_config_by_id(self, ntrip_id: str) -> dict[str, Any]:
        """Deletes the specified NTRIP configuration."""
        endpoint = f"/ntrip/config/{ntrip_id}"

        return self._api_client.delete(endpoint)

    def get_ntrip_status(self) -> dict[str, Any]:
        """Returns NTRIP status."""
        endpoint = "/ntrip/status"

        return self._api_client.get(endpoint)
