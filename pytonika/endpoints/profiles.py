from typing import Any

from ._base import Endpoint


class Profiles(Endpoint):
    def get_profiles_scheduler_config(self) -> dict[str, Any]:
        """Returns all Profiles Scheduler configurations."""
        endpoint = "/profiles/scheduler/config"

        return self._api_client.get(endpoint)

    def create_profiles_scheduler_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Profiles Scheduler configuration."""
        endpoint = "/profiles/scheduler/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def update_profiles_scheduler_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Profiles Scheduler configurations."""
        endpoint = "/profiles/scheduler/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_profiles_scheduler_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified Profiles Scheduler configurations."""
        return [self.delete_profiles_scheduler_config_by_id(scheduler_id) for scheduler_id in config]

    def get_profiles_scheduler_config_by_id(self, scheduler_id: str) -> dict[str, Any]:
        """Returns the specified Profiles Scheduler configuration."""
        endpoint = f"/profiles/scheduler/config/{scheduler_id}"

        return self._api_client.get(endpoint)

    def update_profiles_scheduler_config_by_id(self, scheduler_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Profiles Scheduler configuration."""
        endpoint = f"/profiles/scheduler/config/{scheduler_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def delete_profiles_scheduler_config_by_id(self, scheduler_id: str) -> dict[str, Any]:
        """Deletes the specified Profiles Scheduler configuration."""
        endpoint = f"/profiles/scheduler/config/{scheduler_id}"

        return self._api_client.delete(endpoint)

    def get_profiles_scheduler_global(self) -> dict[str, Any]:
        """Returns Profiles Scheduler general configuration."""
        endpoint = "/profiles/scheduler/global"

        return self._api_client.get(endpoint)

    def update_profiles_scheduler_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Profiles Scheduler general configuration."""
        endpoint = "/profiles/scheduler/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_profiles_status(self) -> dict[str, Any]:
        """Get current profile in use."""
        endpoint = "/profiles/status"

        return self._api_client.get(endpoint)

    def get_profiles_config(self) -> dict[str, Any]:
        """Returns all profiles configurations."""
        endpoint = "/profiles/config"

        return self._api_client.get(endpoint)

    def create_profiles_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates profile configuration."""
        endpoint = "/profiles/config"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def delete_profiles_config(self, config: list[str]) -> list[dict[str, Any]]:
        """Deletes specified profiles configurations."""
        return [self.delete_profiles_config_by_id(profile_id) for profile_id in config]

    def get_profiles_config_by_id(self, profile_id: str) -> dict[str, Any]:
        """Returns specified profiles configuration."""
        endpoint = f"/profiles/config/{profile_id}"

        return self._api_client.get(endpoint)

    def delete_profiles_config_by_id(self, profile_id: str) -> dict[str, Any]:
        """Deletes specified profiles configuration."""
        endpoint = f"/profiles/config/{profile_id}"

        return self._api_client.delete(endpoint)

    def profiles_apply_profile(self, data: dict[str, Any]) -> dict[str, Any]:
        """Applies provided profile."""
        endpoint = "/profiles/actions/apply_profile"

        return self._api_client.post(endpoint, data={"data": data})
