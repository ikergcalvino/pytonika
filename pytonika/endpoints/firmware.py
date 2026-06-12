from typing import Any

from ._base import Endpoint


class Firmware(Endpoint):
    def get_firmware_device_status(self) -> dict[str, Any]:
        """Returns current firmware information."""
        endpoint = "/firmware/device/status"

        return self._api_client.get(endpoint)

    def get_firmware_device_progress_status(self) -> dict[str, Any]:
        """Returns firmware download status from Fota."""
        endpoint = "/firmware/device/progress/status"

        return self._api_client.get(endpoint)

    def upload_firmware_device(self, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads firmware file."""
        endpoint = "/firmware/actions/upload_device_firmware"

        return self._api_client.post(endpoint, data={"data": data})

    def delete_firmware_device(self) -> dict[str, Any]:
        """Deletes uploaded firmware file."""
        endpoint = "/firmware/actions/delete_device_firmware"

        return self._api_client.post(endpoint)

    def get_firmware_device_updates_status(self) -> dict[str, Any]:
        """Returns firmware update information from Fota."""
        endpoint = "/firmware/device/updates/status"

        return self._api_client.get(endpoint)

    def firmware_actions_fota_download(self) -> dict[str, Any]:
        """Starts firmware download from Fota."""
        endpoint = "/firmware/actions/fota_download"

        return self._api_client.post(endpoint)

    def firmware_actions_fota_cancel(self) -> dict[str, Any]:
        """Cancels firmware download from Fota."""
        endpoint = "/firmware/actions/fota_cancel"

        return self._api_client.post(endpoint)

    def firmware_actions_verify(self) -> dict[str, Any]:
        """Verifies uploaded firmware file."""
        endpoint = "/firmware/actions/verify"

        return self._api_client.post(endpoint)

    def firmware_actions_upgrade(self, config: dict[str, Any]) -> dict[str, Any]:
        """Starts firmware upgrade."""
        endpoint = "/firmware/actions/upgrade"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def firmware_actions_factory_reset(self) -> dict[str, Any]:
        """Deprecated. Factory resets device configuration."""
        endpoint = "/firmware/actions/factory_reset"

        return self._api_client.post(endpoint)

    def get_firmware_modem_status(self) -> dict[str, Any]:
        """Returns current modem firmware information."""
        endpoint = "/firmware/modem/status"

        return self._api_client.get(endpoint)

    def get_firmware_modem_progress_status(self) -> dict[str, Any]:
        """Returns modem firmware download status from Fota."""
        endpoint = "/firmware/modem/progress/status"

        return self._api_client.get(endpoint)

    def upload_firmware_modem(self, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads modem firmware file."""
        endpoint = "/firmware/actions/upload_modem_firmware"

        return self._api_client.post(endpoint, data={"data": data})

    def delete_firmware_modem(self) -> dict[str, Any]:
        """Deletes uploaded modem firmware file."""
        endpoint = "/firmware/actions/delete_modem_firmware"

        return self._api_client.post(endpoint)

    def get_firmware_modem_updates_status(self) -> dict[str, Any]:
        """Returns modem firmware update information from Fota."""
        endpoint = "/firmware/modem/updates/status"

        return self._api_client.get(endpoint)

    def firmware_actions_fota_download_modem(self) -> dict[str, Any]:
        """Starts modem firmware download from Fota."""
        endpoint = "/firmware/actions/fota_download_modem"

        return self._api_client.post(endpoint)

    def firmware_actions_verify_modem(self) -> dict[str, Any]:
        """Verifies uploaded modem firmware file."""
        endpoint = "/firmware/actions/verify_modem"

        return self._api_client.post(endpoint)

    def firmware_actions_upgrade_modem(self) -> dict[str, Any]:
        """Starts modem firmware upgrade."""
        endpoint = "/firmware/actions/upgrade_modem"

        return self._api_client.post(endpoint)
