from typing import Any

from ._base import Endpoint


class AWS(Endpoint):
    def get_aws_jobs_config(self) -> dict[str, Any]:
        """Returns all AWS IoT Core job configurations."""
        endpoint = "/aws/jobs/config"

        return self._api_client.get(endpoint)

    def create_aws_jobs_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new AWS IoT Core job configuration."""
        endpoint = "/aws/jobs/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_aws_jobs_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected AWS IoT Core job configurations."""
        endpoint = "/aws/jobs/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_aws_jobs_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected AWS IoT Core job configurations."""
        return [self.delete_aws_jobs_config_by_id(config_id) for config_id in config]

    def get_aws_jobs_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the selected AWS IoT Core job configuration."""
        endpoint = f"/aws/jobs/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_aws_jobs_config_by_id(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads AWS IoT Core job files."""
        endpoint = f"/aws/jobs/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_aws_jobs_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected AWS IoT Core job configuration."""
        endpoint = f"/aws/jobs/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_aws_jobs_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the selected AWS IoT Core job configuration."""
        endpoint = f"/aws/jobs/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_aws_jobs_status(self) -> dict[str, Any]:
        """Returns the status of AWS IoT Core jobs."""
        endpoint = "/aws/jobs/status"

        return self._api_client.get(endpoint)

    def get_aws_provisioning_config(self) -> dict[str, Any]:
        """Returns all AWS IoT Core provisioning configurations."""
        endpoint = "/aws/provisioning/config"

        return self._api_client.get(endpoint)

    def create_aws_provisioning_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new AWS IoT Core provisioning configuration."""
        endpoint = "/aws/provisioning/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_aws_provisioning_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected AWS IoT Core provisioning configurations."""
        endpoint = "/aws/provisioning/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_aws_provisioning_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected AWS IoT Core provisioning configurations."""
        return [self.delete_aws_provisioning_config_by_id(config_id) for config_id in config]

    def get_aws_provisioning_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the selected AWS IoT Core provisioning configuration."""
        endpoint = f"/aws/provisioning/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_aws_provisioning_config_by_id(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads AWS IoT Core provisioning files."""
        endpoint = f"/aws/provisioning/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_aws_provisioning_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected AWS IoT Core provisioning configuration."""
        endpoint = f"/aws/provisioning/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_aws_provisioning_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the selected AWS IoT Core provisioning configuration."""
        endpoint = f"/aws/provisioning/config/{config_id}"

        return self._api_client.delete(endpoint)
