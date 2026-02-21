from .gateway import Gateway


class TRB245(Gateway):
    def __init__(self, base_url: str, *, timeout: float = 10.0, verify: bool = True) -> None:
        super().__init__(base_url, timeout=timeout, verify=verify)
