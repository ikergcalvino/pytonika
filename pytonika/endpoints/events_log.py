from typing import Any

from ._base import Endpoint


class EventsLog(Endpoint):
    def get_events_log_config(self) -> dict[str, Any]:
        """Returns events from all log groups."""
        endpoint = "/events_log/config"

        return self._api_client.get(endpoint)

    def get_events_log_config_by_type(self, event_type: str) -> dict[str, Any]:
        """Returns events from specified log group."""
        endpoint = f"/events_log/config/{event_type}"

        return self._api_client.get(endpoint)
