from typing import Any

from ._endpoint import Endpoint


class Speedtest(Endpoint):
    def speedtest_actions_get_ip(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Converts speed test server URL to IP address."""
        return self._client.request("POST", "/speedtest/actions/get_ip", json=None if data is None else {"data": data})

    def speedtest_actions_refresh(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Refreshes speed test server list on device."""
        return self._client.request("POST", "/speedtest/actions/refresh", json=None if data is None else {"data": data})

    def speedtest_actions_start(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Starts a new speed test."""
        return self._client.request("POST", "/speedtest/actions/start", json=None if data is None else {"data": data})

    def get_speedtest_config_general(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the general speed test configuration."""
        return self._client.request("GET", "/speedtest/config/general", params={"all_options": all_options})

    def update_speedtest_config_general(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the general speed test configuration."""
        return self._client.request("PUT", "/speedtest/config/general", json={"data": config})

    def get_speedtest_options(self) -> dict[str, Any]:
        """Returns a list of available speed test servers."""
        return self._client.request("GET", "/speedtest/options")

    def get_speedtest_status(self, *, exclude: str | None = None) -> dict[str, Any]:
        """Returns information about speed test state."""
        return self._client.request("GET", "/speedtest/status", params={"exclude": exclude})
