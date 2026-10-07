from typing import Any

from ._endpoint import Endpoint, File


class CAN(Endpoint):
    def get_can_gateway_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all CAN gateway configurations."""
        return self._client.request("GET", "/can/gateway/config", params={"all_options": all_options})

    def update_can_gateway_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified CAN gateway configurations."""
        return self._client.request("PUT", "/can/gateway/config", json={"data": config})

    def get_can_gateway_config_by_id(self, gateway_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified CAN gateway configuration."""
        return self._client.request("GET", f"/can/gateway/config/{gateway_id}", params={"all_options": all_options})

    def upload_can_gateway_config_by_id(
        self, gateway_id: str, file: File, *, option: str | None = None
    ) -> dict[str, Any]:
        """Uploads the specified CAN gateway configuration certificate files."""
        return self._client.request(
            "POST", f"/can/gateway/config/{gateway_id}", files={"file": file}, form={"option": option}
        )

    def update_can_gateway_config_by_id(self, gateway_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified CAN gateway configuration."""
        return self._client.request("PUT", f"/can/gateway/config/{gateway_id}", json={"data": config})

    def get_can_gateway_status(self) -> dict[str, Any]:
        """Returns CAN gateway status."""
        return self._client.request("GET", "/can/gateway/status")
