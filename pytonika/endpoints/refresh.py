from typing import Any

from ._endpoint import Endpoint


class Refresh(Endpoint):
    """Endpoints of the "Refresh" page of the Teltonika Web API reference."""

    def refresh(
        self,
        config: dict[str, Any],
    ) -> bytes | dict[str, Any]:
        """Refresh endpoint."""
        return self._client.request(
            "POST",
            "/refresh",
            json=config,
            download=True,
        )
