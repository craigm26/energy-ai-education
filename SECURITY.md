# Security Policy

## Reporting a vulnerability

**Do not open a public issue** for security-sensitive reports.

Use GitHub's [private vulnerability reporting](https://github.com/craigm26/energy-ai-education/security/advisories/new) feature (Security tab → Report a vulnerability), or email the maintainers directly.

### What to include

- Description of the issue and its impact
- Steps to reproduce (minimal reproducible example)
- Affected files, versions, or paths
- Suggested mitigation if known

### Response targets

| Stage | Target |
|-------|--------|
| Acknowledgement | 3 business days |
| Initial assessment | 7 business days |
| Remediation plan | 14 business days |

## Sensitive data policy

This repository is **publicly accessible**. Do not submit:

- **Critical Energy Infrastructure Information (CEII):** specific engineering, vulnerability, or detailed design information about bulk electric system assets, as defined by FERC regulations (18 CFR Part 388)
- **Customer data:** real utility customer identifiers, usage data, or billing information without explicit anonymization and license
- **Operational data:** real-time or near-real-time SCADA/operational data from live grid assets
- **Credentials:** API keys, tokens, passwords, or private keys of any kind

**When in doubt:** contact the maintainers before submitting. We can advise on appropriate handling, including synthetic data alternatives.

## Dependency security

We use GitHub Dependabot for automated dependency updates and the dependency-review action on all PRs. If you discover a vulnerability in a dependency used by this project, please follow the upstream project's responsible disclosure process and also notify us.

## Supply-chain security

This repository targets SLSA Build Level 1 for provenance. CI workflows are pinned to specific commit SHAs. OpenSSF Scorecard runs on a schedule.
