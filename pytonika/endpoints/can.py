from typing import Any

from ._base import Endpoint


class CAN(Endpoint):
    def get_can_gateway_config(self) -> dict[str, Any]:
        """Returns all CAN gateway configurations."""
        endpoint = "/can/gateway/config"

        return self._api_client.get(endpoint)

    def update_can_gateway_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified CAN gateway configurations."""
        endpoint = "/can/gateway/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_can_gateway_config_by_id(self, gateway_id: str) -> dict[str, Any]:
        """Returns the specified CAN gateway configuration."""
        endpoint = f"/can/gateway/config/{gateway_id}"

        return self._api_client.get(endpoint)

    def upload_can_gateway_config_by_id(self, gateway_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads the specified CAN gateway configuration certificate files."""
        endpoint = f"/can/gateway/config/{gateway_id}"

        return self._api_client.post(endpoint, data=data)

    def update_can_gateway_config_by_id(self, gateway_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified CAN gateway configuration."""
        endpoint = f"/can/gateway/config/{gateway_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_can_gateway_status(self) -> dict[str, Any]:
        """Returns CAN gateway status."""
        endpoint = "/can/gateway/status"

        return self._api_client.get(endpoint)
