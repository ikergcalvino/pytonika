from typing import Any

from ._endpoint import Endpoint, File


class Docker(Endpoint):
    def docker_containers_actions_create(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Creates a new container."""
        return self._client.request(
            "POST", "/docker/containers/actions/create", json=None if data is None else {"data": data}
        )

    def docker_containers_actions_get_logs(self, data: dict[str, Any] | None = None) -> bytes | dict[str, Any]:
        """Retrieves logs for a container."""
        return self._client.request(
            "POST", "/docker/containers/actions/get_logs", json=None if data is None else {"data": data}, download=True
        )

    def docker_containers_actions_kill(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Kills a container."""
        return self._client.request(
            "POST", "/docker/containers/actions/kill", json=None if data is None else {"data": data}
        )

    def docker_containers_actions_remove(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Removes a container."""
        return self._client.request(
            "POST", "/docker/containers/actions/remove", json=None if data is None else {"data": data}
        )

    def docker_containers_actions_restart(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Restarts a container."""
        return self._client.request(
            "POST", "/docker/containers/actions/restart", json=None if data is None else {"data": data}
        )

    def docker_containers_actions_start(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Starts a container."""
        return self._client.request(
            "POST", "/docker/containers/actions/start", json=None if data is None else {"data": data}
        )

    def docker_containers_actions_stop(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Stops a container."""
        return self._client.request(
            "POST", "/docker/containers/actions/stop", json=None if data is None else {"data": data}
        )

    def docker_containers_actions_update(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Updates a container."""
        return self._client.request(
            "POST", "/docker/containers/actions/update", json=None if data is None else {"data": data}
        )

    def get_docker_containers_status(self) -> dict[str, Any]:
        """Returns the list of containers."""
        return self._client.request("GET", "/docker/containers/status")

    def get_docker_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the general Docker configuration."""
        return self._client.request("GET", "/docker/global", params={"all_options": all_options})

    def update_docker_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the general Docker configuration."""
        return self._client.request("PUT", "/docker/global", json={"data": config})

    def docker_images_actions_create(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Creates a new image."""
        return self._client.request(
            "POST", "/docker/images/actions/create", json=None if data is None else {"data": data}
        )

    def docker_images_actions_load(self) -> dict[str, Any]:
        """Loads an exported image. First, the image must be uploaded using "upload_image" action."""
        return self._client.request("POST", "/docker/images/actions/load")

    def docker_images_actions_remove(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Removes an image."""
        return self._client.request(
            "POST", "/docker/images/actions/remove", json=None if data is None else {"data": data}
        )

    def docker_images_actions_upload_image(self, file: File) -> dict[str, Any]:
        """Uploads an exported image. After upload, "load" action must be called to load the image into docker."""
        return self._client.request("POST", "/docker/images/actions/upload_image", files={"file": file})

    def get_docker_images_status(self) -> dict[str, Any]:
        """Returns the list of images."""
        return self._client.request("GET", "/docker/images/status")

    def docker_login_actions_check_login(self, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Checks the Docker login configuration."""
        return self._client.request(
            "POST", "/docker/login/actions/check_login", json=None if data is None else {"data": data}
        )

    def get_docker_login_config(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the Docker login configuration."""
        return self._client.request("GET", "/docker/login/config", params={"all_options": all_options})

    def update_docker_login_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the Docker login configuration."""
        return self._client.request("PUT", "/docker/login/config", json={"data": config})

    def get_docker_login_config_by_id(self, config_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns the Docker login configuration."""
        return self._client.request("GET", f"/docker/login/config/{config_id}", params={"all_options": all_options})

    def update_docker_login_config_by_id(
        self, config_id: str, config: dict[str, Any], *, all_options: bool | None = None
    ) -> dict[str, Any]:
        """Updates the Docker login configuration."""
        return self._client.request(
            "PUT", f"/docker/login/config/{config_id}", params={"all_options": all_options}, json={"data": config}
        )

    def get_docker_options(self) -> dict[str, Any]:
        """Returns Docker options."""
        return self._client.request("GET", "/docker/options")
