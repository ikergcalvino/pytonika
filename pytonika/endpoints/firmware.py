from .._client import APIClient


class Firmware:
    def __init__(self, api_client: APIClient) -> None:
        self._api_client = api_client

    def get_firmware_device_status(self) -> dict[str, object]:
        endpoint = "/firmware/device/status"

        return self._api_client.get(endpoint)

    def get_firmware_device_progress_status(self) -> dict[str, object]:
        endpoint = "/firmware/device/progress/status"

        return self._api_client.get(endpoint)

    def get_firmware_device_updates_status(self) -> dict[str, object]:
        endpoint = "/firmware/device/updates/status"

        return self._api_client.get(endpoint)

    def firmware_actions_fota_download(self) -> dict[str, object]:
        endpoint = "/firmware/actions/fota_download"

        return self._api_client.post(endpoint)

    def firmware_actions_upgrade(self, config: dict[str, object]) -> dict[str, object]:
        endpoint = "/firmware/actions/upgrade"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)
