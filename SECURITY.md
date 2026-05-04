# Security Policy

## Supported Versions

| Version            | Supported             |
| ------------------ | --------------------- |
| [`v3.4.0`][v3.4.0] | ✅ Actively supported |
| Older versions     | ❌ Not supported      |

## Reporting a Vulnerability

1. **Private Disclosure via Email** — email <report@jekwwer.com> with:
   - Detailed description of the vulnerability
   - Steps to reproduce
   - Affected versions (if applicable)
   - Suggested fixes or workarounds (if any)

2. **Private Security Advisory on GitHub** — submit via GitHub Security Advisories:
   - Open the repository's [Security Advisories][security-advisories]
   - Click **Create security advisory** and follow prompts

I aim to respond within **48 hours**, with resolution or update within **7 days**.

## Verifying Releases

Each release ships sigstore-attested build provenance. Each `*.whl` and `*.tar.gz` artifact has a matching
`attestation-vX.Y.Z.intoto.jsonl` bundle attached to the GitHub Release.

Verify a downloaded artifact:

```bash
gh attestation verify <artifact-file> --owner Jekwwer
```

The bundle file works with offline tooling (slsa-verifier, in-toto, cosign) for air-gapped verification.

[security-advisories]: https://github.com/Jekwwer/python-workspace/security/advisories
[v3.4.0]: https://github.com/Jekwwer/python-workspace/tree/v3.4.0
