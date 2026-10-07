from typing import Any

from ._endpoint import Endpoint


class EventsReporting(Endpoint):
    def events_reporting_actions_send_test_email(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Sends test email."""
        return self._client.request(
            "POST", "/events_reporting/actions/send_test_email", json=None if data is None else {"data": data}
        )

    def get_events_reporting_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Events Reporting configurations."""
        return self._client.request("GET", "/events_reporting/config", params={"all_options": all_options})

    def create_events_reporting_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new Events Reporting configuration."""
        return self._client.request("POST", "/events_reporting/config", json={"data": config})

    def update_events_reporting_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the selected Events Reporting configurations."""
        return self._client.request("PUT", "/events_reporting/config", json={"data": config})

    def delete_events_reporting_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes the selected Events Reporting configurations."""
        return self._client.request("DELETE", "/events_reporting/config", json={"data": config})

    def get_events_reporting_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the selected Events Reporting configuration."""
        return self._client.request("GET", f"/events_reporting/config/{config_id}", params={"all_options": all_options})

    def update_events_reporting_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the selected Events Reporting configuration."""
        return self._client.request("PUT", f"/events_reporting/config/{config_id}", json={"data": config})

    def delete_events_reporting_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the selected Events Reporting configuration."""
        return self._client.request("DELETE", f"/events_reporting/config/{config_id}")

    def get_events_reporting_options(self) -> dict[str, Any]:
        """Returns Events Reporting options."""
        return self._client.request("GET", "/events_reporting/options")
