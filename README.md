# Pytonika

Pytonika is a lightweight Python client library to interact with **Teltonika Networks device** via their Web API.
It provides simple device abstractions and grouped endpoint interfaces to make automation and scripting straightforward.

- Lightweight, synchronous HTTP client built on top of [httpx](https://www.python-httpx.org/).
- Device wrappers for routers, gateways, access points and switches.

> [!IMPORTANT]
> Pytonika is **not an official Teltonika library**.
> This project is maintained by the community and is not affiliated with or endorsed by Teltonika Networks.

> [!NOTE]
> This project is currently in **early development (alpha)**.
> The API surface and behaviors may change between releases.

---

## Installation

Requirements:
- Python **3.10+**
- [httpx](https://pypi.org/project/httpx/) >= **0.28.1**

Install from PyPI:

```bash
pip install pytonika
```

### Basic usage

```python
>>> from pytonika import Router
>>> router = Router("http://192.168.1.1/")
>>> router.authentication.login("admin", "admin01")
{'success': 'boolean', 'data': {'username': 'string', 'group': 'string', 'token': 'string', 'expires': 'integer'}}
>>> router.authentication.get_session_status()
{'success': 'boolean', 'data': {'active': 'boolean'}}
>>> router.authentication.logout()
{'success': 'boolean', 'data': {'response': 'string'}}
```

> [!CAUTION]
> Use test credentials or a non-production device when experimenting.
> Exposing real devices with default credentials is a security risk.

---

## Contribute

If you want to contribute with Pytonika check out the [Contributing guidelines](CONTRIBUTING.md).

---

## License

[MIT License](LICENSE).

---
