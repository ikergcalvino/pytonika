from typing import Any

from ._base import Endpoint


class IPSec(Endpoint):
    def get_ipsec_config(self) -> dict[str, Any]:
        """Returns all IPsec configurations."""
        endpoint = "/ipsec/config"

        return self._api_client.get(endpoint)

    def create_ipsec_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates IPsec configuration."""
        endpoint = "/ipsec/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_ipsec_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified IPsec configurations."""
        endpoint = "/ipsec/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ipsec_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified IPsec configurations."""
        return [self.delete_ipsec_config_by_id(config_id) for config_id in config]

    def get_ipsec_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified IPsec configuration."""
        endpoint = f"/ipsec/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_ipsec_config_by_id(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads certificates."""
        endpoint = f"/ipsec/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_ipsec_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified IPsec configuration."""
        endpoint = f"/ipsec/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ipsec_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified IPsec configuration."""
        endpoint = f"/ipsec/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_ipsec_status(self) -> dict[str, Any]:
        """Returns the status of all ipsec instances."""
        endpoint = "/ipsec/status"

        return self._api_client.get(endpoint)

    def get_ipsec_status_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the status of the ipsec instance."""
        endpoint = f"/ipsec/status/{config_id}"

        return self._api_client.get(endpoint)

    def upload_ipsec_secrets_config_by_id(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads certificates."""
        endpoint = f"/ipsec/secrets/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def get_ipsec_secrets_config(self) -> dict[str, Any]:
        """Returns all IPsec secrets configurations."""
        endpoint = "/ipsec/secrets/config"

        return self._api_client.get(endpoint)

    def create_ipsec_secrets_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates IPsec secret configuration."""
        endpoint = "/ipsec/secrets/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_ipsec_secrets_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified IPsec secret configurations."""
        endpoint = "/ipsec/secrets/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ipsec_secrets_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified IPsec secret configurations."""
        return [self.delete_ipsec_secrets_config_by_id(config_id) for config_id in config]

    def get_ipsec_secrets_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified IPsec secret configuration."""
        endpoint = f"/ipsec/secrets/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_ipsec_secrets_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified IPsec secret configuration."""
        endpoint = f"/ipsec/secrets/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_ipsec_secrets_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified IPsec secret configuration."""
        endpoint = f"/ipsec/secrets/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_ipsec_global(self) -> dict[str, Any]:
        """Returns IPsec global section."""
        endpoint = "/ipsec/global"

        return self._api_client.get(endpoint)

    def update_ipsec_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates IPsec global configuration."""
        endpoint = "/ipsec/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
