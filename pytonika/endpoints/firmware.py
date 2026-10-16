from typing import Any

from ._endpoint import Endpoint, File


class Firmware(Endpoint):
    def firmware_actions_delete_device_firmware(self) -> dict[str, Any]:
        """Deletes uploaded firmware file."""
        return self._client.request("POST", "/firmware/actions/delete_device_firmware")

    def firmware_actions_delete_modem_firmware(self) -> dict[str, Any]:
        """Deletes uploaded modem firmware file."""
        return self._client.request("POST", "/firmware/actions/delete_modem_firmware")

    def firmware_actions_factory_reset(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Factory resets device configuration."""
        return self._client.request(
            "POST", "/firmware/actions/factory_reset", json=None if data is None else {"data": data}
        )

    def firmware_actions_fota_cancel(self) -> dict[str, Any]:
        """Cancels firmware download from Fota."""
        return self._client.request("POST", "/firmware/actions/fota_cancel")

    def firmware_actions_fota_download(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Starts firmware download from Fota."""
        return self._client.request(
            "POST", "/firmware/actions/fota_download", json=None if data is None else {"data": data}
        )

    def firmware_actions_fota_download_modem(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Starts modem firmware download from Fota."""
        return self._client.request(
            "POST", "/firmware/actions/fota_download_modem", json=None if data is None else {"data": data}
        )

    def firmware_actions_upgrade(self, config: dict[str, Any] | None = None) -> dict[str, Any]:
        """Starts firmware upgrade."""
        return self._client.request(
            "POST", "/firmware/actions/upgrade", json=None if config is None else {"data": config}
        )

    def firmware_actions_upgrade_modem(self) -> dict[str, Any]:
        """Starts modem firmware upgrade."""
        return self._client.request("POST", "/firmware/actions/upgrade_modem")

    def firmware_actions_upload_device_firmware(
        self,
        file: File,
        *,
        suppress_validation: str | None = None,
        force_upgrade: str | None = None,
        keep_settings: str | None = None,
    ) -> dict[str, Any]:
        """Uploads firmware file."""
        return self._client.request(
            "POST",
            "/firmware/actions/upload_device_firmware",
            files={"file": file},
            form={
                "suppress_validation": suppress_validation,
                "force_upgrade": force_upgrade,
                "keep_settings": keep_settings,
            },
        )

    def firmware_actions_upload_modem_firmware(self, file: File, *, force_upgrade: str | None = None) -> dict[str, Any]:
        """Uploads modem firmware file."""
        return self._client.request(
            "POST",
            "/firmware/actions/upload_modem_firmware",
            files={"file": file},
            form={"force_upgrade": force_upgrade},
        )

    def firmware_actions_verify(self) -> dict[str, Any]:
        """Verifies uploaded firmware file."""
        return self._client.request("POST", "/firmware/actions/verify")

    def firmware_actions_verify_modem(self) -> dict[str, Any]:
        """Verifies uploaded modem firmware file."""
        return self._client.request("POST", "/firmware/actions/verify_modem")

    def get_firmware_device_progress_status(self) -> dict[str, Any]:
        """Returns firmware download status from Fota."""
        return self._client.request("GET", "/firmware/device/progress/status")

    def get_firmware_device_status(self) -> dict[str, Any]:
        """Returns current firmware information."""
        return self._client.request("GET", "/firmware/device/status")

    def get_firmware_device_updates_status(self) -> dict[str, Any]:
        """Returns firmware update information from Fota."""
        return self._client.request("GET", "/firmware/device/updates/status")

    def get_firmware_modem_progress_status(self) -> dict[str, Any]:
        """Returns modem firmware download status from Fota."""
        return self._client.request("GET", "/firmware/modem/progress/status")

    def get_firmware_modem_status(self) -> dict[str, Any]:
        """Returns current modem firmware information."""
        return self._client.request("GET", "/firmware/modem/status")

    def get_firmware_modem_updates_status(self) -> dict[str, Any]:
        """Returns modem firmware update information from Fota."""
        return self._client.request("GET", "/firmware/modem/updates/status")
