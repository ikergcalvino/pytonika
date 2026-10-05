from typing import Any

from ._base import Endpoint


class EventsReporting(Endpoint):
    def get_events_reporting_options(self) -> dict[str, Any]:
        """Returns Events Reporting options.

        .. deprecated::
        """
        endpoint = "/events_reporting/options"

        return self._client.request("GET", endpoint)

    def get_events_reporting_config(self) -> dict[str, Any]:
        """Returns all Events Reporting configurations.

        .. deprecated::
        """
        endpoint = "/events_reporting/config"

        return self._client.request("GET", endpoint)

    def create_events_reporting_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Events Reporting configuration.

        .. deprecated::
        """
        endpoint = "/events_reporting/config"

        data = {"data": config}

        return self._client.request("POST", endpoint, json=data)

    def update_events_reporting_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Events Reporting configurations.

        .. deprecated::
        """
        endpoint = "/events_reporting/config"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_events_reporting_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes the selected Events Reporting configurations.

        .. deprecated::
        """
        return [self.delete_events_reporting_config_by_id(rule_id) for rule_id in config]

    def get_events_reporting_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the selected Events Reporting configuration.

        .. deprecated::
        """
        endpoint = f"/events_reporting/config/{config_id}"

        return self._client.request("GET", endpoint)

    def update_events_reporting_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected Events Reporting configuration.

        .. deprecated::
        """
        endpoint = f"/events_reporting/config/{config_id}"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def delete_events_reporting_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the selected Events Reporting configuration.

        .. deprecated::
        """
        endpoint = f"/events_reporting/config/{config_id}"

        return self._client.request("DELETE", endpoint)

    def send_test_email(self, data: dict[str, Any]) -> dict[str, Any]:
        """Sends test email.

        .. deprecated::
        """
        endpoint = "/events_reporting/actions/send_test_email"

        return self._client.request("POST", endpoint, json={"data": data})
