from typing import Any

from ._endpoint import Endpoint


class OperatorLists(Endpoint):
    def get_operator_lists_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns multiple configurations of operator lists."""
        return self._client.request("GET", "/operator_lists/config", params={"all_options": all_options})

    def create_operator_lists_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates configuration for operator lists."""
        return self._client.request("POST", "/operator_lists/config", json={"data": config})

    def update_operator_lists_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple configurations of operator lists."""
        return self._client.request("PUT", "/operator_lists/config", json={"data": config})

    def delete_operator_lists_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes multiple configurations of operator lists."""
        return self._client.request("DELETE", "/operator_lists/config", json={"data": config})

    def get_operator_lists_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified configuration of operator lists."""
        return self._client.request("GET", f"/operator_lists/config/{config_id}", params={"all_options": all_options})

    def update_operator_lists_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified configuration of operator lists."""
        return self._client.request("PUT", f"/operator_lists/config/{config_id}", json={"data": config})

    def delete_operator_lists_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified configuration of operator lists."""
        return self._client.request("DELETE", f"/operator_lists/config/{config_id}")
