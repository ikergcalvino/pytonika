"""Calls every endpoint method against a mocked device and checks it sends a well-formed request."""

import inspect
from collections.abc import Callable
from typing import Any, Literal, get_args, get_origin

import pytest
import respx

from pytonika import endpoints
from pytonika._client import APIClient
from pytonika.endpoints._endpoint import Endpoint

ENDPOINT_CLASSES = [
    cls
    for name in endpoints.__all__
    if inspect.isclass(cls := getattr(endpoints, name)) and issubclass(cls, Endpoint) and cls is not Endpoint
]
METHODS = [
    pytest.param(cls, name, id=f"{cls.__name__}.{name}")
    for cls in ENDPOINT_CLASSES
    for name, _ in inspect.getmembers(cls, inspect.isfunction)
    if not name.startswith("_")
]


def dummy_argument(parameter: inspect.Parameter) -> Any:
    annotation = parameter.annotation
    origin = get_origin(annotation) or annotation

    if parameter.name == "file":
        return ("file.bin", b"content")
    if origin is list:
        return ["id1", "id2"]
    if origin is dict:
        return {"enabled": "1"}
    for option in get_args(annotation):
        if get_origin(option) is Literal:
            return get_args(option)[0]

    return "id1"


def test_every_endpoint_is_exported() -> None:
    assert len(ENDPOINT_CLASSES) > 150
    assert len(METHODS) > 2000


@pytest.mark.parametrize(("endpoint_class", "method_name"), METHODS)
def test_endpoint_method_sends_request(
    api: respx.MockRouter,
    client: APIClient,
    endpoint_class: type[Endpoint],
    method_name: str,
) -> None:
    route = api.route().respond(json={"success": True, "data": {"token": "abc123"}})
    method: Callable[..., Any] = getattr(endpoint_class(client), method_name)
    parameters = inspect.signature(method).parameters.values()
    required = {p.name: dummy_argument(p) for p in parameters if p.default is inspect.Parameter.empty}
    everything = {p.name: dummy_argument(p) for p in parameters}

    method(**required)
    method(**everything)

    assert route.call_count == 2
    for call in route.calls:
        assert call.request.url.path.startswith("/api/")
        assert "{" not in call.request.url.path
