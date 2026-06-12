from typing import Any

from ._base import Endpoint


class SMSGateway(Endpoint):
    def get_sms_gateway_email_to_sms_config(self) -> dict[str, Any]:
        """Returns Email to SMS configuration in an array."""
        endpoint = "/sms_gateway/email_to_sms/config"

        return self._api_client.get(endpoint)

    def update_sms_gateway_email_to_sms_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Email to SMS configuration in an array."""
        endpoint = "/sms_gateway/email_to_sms/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_sms_gateway_email_to_sms_config_by_id(self, email_to_sms_id: str) -> dict[str, Any]:
        """Returns Email to SMS configuration."""
        endpoint = f"/sms_gateway/email_to_sms/config/{email_to_sms_id}"

        return self._api_client.get(endpoint)

    def update_sms_gateway_email_to_sms_config_by_id(
        self, email_to_sms_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates Email to SMS configuration."""
        endpoint = f"/sms_gateway/email_to_sms/config/{email_to_sms_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_sms_gateway_sms_forwarding_to_http_config(self) -> dict[str, Any]:
        """Returns SMS Forwarding to HTTP configuration in an array."""
        endpoint = "/sms_gateway/sms_forwarding/to_http/config"

        return self._api_client.get(endpoint)

    def update_sms_gateway_sms_forwarding_to_http_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SMS Forwarding to HTTP configuration in an array."""
        endpoint = "/sms_gateway/sms_forwarding/to_http/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_sms_gateway_sms_forwarding_to_http_config_by_id(self, forwarding_id: str) -> dict[str, Any]:
        """Returns SMS Forwarding to HTTP configuration."""
        endpoint = f"/sms_gateway/sms_forwarding/to_http/config/{forwarding_id}"

        return self._api_client.get(endpoint)

    def update_sms_gateway_sms_forwarding_to_http_config_by_id(
        self, forwarding_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates SMS Forwarding to HTTP configuration."""
        endpoint = f"/sms_gateway/sms_forwarding/to_http/config/{forwarding_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_sms_gateway_sms_forwarding_to_sms_config(self) -> dict[str, Any]:
        """Returns SMS Forwarding to SMS configuration in an array."""
        endpoint = "/sms_gateway/sms_forwarding/to_sms/config"

        return self._api_client.get(endpoint)

    def update_sms_gateway_sms_forwarding_to_sms_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SMS Forwarding to SMS configuration in an array."""
        endpoint = "/sms_gateway/sms_forwarding/to_sms/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_sms_gateway_sms_forwarding_to_sms_config_by_id(self, forwarding_id: str) -> dict[str, Any]:
        """Returns SMS Forwarding to SMS configuration."""
        endpoint = f"/sms_gateway/sms_forwarding/to_sms/config/{forwarding_id}"

        return self._api_client.get(endpoint)

    def update_sms_gateway_sms_forwarding_to_sms_config_by_id(
        self, forwarding_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates SMS Forwarding to SMS configuration."""
        endpoint = f"/sms_gateway/sms_forwarding/to_sms/config/{forwarding_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_sms_gateway_sms_forwarding_to_smtp_config(self) -> dict[str, Any]:
        """Returns SMS Forwarding to SMTP configuration in an array."""
        endpoint = "/sms_gateway/sms_forwarding/to_smtp/config"

        return self._api_client.get(endpoint)

    def update_sms_gateway_sms_forwarding_to_smtp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SMS Forwarding to SMTP configuration in an array."""
        endpoint = "/sms_gateway/sms_forwarding/to_smtp/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_sms_gateway_sms_forwarding_to_smtp_config_by_id(self, forwarding_id: str) -> dict[str, Any]:
        """Returns SMS Forwarding to SMTP configuration."""
        endpoint = f"/sms_gateway/sms_forwarding/to_smtp/config/{forwarding_id}"

        return self._api_client.get(endpoint)

    def update_sms_gateway_sms_forwarding_to_smtp_config_by_id(
        self, forwarding_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates SMS Forwarding to SMTP configuration."""
        endpoint = f"/sms_gateway/sms_forwarding/to_smtp/config/{forwarding_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_sms_gateway_auto_reply_config(self) -> dict[str, Any]:
        """Returns Auto Reply configuration in an array."""
        endpoint = "/sms_gateway/auto_reply/config"

        return self._api_client.get(endpoint)

    def update_sms_gateway_auto_reply_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Auto Reply configuration in an array."""
        endpoint = "/sms_gateway/auto_reply/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_sms_gateway_auto_reply_config_by_id(self, auto_reply_id: str) -> dict[str, Any]:
        """Returns Auto Reply configuration."""
        endpoint = f"/sms_gateway/auto_reply/config/{auto_reply_id}"

        return self._api_client.get(endpoint)

    def update_sms_gateway_auto_reply_config_by_id(self, auto_reply_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Auto Reply configuration."""
        endpoint = f"/sms_gateway/auto_reply/config/{auto_reply_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
