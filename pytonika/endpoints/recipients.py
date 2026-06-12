from typing import Any

from ._base import Endpoint


class Recipients(Endpoint):
    def get_recipients_phone_groups_config(self) -> dict[str, Any]:
        """Returns all phone group configurations."""
        endpoint = "/recipients/phone_groups/config"

        return self._api_client.get(endpoint)

    def create_recipients_phone_groups_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates phone group configuration."""
        endpoint = "/recipients/phone_groups/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_recipients_phone_groups_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified phone group configurations."""
        endpoint = "/recipients/phone_groups/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_recipients_phone_groups_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified phone group configurations."""
        return [self.delete_recipients_phone_groups_config_by_id(config_id) for config_id in config]

    def get_recipients_phone_groups_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified phone groups configuration."""
        endpoint = f"/recipients/phone_groups/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_recipients_phone_groups_config_by_id(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads phone numbers list."""
        endpoint = f"/recipients/phone_groups/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_recipients_phone_groups_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified phone group configuration."""
        endpoint = f"/recipients/phone_groups/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_recipients_phone_groups_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified phone group configuration."""
        endpoint = f"/recipients/phone_groups/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_recipients_email_users_config(self) -> dict[str, Any]:
        """Returns all email users configurations."""
        endpoint = "/recipients/email_users/config"

        return self._api_client.get(endpoint)

    def create_recipients_email_users_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates email users configuration."""
        endpoint = "/recipients/email_users/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_recipients_email_users_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified email users configurations."""
        endpoint = "/recipients/email_users/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_recipients_email_users_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified email users configurations."""
        return [self.delete_recipients_email_users_config_by_id(config_id) for config_id in config]

    def get_recipients_email_users_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified email users configuration."""
        endpoint = f"/recipients/email_users/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_recipients_email_users_config_by_id(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads server's CA certificate file."""
        endpoint = f"/recipients/email_users/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_recipients_email_users_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified email users configuration."""
        endpoint = f"/recipients/email_users/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_recipients_email_users_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified email users configuration."""
        endpoint = f"/recipients/email_users/config/{config_id}"

        return self._api_client.delete(endpoint)

    def recipients_email_users_actions_send_email(self, data: dict[str, Any]) -> dict[str, Any]:
        """Send test email."""
        endpoint = "/recipients/email_users/actions/send_email"

        return self._api_client.post(endpoint, data={"data": data})
