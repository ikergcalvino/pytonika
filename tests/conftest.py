from collections.abc import Iterator

import pytest
import respx

from pytonika._client import APIClient

BASE_URL = "https://192.168.1.1"
API_URL = f"{BASE_URL}/api"


@pytest.fixture
def api() -> Iterator[respx.MockRouter]:
    with respx.mock(base_url=API_URL, assert_all_called=False) as router:
        yield router


@pytest.fixture
def client() -> Iterator[APIClient]:
    client = APIClient(BASE_URL, timeout=5.0, verify=True)
    yield client
    client.close()
