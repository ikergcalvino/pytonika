from typing import Any

from ._base import Endpoint


class Docker(Endpoint):
    def get_docker_images_status(self) -> dict[str, Any]:
        """Returns the list of images."""
        endpoint = "/docker/images/status"

        return self._api_client.get(endpoint)

    def docker_images_actions_create(self, data: dict[str, Any]) -> dict[str, Any]:
        """Creates a new image."""
        endpoint = "/docker/images/actions/create"

        return self._api_client.post(endpoint, data={"data": data})

    def docker_images_actions_upload_image(self, data: dict[str, Any]) -> dict[str, Any]:
        """Uploads an exported image. After upload, "load" action must be called to load the image into docker."""
        endpoint = "/docker/images/actions/upload_image"

        return self._api_client.post(endpoint, data={"data": data})

    def docker_images_actions_load(self, data: dict[str, Any]) -> dict[str, Any]:
        """Loads an exported image. First, the image must be uploaded using "upload_image" action."""
        endpoint = "/docker/images/actions/load"

        return self._api_client.post(endpoint, data={"data": data})

    def docker_images_actions_remove(self, data: dict[str, Any]) -> dict[str, Any]:
        """Removes an image."""
        endpoint = "/docker/images/actions/remove"

        return self._api_client.post(endpoint, data={"data": data})

    def get_docker_login_config(self) -> dict[str, Any]:
        """Returns the Docker login configuration."""
        endpoint = "/docker/login/config"

        return self._api_client.get(endpoint)

    def update_docker_login_config(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the Docker login configuration."""
        endpoint = "/docker/login/config"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def get_docker_login_config_by_id(self, config_id: str) -> dict[str, Any]:
        """Returns the Docker login configuration."""
        endpoint = f"/docker/login/config/{config_id}"

        return self._api_client.get(endpoint)

    def update_docker_login_config_by_id(self, config_id: str, config: dict[str, Any]) -> dict[str, Any]:
        """Updates the Docker login configuration."""
        endpoint = f"/docker/login/config/{config_id}"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)

    def docker_login_actions_check_login(self) -> dict[str, Any]:
        """Checks the Docker login configuration."""
        endpoint = "/docker/login/actions/check_login"

        return self._api_client.post(endpoint)

    def get_docker_containers_status(self) -> dict[str, Any]:
        """Returns the list of containers."""
        endpoint = "/docker/containers/status"

        return self._api_client.get(endpoint)

    def docker_containers_actions_create(self, data: dict[str, Any]) -> dict[str, Any]:
        """Creates a new container."""
        endpoint = "/docker/containers/actions/create"

        return self._api_client.post(endpoint, data={"data": data})

    def docker_containers_actions_update(self, data: dict[str, Any]) -> dict[str, Any]:
        """Updates a container."""
        endpoint = "/docker/containers/actions/update"

        return self._api_client.post(endpoint, data={"data": data})

    def docker_containers_actions_start(self, data: dict[str, Any]) -> dict[str, Any]:
        """Starts a container."""
        endpoint = "/docker/containers/actions/start"

        return self._api_client.post(endpoint, data={"data": data})

    def docker_containers_actions_stop(self, data: dict[str, Any]) -> dict[str, Any]:
        """Stops a container."""
        endpoint = "/docker/containers/actions/stop"

        return self._api_client.post(endpoint, data={"data": data})

    def docker_containers_actions_restart(self, data: dict[str, Any]) -> dict[str, Any]:
        """Restarts a container."""
        endpoint = "/docker/containers/actions/restart"

        return self._api_client.post(endpoint, data={"data": data})

    def docker_containers_actions_kill(self, data: dict[str, Any]) -> dict[str, Any]:
        """Kills a container."""
        endpoint = "/docker/containers/actions/kill"

        return self._api_client.post(endpoint, data={"data": data})

    def docker_containers_actions_remove(self, data: dict[str, Any]) -> dict[str, Any]:
        """Removes a container."""
        endpoint = "/docker/containers/actions/remove"

        return self._api_client.post(endpoint, data={"data": data})

    def docker_containers_actions_get_logs(self, data: dict[str, Any]) -> dict[str, Any]:
        """Retrieves logs for a container."""
        endpoint = "/docker/containers/actions/get_logs"

        return self._api_client.post(endpoint, data={"data": data})

    def get_docker_global(self) -> dict[str, Any]:
        """Returns the general Docker configuration."""
        endpoint = "/docker/global"

        return self._api_client.get(endpoint)

    def update_docker_global(self, config: list[dict[str, Any]]) -> dict[str, Any]:
        """Updates the general Docker configuration."""
        endpoint = "/docker/global"

        data = {"data": config}

        return self._api_client.put(endpoint, data=data)
