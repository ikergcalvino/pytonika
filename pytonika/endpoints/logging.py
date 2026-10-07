from typing import Any

from ._endpoint import Endpoint


class Logging(Endpoint):
    def logging_actions_delete_log(self) -> dict[str, Any]:
        """Deletes log file."""
        return self._client.request("POST", "/logging/actions/delete_log")

    def get_logging_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Logging configuration."""
        return self._client.request("GET", "/logging/config", params={"all_options": all_options})

    def update_logging_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Logging configuration."""
        return self._client.request("PUT", "/logging/config", json={"data": config})

    def get_logging_config_by_id(self, logging_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Logging configuration."""
        return self._client.request("GET", f"/logging/config/{logging_id}", params={"all_options": all_options})

    def update_logging_config_by_id(self, logging_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Logging configuration."""
        return self._client.request("PUT", f"/logging/config/{logging_id}", json={"data": config})

    def get_logging_services_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Logging Services configuration."""
        return self._client.request("GET", "/logging/services/config", params={"all_options": all_options})

    def create_logging_services_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Service Logging section."""
        return self._client.request("POST", "/logging/services/config", json={"data": config})

    def update_logging_services_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Logging configuration."""
        return self._client.request("PUT", "/logging/services/config", json={"data": config})

    def delete_logging_services_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified service's logging configuration."""
        return self._client.request("DELETE", "/logging/services/config", json={"data": config})

    def get_logging_services_config_by_id(self, service_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Logging configuration."""
        return self._client.request(
            "GET", f"/logging/services/config/{service_id}", params={"all_options": all_options}
        )

    def update_logging_services_config_by_id(self, service_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Logging configuration."""
        return self._client.request("PUT", f"/logging/services/config/{service_id}", json={"data": config})

    def delete_logging_services_config_by_id(self, service_id: str) -> dict[str, Any]:
        """Deletes specified service's logging configuration."""
        return self._client.request("DELETE", f"/logging/services/config/{service_id}")

    def get_logging_services_status_by_id(self, service_id: str) -> dict[str, Any]:
        """Returns information about log file."""
        return self._client.request("GET", f"/logging/services/status/{service_id}")

    def get_logging_status(self) -> dict[str, Any]:
        """Returns information about log file."""
        return self._client.request("GET", "/logging/status")
