from typing import Any

from ._base import Endpoint


class Tinc(Endpoint):
    def get_tinc_hosts_config(self, tinc_id: str) -> dict[str, Any]:
        """Returns all Tinc VPN Host configurations."""
        endpoint = f"/tinc/{tinc_id}/hosts/config"

        return self._api_client.get(endpoint)

    def create_tinc_hosts_config(self, tinc_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Tinc VPN Host configuration."""
        endpoint = f"/tinc/{tinc_id}/hosts/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_tinc_hosts_config(self, tinc_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Tinc VPN Hosts configurations."""
        endpoint = f"/tinc/{tinc_id}/hosts/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_tinc_hosts_config(self, tinc_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Tinc VPN Host configurations."""
        return [self.delete_tinc_host_config_by_id(tinc_id, host_id) for host_id in config]

    def get_tinc_host_config_by_id(self, tinc_id: str, host_id: str) -> dict[str, Any]:
        """Returns the specified Tinc VPN Host configuration."""
        endpoint = f"/tinc/{tinc_id}/hosts/config/{host_id}"

        return self._api_client.get(endpoint)

    def upload_tinc_host_key_file(self, tinc_id: str, host_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads key file."""
        endpoint = f"/tinc/{tinc_id}/hosts/config/{host_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_tinc_host_config_by_id(self, tinc_id: str, host_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Tinc VPN Host configuration."""
        endpoint = f"/tinc/{tinc_id}/hosts/config/{host_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_tinc_host_config_by_id(self, tinc_id: str, host_id: str) -> dict[str, Any]:
        """Deletes the specified Tinc VPN Host configuration."""
        endpoint = f"/tinc/{tinc_id}/hosts/config/{host_id}"

        return self._api_client.delete(endpoint)

    def get_tinc_config(self) -> dict[str, Any]:
        """Returns all Tinc VPN configurations."""
        endpoint = "/tinc/config"

        return self._api_client.get(endpoint)

    def create_tinc_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Tinc VPN configuration."""
        endpoint = "/tinc/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_tinc_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Tinc VPN configurations."""
        endpoint = "/tinc/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_tinc_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Tinc VPN configurations."""
        return [self.delete_tinc_config_by_id(tinc_id) for tinc_id in config]

    def get_tinc_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified Tinc VPN configuration."""
        endpoint = f"/tinc/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_tinc_key_file(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads key file."""
        endpoint = f"/tinc/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_tinc_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Tinc VPN configuration."""
        endpoint = f"/tinc/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_tinc_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Tinc VPN configuration."""
        endpoint = f"/tinc/config/{config_id}"

        return self._api_client.delete(endpoint)
