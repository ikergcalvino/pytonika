from typing import Any

from ._endpoint import Endpoint


class EventsLog(Endpoint):
    def get_events_log_config(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        sortby: str | None = None,
        orderby: str | None = None,
        search: str | None = None,
        id: str | None = None,
        date: str | None = None,
        event_type: str | None = None,
        event: str | None = None,
        type: str | None = None,
        group: str | None = None,
        timestamp: str | None = None,
        fields: str | None = None,
    ) -> dict[str, Any]:
        """Returns events from all log groups."""
        return self._client.request(
            "GET",
            "/events_log/config",
            params={
                "limit": limit,
                "offset": offset,
                "sortby": sortby,
                "orderby": orderby,
                "search": search,
                "id": id,
                "date": date,
                "event_type": event_type,
                "event": event,
                "type": type,
                "group": group,
                "timestamp": timestamp,
                "fields": fields,
            },
        )

    def get_events_log_config_by_event_type(
        self,
        event_type: str,
        *,
        limit: int | None = None,
        offset: int | None = None,
        sortby: str | None = None,
        orderby: str | None = None,
        search: str | None = None,
    ) -> dict[str, Any]:
        """Returns events from specified log group."""
        return self._client.request(
            "GET",
            f"/events_log/config/{event_type}",
            params={"limit": limit, "offset": offset, "sortby": sortby, "orderby": orderby, "search": search},
        )
