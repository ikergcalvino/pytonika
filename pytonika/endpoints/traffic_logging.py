from typing import Any

from ._endpoint import Endpoint


class TrafficLogging(Endpoint):
    def get_ulog_available_interfaces_options(self) -> dict[str, Any]:
        """Returns Traffic Logging options."""
        endpoint = "/ulog/available_interfaces/options"

        return self._client.request("GET", endpoint)

    def get_ulog_config(self) -> dict[str, Any]:
        """Returns the Traffic Logging configuration in an array."""
        endpoint = "/ulog/config"

        return self._client.request("GET", endpoint)

    def update_ulog_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the Traffic Logging configuration in an array."""
        endpoint = "/ulog/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def get_ulog_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the Traffic Logging configuration."""
        endpoint = f"/ulog/config/{config_id}"

        return self._client.request("GET", endpoint)

    def update_ulog_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the Traffic Logging configuration."""
        endpoint = f"/ulog/config/{config_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def get_ulog_status(self) -> dict[str, Any]:
        """Returns Traffic Logging status."""
        endpoint = "/ulog/status"

        return self._client.request("GET", endpoint)

    def get_ulog_ftp_config(self) -> dict[str, Any]:
        """Returns the Traffic Logging FTP configuration."""
        endpoint = "/ulog/ftp/config"

        return self._client.request("GET", endpoint)

    def update_ulog_ftp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the Traffic Logging FTP configuration."""
        endpoint = "/ulog/ftp/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def get_ulog_ftp_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the Traffic Logging FTP configuration."""
        endpoint = f"/ulog/ftp/config/{config_id}"

        return self._client.request("GET", endpoint)

    def update_ulog_ftp_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the Traffic Logging FTP configuration."""
        endpoint = f"/ulog/ftp/config/{config_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)
