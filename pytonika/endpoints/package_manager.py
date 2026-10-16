from typing import Any, Literal

from ._endpoint import Endpoint, File


class PackageManager(Endpoint):
    def package_manager_actions_delete_install_files(self) -> dict[str, Any]:
        """Deletes the uploaded package install files from the device."""
        return self._client.request("POST", "/package_manager/actions/delete_install_files")

    def package_manager_actions_install_multiple_packages(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Starts the installation of multiple packages."""
        return self._client.request(
            "POST", "/package_manager/actions/install_multiple_packages", json=None if data is None else {"data": data}
        )

    def package_manager_actions_install_package(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Installs a package."""
        return self._client.request(
            "POST", "/package_manager/actions/install_package", json=None if data is None else {"data": data}
        )

    def package_manager_actions_remove_multiple_packages(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Starts the removal of multiple packages."""
        return self._client.request(
            "POST", "/package_manager/actions/remove_multiple_packages", json=None if data is None else {"data": data}
        )

    def package_manager_actions_remove_package(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Deletes the specified package."""
        return self._client.request(
            "POST", "/package_manager/actions/remove_package", json=None if data is None else {"data": data}
        )

    def package_manager_actions_update_multiple_packages(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Starts the upgrade of multiple packages."""
        return self._client.request(
            "POST", "/package_manager/actions/update_multiple_packages", json=None if data is None else {"data": data}
        )

    def package_manager_actions_update_package(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Upgrade a package from the server if possible."""
        return self._client.request(
            "POST", "/package_manager/actions/update_package", json=None if data is None else {"data": data}
        )

    def package_manager_actions_upload_package(self, file: File) -> dict[str, Any]:
        """Uploads a zipped package to the device."""
        return self._client.request("POST", "/package_manager/actions/upload_package", files={"file": file})

    def get_package_manager_all_packages_status(
        self, *, refresh_package_list: Literal["0", "1"] | None = None
    ) -> dict[str, Any]:
        """Returns the status of all packages from all feeds."""
        return self._client.request(
            "GET", "/package_manager/all_packages/status", params={"refresh_package_list": refresh_package_list}
        )

    def get_package_manager_all_packages_status_by_id(
        self, status_id: str, *, refresh_package_list: Literal["0", "1"] | None = None
    ) -> dict[str, Any]:
        """Returns the status of all packages for a specific feed."""
        return self._client.request(
            "GET",
            f"/package_manager/all_packages/status/{status_id}",
            params={"refresh_package_list": refresh_package_list},
        )

    def get_package_manager_available_packages_status(
        self, *, refresh_package_list: Literal["0", "1"] | None = None
    ) -> dict[str, Any]:
        """Returns the status of packages available to be installed."""
        return self._client.request(
            "GET", "/package_manager/available_packages/status", params={"refresh_package_list": refresh_package_list}
        )

    def get_package_manager_installed_packages_status(self) -> dict[str, Any]:
        """Returns the status of installed packages."""
        return self._client.request("GET", "/package_manager/installed_packages/status")

    def get_package_manager_language_packages_status(
        self, *, refresh_package_list: Literal["0", "1"] | None = None
    ) -> dict[str, Any]:
        """Returns language packages available to be installed."""
        return self._client.request(
            "GET", "/package_manager/language_packages/status", params={"refresh_package_list": refresh_package_list}
        )

    def get_package_manager_pending_packages_status(self) -> dict[str, Any]:
        """Returns the status of pending packages."""
        return self._client.request("GET", "/package_manager/pending_packages/status")

    def get_package_manager_repository_link_options(self) -> dict[str, Any]:
        """Returns package manager options."""
        return self._client.request("GET", "/package_manager/repository_link/options")

    def get_package_manager_restore_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns package restore configurations."""
        return self._client.request("GET", "/package_manager/restore/config", params={"all_options": all_options})

    def update_package_manager_restore_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates package restore configurations."""
        return self._client.request("PUT", "/package_manager/restore/config", json={"data": config})

    def get_package_manager_restore_config_by_id(
        self, config_id: str, *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Return package restore configuration."""
        return self._client.request(
            "GET", f"/package_manager/restore/config/{config_id}", params={"all_options": all_options}
        )

    def update_package_manager_restore_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update package restore configuration."""
        return self._client.request("PUT", f"/package_manager/restore/config/{config_id}", json={"data": config})
