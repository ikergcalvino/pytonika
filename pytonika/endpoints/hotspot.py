from typing import Any

from ._base import Endpoint


class Hotspot(Endpoint):
    def get_hotspot_themes_global(self) -> dict[str, Any]:
        """Returns Hotspot Landing Page configuration."""
        endpoint = "/hotspot/themes/global"

        return self._api_client.get(endpoint)

    def update_hotspot_themes_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Hotspot Landing Page configuration."""
        endpoint = "/hotspot/themes/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_hotspot_themes_options(self) -> dict[str, Any]:
        """Returns all possible Hotspot theme file names."""
        endpoint = "/hotspot/themes/options"

        return self._api_client.get(endpoint)

    def get_hotspot_themes_config(self) -> dict[str, Any]:
        """Returns all installed/uploaded Hotspot themes."""
        endpoint = "/hotspot/themes/config"

        return self._api_client.get(endpoint)

    def upload_hotspot_theme(self, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads custom Hotspot theme."""
        endpoint = "/hotspot/themes/config"

        return self._api_client.post(endpoint, data={"data": data})

    def delete_hotspot_themes_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes uploaded custom Hotspot theme."""
        return [self.delete_hotspot_themes_config_by_id(theme_id) for theme_id in config]

    def get_hotspot_themes_config_by_id(self, theme_id: str) -> dict[str, Any]:
        """Returns information about a single installed/uploaded Hotspot theme."""
        endpoint = f"/hotspot/themes/config/{theme_id}"

        return self._api_client.get(endpoint)

    def delete_hotspot_themes_config_by_id(self, theme_id: str) -> dict[str, Any]:
        """Deletes uploaded custom Hotspot theme."""
        endpoint = f"/hotspot/themes/config/{theme_id}"

        return self._api_client.delete(endpoint)

    def get_hotspot_theme_file(self, theme_id: str, file_id: str) -> dict[str, Any]:
        """Returns specified file contents of the specified Hotspot theme."""
        endpoint = f"/hotspot/themes/{theme_id}/config/{file_id}"

        return self._api_client.get(endpoint)

    def update_hotspot_theme_file(self, theme_id: str, file_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified file contents of the specified Hotspot theme."""
        endpoint = f"/hotspot/themes/{theme_id}/config/{file_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def download_hotspot_theme(self, theme_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Downloads specified Hotspot theme."""
        endpoint = f"/hotspot/themes/{theme_id}/actions/download"

        return self._api_client.post(endpoint, data={"data": data})

    def reset_hotspot_theme(self, theme_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Resets the specified Hotspot theme file to default."""
        endpoint = f"/hotspot/themes/{theme_id}/actions/reset"

        return self._api_client.post(endpoint, data={"data": data})

    def get_hotspot_images_config_by_id(self, image_id: str) -> dict[str, Any]:
        """Returns specified Hotspot theme images."""
        endpoint = f"/hotspot/images/config/{image_id}"

        return self._api_client.get(endpoint)

    def update_hotspot_images_config_by_id(self, image_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified Hotspot theme images."""
        endpoint = f"/hotspot/images/config/{image_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_hotspot_groups_config(self) -> dict[str, Any]:
        """Returns all Hotspot User Group configurations."""
        endpoint = "/hotspot/groups/config"

        return self._api_client.get(endpoint)

    def create_hotspot_groups_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Hotspot User Group configuration."""
        endpoint = "/hotspot/groups/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_hotspot_groups_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Hotspot User Group configurations."""
        endpoint = "/hotspot/groups/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_hotspot_groups_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Hotspot User Group configurations."""
        return [self.delete_hotspot_groups_config_by_id(group_id) for group_id in config]

    def get_hotspot_groups_config_by_id(self, group_id: str) -> dict[str, Any]:
        """Returns the specified Hotspot User Group configuration."""
        endpoint = f"/hotspot/groups/config/{group_id}"

        return self._api_client.get(endpoint)

    def update_hotspot_groups_config_by_id(self, group_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Hotspot User Group configuration."""
        endpoint = f"/hotspot/groups/config/{group_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_hotspot_groups_config_by_id(self, group_id: str) -> dict[str, Any]:
        """Deletes the specified Hotspot User Group configuration."""
        endpoint = f"/hotspot/groups/config/{group_id}"

        return self._api_client.delete(endpoint)

    def get_hotspot_logs_status(self) -> dict[str, Any]:
        """Fetches logs of Hotspot from database."""
        endpoint = "/hotspot/logs/status"

        return self._api_client.get(endpoint)

    def get_hotspot_status(self) -> dict[str, Any]:
        """Returns Hotspot status."""
        endpoint = "/hotspot/status"

        return self._api_client.get(endpoint)

    def get_hotspot_options(self) -> dict[str, Any]:
        """Returns all available profile names."""
        endpoint = "/hotspot/options"

        return self._api_client.get(endpoint)

    def get_hotspot_options_by_id(self, option_id: str) -> dict[str, Any]:
        """Returns specified profile options."""
        endpoint = f"/hotspot/options/{option_id}"

        return self._api_client.get(endpoint)

    def get_hotspot_config(self) -> dict[str, Any]:
        """Returns all Hotspot configurations."""
        endpoint = "/hotspot/config"

        return self._api_client.get(endpoint)

    def create_hotspot_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Hotspot configuration."""
        endpoint = "/hotspot/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_hotspot_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Hotspot configurations."""
        endpoint = "/hotspot/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_hotspot_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Hotspot configurations."""
        return [self.delete_hotspot_config_by_id(hotspot_id) for hotspot_id in config]

    def get_hotspot_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the specified Hotspot configuration."""
        endpoint = f"/hotspot/config/{config_id}"

        return self._api_client.get(endpoint)

    def upload_hotspot_certificates(self, config_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads certificates."""
        endpoint = f"/hotspot/config/{config_id}"

        return self._api_client.post(endpoint, data={"data": data})

    def update_hotspot_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Hotspot configuration."""
        endpoint = f"/hotspot/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_hotspot_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Deletes the specified Hotspot configuration."""
        endpoint = f"/hotspot/config/{config_id}"

        return self._api_client.delete(endpoint)

    def get_hotspot_user_management_status(self) -> dict[str, Any]:
        """Returns all Hotspot active users."""
        endpoint = "/hotspot/user_management/status"

        return self._api_client.get(endpoint)

    def get_hotspot_user_management_status_by_id(self, user_id: str) -> dict[str, Any]:
        """Returns the specified Hotspot active user."""
        endpoint = f"/hotspot/user_management/status/{user_id}"

        return self._api_client.get(endpoint)

    def get_hotspot_user_management_config(self) -> dict[str, Any]:
        """Returns all Hotspot registered users from database."""
        endpoint = "/hotspot/user_management/config"

        return self._api_client.get(endpoint)

    def delete_hotspot_user_management_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Hotspot registered users from database."""
        return [self.delete_hotspot_user_management_config_by_id(user_id) for user_id in config]

    def get_hotspot_user_management_config_by_id(self, user_id: str) -> dict[str, Any]:
        """Returns the specified Hotspot registered user entry from database."""
        endpoint = f"/hotspot/user_management/config/{user_id}"

        return self._api_client.get(endpoint)

    def delete_hotspot_user_management_config_by_id(self, user_id: str) -> dict[str, Any]:
        """Deletes the specified Hotspot registered user entry from database."""
        endpoint = f"/hotspot/user_management/config/{user_id}"

        return self._api_client.delete(endpoint)

    def hotspot_logout_user(self, data: dict[str, Any]) -> dict[str, Any]:
        """Logs out user identified by his MAC address."""
        endpoint = "/hotspot/user_management/actions/logout_user"

        return self._api_client.post(endpoint, data={"data": data})

    def get_hotspot_users_config(self) -> dict[str, Any]:
        """Returns all Hotspot Users configurations."""
        endpoint = "/hotspot/users/config"

        return self._api_client.get(endpoint)

    def create_hotspot_users_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Hotspot Users configuration."""
        endpoint = "/hotspot/users/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_hotspot_users_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Hotspot Users configurations."""
        endpoint = "/hotspot/users/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_hotspot_users_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Hotspot Users configurations."""
        return [self.delete_hotspot_users_config_by_id(user_id) for user_id in config]

    def get_hotspot_users_config_by_id(self, user_id: str) -> dict[str, Any]:
        """Returns the specified Hotspot Users configuration."""
        endpoint = f"/hotspot/users/config/{user_id}"

        return self._api_client.get(endpoint)

    def update_hotspot_users_config_by_id(self, user_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Hotspot Users configuration."""
        endpoint = f"/hotspot/users/config/{user_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_hotspot_users_config_by_id(self, user_id: str) -> dict[str, Any]:
        """Deletes the specified Hotspot Users configuration."""
        endpoint = f"/hotspot/users/config/{user_id}"

        return self._api_client.delete(endpoint)
