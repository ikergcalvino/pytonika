from typing import Any

from ._base import Endpoint


class AzureIoTHub(Endpoint):
    def get_azure_iot_hub_config_deprecated(self) -> dict[str, Any]:
        """Returns Azure IoT Hub configuration in an array. DEPRECATED."""
        endpoint = "/azure_iot_hub/config"

        return self._api_client.get(endpoint)

    def create_azure_iot_hub_config_deprecated(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Azure IoT Hub configuration in an array. DEPRECATED."""
        endpoint = "/azure_iot_hub/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_azure_iot_hub_config_deprecated(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Azure IoT Hub configuration in an array. DEPRECATED."""
        endpoint = "/azure_iot_hub/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_azure_iot_hub_config_deprecated(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected Azure IoT Hub configurations. DEPRECATED."""
        return [self.delete_azure_iot_hub_config_by_id_deprecated(hub_id) for hub_id in config]

    def get_azure_iot_hub_config_by_id_deprecated(self, config_id: str) -> dict[str, Any]:
        """Returns Azure IoT Hub configuration. DEPRECATED."""
        endpoint = f"/azure_iot_hub/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_azure_iot_hub_config_by_id_deprecated(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Azure IoT Hub configuration. DEPRECATED."""
        endpoint = f"/azure_iot_hub/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_azure_iot_hub_config_by_id_deprecated(self, config_id: str) -> dict[str, Any]:
        """Deletes the selected Azure IoT Hub configurations. DEPRECATED."""
        endpoint = f"/azure_iot_hub/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_azure_iot_hub_config(self) -> dict[str, Any]:
        """Returns all Azure IoT Hub section configurations."""
        endpoint = "/azure/iot_hub/config"

        return self._api_client.get(endpoint)

    def create_azure_iot_hub_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Created Azure IoT Hub configuration."""
        endpoint = "/azure/iot_hub/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_azure_iot_hub_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Azure IoT Hub configuration."""
        endpoint = "/azure/iot_hub/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_azure_iot_hub_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes Azure IoT Hub configurations."""
        return [self.delete_azure_iot_hub_config_by_id(hub_id) for hub_id in config]

    def get_azure_iot_hub_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Azure IoT Hub configuration."""
        endpoint = f"/azure/iot_hub/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_azure_iot_hub_files(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads Azure IoT Hub files."""
        endpoint = f"/azure/iot_hub/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_azure_iot_hub_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Azure IoT Hub configuration."""
        endpoint = f"/azure/iot_hub/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_azure_iot_hub_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes Azure IoT Hub configuration."""
        endpoint = f"/azure/iot_hub/config/{config_id}"

        return self._api_client.delete(endpoint)

    def azure_iot_hub_merge(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Merge the Azure IoT Hub configurations used in the Data to Server configuration.

        Uses the currently provided section ID and the data presented.
        """
        endpoint = f"/azure/iot_hub/actions/merge/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def get_azure_iot_hub_status(self) -> dict[str, Any]:
        """Returns all Azure IoT Hub section configurations."""
        endpoint = "/azure/iot_hub/status"

        return self._api_client.get(endpoint)

    def get_azure_iot_hub_status_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns all Azure IoT Hub section configurations."""
        endpoint = f"/azure/iot_hub/status/{config_id}"

        return self._api_client.get(endpoint)
