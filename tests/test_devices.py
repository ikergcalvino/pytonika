import inspect

import pytest

import pytonika
from pytonika import AccessPoint, Gateway, Router, Switch
from pytonika.endpoints._endpoint import Endpoint

from .conftest import BASE_URL

FAMILIES = (Router, Gateway, AccessPoint, Switch)
DEVICE_CLASSES = [getattr(pytonika, name) for name in pytonika.__all__ if name != "__version__"]


def endpoint_attributes(device: object) -> set[str]:
    return {name for name, value in vars(device).items() if isinstance(value, Endpoint)}


def family_of(device_class: type) -> type:
    return next(family for family in FAMILIES if issubclass(device_class, family))


@pytest.mark.parametrize("device_class", DEVICE_CLASSES, ids=lambda cls: cls.__name__)
def test_device_shares_one_client(device_class: type) -> None:
    with device_class(BASE_URL) as device:
        endpoints = [getattr(device, name) for name in endpoint_attributes(device)]

        assert endpoints
        assert all(endpoint._client is device._client for endpoint in endpoints)


@pytest.mark.parametrize("device_class", DEVICE_CLASSES, ids=lambda cls: cls.__name__)
def test_model_extends_its_family(device_class: type) -> None:
    family = family_of(device_class)

    with family(BASE_URL) as base, device_class(BASE_URL) as device:
        assert endpoint_attributes(base) <= endpoint_attributes(device)


@pytest.mark.parametrize("device_class", DEVICE_CLASSES, ids=lambda cls: cls.__name__)
def test_device_signature(device_class: type) -> None:
    parameters = inspect.signature(device_class).parameters

    assert list(parameters) == ["base_url", "timeout", "verify"]
    assert parameters["timeout"].kind is inspect.Parameter.KEYWORD_ONLY
    assert parameters["verify"].default is True


def test_every_device_is_exported() -> None:
    assert len(DEVICE_CLASSES) == len(set(DEVICE_CLASSES))
    assert all(issubclass(cls, FAMILIES) for cls in DEVICE_CLASSES)


@pytest.mark.parametrize("family", FAMILIES, ids=lambda cls: cls.__name__)
def test_context_manager_closes_client(family: type) -> None:
    with family(BASE_URL) as device:
        assert isinstance(device, family)

    assert device._client._session.is_closed


@pytest.mark.parametrize("device_class", [*FAMILIES, pytonika.RUTX50], ids=lambda cls: cls.__name__)
def test_repr_shows_model_and_address(device_class: type) -> None:
    with device_class(f"{BASE_URL}/") as device:
        assert repr(device) == f"<{device_class.__name__} {BASE_URL}/api>"
