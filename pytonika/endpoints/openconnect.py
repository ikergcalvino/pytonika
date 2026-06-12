from typing import Any

from ._base import Endpoint


class OpenConnect(Endpoint):
    def get_openconnect_client_config(self) -> dict[str, Any]:
        """Returns all OpenConnect configuration sections."""
        endpoint = "/openconnect/client/config"

        return self._api_client.get(endpoint)

    def create_openconnect_client_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates OpenConnect client section."""
        endpoint = "/openconnect/client/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_openconnect_client_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the specified OpenConnect configurations."""
        endpoint = "/openconnect/client/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_openconnect_client_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified OpenConnect configurations."""
        return [self.delete_openconnect_client_config_by_id(config_id) for config_id in config]

    def get_openconnect_client_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified OpenConnect client section."""
        endpoint = f"/openconnect/client/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_openconnect_client_config_by_id(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads OpenConnect client certificates."""
        endpoint = f"/openconnect/client/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_openconnect_client_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified OpenConnect configuration."""
        endpoint = f"/openconnect/client/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_openconnect_client_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified OpenConnect configuration."""
        endpoint = f"/openconnect/client/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_openconnect_client_status(self) -> dict[str, Any]:
        """Returns status of OpenConnect instances."""
        endpoint = "/openconnect/client/status"

        return self._api_client.get(endpoint)

    def get_openconnect_client_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns status of OpenConnect instance."""
        endpoint = f"/openconnect/client/status/{status_id}"

        return self._api_client.get(endpoint)

    def openconnect_client_actions_check_fingerprint(self, data: dict[str, Any]) -> dict[str, Any]:
        """Checks OpenConnect client fingerprint."""
        endpoint = "/openconnect/client/actions/check_fingerprint"

        return self._api_client.post(endpoint, data={"data": data})
