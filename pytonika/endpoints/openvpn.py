from typing import Any

from ._base import Endpoint


class OpenVPN(Endpoint):
    def get_openvpn_clients_config(self, openvpn_id: str) -> dict[str, Any]:
        """Returns all openvpn tls client configuration sections."""
        endpoint = f"/openvpn/{openvpn_id}/clients/config"

        return self._api_client.get(endpoint)

    def create_openvpn_clients_config(self, openvpn_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates openvpn tls section."""
        endpoint = f"/openvpn/{openvpn_id}/clients/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_openvpn_clients_config(self, openvpn_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified openvpn tls client configurations."""
        endpoint = f"/openvpn/{openvpn_id}/clients/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_openvpn_clients_config(self, openvpn_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified openvpn tls client configurations."""
        return [self.delete_openvpn_clients_config_by_id(openvpn_id, clients_id) for clients_id in config]

    def get_openvpn_clients_config_by_id(self, openvpn_id: str, clients_id: str) -> dict[str, Any]:
        """Returns specified openvpn tls client section."""
        endpoint = f"/openvpn/{openvpn_id}/clients/config/{clients_id}"

        return self._api_client.get(endpoint)

    def update_openvpn_clients_config_by_id(
        self, openvpn_id: str, clients_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates specified OpenVPN TLS client configuration."""
        endpoint = f"/openvpn/{openvpn_id}/clients/config/{clients_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_openvpn_clients_config_by_id(self, openvpn_id: str, clients_id: str) -> dict[str, Any]:
        """Deletes specified openvpn tls client configuration."""
        endpoint = f"/openvpn/{openvpn_id}/clients/config/{clients_id}"

        return self._api_client.delete(endpoint)

    def get_openvpn_config(self) -> dict[str, Any]:
        """Returns all openvpn configuration sections."""
        endpoint = "/openvpn/config"

        return self._api_client.get(endpoint)

    def create_openvpn_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates openvpn section."""
        endpoint = "/openvpn/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_openvpn_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified openvpn configurations."""
        endpoint = "/openvpn/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_openvpn_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified openvpn child configurations."""
        return [self.delete_openvpn_config_by_id(config_id) for config_id in config]

    def get_openvpn_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified openvpn section."""
        endpoint = f"/openvpn/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_openvpn_config_by_id(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads custom configuration file."""
        endpoint = f"/openvpn/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_openvpn_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified openvpn configuration."""
        endpoint = f"/openvpn/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_openvpn_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified openvpn configuration."""
        endpoint = f"/openvpn/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_openvpn_status(self) -> dict[str, Any]:
        """Returns all openvpn configuration sections statuses."""
        endpoint = "/openvpn/status"

        return self._api_client.get(endpoint)

    def get_openvpn_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns single openvpn configuration instance status."""
        endpoint = f"/openvpn/status/{status_id}"

        return self._api_client.get(endpoint)

    def openvpn_actions_download(self, openvpn_id: str) -> dict[str, Any]:
        """Downloads specified configuration file."""
        endpoint = f"/openvpn/{openvpn_id}/actions/download"

        return self._api_client.post(endpoint)
