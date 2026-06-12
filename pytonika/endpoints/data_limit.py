from typing import Any

from ._base import Endpoint


class DataLimit(Endpoint):
    def get_data_limit_config(self) -> dict[str, Any]:
        """Returns Data Limit configurations."""
        endpoint = "/data_limit/config"

        return self._api_client.get(endpoint)

    def create_data_limit_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Data Limit configuration."""
        endpoint = "/data_limit/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_data_limit_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Data limit configurations."""
        endpoint = "/data_limit/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_data_limit_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes Data Limit configurations."""
        return [self.delete_data_limit_config_by_id(limit_id) for limit_id in config]

    def get_data_limit_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Data Limit configuration."""
        endpoint = f"/data_limit/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_data_limit_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Data Limit configuration."""
        endpoint = f"/data_limit/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_data_limit_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes Data Limit configuration."""
        endpoint = f"/data_limit/config/{config_id}"

        return self._api_client.delete(endpoint)

    def data_limit_clear(self, data: dict[str, Any]) -> dict[str, Any]:
        """Clears data limit of the specified interface."""
        endpoint = "/data_limit/actions/clear"

        return self._api_client.post(endpoint, data={"data": data})

    def get_data_limit_status(self) -> dict[str, Any]:
        """Returns Data Limit configurations status."""
        endpoint = "/data_limit/status"

        return self._api_client.get(endpoint)

    def get_data_limit_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns Data Limit status of specified configuration."""
        endpoint = f"/data_limit/status/{status_id}"

        return self._api_client.get(endpoint)
