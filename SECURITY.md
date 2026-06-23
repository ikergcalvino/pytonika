# Security Policy

## Supported versions

Pytonika is pre-1.0 and under active development. Security fixes are applied to
the **latest released version** on [PyPI](https://pypi.org/project/pytonika/)
only. Please make sure you are on the latest version before reporting an issue.

| Version | Supported |
|---------|-----------|
| Latest release | ✅ |
| Older releases | ❌ |

## Reporting a vulnerability

> [!IMPORTANT]
> Please **do not** report security vulnerabilities through public GitHub issues.

Instead, report them privately through GitHub's
[private vulnerability reporting](https://github.com/ikergcalvino/pytonika/security/advisories/new).
If you are unable to use that, contact the maintainer at
**iker.gcalvino@udc.es**.

Please include:

- A description of the vulnerability and its impact.
- Steps to reproduce, or a proof of concept.
- The Pytonika version and Python version affected.

You can expect an acknowledgement within a few days. Once the issue is
confirmed and fixed, a new release will be published and the reporter credited
(unless anonymity is requested).

## Scope and considerations

Pytonika is an HTTP client library for Teltonika devices. Keep in mind when
using it:

- **Credentials and tokens.** `authentication.login()` sends the username and
  password to the device and stores the returned Bearer token in memory on the
  client. Treat both as secrets and never hard-code or commit them.
- **TLS verification.** Devices often ship with self-signed certificates. You
  can pass `verify=False` to disable certificate verification, but this exposes
  the connection to man-in-the-middle attacks. Prefer providing a trusted CA
  bundle and keep verification enabled outside of local, trusted networks.
- **Transport.** Always connect over HTTPS when the device supports it; `http://`
  sends credentials and tokens in clear text.

These are inherent to how the device API works rather than vulnerabilities in
Pytonika itself, but they matter for using the library safely.
