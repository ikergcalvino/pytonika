from typing import Any, Literal

from ._endpoint import Endpoint, File


class GreengrassV2(Endpoint):
    def get_greengrass_config(self) -> dict[str, Any]:
        """Get Greengrass V2 configuration."""
        return self._client.request("GET", "/greengrass/config")

    def update_greengrass_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Update Greengrass V2 configuration."""
        return self._client.request("PUT", "/greengrass/config", json={"data": config})

    def get_greengrass_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Get Greengrass V2 configuration section."""
        return self._client.request("GET", f"/greengrass/config/{config_id}")

    def upload_greengrass_config_by_id(
        self,
        config_id: str,
        file: File,
        *,
        option: Literal["aws_config", "certificate_file_path", "config_file_path", "private_key_path", "root_ca_path"]
        | None = None,
    ) -> dict[str, Any]:
        """Upload Greengrass V2 configuration file."""
        return self._client.request(
            "POST", f"/greengrass/config/{config_id}", files={"file": file}, form={"option": option}
        )

    def update_greengrass_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update Greengrass V2 configuration section."""
        return self._client.request("PUT", f"/greengrass/config/{config_id}", json={"data": config})

    def get_greengrass_effective_config(self) -> dict[str, Any]:
        """Read the effective Greengrass V2 configuration."""
        return self._client.request("GET", "/greengrass/effective_config")

    def get_greengrass_logging_config(self) -> dict[str, Any]:
        """Get Greengrass V2 logging configuration."""
        return self._client.request("GET", "/greengrass/logging/config")

    def update_greengrass_logging_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Update Greengrass V2 logging configuration."""
        return self._client.request("PUT", "/greengrass/logging/config", json={"data": config})

    def get_greengrass_logging_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Get Greengrass V2 logging configuration section."""
        return self._client.request("GET", f"/greengrass/logging/config/{config_id}")

    def update_greengrass_logging_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update Greengrass V2 logging configuration section."""
        return self._client.request("PUT", f"/greengrass/logging/config/{config_id}", json={"data": config})

    def get_greengrass_logs(self) -> dict[str, Any]:
        """List Greengrass V2 log files."""
        return self._client.request("GET", "/greengrass/logs")

    def get_greengrass_logs_by_filename(self, filename: str) -> dict[str, Any]:
        """Read Greengrass V2 log file."""
        return self._client.request("GET", f"/greengrass/logs/{filename}")

    def get_greengrass_status(self) -> dict[str, Any]:
        """Read the Greengrass V2 status."""
        return self._client.request("GET", "/greengrass/status")
