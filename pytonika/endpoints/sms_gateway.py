from typing import Any

from ._endpoint import Endpoint


class SMSGateway(Endpoint):
    def get_sms_gateway_auto_reply_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Auto Reply configuration in an array."""
        return self._client.request("GET", "/sms_gateway/auto_reply/config", params={"all_options": all_options})

    def update_sms_gateway_auto_reply_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Auto Reply configuration in an array."""
        return self._client.request("PUT", "/sms_gateway/auto_reply/config", json={"data": config})

    def get_sms_gateway_auto_reply_config_by_id(
        self, auto_reply_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns Auto Reply configuration."""
        return self._client.request(
            "GET", f"/sms_gateway/auto_reply/config/{auto_reply_id}", params={"all_options": all_options}
        )

    def update_sms_gateway_auto_reply_config_by_id(self, auto_reply_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Auto Reply configuration."""
        return self._client.request("PUT", f"/sms_gateway/auto_reply/config/{auto_reply_id}", json={"data": config})

    def get_sms_gateway_email_to_sms_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Email to SMS configuration in an array."""
        return self._client.request("GET", "/sms_gateway/email_to_sms/config", params={"all_options": all_options})

    def update_sms_gateway_email_to_sms_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Email to SMS configuration in an array."""
        return self._client.request("PUT", "/sms_gateway/email_to_sms/config", json={"data": config})

    def get_sms_gateway_email_to_sms_config_by_id(
        self, email_to_sms_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns Email to SMS configuration."""
        return self._client.request(
            "GET", f"/sms_gateway/email_to_sms/config/{email_to_sms_id}", params={"all_options": all_options}
        )

    def update_sms_gateway_email_to_sms_config_by_id(
        self, email_to_sms_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates Email to SMS configuration."""
        return self._client.request("PUT", f"/sms_gateway/email_to_sms/config/{email_to_sms_id}", json={"data": config})

    def get_sms_gateway_post_get_config(self) -> dict[str, Any]:
        """Returns Mobile Post/Get configuration in an array."""
        return self._client.request("GET", "/sms_gateway/post_get/config")

    def update_sms_gateway_post_get_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates Mobile Post/Get configuration in an array."""
        return self._client.request("PUT", "/sms_gateway/post_get/config", json={"data": config})

    def get_sms_gateway_post_get_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns Mobile Post/Get configuration."""
        return self._client.request("GET", f"/sms_gateway/post_get/config/{config_id}")

    def update_sms_gateway_post_get_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Mobile Post/Get configuration."""
        return self._client.request("PUT", f"/sms_gateway/post_get/config/{config_id}", json={"data": config})

    def get_sms_gateway_sms_forwarding_to_http_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns SMS Forwarding to HTTP configuration in an array."""
        return self._client.request(
            "GET", "/sms_gateway/sms_forwarding/to_http/config", params={"all_options": all_options}
        )

    def update_sms_gateway_sms_forwarding_to_http_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SMS Forwarding to HTTP configuration in an array."""
        return self._client.request("PUT", "/sms_gateway/sms_forwarding/to_http/config", json={"data": config})

    def get_sms_gateway_sms_forwarding_to_http_config_by_id(
        self, forwarding_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns SMS Forwarding to HTTP configuration."""
        return self._client.request(
            "GET", f"/sms_gateway/sms_forwarding/to_http/config/{forwarding_id}", params={"all_options": all_options}
        )

    def update_sms_gateway_sms_forwarding_to_http_config_by_id(
        self, forwarding_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates SMS Forwarding to HTTP configuration."""
        return self._client.request(
            "PUT", f"/sms_gateway/sms_forwarding/to_http/config/{forwarding_id}", json={"data": config}
        )

    def get_sms_gateway_sms_forwarding_to_sms_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns SMS Forwarding to SMS configuration in an array."""
        return self._client.request(
            "GET", "/sms_gateway/sms_forwarding/to_sms/config", params={"all_options": all_options}
        )

    def update_sms_gateway_sms_forwarding_to_sms_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SMS Forwarding to SMS configuration in an array."""
        return self._client.request("PUT", "/sms_gateway/sms_forwarding/to_sms/config", json={"data": config})

    def get_sms_gateway_sms_forwarding_to_sms_config_by_id(
        self, forwarding_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns SMS Forwarding to SMS configuration."""
        return self._client.request(
            "GET", f"/sms_gateway/sms_forwarding/to_sms/config/{forwarding_id}", params={"all_options": all_options}
        )

    def update_sms_gateway_sms_forwarding_to_sms_config_by_id(
        self, forwarding_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates SMS Forwarding to SMS configuration."""
        return self._client.request(
            "PUT", f"/sms_gateway/sms_forwarding/to_sms/config/{forwarding_id}", json={"data": config}
        )

    def get_sms_gateway_sms_forwarding_to_smtp_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns SMS Forwarding to SMTP configuration in an array."""
        return self._client.request(
            "GET", "/sms_gateway/sms_forwarding/to_smtp/config", params={"all_options": all_options}
        )

    def update_sms_gateway_sms_forwarding_to_smtp_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates SMS Forwarding to SMTP configuration in an array."""
        return self._client.request("PUT", "/sms_gateway/sms_forwarding/to_smtp/config", json={"data": config})

    def get_sms_gateway_sms_forwarding_to_smtp_config_by_id(
        self, forwarding_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns SMS Forwarding to SMTP configuration."""
        return self._client.request(
            "GET", f"/sms_gateway/sms_forwarding/to_smtp/config/{forwarding_id}", params={"all_options": all_options}
        )

    def update_sms_gateway_sms_forwarding_to_smtp_config_by_id(
        self, forwarding_id: str, config: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates SMS Forwarding to SMTP configuration."""
        return self._client.request(
            "PUT", f"/sms_gateway/sms_forwarding/to_smtp/config/{forwarding_id}", json={"data": config}
        )
