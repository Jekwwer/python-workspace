# Python Workspace

[![github-release](https://img.shields.io/github/v/release/Jekwwer/python-workspace?logo=github&logoColor=white&display_name=tag)](https://github.com/Jekwwer/python-workspace/releases/latest)
[![github-release-date](https://img.shields.io/github/release-date/Jekwwer/python-workspace?logo=github&logoColor=white)](https://github.com/Jekwwer/python-workspace/releases/latest)
[![github-commits-since-latest-release](https://img.shields.io/github/commits-since/Jekwwer/python-workspace/latest?logo=github&logoColor=white)](https://github.com/Jekwwer/python-workspace/releases/latest)
[![tests-status](https://img.shields.io/github/actions/workflow/status/Jekwwer/python-workspace/ci.yml?label=tests&logo=githubactions&logoColor=white)](https://github.com/Jekwwer/python-workspace/actions/workflows/ci.yml)
[![pre-commit-ci-status](https://results.pre-commit.ci/badge/github/Jekwwer/python-workspace/main.svg)](https://results.pre-commit.ci/latest/github/Jekwwer/python-workspace/main)
[![tests-coverage-status](https://img.shields.io/codecov/c/github/Jekwwer/python-workspace?logo=codecov&logoColor=white)](https://codecov.io/gh/Jekwwer/python-workspace)
[![openssf-scorecard](https://api.scorecard.dev/projects/github.com/Jekwwer/python-workspace/badge)](https://scorecard.dev/viewer/?uri=github.com/Jekwwer/python-workspace)
[![openssf-best-practices](https://www.bestpractices.dev/projects/12679/badge)](https://www.bestpractices.dev/projects/12679)
[![github-open-issues](https://img.shields.io/github/issues/Jekwwer/python-workspace?logo=github&logoColor=white)](https://github.com/Jekwwer/python-workspace/issues)
[![license](https://img.shields.io/github/license/Jekwwer/python-workspace)](https://github.com/Jekwwer/python-workspace/blob/main/LICENSE)

## Project Overview 🚀

Python project template with Poetry-managed venvs, devcontainer + VS Code integration, and a full lint/type/test/docs
toolchain wired into pre-commit and GitHub Actions.

## Features ✨

- **devcontainer + VS Code:** Ubuntu-based Docker container, Python 3.14, Poetry, plus recommended extensions and
  workspace settings.
- **Dependency Management:** Poetry (`pyproject.toml` + `poetry.lock`).
- **Virtual Environments:** Project-scoped `.venv` auto-managed by Poetry.
- **Linting + Formatting:** Ruff (Python), Prettier (JSON/Markdown/YAML).
- **Type Checking:** MyPy with strict type checks; auto-installs missing stubs at runtime.
- **Testing:** pytest with coverage.
- **Spell Checking:** cspell over code + docs.
- **Pre-commit Hooks:** Ruff, MyPy, pytest, rstfmt, yamllint, markdownlint, markdown-link-check, actionlint, gitleaks,
  validate-pyproject.
- **CI/CD:** GitHub Actions for tests, semantic-release with sigstore-attested wheel + sdist asset publishing, Sphinx
  docs deployment.
- **Security CI:** Codecov coverage + Test Analytics, dependency review (PR CVE gate), CodeQL SAST (weekly), OpenSSF
  Scorecard (weekly + push).
- **Documentation:** Sphinx (`autoapi`, `napoleon`, `viewcode`) with live preview + GitHub Pages publish.
- **In-Repo Guides:** `CONTRIBUTING.md`, `STYLEGUIDE.md`, `SECURITY.md`.

## Installation 📦

**Codespaces or local devcontainer (recommended):**

[![open-in-github-codespaces](https://github.com/codespaces/badge.svg)][open-in-codespaces]

**Pure local:** install Python 3.14, Poetry ≥2.4, Node.js ≥22, then:

```bash
git clone https://github.com/Jekwwer/python-workspace.git
cd python-workspace
make install
```

## Fork Setup 🔑

Optional GitHub-side config for forks:

- **`SCORECARD_TOKEN`** secret: enables OpenSSF Scorecard's Branch-Protection check. Create a fine-grained PAT scoped to
  the fork repo with `Administration: Read`, then add as repo secret. Other checks run without it.

## Usage 🛠️

Most workflows go through `Makefile` targets. Run `make help` for the full list.

```bash
make install            # install Python + Node deps + pre-commit hooks
make check              # format + lint + type + spell
make test               # pytest with coverage
make pre-commit         # run all pre-commit hooks against all files
make docs-build         # build HTML docs (Sphinx)
make docs-serve         # live-serve docs locally
poetry run cli --help   # invoke the project CLI
```

Toolchain config (formatter, linter, type checker, spell checker) documented in [`STYLEGUIDE.md`][STYLEGUIDE].

## Contributing 👥

See [Contributing Guidelines][CONTRIBUTING] and [Issues][issues].

## License 🛡️

[MIT License][LICENSE].

**Forking:** Add your own copyright line below the existing one in `LICENSE`; do not replace it. The semantic-release
`exec` plugin auto-updates year ranges on each release.

## Contact 📬

<evgenii.shiliaev@jekwwer.com> or open an [issue][issues].

---

**Migration Notes:**

- **[v3.0.0]:** requires Python 3.14 (was 3.12 in all prior releases).
- **[v2.0.0]:** Poetry replaces PDM for dependency management (last PDM-based release: [v1.0.1]).

[CONTRIBUTING]: CONTRIBUTING.md
[LICENSE]: LICENSE
[STYLEGUIDE]: STYLEGUIDE.md
[issues]: https://github.com/Jekwwer/python-workspace/issues
[open-in-codespaces]: https://codespaces.new/Jekwwer/python-workspace
[v1.0.1]: https://github.com/Jekwwer/python-workspace/tree/v1.0.1
[v2.0.0]: https://github.com/Jekwwer/python-workspace/tree/v2.0.0
[v3.0.0]: https://github.com/Jekwwer/python-workspace/tree/v3.0.0
