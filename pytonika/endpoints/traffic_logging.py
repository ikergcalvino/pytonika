from typing import Any

from ._endpoint import Endpoint, File


class TrafficLogging(Endpoint):
    def get_ulog_available_interfaces_options(self) -> dict[str, Any]:
        """Returns Traffic Logging options."""
        return self._client.request("GET", "/ulog/available_interfaces/options")

    def get_ulog_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the Traffic Logging configuration in an array."""
        return self._client.request("GET", "/ulog/config", params={"all_options": all_options})

    def update_ulog_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the Traffic Logging configuration in an array."""
        return self._client.request("PUT", "/ulog/config", json={"data": config})

    def get_ulog_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the Traffic Logging configuration."""
        return self._client.request("GET", f"/ulog/config/{config_id}", params={"all_options": all_options})

    def update_ulog_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the Traffic Logging configuration."""
        return self._client.request("PUT", f"/ulog/config/{config_id}", json={"data": config})

    def ulog_ftp_actions_generate_key(self) -> dict[str, Any]:
        """Generate SSH key pair for SFTP authentication."""
        return self._client.request("POST", "/ulog/ftp/actions/generate_key")

    def ulog_ftp_actions_scan_key(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Scan SFTP server's public key."""
        return self._client.request("POST", "/ulog/ftp/actions/scan_key", json=None if data is None else data)

    def get_ulog_ftp_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the Traffic Logging FTP configuration."""
        return self._client.request("GET", "/ulog/ftp/config", params={"all_options": all_options})

    def update_ulog_ftp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the Traffic Logging FTP configuration."""
        return self._client.request("PUT", "/ulog/ftp/config", json={"data": config})

    def get_ulog_ftp_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the Traffic Logging FTP configuration."""
        return self._client.request("GET", f"/ulog/ftp/config/{config_id}", params={"all_options": all_options})

    def upload_ulog_ftp_config_by_id(self, config_id: str, file: File, *, option: str | None = None) -> dict[str, Any]:
        """Upload private SSH key for SFTP authentication."""
        return self._client.request(
            "POST", f"/ulog/ftp/config/{config_id}", files={"file": file}, form={"option": option}
        )

    def update_ulog_ftp_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the Traffic Logging FTP configuration."""
        return self._client.request("PUT", f"/ulog/ftp/config/{config_id}", json={"data": config})

    def get_ulog_status(self) -> dict[str, Any]:
        """Returns Traffic Logging status."""
        return self._client.request("GET", "/ulog/status")
