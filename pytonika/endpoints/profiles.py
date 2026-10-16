from typing import Any

from ._endpoint import Endpoint


class Profiles(Endpoint):
    def profiles_actions_apply_profile(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Applies provided profile."""
        return self._client.request(
            "POST", "/profiles/actions/apply_profile", json=None if data is None else {"data": data}
        )

    def get_profiles_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all profiles configurations."""
        return self._client.request("GET", "/profiles/config", params={"all_options": all_options})

    def create_profiles_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates profile configuration."""
        return self._client.request("POST", "/profiles/config", json={"data": config})

    def delete_profiles_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified profiles configurations."""
        return self._client.request("DELETE", "/profiles/config", json={"data": config})

    def get_profiles_config_by_id(self, profile_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns specified profiles configuration."""
        return self._client.request("GET", f"/profiles/config/{profile_id}", params={"all_options": all_options})

    def delete_profiles_config_by_id(self, profile_id: str) -> dict[str, Any]:
        """Deletes specified profiles configuration."""
        return self._client.request("DELETE", f"/profiles/config/{profile_id}")

    def get_profiles_scheduler_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns all Profiles Scheduler configurations."""
        return self._client.request("GET", "/profiles/scheduler/config", params={"all_options": all_options})

    def create_profiles_scheduler_config(self, config: dict[str, Any]) -> dict[str, Any]:
        """Creates Profiles Scheduler configuration."""
        return self._client.request("POST", "/profiles/scheduler/config", json={"data": config})

    def update_profiles_scheduler_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates specified Profiles Scheduler configurations."""
        return self._client.request("PUT", "/profiles/scheduler/config", json={"data": config})

    def delete_profiles_scheduler_config(self, config: list[str]) -> dict[str, Any]:
        """Deletes specified Profiles Scheduler configurations."""
        return self._client.request("DELETE", "/profiles/scheduler/config", json={"data": config})

    def get_profiles_scheduler_config_by_id(
        self, scheduler_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Returns the specified Profiles Scheduler configuration."""
        return self._client.request(
            "GET", f"/profiles/scheduler/config/{scheduler_id}", params={"all_options": all_options}
        )

    def update_profiles_scheduler_config_by_id(self, scheduler_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the specified Profiles Scheduler configuration."""
        return self._client.request("PUT", f"/profiles/scheduler/config/{scheduler_id}", json={"data": config})

    def delete_profiles_scheduler_config_by_id(self, scheduler_id: str) -> dict[str, Any]:
        """Deletes the specified Profiles Scheduler configuration."""
        return self._client.request("DELETE", f"/profiles/scheduler/config/{scheduler_id}")

    def get_profiles_scheduler_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns Profiles Scheduler general configuration."""
        return self._client.request("GET", "/profiles/scheduler/global", params={"all_options": all_options})

    def update_profiles_scheduler_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates Profiles Scheduler general configuration."""
        return self._client.request("PUT", "/profiles/scheduler/global", json={"data": config})

    def get_profiles_status(self) -> dict[str, Any]:
        """Get current profile in use."""
        return self._client.request("GET", "/profiles/status")
