from typing import Any, Literal

from ._endpoint import Endpoint


class UniversalGateway(Endpoint):
    def get_universal_gateway_options(self) -> dict[str, Any]:
        """Returns available tag options. A tag is an abstraction representing a single data point (such as a value
        or parameter) that can be read from or written to various protocol clients.
        """
        return self._client.request("GET", "/universal_gateway/options")

    def get_universal_gateway_status(
        self,
        *,
        client_service: Literal["dnp3_client", "iec60870_client", "impulse_counter", "mbus_client", "modbus_client"]
        | None = None,
    ) -> dict[str, Any]:
        """Returns tag ids from all configured data sources. A tag is an abstraction representing a single data point
        (such as a value or parameter) that can be read from or written to various protocol clients.
        """
        return self._client.request("GET", "/universal_gateway/status", params={"client_service": client_service})
