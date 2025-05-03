from .router import Router


class RUT956(Router):
    def __init__(self, base_url: str):
        super().__init__(base_url)

    def __getattr__(self, attr):
        for endpoint in []:

            if hasattr(endpoint, attr):
                return getattr(endpoint, attr)

        return super().__getattr__(attr)
