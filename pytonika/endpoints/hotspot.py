from typing import Any, Literal

from ._endpoint import Endpoint, File


class Hotspot(Endpoint):
    def get_hotspot_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Hotspot configurations."""
        return self._client.request("GET", "/hotspot/config", params={"all_options": all_options})

    def create_hotspot_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Hotspot configuration."""
        return self._client.request("POST", "/hotspot/config", json={"data": config})

    def update_hotspot_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Hotspot configurations."""
        return self._client.request("PUT", "/hotspot/config", json={"data": config})

    def delete_hotspot_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Hotspot configurations."""
        return self._client.request("DELETE", "/hotspot/config", json={"data": config})

    def get_hotspot_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Hotspot configuration."""
        return self._client.request("GET", f"/hotspot/config/{config_id}", params={"all_options": all_options})

    def upload_hotspot_config_by_id(
        self, config_id: str, file: File, *, option: Literal["sslcafile", "sslcertfile", "sslkeyfile"] | None = None
    ) -> dict[str, Any]:
        """Uploads certificates."""
        return self._client.request(
            "POST", f"/hotspot/config/{config_id}", files={"file": file}, form={"option": option}
        )

    def update_hotspot_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Hotspot configuration."""
        return self._client.request("PUT", f"/hotspot/config/{config_id}", json={"data": config})

    def delete_hotspot_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Hotspot configuration."""
        return self._client.request("DELETE", f"/hotspot/config/{config_id}")

    def get_hotspot_groups_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Hotspot User Group configurations."""
        return self._client.request("GET", "/hotspot/groups/config", params={"all_options": all_options})

    def create_hotspot_groups_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Hotspot User Group configuration."""
        return self._client.request("POST", "/hotspot/groups/config", json={"data": config})

    def update_hotspot_groups_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Hotspot User Group configurations."""
        return self._client.request("PUT", "/hotspot/groups/config", json={"data": config})

    def delete_hotspot_groups_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Hotspot User Group configurations."""
        return self._client.request("DELETE", "/hotspot/groups/config", json={"data": config})

    def get_hotspot_groups_config_by_id(self, group_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Hotspot User Group configuration."""
        return self._client.request("GET", f"/hotspot/groups/config/{group_id}", params={"all_options": all_options})

    def update_hotspot_groups_config_by_id(self, group_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Hotspot User Group configuration."""
        return self._client.request("PUT", f"/hotspot/groups/config/{group_id}", json={"data": config})

    def delete_hotspot_groups_config_by_id(self, group_id: str) -> dict[str, Any]:
        """Deletes the specified Hotspot User Group configuration."""
        return self._client.request("DELETE", f"/hotspot/groups/config/{group_id}")

    def get_hotspot_images_config_by_id(self, image_id: str) -> dict[str, Any]:
        """Returns specified Hotspot theme images."""
        return self._client.request("GET", f"/hotspot/images/config/{image_id}")

    def update_hotspot_images_config_by_id(self, image_id: str, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Hotspot theme images."""
        return self._client.request("PUT", f"/hotspot/images/config/{image_id}", json={"data": config})

    def get_hotspot_logs_status(self) -> dict[str, Any]:
        """Fetches logs of Hotspot from database."""
        return self._client.request("GET", "/hotspot/logs/status")

    def get_hotspot_options(self) -> dict[str, Any]:
        """Returns all available profile names."""
        return self._client.request("GET", "/hotspot/options")

    def get_hotspot_options_by_id(self, option_id: str) -> dict[str, Any]:
        """Returns specified profile options."""
        return self._client.request("GET", f"/hotspot/options/{option_id}")

    def get_hotspot_registered_users_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Hotspot Self-Registered Users configurations."""
        return self._client.request("GET", "/hotspot/registered_users/config", params={"all_options": all_options})

    def update_hotspot_registered_users_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Hotspot Self-Registered Users configurations."""
        return self._client.request("PUT", "/hotspot/registered_users/config", json={"data": config})

    def delete_hotspot_registered_users_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Hotspot Self-Registered Users configurations."""
        return self._client.request("DELETE", "/hotspot/registered_users/config", json={"data": config})

    def get_hotspot_registered_users_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Hotspot Self-Registered Users configuration."""
        return self._client.request(
            "GET", f"/hotspot/registered_users/config/{config_id}", params={"all_options": all_options}
        )

    def update_hotspot_registered_users_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Hotspot Self-Registered Users configuration."""
        return self._client.request("PUT", f"/hotspot/registered_users/config/{config_id}", json={"data": config})

    def delete_hotspot_registered_users_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Hotspot Self-Registered Users configuration."""
        return self._client.request("DELETE", f"/hotspot/registered_users/config/{config_id}")

    def get_hotspot_sms_users_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Hotspot SMS Users configurations."""
        return self._client.request("GET", "/hotspot/sms_users/config", params={"all_options": all_options})

    def update_hotspot_sms_users_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Hotspot SMS Users configurations."""
        return self._client.request("PUT", "/hotspot/sms_users/config", json={"data": config})

    def delete_hotspot_sms_users_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Hotspot SMS Users configurations."""
        return self._client.request("DELETE", "/hotspot/sms_users/config", json={"data": config})

    def get_hotspot_sms_users_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Hotspot SMS Users configuration."""
        return self._client.request(
            "GET", f"/hotspot/sms_users/config/{config_id}", params={"all_options": all_options}
        )

    def update_hotspot_sms_users_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Hotspot SMS Users configuration."""
        return self._client.request("PUT", f"/hotspot/sms_users/config/{config_id}", json={"data": config})

    def delete_hotspot_sms_users_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Hotspot SMS Users configuration."""
        return self._client.request("DELETE", f"/hotspot/sms_users/config/{config_id}")

    def get_hotspot_status(self) -> dict[str, Any]:
        """Returns Hotspot status."""
        return self._client.request("GET", "/hotspot/status")

    def get_hotspot_status_by_id(self, status_id: str) -> dict[str, Any]:
        """Returns specified Hotspot instance status."""
        return self._client.request("GET", f"/hotspot/status/{status_id}")

    def get_hotspot_themes_config(self) -> dict[str, Any]:
        """Returns all installed/uploaded Hotspot themes."""
        return self._client.request("GET", "/hotspot/themes/config")

    def upload_hotspot_themes_config(self, file: File) -> dict[str, Any]:
        """Uploads custom Hotspot theme."""
        return self._client.request("POST", "/hotspot/themes/config", files={"file": file})

    def update_hotspot_themes_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates settings of multiple Hotspot themes."""
        return self._client.request("PUT", "/hotspot/themes/config", json={"data": config})

    def delete_hotspot_themes_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes uploaded custom Hotspot theme."""
        return self._client.request("DELETE", "/hotspot/themes/config", json={"data": config})

    def get_hotspot_themes_config_by_id(self, theme_id: str) -> dict[str, Any]:
        """Returns information about a single installed/uploaded Hotspot theme."""
        return self._client.request("GET", f"/hotspot/themes/config/{theme_id}")

    def update_hotspot_themes_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates settings of the specified Hotspot theme."""
        return self._client.request("PUT", f"/hotspot/themes/config/{config_id}", json={"data": config})

    def delete_hotspot_themes_config_by_id(self, theme_id: str) -> dict[str, Any]:
        """Deletes uploaded custom Hotspot theme."""
        return self._client.request("DELETE", f"/hotspot/themes/config/{theme_id}")

    def get_hotspot_themes_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Hotspot Landing Page configuration."""
        return self._client.request("GET", "/hotspot/themes/global", params={"all_options": all_options})

    def update_hotspot_themes_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Hotspot Landing Page configuration."""
        return self._client.request("PUT", "/hotspot/themes/global", json={"data": config})

    def get_hotspot_themes_options(self) -> dict[str, Any]:
        """Returns all possible Hotspot theme file names."""
        return self._client.request("GET", "/hotspot/themes/options")

    def hotspot_themes_actions_download(self, theme_id: str) -> bytes | dict[str, Any]:
        """Downloads specified Hotspot theme."""
        return self._client.request("POST", f"/hotspot/themes/{theme_id}/actions/download", download=True)

    def hotspot_themes_actions_reset(self, theme_id: str, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Resets the specified Hotspot theme file to default."""
        return self._client.request(
            "POST", f"/hotspot/themes/{theme_id}/actions/reset", json=None if data is None else {"data": data}
        )

    def get_hotspot_themes_file_by_id(self, theme_id: str, file_id: str) -> dict[str, Any]:
        """Returns specified file contents of the specified Hotspot theme."""
        return self._client.request("GET", f"/hotspot/themes/{theme_id}/config/{file_id}")

    def update_hotspot_themes_file_by_id(self, theme_id: str, file_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified file contents of the specified Hotspot theme."""
        return self._client.request("PUT", f"/hotspot/themes/{theme_id}/config/{file_id}", json={"data": config})

    def hotspot_user_management_actions_logout_user(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Logs out user identified by his MAC address."""
        return self._client.request(
            "POST", "/hotspot/user_management/actions/logout_user", json=None if data is None else {"data": data}
        )

    def get_hotspot_user_management_config(self) -> dict[str, Any]:
        """Returns all Hotspot registered users from database."""
        return self._client.request("GET", "/hotspot/user_management/config")

    def delete_hotspot_user_management_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Deletes specified Hotspot registered users from database."""
        return self._client.request("DELETE", "/hotspot/user_management/config", json={"data": config})

    def get_hotspot_user_management_config_by_id(self, user_id: str, *, type: str | None = None) -> dict[str, Any]:
        """Returns the specified Hotspot registered user entry from database."""
        return self._client.request("GET", f"/hotspot/user_management/config/{user_id}", params={"type": type})

    def delete_hotspot_user_management_config_by_id(
        self, user_id: str, config: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Deletes the specified Hotspot registered user entry from database."""
        return self._client.request(
            "DELETE", f"/hotspot/user_management/config/{user_id}", json=None if config is None else {"data": config}
        )

    def get_hotspot_user_management_status(self, *, period: str | None = None) -> dict[str, Any]:
        """Returns all Hotspot active users."""
        return self._client.request("GET", "/hotspot/user_management/status", params={"period": period})

    def get_hotspot_user_management_status_by_id(self, user_id: str) -> dict[str, Any]:
        """Returns the specified Hotspot active user."""
        return self._client.request("GET", f"/hotspot/user_management/status/{user_id}")

    def get_hotspot_users_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Hotspot Users configurations."""
        return self._client.request("GET", "/hotspot/users/config", params={"all_options": all_options})

    def create_hotspot_users_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Hotspot Users configuration."""
        return self._client.request("POST", "/hotspot/users/config", json={"data": config})

    def update_hotspot_users_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Hotspot Users configurations."""
        return self._client.request("PUT", "/hotspot/users/config", json={"data": config})

    def delete_hotspot_users_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Hotspot Users configurations."""
        return self._client.request("DELETE", "/hotspot/users/config", json={"data": config})

    def get_hotspot_users_config_by_id(self, user_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the specified Hotspot Users configuration."""
        return self._client.request("GET", f"/hotspot/users/config/{user_id}", params={"all_options": all_options})

    def update_hotspot_users_config_by_id(self, user_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Hotspot Users configuration."""
        return self._client.request("PUT", f"/hotspot/users/config/{user_id}", json={"data": config})

    def delete_hotspot_users_config_by_id(self, user_id: str) -> dict[str, Any]:
        """Deletes the specified Hotspot Users configuration."""
        return self._client.request("DELETE", f"/hotspot/users/config/{user_id}")
