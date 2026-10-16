from typing import Any

from ._endpoint import Endpoint, File


class Recipients(Endpoint):
    def recipients_email_users_actions_send_email(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Send test email."""
        return self._client.request(
            "POST", "/recipients/email_users/actions/send_email", json=None if data is None else {"data": data}
        )

    def get_recipients_email_users_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all email users configurations."""
        return self._client.request("GET", "/recipients/email_users/config", params={"all_options": all_options})

    def create_recipients_email_users_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates email users configuration."""
        return self._client.request("POST", "/recipients/email_users/config", json={"data": config})

    def update_recipients_email_users_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified email users configurations."""
        return self._client.request("PUT", "/recipients/email_users/config", json={"data": config})

    def delete_recipients_email_users_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified email users configurations."""
        return self._client.request("DELETE", "/recipients/email_users/config", json={"data": config})

    def get_recipients_email_users_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified email users configuration."""
        return self._client.request(
            "GET", f"/recipients/email_users/config/{config_id}", params={"all_options": all_options}
        )

    def upload_recipients_email_users_config_by_id(self, config_id: str, file: File) -> dict[str, Any]:
        """Uploads server's CA certificate file."""
        return self._client.request("POST", f"/recipients/email_users/config/{config_id}", files={"file": file})

    def update_recipients_email_users_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified email users configuration."""
        return self._client.request("PUT", f"/recipients/email_users/config/{config_id}", json={"data": config})

    def delete_recipients_email_users_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified email users configuration."""
        return self._client.request("DELETE", f"/recipients/email_users/config/{config_id}")

    def get_recipients_phone_groups_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all phone group configurations."""
        return self._client.request("GET", "/recipients/phone_groups/config", params={"all_options": all_options})

    def create_recipients_phone_groups_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates phone group configuration."""
        return self._client.request("POST", "/recipients/phone_groups/config", json={"data": config})

    def update_recipients_phone_groups_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified phone group configurations."""
        return self._client.request("PUT", "/recipients/phone_groups/config", json={"data": config})

    def delete_recipients_phone_groups_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified phone group configurations."""
        return self._client.request("DELETE", "/recipients/phone_groups/config", json={"data": config})

    def get_recipients_phone_groups_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified phone groups configuration."""
        return self._client.request(
            "GET", f"/recipients/phone_groups/config/{config_id}", params={"all_options": all_options}
        )

    def upload_recipients_phone_groups_config_by_id(self, config_id: str, file: File) -> dict[str, Any]:
        """Uploads phone numbers list."""
        return self._client.request("POST", f"/recipients/phone_groups/config/{config_id}", files={"file": file})

    def update_recipients_phone_groups_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified phone group configuration."""
        return self._client.request("PUT", f"/recipients/phone_groups/config/{config_id}", json={"data": config})

    def delete_recipients_phone_groups_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified phone group configuration."""
        return self._client.request("DELETE", f"/recipients/phone_groups/config/{config_id}")
