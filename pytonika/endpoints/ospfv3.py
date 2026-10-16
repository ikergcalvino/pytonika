from typing import Any, Literal

from ._endpoint import Endpoint, File


class OSPFv3(Endpoint):
    def get_ospfv3_global(self, *, all_options: bool | None = None) -> dict[str, Any]:
        """Returns OSPFv3 global configuration."""
        return self._client.request("GET", "/ospfv3/global", params={"all_options": all_options})

    def upload_ospfv3_global(
        self, file: File, *, option: Literal["ospf6d_custom_conf"] | None = None
    ) -> dict[str, Any]:
        """Uploads custom OSPFv3 configuration file."""
        return self._client.request("POST", "/ospfv3/global", files={"file": file}, form={"option": option})

    def update_ospfv3_global(self, config: dict[str, Any]) -> dict[str, Any]:
        """Updates specified OSPFv3 global configuration."""
        return self._client.request("PUT", "/ospfv3/global", json={"data": config})
