# Contributing to Pytonika

Thanks for your interest in improving Pytonika! Contributions, bug reports and
feature requests are all welcome. This guide covers how the project is
organized, how to set up your environment and the conventions it follows.

> [!NOTE]
> Pytonika is **not an official Teltonika library** and is not affiliated with
> Teltonika Networks. Endpoint and device definitions are derived from the
> public [Teltonika Web API reference](https://developers.teltonika-networks.com/).

## Ways to contribute

- **Report a bug** or **request a feature** by opening an
  [issue](https://github.com/ikergcalvino/pytonika/issues/new/choose).
- **Report a missing or incorrect endpoint, or an unsupported device**, using
  the dedicated issue templates. Include the device model, its firmware version
  and a link to the API reference: that is what is needed to fix it.
- **Open a pull request** to fix a bug in the hand-written code, improve the
  documentation, the tests or the CI.

## How the code is organized

```
pytonika/
├── _client.py           # APIClient: the HTTP layer (hand-written)
├── endpoints/
│   ├── _endpoint.py     # Endpoint base class and the File upload type (hand-written)
│   ├── authentication.py# login / logout / session (hand-written)
│   └── <group>.py       # one class per API documentation page (generated)
└── devices/
    └── <family>/        # Router, Gateway, AccessPoint, Switch and one class per model (generated)
```

- **`APIClient`** wraps an `httpx.Client` and exposes a single `request()`
  method. Responses are returned as the device sends them.
- **Endpoint classes** have one method per API operation. Each method is a
  single call to `self._client.request(...)`.
- **Device classes**: each family base attaches the endpoint groups common to
  all its models; each model adds only the groups specific to it.

### Generated code

The modules in `pytonika/endpoints/` (except `_endpoint.py` and
`authentication.py`) and in `pytonika/devices/` are **generated from the
Teltonika OpenAPI specifications**, for the latest firmware documented for each
model. Manual edits to these files are overwritten the next time they are
regenerated.

To fix or add an endpoint or a device, please
[open an issue](https://github.com/ikergcalvino/pytonika/issues/new/choose)
instead of editing the generated files: the maintainer regenerates the code from
the specification.

Generated code follows these rules, which any manual change must respect:

| API operation | Method name |
|---|---|
| `GET /wireguard/config` | `get_wireguard_config` |
| `GET /wireguard/config/{id}` | `get_wireguard_config_by_id` |
| `POST /wireguard/config` | `create_wireguard_config` |
| `PUT /wireguard/config/{id}` | `update_wireguard_config_by_id` |
| `DELETE /wireguard/config` | `delete_wireguard_config` |
| `POST` with a file upload | `upload_<path>` |
| `POST /wireguard/actions/generate_keys` | `wireguard_actions_generate_keys` |

- Request bodies are wrapped as `{"data": ...}`, as the API expects.
- Query parameters and extra upload fields are optional keyword-only arguments.
- File uploads take a `file` argument; downloads return `bytes`.
- The docstring is the summary from the API reference.

```python
def get_wireguard_config_by_id(self, wireguard_id: str, *, all_options: bool | None = None) -> dict[str, Any]:
    """Returns the specified Wireguard configuration."""
    return self._client.request("GET", f"/wireguard/config/{wireguard_id}", params={"all_options": all_options})
```

## Development setup

> [!IMPORTANT]
> An **editable install is required**: the package reads its own version via
> `importlib.metadata`, so it must be installed to import correctly.

```bash
git clone https://github.com/ikergcalvino/pytonika.git
cd pytonika

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -e ".[dev]"
```

Pytonika supports Python **3.11** and later.

## Quality checks

CI runs these checks on every push and pull request to `main` and `develop`,
with the tests on every supported Python version. Run them locally before
pushing:

```bash
ruff check .                 # lint
ruff format --check .        # formatting (use `ruff format .` to fix)
ty check pytonika tests      # type checking
pytest                       # tests, with a coverage threshold of 80%
python -m build              # build sdist + wheel
twine check dist/*           # validate package metadata
```

- The codebase is fully typed (`py.typed`) and the `ANN` lint rules are
  enforced, so **all signatures must have type hints**.
- Line length is 120 and strings use double quotes (enforced by ruff).
- Tests use [respx](https://lundberg.github.io/respx/) to mock HTTP requests;
  no real device is needed.

## Branching and pull requests

- Branch off **`develop`** and target your pull request at **`develop`**.
  `main` is reserved for releases.
- Keep pull requests focused: one logical change per PR.
- Fill in the PR template and make sure the checks pass before requesting
  review. If your change modifies or removes public API, mark it as a breaking
  change.
- Commit messages follow a [Conventional Commits](https://www.conventionalcommits.org/)
  style (`feat:`, `fix:`, `docs:`, `ci:`, `chore:`, …).

## License

By contributing, you agree that your contributions will be licensed under the
[MIT License](LICENSE).
