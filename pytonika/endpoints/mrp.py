from typing import Any

from ._endpoint import Endpoint


class MRP(Endpoint):
    def get_mrp_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all MRP configurations."""
        return self._client.request("GET", "/mrp/config", params={"all_options": all_options})

    def update_mrp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified MRP configurations."""
        return self._client.request("PUT", "/mrp/config", json={"data": config})

    def get_mrp_config_by_id(self, mrp_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified MRP configuration."""
        return self._client.request("GET", f"/mrp/config/{mrp_id}", params={"all_options": all_options})

    def update_mrp_config_by_id(self, mrp_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified MRP configuration."""
        return self._client.request("PUT", f"/mrp/config/{mrp_id}", json={"data": config})

    def get_mrp_instance_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all MRP section configurations."""
        return self._client.request("GET", "/mrp/instance/config", params={"all_options": all_options})

    def update_mrp_instance_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified MRP section configurations."""
        return self._client.request("PUT", "/mrp/instance/config", json={"data": config})

    def get_mrp_instance_config_by_id(self, instance_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified MRP section configuration."""
        return self._client.request("GET", f"/mrp/instance/config/{instance_id}", params={"all_options": all_options})

    def update_mrp_instance_config_by_id(self, instance_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified MRP section configuration."""
        return self._client.request("PUT", f"/mrp/instance/config/{instance_id}", json={"data": config})
