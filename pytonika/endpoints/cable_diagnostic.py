from typing import Any

from ._base import Endpoint


class CableDiagnostic(Endpoint):
    def cable_diagnostic_actions_run(self, config: dict[str, Any]) -> dict[str, Any]:
        """Runs selected port's cable diagnostic and retrieves the results."""
        endpoint = "/cable_diagnostic/actions/run"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)
