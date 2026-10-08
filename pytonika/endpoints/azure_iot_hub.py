from typing import Any, Literal

from ._endpoint import Endpoint, File


class AzureIoTHub(Endpoint):
    def azure_iot_hub_actions_merge(self, config_id: str, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Merge the Azure IoT Hub configurations that were used in the Data to Server configuration with the
        currently provided section ID and the data presented.
        """
        return self._client.request(
            "POST", f"/azure/iot_hub/actions/merge/{config_id}", json=None if data is None else {"data": data}
        )

    def get_azure_iot_hub_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Azure IoT Hub section configurations."""
        return self._client.request("GET", "/azure/iot_hub/config", params={"all_options": all_options})

    def create_azure_iot_hub_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Created Azure IoT Hub configuration."""
        return self._client.request("POST", "/azure/iot_hub/config", json={"data": config})

    def update_azure_iot_hub_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Azure IoT Hub configuration."""
        return self._client.request("PUT", "/azure/iot_hub/config", json={"data": config})

    def delete_azure_iot_hub_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes Azure IoT Hub configurations."""
        return self._client.request("DELETE", "/azure/iot_hub/config", json={"data": config})

    def get_azure_iot_hub_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Azure IoT Hub configuration."""
        return self._client.request("GET", f"/azure/iot_hub/config/{config_id}", params={"all_options": all_options})

    def upload_azure_iot_hub_config_by_id(
        self, config_id: str, file: File, *, option: Literal["x509certificate", "x509privatekey"] | None = None
    ) -> dict[str, Any]:
        """Uploads Azure IoT Hub files."""
        return self._client.request(
            "POST", f"/azure/iot_hub/config/{config_id}", files={"file": file}, form={"option": option}
        )

    def update_azure_iot_hub_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Azure IoT Hub configuration."""
        return self._client.request("PUT", f"/azure/iot_hub/config/{config_id}", json={"data": config})

    def delete_azure_iot_hub_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes Azure IoT Hub configuration."""
        return self._client.request("DELETE", f"/azure/iot_hub/config/{config_id}")

    def get_azure_iot_hub_status(self) -> dict[str, Any]:
        """Returns all Azure IoT Hub section configurations."""
        return self._client.request("GET", "/azure/iot_hub/status")

    def get_azure_iot_hub_status_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns all Azure IoT Hub section configurations."""
        return self._client.request("GET", f"/azure/iot_hub/status/{config_id}")

    def get_azure_iot_hub_config_deprecated(self) -> dict[str, Any]:
        """Returns Azure IoT Hub configuration in an array."""
        return self._client.request("GET", "/azure_iot_hub/config")

    def create_azure_iot_hub_config_deprecated(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Azure IoT Hub configuration in an array."""
        return self._client.request("POST", "/azure_iot_hub/config", json={"data": config})

    def update_azure_iot_hub_config_deprecated(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Azure IoT Hub configuration in an array."""
        return self._client.request("PUT", "/azure_iot_hub/config", json={"data": config})

    def delete_azure_iot_hub_config_deprecated(self, config: list[str]) -> dict[str, Any]:
        """Deletes the selected Azure IoT Hub configurations."""
        return self._client.request("DELETE", "/azure_iot_hub/config", json={"data": config})

    def get_azure_iot_hub_config_by_id_deprecated(self, config_id: str) -> dict[str, Any]:
        """Returns Azure IoT Hub configuration."""
        return self._client.request("GET", f"/azure_iot_hub/config/{config_id}")

    def update_azure_iot_hub_config_by_id_deprecated(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Azure IoT Hub configuration."""
        return self._client.request("PUT", f"/azure_iot_hub/config/{config_id}", json={"data": config})

    def delete_azure_iot_hub_config_by_id_deprecated(self, config_id: str) -> dict[str, Any]:
        """Deletes the selected Azure IoT Hub configurations."""
        return self._client.request("DELETE", f"/azure_iot_hub/config/{config_id}")
