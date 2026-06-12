from typing import Any

from ._base import Endpoint


class eSIM(Endpoint):
    def get_esim_status(self) -> dict[str, Any]:
        """Returns multiple eSIM statuses."""
        endpoint = "/esim/status"

        return self._api_client.get(endpoint)

    def get_esim_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns specified eSIM status."""
        endpoint = f"/esim/status/{status_id}"

        return self._api_client.get(endpoint)

    def get_esim_config(self) -> dict[str, Any]:
        """Returns multiple eSIM configurations."""
        endpoint = "/esim/config"

        return self._api_client.get(endpoint)

    def update_esim_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates multiple eSIM configurations."""
        endpoint = "/esim/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_esim_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes multiple eSIM configurations."""
        return [self.delete_esim_config_by_id(config_id) for config_id in config]

    def get_esim_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns specified eSIM configuration."""
        endpoint = f"/esim/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_esim_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified eSIM configuration."""
        endpoint = f"/esim/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_esim_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes specified eSIM configuration."""
        endpoint = f"/esim/config/{config_id}"

        return self._api_client.delete(endpoint)

    def esim_actions_download(self, data: dict[str, Any]) -> dict[str, Any]:
        """Downloads eSIM profile."""
        endpoint = "/esim/actions/download"

        return self._api_client.post(endpoint, data={"data": data})

    def esim_actions_process_notifications(self, data: dict[str, Any]) -> dict[str, Any]:
        """Processes pending eSIM notifications."""
        endpoint = "/esim/actions/process_notifications"

        return self._api_client.post(endpoint, data={"data": data})

    def esim_actions_clear_errors(self, data: dict[str, Any]) -> dict[str, Any]:
        """Clear eSIM errors."""
        endpoint = "/esim/actions/clear_errors"

        return self._api_client.post(endpoint, data={"data": data})
