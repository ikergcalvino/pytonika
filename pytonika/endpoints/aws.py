from typing import Any

from ._endpoint import Endpoint, File


class AWS(Endpoint):
    def get_aws_jobs_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all AWS IoT Core job configurations."""
        return self._client.request("GET", "/aws/jobs/config", params={"all_options": all_options})

    def create_aws_jobs_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new AWS IoT Core job configuration."""
        return self._client.request("POST", "/aws/jobs/config", json={"data": config})

    def update_aws_jobs_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected AWS IoT Core job configurations."""
        return self._client.request("PUT", "/aws/jobs/config", json={"data": config})

    def delete_aws_jobs_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the selected AWS IoT Core job configurations."""
        return self._client.request("DELETE", "/aws/jobs/config", json={"data": config})

    def get_aws_jobs_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the selected AWS IoT Core job configuration."""
        return self._client.request("GET", f"/aws/jobs/config/{config_id}", params={"all_options": all_options})

    def upload_aws_jobs_config_by_id(self, config_id: str, file: File, *, option: str | None = None) -> dict[str, Any]:
        """Uploads AWS IoT Core job files."""
        return self._client.request(
            "POST", f"/aws/jobs/config/{config_id}", files={"file": file}, form={"option": option}
        )

    def update_aws_jobs_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected AWS IoT Core job configuration."""
        return self._client.request("PUT", f"/aws/jobs/config/{config_id}", json={"data": config})

    def delete_aws_jobs_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the selected AWS IoT Core job configuration."""
        return self._client.request("DELETE", f"/aws/jobs/config/{config_id}")

    def get_aws_jobs_status(self) -> dict[str, Any]:
        """Returns the status of AWS IoT Core jobs."""
        return self._client.request("GET", "/aws/jobs/status")

    def get_aws_provisioning_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all AWS IoT Core provisioning configurations."""
        return self._client.request("GET", "/aws/provisioning/config", params={"all_options": all_options})

    def create_aws_provisioning_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new AWS IoT Core provisioning configuration."""
        return self._client.request("POST", "/aws/provisioning/config", json={"data": config})

    def update_aws_provisioning_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected AWS IoT Core provisioning configurations."""
        return self._client.request("PUT", "/aws/provisioning/config", json={"data": config})

    def delete_aws_provisioning_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the selected AWS IoT Core provisioning configurations."""
        return self._client.request("DELETE", "/aws/provisioning/config", json={"data": config})

    def get_aws_provisioning_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the selected AWS IoT Core provisioning configuration."""
        return self._client.request("GET", f"/aws/provisioning/config/{config_id}", params={"all_options": all_options})

    def upload_aws_provisioning_config_by_id(
        self, config_id: str, file: File, *, option: str | None = None
    ) -> dict[str, Any]:
        """Uploads AWS IoT Core provisioning files."""
        return self._client.request(
            "POST", f"/aws/provisioning/config/{config_id}", files={"file": file}, form={"option": option}
        )

    def update_aws_provisioning_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected AWS IoT Core provisioning configuration."""
        return self._client.request("PUT", f"/aws/provisioning/config/{config_id}", json={"data": config})

    def delete_aws_provisioning_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the selected AWS IoT Core provisioning configuration."""
        return self._client.request("DELETE", f"/aws/provisioning/config/{config_id}")
