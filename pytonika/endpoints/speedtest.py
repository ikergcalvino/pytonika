from typing import Any

from ._base import Endpoint


class Speedtest(Endpoint):
    def get_speedtest_config_general(self) -> dict[str, Any]:
        """Returns the general speed test configuration."""
        endpoint = "/speedtest/config/general"

        return self._client.request("GET", endpoint)

    def update_speedtest_config_general(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the general speed test configuration."""
        endpoint = "/speedtest/config/general"

        data = {"data": config}

        return self._client.request("PUT", endpoint, json=data)

    def get_speedtest_status(self) -> dict[str, Any]:
        """Returns information about speed test state."""
        endpoint = "/speedtest/status"

        return self._client.request("GET", endpoint)

    def get_speedtest_options(self) -> dict[str, Any]:
        """Returns a list of available speed test servers."""
        endpoint = "/speedtest/options"

        return self._client.request("GET", endpoint)

    def speedtest_get_ip(self, data: dict[str, Any]) -> dict[str, Any]:
        """Converts speed test server URL to IP address."""
        endpoint = "/speedtest/actions/get_ip"

        return self._client.request("POST", endpoint, json={"data": data})

    def speedtest_refresh(self, data: dict[str, Any]) -> dict[str, Any]:
        """Refreshes speed test server list on device."""
        endpoint = "/speedtest/actions/refresh"

        return self._client.request("POST", endpoint, json={"data": data})

    def speedtest_start(self, data: dict[str, Any]) -> dict[str, Any]:
        """Starts a new speed test."""
        endpoint = "/speedtest/actions/start"

        return self._client.request("POST", endpoint, json={"data": data})
