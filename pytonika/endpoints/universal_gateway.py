from typing import Any

from ._base import Endpoint


class UniversalGateway(Endpoint):
    def get_universal_gateway_options(self) -> dict[str, Any]:
        """Returns available tag options.

        A tag is an abstraction representing a single data point (such as a value or parameter)
        that can be read from or written to various protocol clients.
        """
        endpoint = "/universal_gateway/options"

        return self._api_client.get(endpoint)

    def get_universal_gateway_status(self) -> dict[str, Any]:
        """Returns tag ids from all configured data sources.

        A tag is an abstraction representing a single data point (such as a value or parameter)
        that can be read from or written to various protocol clients.
        """
        endpoint = "/universal_gateway/status"

        return self._api_client.get(endpoint)
