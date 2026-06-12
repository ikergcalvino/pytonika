from typing import Any

from ._base import Endpoint


class Backup(Endpoint):
    def get_backup_status(self) -> dict[str, Any]:
        """Returns informations about created backup, default configuration."""
        endpoint = "/backup/status"

        return self._api_client.get(endpoint)

    def backup_actions_create_default(self) -> dict[str, Any]:
        """Creates default configuration."""
        endpoint = "/backup/actions/create_default"

        return self._api_client.post(endpoint)

    def backup_actions_remove_default(self) -> dict[str, Any]:
        """Removes default configuration."""
        endpoint = "/backup/actions/remove_default"

        return self._api_client.post(endpoint)

    def backup_actions_generate(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Generates backup configuration to download."""
        endpoint = "/backup/actions/generate"

        if data:
            return self._api_client.post(endpoint, data={"data": data})

        return self._api_client.post(endpoint)

    def backup_actions_download(self) -> dict[str, Any]:
        """Downloads generated backup file."""
        endpoint = "/backup/actions/download"

        return self._api_client.post(endpoint)

    def backup_actions_upload(self, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads backup into device to apply."""
        endpoint = "/backup/actions/upload"

        return self._api_client.post(endpoint, data={"data": data})

    def backup_actions_delete(self) -> dict[str, Any]:
        """Removes backup file from device."""
        endpoint = "/backup/actions/delete"

        return self._api_client.post(endpoint)

    def backup_actions_apply(self) -> dict[str, Any]:
        """Applies backup from backup file."""
        endpoint = "/backup/actions/apply"

        return self._api_client.post(endpoint)

    def backup_actions_reset_settings(self) -> dict[str, Any]:
        """Resets device configuration."""
        endpoint = "/backup/actions/reset_settings"

        return self._api_client.post(endpoint)
