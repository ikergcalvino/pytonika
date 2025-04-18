from typing import Any, Dict, List, Optional, Tuple, Union


class Firmware:
    def __init__(self, api_client):
        self._api_client = api_client

    def get_firmware_device_status(self) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/firmware/device/status"

        return self._api_client.get(endpoint)

    def get_firmware_device_progress_status(self) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/firmware/device/progress/status"

        return self._api_client.get(endpoint)

    def get_firmware_device_updates_status(self) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/firmware/device/updates/status"

        return self._api_client.get(endpoint)

    def firmware_actions_fota_download(self) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/firmware/actions/fota_download"

        return self._api_client.post(endpoint)

    def firmware_actions_upgrade(self, data: Dict[str, Any]) -> Tuple[bool, Union[Dict[str, Any], List[Dict[str, Any]]]]:
        endpoint = "/firmware/actions/upgrade"

        return self._api_client.post(endpoint, data=data)
