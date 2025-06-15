# Style Guide

This document outlines the style guide for **Jekwwer/python-workspace**. It covers commit message formatting, coding
conventions, repository structure, and other aspects detailed in [Scope][SCOPE]. Adhering to these guidelines ensures a
consistent and readable project.

## Introduction

### Purpose

This guide standardizes coding and documentation practices to ensure consistency, enhance readability, and support
effective collaboration.

### Audience

This style guide is intended for:

- **Developers and Contributors:** Those writing code or documentation for the project.
- **Maintainers:** Individuals responsible for reviewing and merging contributions.
- **Reviewers:** Participants in code reviews to ensure adherence to standards.

### Scope

This document covers:

- **Repository Structure:** Directory layout, file naming conventions, and configuration file details.
- **Naming Conventions:** Standards for variables, constants, functions, and file/directory names.
- **Code Formatting and Style:** Guidelines on indentation, line length, brace styles, comments, EditorConfig settings,
  and linting/formatting tools.
- **Documentation:** Standards for creating and maintaining project documentation.
- **Additional Best Practices:** Other practices to improve overall code quality and project maintainability.

## Project Overview

### Project Goals

Provide a robust repository that delivers a ready-to-use Python development environment leveraging Docker-based
devcontainer technology and GitHub Codespaces with VS Code.

### Technology Stack

- **Editor:** Visual Studio Code (workspace settings, recommended extensions)
- **Devcontainer:** Docker config (`devcontainer.json`)
- **Pre-commit Hooks:** pre-commit (`.pre-commit-config.yaml`)
- **Build and Packaging:** Python 3.12, Poetry
- **Linting and Formatting:** Ruff, Prettier, rstfmt
- **Type Checking:** MyPy
- **Testing:** pytest, pytest-cov
- **Documentation:** Sphinx
- **CI/CD:** GitHub Actions

### Target Audience

Python developers who need a zero-setup, standardized workspace template optimized for GitHub Codespaces and VS Code.

## Repository Structure

### Directory Layout

```plaintext
/ (root)                                # repository root
├── .devcontainer                       ├── # devcontainer-related configurations
│   ├── devcontainer.json               │   ├── # devcontainer setup
│   └── post-create.sh                  │   └── # post-create initialization script
├── .github                             ├── # GitHub-related configurations
│   ├── ISSUE_TEMPLATE                  │   ├── # issue templates
│   │   └── *                           │   │   └── # all files in the folder
│   ├── PULL_REQUEST_TEMPLATE           │   ├── # pull request templates
│   │   └── *                           │   │   └── # all files in the folder
│   ├── workflows                       │   ├── # GitHub workflows
│   │   ├── ci.yml                      │   │   ├── # ci pipeline workflow
│   │   ├── docs.yml                    │   │   ├── # docs deploy workflow
│   │   └── release.yml                 │   │   └── # release workflow
│   ├── dependabot.yml                  │   ├── # Dependabot configuration
│   ├── FUNDING.yml                     │   ├── # funding configuration
│   └── PULL_REQUEST_TEMPLATE.md        │   └── # default pull request template
├── .vscode                             ├── # VS Code-related configurations
│   └── launch.json                     │   └── # launch & debug configuration
├── docs                                ├── # documentation files
│   └── source                          │   └── # Sphinx-related configurations
│       ├── conf.py                     │       ├── # Sphinx configuration
│       └── index.rst                   │       └── # main documentation entry
├── src                                 ├── # source code
│   └── python_workspace                │   └── # core package
│       ├── __init__.py                 │       ├── # package initializer
│       ├── cli.py                      │       ├── # cli entrypoint
│       └── utils.py                    │       └── # utility functions
├── test                                ├── # test suite
│   ├── cli_test.py                     │   ├── # cli functionality tests
│   └── utils_test.py                   │   └── # utility functions tests
├── .editorconfig                       ├── # editor configuration
├── .gitignore                          ├── # files to ignore in Git
├── .markdownlint.json                  ├── # markdown linting configuration
├── .pre-commit-config.yaml             ├── # pre-commit hook configuration
├── .prettierrc                         ├── # Prettier configuration
├── .releaserc.js                       ├── # semantic release configuration
├── .yamllint.yml                       ├── # yaml linting configuration
├── CHANGELOG.md                        ├── # changelog
├── CODE_OF_CONDUCT.md                  ├── # code of conduct
├── CONTRIBUTING.md                     ├── # contributing guidelines
├── cspell.json                         ├── # spell checking configuration
├── LICENSE                             ├── # main license
├── Makefile                            ├── # common development tasks
├── package-lock.json                   ├── # npm lock file
├── package.json                        ├── # npm package metadata
├── poetry.lock                         ├── # poetry lock file
├── pyproject.toml                      ├── # Python project metadata
├── README.md                           ├── # project README
├── SECURITY.md                         ├── # security information
└── STYLEGUIDE.md                       └── # style guide
```

