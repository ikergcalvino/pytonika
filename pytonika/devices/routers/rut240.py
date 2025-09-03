from .router import Router


class RUT240(Router):
    def __init__(self, base_url: str) -> None:
        super().__init__(base_url)

        self._endpoints.extend([])

    def __getattr__(self, attr: str):
        for endpoint in self._endpoints:
            if hasattr(endpoint, attr):
                return getattr(endpoint, attr)

        return super().__getattr__(attr)
