from typing import Any

from ._base import Endpoint


class MRP(Endpoint):
    def get_mrp_config(self) -> dict[str, Any]:
        """Returns all MRP configurations."""
        endpoint = "/mrp/config"

        return self._api_client.get(endpoint)

    def update_mrp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified MRP configurations."""
        endpoint = "/mrp/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_mrp_config_by_id(self, mrp_id: str) -> dict[str, Any]:
        """Returns the specified MRP configuration."""
        endpoint = f"/mrp/config/{mrp_id}"

        return self._api_client.get(endpoint)

    def update_mrp_config_by_id(self, mrp_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified MRP configuration."""
        endpoint = f"/mrp/config/{mrp_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_mrp_instance_config(self) -> dict[str, Any]:
        """Returns all MRP section configurations."""
        endpoint = "/mrp/instance/config"

        return self._api_client.get(endpoint)

    def update_mrp_instance_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified MRP section configurations."""
        endpoint = "/mrp/instance/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_mrp_instance_config_by_id(self, instance_id: str) -> dict[str, Any]:
        """Returns the specified MRP section configuration."""
        endpoint = f"/mrp/instance/config/{instance_id}"

        return self._api_client.get(endpoint)

    def update_mrp_instance_config_by_id(self, instance_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified MRP section configuration."""
        endpoint = f"/mrp/instance/config/{instance_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
