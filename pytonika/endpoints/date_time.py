from typing import Any, Literal

from ._endpoint import Endpoint, File


class DateTime(Endpoint):
    def get_date_time_ntp_client_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns NTP Client configuration in an array."""
        return self._client.request("GET", "/date_time/ntp/client/config", params={"all_options": all_options})

    def update_date_time_ntp_client_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates NTP Client configuration in an array."""
        return self._client.request("PUT", "/date_time/ntp/client/config", json={"data": config})

    def get_date_time_ntp_client_config_by_id(
        self, client_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns NTP Client configuration."""
        return self._client.request(
            "GET", f"/date_time/ntp/client/config/{client_id}", params={"all_options": all_options}
        )

    def update_date_time_ntp_client_config_by_id(self, client_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates NTP Client configuration."""
        return self._client.request("PUT", f"/date_time/ntp/client/config/{client_id}", json={"data": config})

    def get_date_time_ntp_client_timezones_options(self) -> dict[str, Any]:
        """Returns available NTP client options."""
        return self._client.request("GET", "/date_time/ntp/client/timezones/options")

    def get_date_time_ntp_server_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns NTP Server configuration in an array."""
        return self._client.request("GET", "/date_time/ntp/server/config", params={"all_options": all_options})

    def update_date_time_ntp_server_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates NTP Server configuration in an array."""
        return self._client.request("PUT", "/date_time/ntp/server/config", json={"data": config})

    def get_date_time_ntp_server_config_by_id(
        self, server_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns NTP Server configuration."""
        return self._client.request(
            "GET", f"/date_time/ntp/server/config/{server_id}", params={"all_options": all_options}
        )

    def update_date_time_ntp_server_config_by_id(self, server_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates NTP Server configuration."""
        return self._client.request("PUT", f"/date_time/ntp/server/config/{server_id}", json={"data": config})

    def get_date_time_ntp_time_servers_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all NTP Remote Server configurations."""
        return self._client.request("GET", "/date_time/ntp/time_servers/config", params={"all_options": all_options})

    def create_date_time_ntp_time_servers_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates a new NTP Remote Server configuration."""
        return self._client.request("POST", "/date_time/ntp/time_servers/config", json={"data": config})

    def update_date_time_ntp_time_servers_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified NTP Remote Server configurations."""
        return self._client.request("PUT", "/date_time/ntp/time_servers/config", json={"data": config})

    def delete_date_time_ntp_time_servers_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified NTP Remote Server configurations."""
        return self._client.request("DELETE", "/date_time/ntp/time_servers/config", json={"data": config})

    def get_date_time_ntp_time_servers_config_by_id(
        self, server_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified NTP Remote Server configuration."""
        return self._client.request(
            "GET", f"/date_time/ntp/time_servers/config/{server_id}", params={"all_options": all_options}
        )

    def update_date_time_ntp_time_servers_config_by_id(self, server_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified NTP Remote Server configuration."""
        return self._client.request("PUT", f"/date_time/ntp/time_servers/config/{server_id}", json={"data": config})

    def delete_date_time_ntp_time_servers_config_by_id(self, server_id: str) -> dict[str, Any]:
        """Deletes the specified NTP Remote Server configuration."""
        return self._client.request("DELETE", f"/date_time/ntp/time_servers/config/{server_id}")

    def get_date_time_ntpd_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the NTPD configuration in an array."""
        return self._client.request("GET", "/date_time/ntpd/config", params={"all_options": all_options})

    def update_date_time_ntpd_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the NTPD configuration in an array."""
        return self._client.request("PUT", "/date_time/ntpd/config", json={"data": config})

    def get_date_time_ntpd_config_by_id(self, ntpd_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the NTPD configuration."""
        return self._client.request("GET", f"/date_time/ntpd/config/{ntpd_id}", params={"all_options": all_options})

    def upload_date_time_ntpd_config_by_id(
        self, ntpd_id: str, file: File, *, option: Literal["config_file"] | None = None
    ) -> dict[str, Any]:
        """Uploads the NTPD config file."""
        return self._client.request(
            "POST", f"/date_time/ntpd/config/{ntpd_id}", files={"file": file}, form={"option": option}
        )

    def update_date_time_ntpd_config_by_id(self, ntpd_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the NTPD configuration."""
        return self._client.request("PUT", f"/date_time/ntpd/config/{ntpd_id}", json={"data": config})

    def get_date_time_ntpd_keys_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all NTPD authentication keys configuration."""
        return self._client.request("GET", "/date_time/ntpd/keys/config", params={"all_options": all_options})

    def update_date_time_ntpd_keys_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates NTPD authentication keys array."""
        return self._client.request("PUT", "/date_time/ntpd/keys/config", json={"data": config})

    def get_date_time_ntpd_keys_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns a single authentication key."""
        return self._client.request(
            "GET", f"/date_time/ntpd/keys/config/{config_id}", params={"all_options": all_options}
        )

    def update_date_time_ntpd_keys_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates an authentication key."""
        return self._client.request("PUT", f"/date_time/ntpd/keys/config/{config_id}", json={"data": config})

    def delete_date_time_ntpd_keys_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes an authentication key."""
        return self._client.request("DELETE", f"/date_time/ntpd/keys/config/{config_id}")

    def get_date_time_ntpd_servers_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all NTP servers configuration."""
        return self._client.request("GET", "/date_time/ntpd/servers/config", params={"all_options": all_options})

    def update_date_time_ntpd_servers_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates NTP server instances array."""
        return self._client.request("PUT", "/date_time/ntpd/servers/config", json={"data": config})

    def get_date_time_ntpd_servers_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns a single NTP server instance."""
        return self._client.request(
            "GET", f"/date_time/ntpd/servers/config/{config_id}", params={"all_options": all_options}
        )

    def update_date_time_ntpd_servers_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates an NTP server instance."""
        return self._client.request("PUT", f"/date_time/ntpd/servers/config/{config_id}", json={"data": config})

    def delete_date_time_ntpd_servers_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes an NTP server instance."""
        return self._client.request("DELETE", f"/date_time/ntpd/servers/config/{config_id}")
