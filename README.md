# Python Workspace

![github-release](https://img.shields.io/github/v/release/Jekwwer/python-workspace?logo=github&link=https%3A%2F%2Fgithub.com%2FJekwwer%2Fpython-workspace%2Freleases%2Flatest)
![github-release-date](https://img.shields.io/github/release-date/Jekwwer/python-workspace?link=https%3A%2F%2Fgithub.com%2FJekwwer%2Fpython-workspace%2Freleases%2Flatest)
![github-commits-since-latest-release](https://img.shields.io/github/commits-since/Jekwwer/python-workspace/latest?link=https%3A%2F%2Fgithub.com%2FJekwwer%2Fpython-workspace%2Freleases%2Flatest)
![tests-status](https://img.shields.io/github/actions/workflow/status/Jekwwer/python-workspace/ci.yml?label=tests)
[![tests-coverage-status](https://codecov.io/gh/Jekwwer/python-workspace/graph/badge.svg?token=5PLRAD5I82)](https://codecov.io/gh/Jekwwer/python-workspace)
![libraries.io-dependency-status-for-github-repo](https://img.shields.io/librariesio/github/Jekwwer/python-workspace?logo=librariesdotio&logoColor=%23FFFFFF)
![github-open-issues](https://img.shields.io/github/issues/Jekwwer/python-workspace?logo=github&link=https%3A%2F%2Fgithub.com%2FJekwwer%2Fpython-workspace%2Fissues)
![is-maintained](https://img.shields.io/maintenance/yes/2025)
![license](https://img.shields.io/github/license/Jekwwer/python-workspace?link=https%3A%2F%2Fgithub.com%2FJekwwer%2Fpython-workspace%2Fblob%2Fmain%2FLICENSE)

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
- **CI/CD:** GitHub Actions for tests, semantic-release, Sphinx docs deployment.
- **Security CI:** Codecov coverage + Test Analytics, dependency review (PR CVE gate), CodeQL SAST (weekly schedule).
- **Documentation:** Sphinx (`autoapi`, `napoleon`, `viewcode`) with live preview + GitHub Pages publish.
- **In-Repo Guides:** `CONTRIBUTING.md`, `STYLEGUIDE.md`, `SECURITY.md`.

## Installation 📦

**Codespaces or local devcontainer (recommended):**

[![open-in-github-codespaces](https://github.com/codespaces/badge.svg)][open-in-codespaces]

**Pure local:** install Python 3.14, Poetry ≥2.3, Node.js ≥22, then:

```bash
git clone https://github.com/Jekwwer/python-workspace.git
cd python-workspace
make install
```

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

**Migration Note:** This project previously used PDM (last PDM-based release: [v1.0.1]). As of [v2.0.0], Poetry is used
for dependency and environment management.

[CONTRIBUTING]: CONTRIBUTING.md
[LICENSE]: LICENSE
[STYLEGUIDE]: STYLEGUIDE.md
[issues]: https://github.com/Jekwwer/python-workspace/issues
[open-in-codespaces]: https://codespaces.new/Jekwwer/python-workspace
[v1.0.1]: https://github.com/Jekwwer/python-workspace/tree/v1.0.1
[v2.0.0]: https://github.com/Jekwwer/python-workspace/tree/v2.0.0
