from typing import Any

from ._base import Endpoint


class Logging(Endpoint):
    def get_logging_services_config(self) -> dict[str, Any]:
        """Returns Logging Services configuration."""
        endpoint = "/logging/services/config"

        return self._api_client.get(endpoint)

    def create_logging_services_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Service Logging section."""
        endpoint = "/logging/services/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_logging_services_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Logging configuration."""
        endpoint = "/logging/services/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_logging_services_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified service's logging configuration."""
        return [self.delete_logging_services_config_by_id(service_id) for service_id in config]

    def get_logging_services_config_by_id(self, service_id: str) -> dict[str, Any]:
        """Returns Logging configuration."""
        endpoint = f"/logging/services/config/{service_id}"

        return self._api_client.get(endpoint)

    def update_logging_services_config_by_id(self, service_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Logging configuration."""
        endpoint = f"/logging/services/config/{service_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_logging_services_config_by_id(self, service_id: str) -> dict[str, Any]:
        """Deletes specified service's logging configuration."""
        endpoint = f"/logging/services/config/{service_id}"

        return self._api_client.delete(endpoint)

    def get_logging_services_status_by_id(self, service_id: str) -> dict[str, Any]:
        """Returns information about log file."""
        endpoint = f"/logging/services/status/{service_id}"

        return self._api_client.get(endpoint)

    def get_logging_config(self) -> dict[str, Any]:
        """Returns Logging configuration."""
        endpoint = "/logging/config"

        return self._api_client.get(endpoint)

    def update_logging_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Logging configuration."""
        endpoint = "/logging/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_logging_config_by_id(self, logging_id: str) -> dict[str, Any]:
        """Returns Logging configuration."""
        endpoint = f"/logging/config/{logging_id}"

        return self._api_client.get(endpoint)

    def update_logging_config_by_id(self, logging_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Logging configuration."""
        endpoint = f"/logging/config/{logging_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_logging_status(self) -> dict[str, Any]:
        """Returns information about log file."""
        endpoint = "/logging/status"

        return self._api_client.get(endpoint)

    def delete_log(self) -> dict[str, Any]:
        """Deletes log file."""
        endpoint = "/logging/actions/delete_log"

        return self._api_client.post(endpoint)
