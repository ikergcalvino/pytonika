import ssl

from . import devices
from ._client import APIClient
from .devices import AccessPoint, Gateway, Router, Switch

ISSUES_URL = "https://github.com/ikergcalvino/pytonika/issues/new/choose"


def connect(
    base_url: str,
    *,
    timeout: float = 10.0,
    verify: bool | ssl.SSLContext = True,
) -> Router | Gateway | AccessPoint | Switch:
    """Identifies the device at ``base_url`` and returns an instance of its model class.

    The model is read from the unauthenticated status endpoint, so no credentials are needed.

    Raises ``ValueError`` if the device does not report its model, or reports a model this version of Pytonika does
    not support, and the usual ``httpx`` exceptions if it cannot be reached.
    """
    probe = APIClient(base_url, timeout=timeout, verify=verify)

    try:
        response = probe.request("GET", "/unauthorized/status")
    finally:
        probe.close()

    model = str((response.get("data") or {}).get("device_model") or "").upper()

    if not model:
        raise ValueError(f"The device at {base_url} did not report its model: {response}")

    if model not in devices.__all__:
        raise ValueError(
            f"Unsupported device model {model!r} at {base_url}. Use the generic class of its family (Router, "
            f"Gateway, AccessPoint or Switch), or request support for it at {ISSUES_URL}"
        )

    device_class: type[Router | Gateway | AccessPoint | Switch] = getattr(devices, model)

    return device_class(base_url, timeout=timeout, verify=verify)
