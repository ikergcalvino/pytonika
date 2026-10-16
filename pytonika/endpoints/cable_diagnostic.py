from typing import Any

from ._endpoint import Endpoint


class CableDiagnostic(Endpoint):
    def cable_diagnostic_actions_run(
        self, config: dict[str, Any] | None = None, *, use_cache: bool | None = None
    ) -> dict[str, Any]:
        """Runs selected port's cable diagnostic and retrieves the results."""
        return self._client.request(
            "POST",
            "/cable_diagnostic/actions/run",
            params={"use_cache": use_cache},
            json=None if config is None else {"data": config},
        )
