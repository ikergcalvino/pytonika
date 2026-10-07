from typing import Any

from ._endpoint import Endpoint, File


class Dot1X(Endpoint):
    def get_dot1x_client_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get all 802.1X client configurations."""
        return self._client.request("GET", "/dot1x/client/config", params={"all_options": all_options})

    def update_dot1x_client_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Edit multiple 802.1X client configurations."""
        return self._client.request("PUT", "/dot1x/client/config", json={"data": config})

    def get_dot1x_client_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get a single 802.1X client configuration."""
        return self._client.request("GET", f"/dot1x/client/config/{config_id}", params={"all_options": all_options})

    def update_dot1x_client_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update a single 802.1X client configuration."""
        return self._client.request("PUT", f"/dot1x/client/config/{config_id}", json={"data": config})

    def get_dot1x_ports_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get all 802.1X port configurations."""
        return self._client.request("GET", "/dot1x/ports/config", params={"all_options": all_options})

    def update_dot1x_ports_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Edit multiple 802.1X port configurations."""
        return self._client.request("PUT", "/dot1x/ports/config", json={"data": config})

    def get_dot1x_ports_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get a single 802.1X port configuration."""
        return self._client.request("GET", f"/dot1x/ports/config/{config_id}", params={"all_options": all_options})

    def upload_dot1x_ports_config_by_id(
        self, config_id: str, file: File, *, option: str | None = None
    ) -> dict[str, Any]:
        """Upload 802.1X client certificates."""
        return self._client.request(
            "POST", f"/dot1x/ports/config/{config_id}", files={"file": file}, form={"option": option}
        )

    def update_dot1x_ports_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update a single 802.1X port configuration."""
        return self._client.request("PUT", f"/dot1x/ports/config/{config_id}", json={"data": config})

    def get_dot1x_ports_status(self) -> dict[str, Any]:
        """Get all 802.1X port statuses."""
        return self._client.request("GET", "/dot1x/ports/status")

    def get_dot1x_ports_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Get single 802.1X port status."""
        return self._client.request("GET", f"/dot1x/ports/status/{status_id}")

    def dot1x_radius_actions_test(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """send an auth request to a RADIUS server."""
        return self._client.request("POST", "/dot1x/radius/actions/test", json=None if data is None else {"data": data})

    def get_dot1x_radius_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get all radius client configurations."""
        return self._client.request("GET", "/dot1x/radius/config", params={"all_options": all_options})

    def create_dot1x_radius_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create a radius client configuration."""
        return self._client.request("POST", "/dot1x/radius/config", json={"data": config})

    def update_dot1x_radius_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Edit multiple radius client configurations."""
        return self._client.request("PUT", "/dot1x/radius/config", json={"data": config})

    def delete_dot1x_radius_config(self, config: list[str]) -> dict[str, Any]:
        """Delete multiple radius client configurations."""
        return self._client.request("DELETE", "/dot1x/radius/config", json={"data": config})

    def get_dot1x_radius_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Get a single radius client configuration."""
        return self._client.request("GET", f"/dot1x/radius/config/{config_id}", params={"all_options": all_options})

    def update_dot1x_radius_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Edit a single radius client configuration."""
        return self._client.request("PUT", f"/dot1x/radius/config/{config_id}", json={"data": config})

    def delete_dot1x_radius_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete a single radius client configuration."""
        return self._client.request("DELETE", f"/dot1x/radius/config/{config_id}")
