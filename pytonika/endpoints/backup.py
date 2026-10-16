from typing import Any, Literal

from ._endpoint import Endpoint, File


class Backup(Endpoint):
    def backup_actions_apply(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Applies backup from backup file."""
        return self._client.request("POST", "/backup/actions/apply", json=None if data is None else {"data": data})

    def backup_actions_clear_errors(self) -> dict[str, Any]:
        """Returns and clears errors from last backup apply."""
        return self._client.request("POST", "/backup/actions/clear_errors")

    def backup_actions_create_default(self) -> dict[str, Any]:
        """Creates default configuration."""
        return self._client.request("POST", "/backup/actions/create_default")

    def backup_actions_delete(self) -> dict[str, Any]:
        """Removes backup file from device."""
        return self._client.request("POST", "/backup/actions/delete")

    def backup_actions_download(self) -> bytes | dict[str, Any]:
        """Downloads generated backup file."""
        return self._client.request("POST", "/backup/actions/download", download=True)

    def backup_actions_generate(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Generates backup configuration to download."""
        return self._client.request("POST", "/backup/actions/generate", json=None if data is None else {"data": data})

    def backup_actions_remove_default(self) -> dict[str, Any]:
        """Removes default configuration."""
        return self._client.request("POST", "/backup/actions/remove_default")

    def backup_actions_reset_settings(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Resets device configuration."""
        return self._client.request(
            "POST", "/backup/actions/reset_settings", json=None if data is None else {"data": data}
        )

    def backup_actions_upload(
        self, file: File, *, encrypt: Literal["0", "1"] | None = None, password: str | None = None
    ) -> dict[str, Any]:
        """Uploads backup into device to apply."""
        return self._client.request(
            "POST", "/backup/actions/upload", files={"file": file}, form={"encrypt": encrypt, "password": password}
        )

    def backup_actions_validate(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Validates uploaded backup file."""
        return self._client.request("POST", "/backup/actions/validate", json=None if data is None else {"data": data})

    def get_backup_errors_status(self) -> dict[str, Any]:
        """Returns informations about collected errors from last backup apply."""
        return self._client.request("GET", "/backup/errors/status")

    def get_backup_pkg_errors_status(self) -> dict[str, Any]:
        """Returns informations about collected errors from last backup apply after installing packages."""
        return self._client.request("GET", "/backup/pkg_errors/status")

    def get_backup_status(self) -> dict[str, Any]:
        """Returns informations about created backup, default configuration."""
        return self._client.request("GET", "/backup/status")
