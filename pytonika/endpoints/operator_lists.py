from typing import Any

from ._endpoint import Endpoint


class OperatorLists(Endpoint):
    def get_operator_lists_config(self) -> dict[str, Any]:
        """Returns multiple configurations of operator lists."""
        endpoint = "/operator_lists/config"

        return self._client.request("GET", endpoint)

    def create_operator_lists_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates configuration for operator lists."""
        endpoint = "/operator_lists/config"

        data = {"data": config}

        return self._client.request("POST", endpoint, json=data)

    def update_operator_lists_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple configurations of operator lists."""
        endpoint = "/operator_lists/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_operator_lists_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes multiple configurations of operator lists."""
        return [self.delete_operator_lists_config_by_id(config_id) for config_id in config]

    def get_operator_lists_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified configuration of operator lists."""
        endpoint = f"/operator_lists/config/{config_id}"

        return self._client.request("GET", endpoint)

    def update_operator_lists_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified configuration of operator lists."""
        endpoint = f"/operator_lists/config/{config_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_operator_lists_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified configuration of operator lists."""
        endpoint = f"/operator_lists/config/{config_id}"

        return self._client.request("DELETE", endpoint)
