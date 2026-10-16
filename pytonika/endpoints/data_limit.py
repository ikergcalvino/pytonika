from typing import Any

from ._endpoint import Endpoint


class DataLimit(Endpoint):
    def data_limit_actions_clear(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Clears data limit of the specified interface."""
        return self._client.request("POST", "/data_limit/actions/clear", json=None if data is None else {"data": data})

    def get_data_limit_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Data Limit configurations."""
        return self._client.request("GET", "/data_limit/config", params={"all_options": all_options})

    def create_data_limit_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Data Limit configuration."""
        return self._client.request("POST", "/data_limit/config", json={"data": config})

    def update_data_limit_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Data limit configurations."""
        return self._client.request("PUT", "/data_limit/config", json={"data": config})

    def delete_data_limit_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes Data Limit configurations."""
        return self._client.request("DELETE", "/data_limit/config", json={"data": config})

    def get_data_limit_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Data Limit configuration."""
        return self._client.request("GET", f"/data_limit/config/{config_id}", params={"all_options": all_options})

    def update_data_limit_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Data Limit configuration."""
        return self._client.request("PUT", f"/data_limit/config/{config_id}", json={"data": config})

    def delete_data_limit_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes Data Limit configuration."""
        return self._client.request("DELETE", f"/data_limit/config/{config_id}")

    def get_data_limit_status(self) -> dict[str, Any]:
        """Returns Data Limit configurations status."""
        return self._client.request("GET", "/data_limit/status")

    def get_data_limit_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns Data Limit status of specified configuration."""
        return self._client.request("GET", f"/data_limit/status/{status_id}")
