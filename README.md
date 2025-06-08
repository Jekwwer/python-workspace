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

This repository is a robust template for Python development using **Poetry** and isolated virtual environments,
delivering a consistent and reproducible local package workflow. It comes equipped with tools for testing, formatting,
linting, spell-checking, a ready-to-use devcontainer, custom VS Code settings, essential repo files, automated checks,
integrated VS Code extensions, semantic releases, automated documentation deployment, and extensive in-repo guides for
project management and customization.

## Features ✨

- **Devcontainer & VS Code:** Ubuntu-based Docker container with Python 3.12 and Poetry installed, plus recommended VS
  Code extensions and workspace settings.
- **Dependency Management:** Poetry for declarative `pyproject.toml` configuration and `poetry.lock` locking.
- **Virtual Environments:** Project-scoped `.venv` directory automatically managed by Poetry (no need to install or
  activate manually).
- **Linting & Formatting:** Ruff for Python, Prettier for JSON/Markdown/YAML; enforced via pre-commit hooks and editor
  integrations.
- **Type Checking:** MyPy with automatic installation of missing stub packages.
- **Testing:** pytest suite with coverage reporting.
- **Spell Checking:** cspell for both code and documentation.
- **Pre-commit Hooks:** Automates Ruff, MyPy, pytest, rstfmt, yamllint, markdownlint, markdown-link-check, pyupgrade,
  and more.
- **CI/CD:** GitHub Actions for linting, testing, semantic-release versioning, and Sphinx docs deployment.
- **Documentation:** Sphinx configured with `autoapi`, `napoleon`, and `viewcode`; live preview during development and
  publishing to GitHub Pages.

- **In-Repo Guides:** `CONTRIBUTING.md`, `STYLEGUIDE.md`, `SECURITY.md` to enforce best practices and streamline
  onboarding.

## Installation 📦

Designed for **GitHub Codespaces**—running locally is untested and may require extra configuration.

[![open-in-github-codespaces](https://github.com/codespaces/badge.svg)][open-in-codespaces]

## Usage 🛠️

Most manual quality checks and workflows are exposed via `Makefile` targets. These commands mirror the editor
integrations, pre-commit hooks, and CI pipelines.

### CLI

Invoke the project’s command-line interface:

```bash
poetry run cli --help
```

### Formatting

Most formatting tasks are automated and enforced using various tools. Feel free to adjust these settings for your
project. The repository configurations are described in the [`STYLEGUIDE.md`][STYLEGUIDE].

```bash
make format             # check formatting
make format-fix         # apply formatting fixes
```

### Linting

```bash
make lint               # detect lint issues
make lint-fix           # auto-fix lint issues
```

### Static Analysis

- **Type Checking** with MyPy

  ```bash
  make type
  ```

- **Spell Checking** with cspell

  ```bash
  make spell
  ```

### Testing

Run the test suite (with coverage):

```bash
make test
```

### Documentation

- **Build HTML docs** with Sphinx:

  ```bash
  make docs-build
  ```

- **Live-serve docs** locally:

  ```bash
  make docs-serve
  ```

- **Clean docs** build artifacts:

  ```bash
  make docs-clean
  ```

## Contributing 👥

Contributions are welcome! Please read the [Contributing Guidelines][CONTRIBUTING] and check the [Issues][issues] page.

## License 🛡️

This project is licensed under the [MIT License][LICENSE].

## Contact 📬

For questions, reach out via [evgenii.shiliaev@jekwwer.com][evgenii.shiliaev@jekwwer.com] or open an [issue][issues].

---

**Migration Note:** This project previously used PDM (last PDM-based release: [v1.0.1]). As of [v2.0.0], Poetry is used
for dependency and environment management.

---

This document is based on a template by [Evgenii Shiliaev][evgenii-shiliaev-github], licensed under [CC BY
4.0][jekwwer-markdown-docs-kit-license]. All additional content is licensed under [LICENSE][LICENSE].

[CONTRIBUTING]: CONTRIBUTING.md
[LICENSE]: LICENSE
[STYLEGUIDE]: STYLEGUIDE.md
[evgenii-shiliaev-github]: https://github.com/Jekwwer
[evgenii.shiliaev@jekwwer.com]: mailto:evgenii.shiliaev@jekwwer.com
[issues]: https://github.com/Jekwwer/python-workspace/issues
[jekwwer-markdown-docs-kit-license]: https://github.com/Jekwwer/markdown-docs-kit/blob/main/LICENSE
[open-in-codespaces]: https://codespaces.new/Jekwwer/python-workspace
[v1.0.1]: https://github.com/Jekwwer/python-workspace/tree/v1.0.1
[v2.0.0]: https://github.com/Jekwwer/python-workspace/tree/v2.0.0
