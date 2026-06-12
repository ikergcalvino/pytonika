from typing import Any

from ._base import Endpoint


class PackageManager(Endpoint):
    def get_package_manager_all_packages_status(self) -> dict[str, Any]:
        """Returns the status of all packages."""
        endpoint = "/package_manager/all_packages/status"

        return self._api_client.get(endpoint)

    def get_package_manager_installed_packages_status(self) -> dict[str, Any]:
        """Returns the status of installed packages. DEPRECATED."""
        endpoint = "/package_manager/installed_packages/status"

        return self._api_client.get(endpoint)

    def get_package_manager_pending_packages_status(self) -> dict[str, Any]:
        """Returns the status of pending packages. DEPRECATED."""
        endpoint = "/package_manager/pending_packages/status"

        return self._api_client.get(endpoint)

    def get_package_manager_available_packages_status(self) -> dict[str, Any]:
        """Returns the status of packages available to be installed. DEPRECATED."""
        endpoint = "/package_manager/available_packages/status"

        return self._api_client.get(endpoint)

    def get_package_manager_language_packages_status(self) -> dict[str, Any]:
        """Returns language packages available to be installed. DEPRECATED."""
        endpoint = "/package_manager/language_packages/status"

        return self._api_client.get(endpoint)

    def get_package_manager_repository_link_options(self) -> dict[str, Any]:
        """Returns package manager options."""
        endpoint = "/package_manager/repository_link/options"

        return self._api_client.get(endpoint)

    def package_manager_upload_package(self, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads a zipped package to the device."""
        endpoint = "/package_manager/actions/upload_package"

        return self._api_client.post(endpoint, data={"data": data})

    def package_manager_install_package(self, data: dict[str, Any]) -> dict[str, Any]:
        """Installs a package."""
        endpoint = "/package_manager/actions/install_package"

        return self._api_client.post(endpoint, data={"data": data})

    def package_manager_update_package(self, data: dict[str, Any]) -> dict[str, Any]:
        """Upgrade a package from the server if possible."""
        endpoint = "/package_manager/actions/update_package"

        return self._api_client.post(endpoint, data={"data": data})

    def package_manager_remove_package(self, data: dict[str, Any]) -> dict[str, Any]:
        """Deletes the specified package."""
        endpoint = "/package_manager/actions/remove_package"

        return self._api_client.post(endpoint, data={"data": data})

    def package_manager_delete_install_files(self, data: dict[str, Any]) -> dict[str, Any]:
        """Deletes the uploaded package install files from the device."""
        endpoint = "/package_manager/actions/delete_install_files"

        return self._api_client.post(endpoint, data={"data": data})

    def package_manager_install_multiple_packages(self, data: dict[str, Any]) -> dict[str, Any]:
        """Starts the installation of multiple packages."""
        endpoint = "/package_manager/actions/install_multiple_packages"

        return self._api_client.post(endpoint, data={"data": data})

    def package_manager_remove_multiple_packages(self, data: dict[str, Any]) -> dict[str, Any]:
        """Starts the removal of multiple packages."""
        endpoint = "/package_manager/actions/remove_multiple_packages"

        return self._api_client.post(endpoint, data={"data": data})

    def package_manager_update_multiple_packages(self, data: dict[str, Any]) -> dict[str, Any]:
        """Starts the upgrade of multiple packages."""
        endpoint = "/package_manager/actions/update_multiple_packages"

        return self._api_client.post(endpoint, data={"data": data})

    def get_package_manager_restore_config(self) -> dict[str, Any]:
        """Returns package restore configurations."""
        endpoint = "/package_manager/restore/config"

        return self._api_client.get(endpoint)

    def update_package_manager_restore_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates package restore configurations."""
        endpoint = "/package_manager/restore/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_package_manager_restore_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Return package restore configuration."""
        endpoint = f"/package_manager/restore/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_package_manager_restore_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Update package restore configuration."""
        endpoint = f"/package_manager/restore/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
