from typing import Any

from ._base import Endpoint


class Dot1X(Endpoint):
    def get_dot1x_radius_config(self) -> dict[str, Any]:
        """Get all radius client configurations."""
        endpoint = "/dot1x/radius/config/"

        return self._api_client.get(endpoint)

    def create_dot1x_radius_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Create a radius client configuration."""
        endpoint = "/dot1x/radius/config/"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_dot1x_radius_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Edit multiple radius client configurations."""
        endpoint = "/dot1x/radius/config/"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dot1x_radius_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Delete multiple radius client configurations."""
        return [self.delete_dot1x_radius_config_by_id(config_id) for config_id in config]

    def get_dot1x_radius_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Get a single radius client configuration."""
        endpoint = f"/dot1x/radius/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_dot1x_radius_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Edit a single radius client configuration."""
        endpoint = f"/dot1x/radius/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_dot1x_radius_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Delete a single radius client configuration."""
        endpoint = f"/dot1x/radius/config/{config_id}"

        return self._api_client.delete(endpoint)

    def dot1x_radius_actions_test(self, data: dict[str, Any]) -> dict[str, Any]:
        """Send an auth request to a RADIUS server."""
        endpoint = "/dot1x/radius/actions/test"

        return self._api_client.post(endpoint, data={"data": data})

    def get_dot1x_ports_config(self) -> dict[str, Any]:
        """Get all 802.1X port configurations."""
        endpoint = "/dot1x/ports/config"

        return self._api_client.get(endpoint)

    def update_dot1x_ports_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Edit multiple 802.1X port configurations."""
        endpoint = "/dot1x/ports/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_dot1x_ports_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Get a single 802.1X port configuration."""
        endpoint = f"/dot1x/ports/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_dot1x_ports_config_by_id(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Upload 802.1X client certificates."""
        endpoint = f"/dot1x/ports/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_dot1x_ports_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update a single 802.1X port configuration."""
        endpoint = f"/dot1x/ports/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_dot1x_ports_status(self) -> dict[str, Any]:
        """Get all 802.1X port statuses."""
        endpoint = "/dot1x/ports/status"

        return self._api_client.get(endpoint)

    def get_dot1x_ports_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Get single 802.1X port status."""
        endpoint = f"/dot1x/ports/status/{status_id}"

        return self._api_client.get(endpoint)

    def get_dot1x_client_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Get a single 802.1X client configuration. (DEPRECATED)"""
        endpoint = f"/dot1x/client/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_dot1x_client_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update a single 802.1X client configuration. (DEPRECATED)"""
        endpoint = f"/dot1x/client/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_dot1x_client_config(self) -> dict[str, Any]:
        """Get all 802.1X client configurations. (DEPRECATED)"""
        endpoint = "/dot1x/client/config"

        return self._api_client.get(endpoint)

    def update_dot1x_client_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Edit multiple 802.1X client configurations. (DEPRECATED)"""
        endpoint = "/dot1x/client/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
