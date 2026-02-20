from ._base import Endpoint


class System(Endpoint):

    def system_actions_change_password_firstlogin(self, config: dict[str, object]) -> dict[str, object]:
        endpoint = "/system/actions/change_password_firstlogin"

        data = {"data": config}

        return self._api_client.post(endpoint, data=data)

    def system_actions_reboot(self) -> dict[str, object]:
        endpoint = "/system/actions/reboot"

        return self._api_client.post(endpoint)