### File Naming Conventions

- **Repository Documentation Files:** Use **SCREAMING_SNAKE_CASE** for key documentation files (e.g.,
  `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `README.md`, `SECURITY.md`).
- **Configuration Files:** Tool configuration files (e.g., `cspell.json`, `.editorconfig`, `.pre-commit-config.yaml`,
  `.prettierrc`) use lowercase naming, following the specific requirements of each tool.
- **Shell Files:** Use **snake_case** for executable scripts (e.g., `build_docs.sh`, `deploy_app.sh`).
- **Python Files:** Use **snake_case** for modules and packages (e.g., `data_loader.py`, `utils.py`). Test modules
  should follow the `<name>_test.py` pattern.
- **GitHub and Workflow Files:** Files within the `.github` directory—such as `dependabot.yml`, `FUNDING.yml`, and
  templates under `ISSUE_TEMPLATE`/`PULL_REQUEST_TEMPLATE`—follow GitHub’s naming conventions. In `.github/workflows/`,
  use **kebab-case** for YAML workflow files (e.g., `deploy-app.yml`, `run-tests.yml`).

### Directory Naming Conventions

- **General Directories:** Use lowercase letters and **kebab-case** for multi-word names (e.g., `node-modules`,
  `source-files`). Choose names that clearly indicate the directory’s content or purpose (e.g., `docs` for
  documentation, `assets` for media).
- **Python Package Directories:** Under `src/` (or any Python package hierarchy), use **snake_case** to match module
  naming conventions (e.g., `python_workspace`, `data_loader`).
- **Special Directories:** Directories prefixed with a dot (e.g., `.github`, `.devcontainer`) have specific roles and
  should remain unchanged.

### Configuration Files

Key configuration files in the repository:

- `.devcontainer/devcontainer.json`: Development container setup, including VS Code settings, environment variables, and
  extensions.
- `.github/dependabot.yml`: Dependabot configuration for automated dependency version updates.
- `docs/source/conf.py`: Sphinx configuration file defining documentation build parameters, extensions, and theme.
- `.gitignore`: Files and directories excluded from version control.
- `.editorconfig`: EditorConfig rules for consistent code style across editors.
- `.markdownlint.json`: Markdown linting rules and file exclusions.
- `.pre-commit-config.yaml`: Definitions for pre-commit hooks (linting, formatting, type checks, tests).
- `.prettierrc`: Prettier formatting rules for JSON, YAML, Markdown, etc.
- `.releaserc.js`: semantic-release configuration, defining release branches, plugins, and versioning strategy.
- `.yamllint`: YAML linting configuration for CI and project YAML files.
- `cspell.json`: Code spell-check configuration with custom dictionaries and file globs.
- `Makefile`: Targets for common development tasks (linting, formatting, type checking, spell-checking, testing,
  running, and releasing).
- `package-lock.json`: npm lockfile capturing exact dependency versions.
- `package.json`: npm manifest with project metadata, script definitions, and dependency declarations.
- `poetry.lock`: Poetry lockfile locking Python dependency versions for reproducible environments.
- `pyproject.toml`: Python project metadata, Poetry settings, build-system requirements, and tool configurations
  (linting, typing, docs).

## Naming Conventions

### General Guidelines

Naming should be clear, descriptive, and consistent across the project to ensure maintainability and readability.

### Variables

- **Python:** Use **snake_case** for variable names to enhance readability (e.g., `my_variable`).

### Constants

- **Python:** Use **SCREAMING_SNAKE_CASE** for constants to distinguish them from regular variables (e.g., `MAX_LIMIT`).

### Functions / Methods

- **General:** Names should be descriptive verbs conveying the action performed.
- **Python:** Use **snake_case** for function and method names (e.g., `update_profile_svg`).

### Classes

- **Python:** Use **CamelCase** for class names to clearly distinguish types (e.g., `ProfileCardGenerator`).

### Files

See [File Naming Conventions][FILE_NAMING_CONVENTIONS].

## Code Formatting and Style

The project adheres to the rules specified in the `.editorconfig`, `.markdownlint.json`, `.prettierrc`, `.yamllint` and
`pyproject.toml` configuration files.

### Indentation and Spacing

- **General Guidelines:** Use **2 spaces** per indentation level throughout the project. Tabs are allowed only for
  `Makefile`. _(Enforced by EditorConfig and Prettier for supported files)_
- **Python:** Use **4 spaces** per indentation level for Python files. _(Enforced by EditorConfig)_

### Line Length

- **Code Files:** Limit lines to **88 characters**. _(Enforced by Ruff for Python, Prettier for supported files, and
  yamllint pre-commit hook for YAML)_
- **Markdown:** Allow up to **120 characters** per line. _(Enforced by Prettier and markdownlint pre-commit)_
- **reStructuredText:** Allow up to **120 characters** per line. _(Enforced by rstfmt pre-commit)_
- **JSON:** No line-length limit. _(Enforced by Prettier)_

### Braces and Control Structures

- **Python:** Python uses indentation to define code blocks instead of braces. Ensure consistent and correct
  indentation.

### Comments and Documentation

- **General Guidance:** All comments should enhance clarity and avoid redundancy with well-named functions and
  variables. Ensure comments do not exceed the maximum line length.
- **Inline Comments:** Place concise inline comments on the same line or immediately above the code they describe.
- **Block Comments / Docstrings:** Follow the Google-style docstring convention. The first line should be a short
  summary. _(Enforced by Ruff)_

  ```python
  """A script to fetch GitHub data, calculate streaks, and generate a heatmap grid."""
  ```

- **File Header Comments:** Every source file (except JSON, Markdown, `Python` and `LICENSE`) should begin with a
  one-line header comment describing its purpose.

  ```plaintext
  # .gitignore: Specifies files and directories that should not be tracked by Git.
  ```

  If a file starts with a shebang (e.g., `#!/bin/bash`), place the header comment immediately after the shebang line.

### EditorConfig

- **Purpose:** The `.editorconfig` file ensures consistent coding styles across all editors by specifying:
  - **Indentation:** 2 spaces (4 spaces for Python; tab-indented with 2-space width for `Makefile`)
  - **Line Endings:** Unix-style (`lf`)
  - **Charset:** UTF-8
  - **Max Line Length:** 88, 120 for Markdown/reStructuredText _(Note: `.editorconfig` provides these values for
    reference; enforcement is handled by other tools.)_
  - **Final Newline:** Enforced
  - **Trailing Whitespace:** Trimmed (with exceptions)
- **Note:** Contributors should use an editor that supports EditorConfig to automatically apply these settings.

### Prettier

- **Purpose:** The `.prettierrc` file defines formatting rules for Prettier-supported files:
  - **Semicolons:** Enabled
  - **Quote Style:** Single quotes
  - **Trailing Commas:** Added where possible
  - **Tab Width:** 2 spaces
  - **End of Line:** Unix-style (`lf`)
  - **Print Width:** 88 120 for Markdown; JSON has no enforced limit.
- **Note:** Prettier runs in VS Code and as a pre-commit hook to auto-format code before commits.

### Ruff

- **Purpose:** Provide fast, incremental linting and formatting for Python code, enforcing style rules (line length,
  import order, docstrings) and catching errors early.
- **Note:** Ruff runs as a local pre-commit hook to auto-format code before commits.

### Additional Code Quality Tools

- **Pre-commit Framework:** Enforces automated checks before each commit via `.pre-commit-config.yaml`:
  - **pre-commit-hooks:** Normalizes line endings, trims whitespace, validates JSON/TOML/YAML syntax, detects private
    keys, checks for merge conflicts, enforces shebangs, and other generic sanity checks.
  - **pygrep-hooks:** Catches anti-patterns and enforces conventions (no `eval`, no `log.warn`, blanket
    `# noqa`/`# type: ignore`, improper mock usage, stray Unicode replacement chars).
- **markdownlint-cli & markdown-link-check:** Lints Markdown files according to `.markdownlint.json` rules and validate
  links.
- **yamllint:** Lints YAML files according to `.yamllint.yml` rules.
- **pyupgrade:** Auto-upgrades Python syntax to modern versions.
- **mypy:** Does static type checks for Python code.
- **rstfmt:** Formats reStructuredText files to comply with style rules.

## Documentation

### Inline Documentation

See [Comments and Documentation][COMMENTS-AND-DOCUMENTATION].

### External Documentation

- **Repository Documentation:** The root-level `README.md` offers an overview of the project and a preview of its
  appearance on the profile. Additional key documents such as `CONTRIBUTING.md`, `STYLEGUIDE.md`, `SECURITY.md`, and
  `LICENSE` are also maintained at the repository root.

  _Note: File and directory names referenced in Markdown should always be formatted using backticks, for example:_

  ```markdown
  The `.editorconfig` file ensures consistent coding styles across all editors.
  ```

- **Project Documentation:** Comprehensive documentation is built with Sphinx. Source files live in `docs/source/`
  (e.g., `index.rst`, `api/*.rst`), and the Sphinx config is in `docs/source/conf.py`. The generated HTML output appears
  in `docs/build/`.
  - **Features:**
    - Auto-generated API reference via the `autoapi` extension.
    - Google/NumPy-style docstring support with `napoleon` extension.
    - Source code linking through `viewcode` extension.

### Markdown References

- **Reference-Style Links:** Use reference-style links for clarity. For example:

  ```markdown
  [info][link]

  [link]: https://example.com
  ```

- **Local References:** For links to repository-related documents (e.g., `CONTRIBUTING.md` or `CODE_OF_CONDUCT.md`) or
  internal sections, use **SCREAMING_SNAKE_CASE** for link identifiers and omit the file extension for documents. For
  example:

  ```markdown
  See [Code of Conduct][CODE_OF_CONDUCT].

  [CODE_OF_CONDUCT]: CODE_OF_CONDUCT.md
  ```

  And for internal sections:

  ```markdown
  See [File Naming Conventions][FILE_NAMING_CONVENTIONS].

  [FILE_NAMING_CONVENTIONS]: #file-naming-conventions
  ```

  **Note:** Local references should always appear at the top and be sorted alphabetically. For example:

  ```markdown
  [FILE_NAMING_CONVENTIONS]: #file-naming-conventions
  [SECURITY]: SECURITY.md
  [external-link]: https://example.com
  ```

- **External Links:** For links that reference external resources, use **kebab-case** for link identifiers. For example:

  ```markdown
  [info][external-link]

  [external-link]: https://example.com
  ```

  **Note:** External references should be sorted alphabetically and always appear below local references. For example:

  ```markdown
  [SECURITY]: SECURITY.md
  [external-link]: https://example.com
  ```

### Documentation Tools and Best Practices

#### Tools

- **sphinx:** Foundation for external docs. Auto-deploys to GitHub Pages on new releases; local commands:
  `make docs-build` (build) and `make docs-serve` (live preview).
- **rstfmt:** Formats reStructuredText files. Runs as a pre-commit hook; local command: `make format`.
- **cspell:** Spell-checks code and Markdown. Runs as a pre-commit hook; local command: `make spell`.
- **markdown-link-check:** Validates Markdown links. Runs as a pre-commit hook.
- **markdownlint:** Enforces Markdown style rules. Runs as a pre-commit hook.

#### Consistency and Updates

- Update documentation alongside code changes.
- Contributors should update docs when introducing new features or modifying existing functionality.

#### Style and Tone

- Maintain a semi-formal tone appropriate for a tech-oriented audience.
- Use clear, precise language and consistent formatting throughout.

#### Contribution Guidelines

- Documentation contributions follow the same process as code changes—submit pull requests for review according to the
  contribution guidelines.

## Additional Best Practices

### Security and Privacy

- Avoid exposing sensitive information in logs or error messages.
- Regularly review dependencies for security vulnerabilities.

### Error Handling and Logging

- Implement robust error handling to manage unexpected issues gracefully.
- Use structured logging to capture context without exposing sensitive data.

### Code Organization and Maintenance

- Keep the codebase clean and modular to facilitate understanding and future extensions.
- Regularly review and refactor code to eliminate redundancy.
- Use design patterns where appropriate to improve clarity and reusability.

## Conclusion

### Continuous Improvement

This document is a living resource that should evolve with the project. As new best practices emerge or project
requirements change, please update the guide to keep it relevant and effective.

### Feedback and Updates

Your input is valuable. If you have suggestions for improvements, clarifications, or additional guidelines, please reach
out to the maintainers or submit an [issue][issues]. For contributing guidelines, refer to
[`CONTRIBUTING.md`][CONTRIBUTING]; for security concerns, see [`SECURITY.md`][SECURITY]; for discussions, consult the
project's [discussion board][discussions] or contact the project owner at
[evgenii.shiliaev@jekwwer.com][evgenii.shiliaev@jekwwer.com].

---

This document is based on a template by [Evgenii Shiliaev][evgenii-shiliaev-github], licensed under [CC BY
4.0][jekwwer-markdown-docs-kit-license]. All additional content is licensed under [LICENSE][LICENSE].

[COMMENTS-AND-DOCUMENTATION]: #comments-and-documentation
[CONTRIBUTING]: CONTRIBUTING.md
[FILE_NAMING_CONVENTIONS]: #file-naming-conventions
[LICENSE]: LICENSE
[SCOPE]: #scope
[SECURITY]: SECURITY.md
[discussions]: https://github.com/Jekwwer/python-workspace/discussions
[evgenii-shiliaev-github]: https://github.com/Jekwwer
[evgenii.shiliaev@jekwwer.com]: mailto:evgenii.shiliaev@jekwwer.com
[issues]: https://github.com/Jekwwer/python-workspace/issues
[jekwwer-markdown-docs-kit-license]: https://github.com/Jekwwer/markdown-docs-kit/blob/main/LICENSE
