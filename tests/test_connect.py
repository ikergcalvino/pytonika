import pytest
import respx

import pytonika

from .conftest import BASE_URL


def status(model: object) -> dict:
    return {"success": True, "data": {"device_model": model, "api_version": "1.18"}}


@pytest.mark.parametrize(("model", "expected"), [("RUT956", pytonika.RUT956), ("rutx50", pytonika.RUTX50)])
def test_returns_the_model_class(api: respx.MockRouter, model: str, expected: type) -> None:
    api.get("/unauthorized/status").respond(json=status(model))

    with pytonika.connect(BASE_URL, timeout=5.0, verify=False) as device:
        assert type(device) is expected


@pytest.mark.parametrize("model", ["RUTX99", "TRB999", "Router"])
def test_unsupported_model_raises(api: respx.MockRouter, model: str) -> None:
    api.get("/unauthorized/status").respond(json=status(model))

    with pytest.raises(ValueError, match="Unsupported device model"):
        pytonika.connect(BASE_URL)


@pytest.mark.parametrize("response", [status(None), {"success": False, "errors": []}])
def test_missing_model_raises(api: respx.MockRouter, response: dict) -> None:
    api.get("/unauthorized/status").respond(json=response)

    with pytest.raises(ValueError, match="did not report its model"):
        pytonika.connect(BASE_URL)


def test_is_exported() -> None:
    assert "connect" in pytonika.__all__
