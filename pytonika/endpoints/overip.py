from typing import Any

from ._base import Endpoint


class OverIP(Endpoint):
    def get_overip_filters_config(self, overip_id: str) -> dict[str, Any]:
        """Returns all OverIP IP Filter rules."""
        endpoint = f"/overip/{overip_id}/filters/config"

        return self._api_client.get(endpoint)

    def create_overip_filters_config(self, overip_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Creates OverIP IP Filter rule."""
        endpoint = f"/overip/{overip_id}/filters/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_overip_filters_config(self, overip_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OverIP IP Filter rules."""
        endpoint = f"/overip/{overip_id}/filters/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_overip_filters_config(self, overip_id: str, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified OverIP IP Filter rules."""
        return [self.delete_overip_filters_config_by_id(overip_id, filter_id) for filter_id in config]

    def get_overip_filters_config_by_id(self, overip_id: str, filter_id: str) -> dict[str, Any]:
        """Returns the specified OverIP IP Filter rule."""
        endpoint = f"/overip/{overip_id}/filters/config/{filter_id}"

        return self._api_client.get(endpoint)

    def update_overip_filters_config_by_id(
        self, overip_id: str, filter_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the specified OverIP IP Filter rule."""
        endpoint = f"/overip/{overip_id}/filters/config/{filter_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_overip_filters_config_by_id(self, overip_id: str, filter_id: str) -> dict[str, Any]:
        """Deletes the specified OverIP IP Filter rule."""
        endpoint = f"/overip/{overip_id}/filters/config/{filter_id}"

        return self._api_client.delete(endpoint)

    def get_overip_config(self) -> dict[str, Any]:
        """Returns all OverIP configurations."""
        endpoint = "/overip/config"

        return self._api_client.get(endpoint)

    def create_overip_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates OverIP configuration."""
        endpoint = "/overip/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_overip_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified OverIP configurations."""
        endpoint = "/overip/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_overip_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified OverIP configurations."""
        return [self.delete_overip_config_by_id(config_id) for config_id in config]

    def get_overip_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified OverIP configuration."""
        endpoint = f"/overip/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_overip_config_by_id(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads the specified OverIP configuration certificate files."""
        endpoint = f"/overip/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_overip_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified OverIP configuration."""
        endpoint = f"/overip/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_overip_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified OverIP configuration."""
        endpoint = f"/overip/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_overip_status(self) -> dict[str, Any]:
        """Returns OverIP status."""
        endpoint = "/overip/status"

        return self._api_client.get(endpoint)
