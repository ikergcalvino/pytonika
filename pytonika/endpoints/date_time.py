from typing import Any

from ._base import Endpoint


class DateTime(Endpoint):
    def get_date_time_ntpd_config(self) -> dict[str, Any]:
        """Returns the NTPD configuration in an array."""
        endpoint = "/date_time/ntpd/config"

        return self._api_client.get(endpoint)

    def update_date_time_ntpd_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the NTPD configuration in an array."""
        endpoint = "/date_time/ntpd/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_date_time_ntpd_config_by_id(self, ntpd_id: str) -> dict[str, Any]:
        """Returns the NTPD configuration."""
        endpoint = f"/date_time/ntpd/config/{ntpd_id}"

        return self._api_client.get(endpoint)

    def upload_date_time_ntpd_config_by_id(self, ntpd_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads the NTPD config file."""
        endpoint = f"/date_time/ntpd/config/{ntpd_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_date_time_ntpd_config_by_id(self, ntpd_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the NTPD configuration."""
        endpoint = f"/date_time/ntpd/config/{ntpd_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_date_time_ntp_client_timezones_options(self) -> dict[str, Any]:
        """Returns available NTP client options."""
        endpoint = "/date_time/ntp/client/timezones/options"

        return self._api_client.get(endpoint)

    def get_date_time_ntp_client_config(self) -> dict[str, Any]:
        """Returns NTP Client configuration in an array."""
        endpoint = "/date_time/ntp/client/config"

        return self._api_client.get(endpoint)

    def update_date_time_ntp_client_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates NTP Client configuration in an array."""
        endpoint = "/date_time/ntp/client/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_date_time_ntp_client_config_by_id(self, client_id: str) -> dict[str, Any]:
        """Returns NTP Client configuration."""
        endpoint = f"/date_time/ntp/client/config/{client_id}"

        return self._api_client.get(endpoint)

    def update_date_time_ntp_client_config_by_id(self, client_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates NTP Client configuration."""
        endpoint = f"/date_time/ntp/client/config/{client_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_date_time_ntp_time_servers_config(self) -> dict[str, Any]:
        """Returns all NTP Remote Server configurations."""
        endpoint = "/date_time/ntp/time_servers/config"

        return self._api_client.get(endpoint)

    def create_date_time_ntp_time_servers_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new NTP Remote Server configuration."""
        endpoint = "/date_time/ntp/time_servers/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_date_time_ntp_time_servers_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified NTP Remote Server configurations."""
        endpoint = "/date_time/ntp/time_servers/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_date_time_ntp_time_servers_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified NTP Remote Server configurations."""
        return [self.delete_date_time_ntp_time_servers_config_by_id(server_id) for server_id in config]

    def get_date_time_ntp_time_servers_config_by_id(self, server_id: str) -> dict[str, Any]:
        """Returns the specified NTP Remote Server configuration."""
        endpoint = f"/date_time/ntp/time_servers/config/{server_id}"

        return self._api_client.get(endpoint)

    def update_date_time_ntp_time_servers_config_by_id(self, server_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified NTP Remote Server configuration."""
        endpoint = f"/date_time/ntp/time_servers/config/{server_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_date_time_ntp_time_servers_config_by_id(self, server_id: str) -> dict[str, Any]:
        """Deletes the specified NTP Remote Server configuration."""
        endpoint = f"/date_time/ntp/time_servers/config/{server_id}"

        return self._api_client.delete(endpoint)

    def get_date_time_ntp_server_config(self) -> dict[str, Any]:
        """Returns NTP Server configuration in an array."""
        endpoint = "/date_time/ntp/server/config"

        return self._api_client.get(endpoint)

    def update_date_time_ntp_server_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates NTP Server configuration in an array."""
        endpoint = "/date_time/ntp/server/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_date_time_ntp_server_config_by_id(self, server_id: str) -> dict[str, Any]:
        """Returns NTP Server configuration."""
        endpoint = f"/date_time/ntp/server/config/{server_id}"

        return self._api_client.get(endpoint)

    def update_date_time_ntp_server_config_by_id(self, server_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates NTP Server configuration."""
        endpoint = f"/date_time/ntp/server/config/{server_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
