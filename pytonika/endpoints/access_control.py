from typing import Any

from ._endpoint import Endpoint, File


class AccessControl(Endpoint):
    def get_access_control_cli_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns CLI configuration."""
        return self._client.request("GET", "/access_control/cli/config", params={"all_options": all_options})

    def update_access_control_cli_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates CLI configuration."""
        return self._client.request("PUT", "/access_control/cli/config", json={"data": config})

    def get_access_control_cli_config_by_id(self, cli_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns CLI configuration."""
        return self._client.request("GET", f"/access_control/cli/config/{cli_id}", params={"all_options": all_options})

    def update_access_control_cli_config_by_id(self, cli_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates CLI configuration."""
        return self._client.request("PUT", f"/access_control/cli/config/{cli_id}", json={"data": config})

    def access_control_device_pairing_actions_unpair(self) -> dict[str, Any]:
        """Unpairs all paired devices."""
        return self._client.request("POST", "/access_control/device_pairing/actions/unpair")

    def get_access_control_device_pairing_config_general(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the device pairing configuration."""
        return self._client.request(
            "GET", "/access_control/device_pairing/config/general", params={"all_options": all_options}
        )

    def update_access_control_device_pairing_config_general(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the device pairing configuration."""
        return self._client.request("PUT", "/access_control/device_pairing/config/general", json={"data": config})

    def get_access_control_device_pairing_status(self) -> dict[str, Any]:
        """Returns status about all paired devices."""
        return self._client.request("GET", "/access_control/device_pairing/status")

    def get_access_control_pam_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all PAM configurations."""
        return self._client.request("GET", "/access_control/pam/config", params={"all_options": all_options})

    def create_access_control_pam_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates PAM configuration."""
        return self._client.request("POST", "/access_control/pam/config", json={"data": config})

    def update_access_control_pam_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified PAM configurations."""
        return self._client.request("PUT", "/access_control/pam/config", json={"data": config})

    def delete_access_control_pam_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified PAM configurations."""
        return self._client.request("DELETE", "/access_control/pam/config", json={"data": config})

    def get_access_control_pam_config_by_id(self, pam_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified PAM configuration."""
        return self._client.request("GET", f"/access_control/pam/config/{pam_id}", params={"all_options": all_options})

    def update_access_control_pam_config_by_id(self, pam_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified PAM configuration."""
        return self._client.request("PUT", f"/access_control/pam/config/{pam_id}", json={"data": config})

    def delete_access_control_pam_config_by_id(self, pam_id: str) -> dict[str, Any]:
        """Deletes specified PAM configuration."""
        return self._client.request("DELETE", f"/access_control/pam/config/{pam_id}")

    def get_access_control_pam_options(self) -> dict[str, Any]:
        """Returns PAM allowed modules."""
        return self._client.request("GET", "/access_control/pam/options")

    def access_control_security_attempts_actions_unblock_all(self) -> dict[str, Any]:
        """Unblocks all blocked entries."""
        return self._client.request("POST", "/access_control/security/attempts/actions/unblock_all")

    def get_access_control_security_attempts_config(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        sortby: str | None = None,
        orderby: str | None = None,
        search: str | None = None,
        id: str | None = None,
        ip: str | None = None,
        mac: str | None = None,
        destination_ip: str | None = None,
        port: str | None = None,
        proto: str | None = None,
        counter: str | None = None,
        iteration_count: str | None = None,
        blocked_time: str | None = None,
        fields: str | None = None,
    ) -> dict[str, Any]:
        """Returns all login attempts."""
        return self._client.request(
            "GET",
            "/access_control/security/attempts/config",
            params={
                "limit": limit,
                "offset": offset,
                "sortby": sortby,
                "orderby": orderby,
                "search": search,
                "id": id,
                "ip": ip,
                "mac": mac,
                "destination_ip": destination_ip,
                "port": port,
                "proto": proto,
                "counter": counter,
                "iteration_count": iteration_count,
                "blocked_time": blocked_time,
                "fields": fields,
            },
        )

    def delete_access_control_security_attempts_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified login attempts."""
        return self._client.request("DELETE", "/access_control/security/attempts/config", json={"data": config})

    def get_access_control_security_attempts_config_by_id(self, attempt_id: str) -> dict[str, Any]:
        """Returns the specified login attempt."""
        return self._client.request("GET", f"/access_control/security/attempts/config/{attempt_id}")

    def delete_access_control_security_attempts_config_by_id(self, attempt_id: str) -> dict[str, Any]:
        """Deletes the specified login attempt."""
        return self._client.request("DELETE", f"/access_control/security/attempts/config/{attempt_id}")

    def get_access_control_security_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns IP Block configuration."""
        return self._client.request("GET", "/access_control/security/config", params={"all_options": all_options})

    def update_access_control_security_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates IP Block configuration."""
        return self._client.request("PUT", "/access_control/security/config", json={"data": config})

    def get_access_control_security_config_by_id(
        self, security_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns IP Block configuration."""
        return self._client.request(
            "GET", f"/access_control/security/config/{security_id}", params={"all_options": all_options}
        )

    def update_access_control_security_config_by_id(self, security_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates IP Block configuration."""
        return self._client.request("PUT", f"/access_control/security/config/{security_id}", json={"data": config})

    def access_control_sessions_actions_terminate(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Terminate an active session."""
        return self._client.request(
            "POST", "/access_control/sessions/actions/terminate", json=None if data is None else data
        )

    def get_access_control_sessions_status(
        self, *, type: str | None = None, seen_ip: str | None = None
    ) -> dict[str, Any]:
        """Get active sessions."""
        return self._client.request("GET", "/access_control/sessions/status", params={"type": type, "seen_ip": seen_ip})

    def get_access_control_ssh_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns SSH configuration."""
        return self._client.request("GET", "/access_control/ssh/config", params={"all_options": all_options})

    def update_access_control_ssh_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SSH configuration."""
        return self._client.request("PUT", "/access_control/ssh/config", json={"data": config})

    def get_access_control_ssh_config_by_id(self, ssh_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns SSH configuration."""
        return self._client.request("GET", f"/access_control/ssh/config/{ssh_id}", params={"all_options": all_options})

    def update_access_control_ssh_config_by_id(self, ssh_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates SSH configuration."""
        return self._client.request("PUT", f"/access_control/ssh/config/{ssh_id}", json={"data": config})

    def get_access_control_telnet_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Telnet configuration."""
        return self._client.request("GET", "/access_control/telnet/config", params={"all_options": all_options})

    def update_access_control_telnet_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Telnet configuration."""
        return self._client.request("PUT", "/access_control/telnet/config", json={"data": config})

    def get_access_control_telnet_config_by_id(
        self, telnet_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns Telnet configuration."""
        return self._client.request(
            "GET", f"/access_control/telnet/config/{telnet_id}", params={"all_options": all_options}
        )

    def update_access_control_telnet_config_by_id(self, telnet_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Telnet configuration."""
        return self._client.request("PUT", f"/access_control/telnet/config/{telnet_id}", json={"data": config})

    def access_control_webui_actions_download(self) -> bytes | dict[str, Any]:
        """Downloads default certificate authority file."""
        return self._client.request("POST", "/access_control/webui/actions/download", download=True)

    def access_control_webui_actions_generate(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Re-generate default self-signed HTTPS certificate."""
        return self._client.request(
            "POST", "/access_control/webui/actions/generate", json=None if data is None else {"data": data}
        )

    def get_access_control_webui_certificate_status(self) -> dict[str, Any]:
        """Returns information about HTTPS certificate."""
        return self._client.request("GET", "/access_control/webui/certificate/status")

    def get_access_control_webui_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns WebUI configuration."""
        return self._client.request("GET", "/access_control/webui/config", params={"all_options": all_options})

    def update_access_control_webui_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates WebUI configuration."""
        return self._client.request("PUT", "/access_control/webui/config", json={"data": config})

    def get_access_control_webui_config_by_id(
        self, webui_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns WebUI configuration."""
        return self._client.request(
            "GET", f"/access_control/webui/config/{webui_id}", params={"all_options": all_options}
        )

    def upload_access_control_webui_config_by_id(
        self, webui_id: str, file: File, *, option: str | None = None
    ) -> dict[str, Any]:
        """Uploads certificate or private key file."""
        return self._client.request(
            "POST", f"/access_control/webui/config/{webui_id}", files={"file": file}, form={"option": option}
        )

    def update_access_control_webui_config_by_id(self, webui_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates WebUI configuration."""
        return self._client.request("PUT", f"/access_control/webui/config/{webui_id}", json={"data": config})

    def get_access_control_webui_status(self) -> dict[str, Any]:
        """Returns all Access Control statuses."""
        return self._client.request("GET", "/access_control/webui/status")
