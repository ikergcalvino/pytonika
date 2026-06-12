from typing import Any

from ._base import Endpoint


class AccessControl(Endpoint):
    def get_access_control_telnet_config(self) -> dict[str, Any]:
        """Returns Telnet configuration."""
        endpoint = "/access_control/telnet/config"

        return self._api_client.get(endpoint)

    def update_access_control_telnet_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Telnet configuration."""
        endpoint = "/access_control/telnet/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_access_control_telnet_config_by_id(self, telnet_id: str) -> dict[str, Any]:
        """Returns Telnet configuration."""
        endpoint = f"/access_control/telnet/config/{telnet_id}"

        return self._api_client.get(endpoint)

    def update_access_control_telnet_config_by_id(self, telnet_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Telnet configuration."""
        endpoint = f"/access_control/telnet/config/{telnet_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_access_control_pam_options(self) -> dict[str, Any]:
        """Returns PAM allowed modules."""
        endpoint = "/access_control/pam/options"

        return self._api_client.get(endpoint)

    def get_access_control_pam_config(self) -> dict[str, Any]:
        """Returns all PAM configurations."""
        endpoint = "/access_control/pam/config"

        return self._api_client.get(endpoint)

    def create_access_control_pam_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates PAM configuration."""
        endpoint = "/access_control/pam/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_access_control_pam_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified PAM configurations."""
        endpoint = "/access_control/pam/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_access_control_pam_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified PAM configurations."""
        return [self.delete_access_control_pam_config_by_id(pam_id) for pam_id in config]

    def get_access_control_pam_config_by_id(self, pam_id: str) -> dict[str, Any]:
        """Returns the specified PAM configuration."""
        endpoint = f"/access_control/pam/config/{pam_id}"

        return self._api_client.get(endpoint)

    def update_access_control_pam_config_by_id(self, pam_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified PAM configuration."""
        endpoint = f"/access_control/pam/config/{pam_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_access_control_pam_config_by_id(self, pam_id: str) -> dict[str, Any]:
        """Deletes specified PAM configuration."""
        endpoint = f"/access_control/pam/config/{pam_id}"

        return self._api_client.delete(endpoint)

    def get_access_control_security_config(self) -> dict[str, Any]:
        """Returns IP Block configuration."""
        endpoint = "/access_control/security/config"

        return self._api_client.get(endpoint)

    def update_access_control_security_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates IP Block configuration."""
        endpoint = "/access_control/security/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_access_control_security_config_by_id(self, security_id: str) -> dict[str, Any]:
        """Returns IP Block configuration."""
        endpoint = f"/access_control/security/config/{security_id}"

        return self._api_client.get(endpoint)

    def update_access_control_security_config_by_id(self, security_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates IP Block configuration."""
        endpoint = f"/access_control/security/config/{security_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_access_control_security_attempts_config(self) -> dict[str, Any]:
        """Returns all login attempts."""
        endpoint = "/access_control/security/attempts/config"

        return self._api_client.get(endpoint)

    def delete_access_control_security_attempts_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified login attempts."""
        return [self.delete_access_control_security_attempts_config_by_id(attempt_id) for attempt_id in config]

    def get_access_control_security_attempts_config_by_id(self, attempt_id: str) -> dict[str, Any]:
        """Returns the specified login attempt."""
        endpoint = f"/access_control/security/attempts/config/{attempt_id}"

        return self._api_client.get(endpoint)

    def delete_access_control_security_attempts_config_by_id(self, attempt_id: str) -> dict[str, Any]:
        """Deletes the specified login attempt."""
        endpoint = f"/access_control/security/attempts/config/{attempt_id}"

        return self._api_client.delete(endpoint)

    def access_control_security_attempts_actions_unblock_all(self) -> dict[str, Any]:
        """Unblocks all blocked entries."""
        endpoint = "/access_control/security/attempts/actions/unblock_all"

        return self._api_client.post(endpoint)

    def get_access_control_webui_status(self) -> dict[str, Any]:
        """Returns all Access Control statuses."""
        endpoint = "/access_control/webui/status"

        return self._api_client.get(endpoint)

    def get_access_control_webui_certificate_status(self) -> dict[str, Any]:
        """Returns information about HTTPS certificate."""
        endpoint = "/access_control/webui/certificate/status"

        return self._api_client.get(endpoint)

    def get_access_control_webui_config(self) -> dict[str, Any]:
        """Returns WebUI configuration."""
        endpoint = "/access_control/webui/config"

        return self._api_client.get(endpoint)

    def update_access_control_webui_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates WebUI configuration."""
        endpoint = "/access_control/webui/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_access_control_webui_config_by_id(self, webui_id: str) -> dict[str, Any]:
        """Returns WebUI configuration."""
        endpoint = f"/access_control/webui/config/{webui_id}"

        return self._api_client.get(endpoint)

    def upload_access_control_webui_config_by_id(self, webui_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads certificate or private key file."""
        endpoint = f"/access_control/webui/config/{webui_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_access_control_webui_config_by_id(self, webui_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates WebUI configuration."""
        endpoint = f"/access_control/webui/config/{webui_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def access_control_webui_actions_download(self) -> dict[str, Any]:
        """Downloads default certificate authority file."""
        endpoint = "/access_control/webui/actions/download"

        return self._api_client.post(endpoint)

    def access_control_webui_actions_generate(self) -> dict[str, Any]:
        """Re-generate default self-signed HTTPS certificate."""
        endpoint = "/access_control/webui/actions/generate"

        return self._api_client.post(endpoint)

    def get_access_control_ssh_config(self) -> dict[str, Any]:
        """Returns SSH configuration."""
        endpoint = "/access_control/ssh/config"

        return self._api_client.get(endpoint)

    def update_access_control_ssh_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SSH configuration."""
        endpoint = "/access_control/ssh/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_access_control_ssh_config_by_id(self, ssh_id: str) -> dict[str, Any]:
        """Returns SSH configuration."""
        endpoint = f"/access_control/ssh/config/{ssh_id}"

        return self._api_client.get(endpoint)

    def update_access_control_ssh_config_by_id(self, ssh_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates SSH configuration."""
        endpoint = f"/access_control/ssh/config/{ssh_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_access_control_cli_config(self) -> dict[str, Any]:
        """Returns CLI configuration."""
        endpoint = "/access_control/cli/config"

        return self._api_client.get(endpoint)

    def update_access_control_cli_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates CLI configuration."""
        endpoint = "/access_control/cli/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_access_control_cli_config_by_id(self, cli_id: str) -> dict[str, Any]:
        """Returns CLI configuration."""
        endpoint = f"/access_control/cli/config/{cli_id}"

        return self._api_client.get(endpoint)

    def update_access_control_cli_config_by_id(self, cli_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates CLI configuration."""
        endpoint = f"/access_control/cli/config/{cli_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
