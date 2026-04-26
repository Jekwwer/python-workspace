# Style Guide

Coding and documentation conventions for **Jekwwer/python-workspace**.

## Technology Stack

- **Editor:** Visual Studio Code (workspace settings, recommended extensions)
- **devcontainer:** Docker config (`devcontainer.json`)
- **Pre-commit Hooks:** pre-commit (`.pre-commit-config.yaml`)
- **Build and Packaging:** Python 3.14, Poetry
- **Linting and Formatting:** Ruff, Prettier, rstfmt
- **Type Checking:** MyPy
- **Testing:** pytest, pytest-cov
- **Documentation:** Sphinx
- **CI/CD:** GitHub Actions

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
│   ├── extensions.json                 │   ├── # recommended extensions
│   ├── launch.json                     │   ├── # launch & debug configuration
│   └── settings.json                   │   └── # workspace editor settings
├── docs                                ├── # documentation files
│   └── source                          │   └── # Sphinx-related configurations
│       ├── conf.py                     │       ├── # Sphinx configuration
│       └── index.rst                   │       └── # main documentation entry
├── src                                 ├── # source code
│   └── my_package                      │   └── # core package (placeholder — rename when forking)
│       ├── __init__.py                 │       ├── # package initializer
│       ├── __main__.py                 │       ├── # python -m entry point
│       ├── cli.py                      │       ├── # cli entrypoint
│       ├── py.typed                    │       ├── # PEP 561 typing marker
│       └── utils.py                    │       └── # utility functions
├── tests                               ├── # test suite
│   ├── cli_test.py                     │   ├── # cli functionality tests
│   └── utils_test.py                   │   └── # utility functions tests
├── .cspell.json                        ├── # spell checking configuration
├── .editorconfig                       ├── # editor configuration
├── .gitignore                          ├── # files to ignore in Git
├── .markdown-link-check.json           ├── # markdown link check configuration
├── .markdownlint.yaml                  ├── # markdown linting configuration
├── .markdownlintignore                 ├── # markdown lint exclusions
├── .pre-commit-config.yaml             ├── # pre-commit hook configuration
├── .prettierignore                     ├── # Prettier exclusions
├── .prettierrc.json                    ├── # Prettier configuration
├── .releaserc.cjs                      ├── # semantic release configuration
├── .yamllint.yaml                      ├── # yaml linting configuration
├── CHANGELOG.md                        ├── # changelog
├── CODE_OF_CONDUCT.md                  ├── # code of conduct
├── CONTRIBUTING.md                     ├── # contributing guidelines
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
- **Configuration Files:** Tool configuration files (e.g., `.cspell.json`, `.editorconfig`, `.pre-commit-config.yaml`,
  `.prettierrc.json`) use lowercase naming, following the specific requirements of each tool.
- **Shell Files:** Use **snake_case** for executable scripts (e.g., `build_docs.sh`, `deploy_app.sh`).
- **Python Files:** Use **snake_case** for modules and packages (e.g., `data_loader.py`, `utils.py`). Test modules use
  the `<name>_test.py` pattern.
- **GitHub Files:** Files within the `.github` directory fall into two groups:
  - **GitHub-mandated names** (use exactly as required): `CODEOWNERS`, `FUNDING.yml`, `SUPPORT.md`,
    `PULL_REQUEST_TEMPLATE.md`, `dependabot.yml`, and `ISSUE_TEMPLATE/config.yml`.
  - **User-named YAML** under `.github/workflows/`, `.github/ISSUE_TEMPLATE/`, and `.github/DISCUSSION_TEMPLATE/`: use
    **kebab-case** (e.g., `deploy-app.yml`, `bug.yml`, `show-and-tell.yml`). Discussion template filenames must also
    match their GitHub Discussion category slug.

### Directory Naming Conventions

- **General Directories:** Use lowercase letters and **kebab-case** for multi-word names (e.g., `node-modules`,
  `source-files`). Choose names that clearly indicate the directory's content or purpose (e.g., `docs` for
  documentation, `assets` for media).
- **Python Package Directories:** Under `src/` (or any Python package hierarchy), use **snake_case** to match module
  naming conventions (e.g., `my_package`, `data_loader`).
- **Special Directories:** Directories prefixed with a dot (e.g., `.github`, `.devcontainer`) have specific roles; leave
  unchanged.

### Configuration Files

Key configuration files in the repository:

- `.devcontainer/devcontainer.json`: devcontainer setup (base image, features, ports, post-create) + VS Code extension
  auto-install
- `.github/dependabot.yml`: Dependabot config for dep version updates
- `.vscode/extensions.json`: Recommended VS Code extensions
- `.vscode/launch.json`: Debug configs for CLI and current file
- `.vscode/settings.json`: Workspace VS Code settings (editor, formatter, linter, interpreter)
- `docs/source/conf.py`: Sphinx config (build params, extensions, theme)
- `.cspell.json`: Spell-check config (dictionaries, file globs)
- `.editorconfig`: Editor style rules
- `.gitignore`: Files/directories excluded from version control
- `.markdown-link-check.json`: markdown-link-check config (timeouts, retry policy)
- `.markdownlint.yaml`: Markdown linting rules
- `.markdownlintignore`: Markdown linter file exclusions
- `.pre-commit-config.yaml`: Pre-commit hook definitions
- `.prettierignore`: Prettier file exclusions
- `.prettierrc.json`: Prettier formatting rules
- `.releaserc.cjs`: semantic-release config (branches, plugins, versioning)
- `.yamllint.yaml`: YAML linting config
- `Makefile`: Common dev task targets
- `package-lock.json`: npm lockfile
- `package.json`: npm manifest (metadata, scripts, deps)
- `poetry.lock`: Poetry lockfile
- `pyproject.toml`: Python project metadata, Poetry settings, build system, tool configs

## Naming Conventions

### Variables

- **Python:** Use **snake_case** for variable names (e.g., `my_variable`).

### Constants

- **Python:** Use **SCREAMING_SNAKE_CASE** for constants (e.g., `MAX_LIMIT`).

### Functions / Methods

- **General:** Use descriptive verbs conveying the action performed.
- **Python:** Use **snake_case** for function and method names (e.g., `update_profile_svg`).

### Classes

- **Python:** Use **CamelCase** for class names (e.g., `ProfileCardGenerator`).

### Files

See [File Naming Conventions][FILE_NAMING_CONVENTIONS].

## Code Formatting and Style

The project adheres to the rules specified in the `.editorconfig`, `.markdownlint.yaml`, `.prettierrc.json`,
`.yamllint.yaml` and `pyproject.toml` configuration files.

### Indentation and Spacing

- **General Guidelines:** Use **2 spaces** per indentation level throughout the project. Tabs are allowed only for
  `Makefile`. _(Enforced by EditorConfig and Prettier for supported files)_
- **Python:** Use **4 spaces** per indentation level for Python files. _(Enforced by EditorConfig)_

### Line Length

- **Code Files:** Limit lines to **88 characters**. _(Enforced by Ruff for Python, Prettier for supported files, and
  yamllint pre-commit hook for YAML)_
- **Markdown:** Allow up to **120 characters** per line. _(Enforced by Prettier and markdownlint pre-commit)_
- **reStructuredText:** Allow up to **120 characters** per line. _(Enforced by rstfmt pre-commit)_
- **JSON:** Allow up to **88 characters** per line. _(Enforced by Prettier)_

### Comments and Documentation

- **General Guidance:** Comments add clarity beyond what well-named functions and variables convey. Keep them within the
  maximum line length.
- **Inline Comments:** Place concise inline comments on the same line or immediately above the code they describe.
- **Block Comments / Docstrings:** Follow the Google-style docstring convention. First line: short summary. _(Enforced
  by Ruff)_

  ```python
  """A script to fetch GitHub data, calculate streaks, and generate a heatmap grid."""
  ```

- **File Header Comments:** Begin every source file (except JSON, Markdown, Python, and `LICENSE`) with a one-line
  header comment describing its purpose.

  ```plaintext
  # .gitignore: Specifies files and directories that should not be tracked by Git.
  ```

  If a file starts with a shebang (e.g., `#!/bin/bash`), place the header comment immediately after the shebang line.

### EditorConfig

- **Purpose:** `.editorconfig` defines per-language editor settings:
  - **Indentation:** 2 spaces (4 for Python; tab-indented with 4-space width for `Makefile`)
  - **Line Endings:** Unix-style (`lf`)
  - **Charset:** UTF-8
  - **Max Line Length:** 88, 120 for Markdown/reStructuredText _(reference values; enforced by other tools)_
  - **Final Newline:** Enforced
  - **Trailing Whitespace:** Trimmed (with exceptions)

### Prettier

- **Purpose:** `.prettierrc.json` defines formatting rules for Prettier-supported files:
  - **Quote Style:** Single quotes
  - **Print Width:** 88, 120 for Markdown
  - **Prose Wrap:** Always (auto-wrap Markdown paragraphs at print width)
- **Note:** Other rules (semicolons, trailing commas, tab width 2, LF line endings) inherit from Prettier 3.x defaults.
  `.prettierignore` lists skipped files (currently `CHANGELOG.md`, `poetry.lock`, `package-lock.json`). Runs in VS Code
  and as a pre-commit hook.

### Ruff

- **Purpose:** Lint and format Python (line length, import order, docstrings).
- **Note:** Runs as a local pre-commit hook.

### Additional Code Quality Tools

- **Pre-commit Framework:** Automated checks via `.pre-commit-config.yaml`. Hooks default to `pre-commit` stage;
  `commit-msg` hooks opt in explicitly. Hook names follow `category:action` (e.g. `lint:ruff`, `validate:json`,
  `format:prettier`). Revisions bumped by Dependabot.
  - **pre-commit-hooks:** Generic checks (line endings, whitespace, JSON/TOML/YAML syntax, private keys, merge
    conflicts, shebangs, `*_test.py` naming).
  - **pygrep-hooks:** Python anti-patterns (no `eval`, no `log.warn`, blanket `# noqa`/`# type: ignore`, mock misuse).
  - **ruff:** Lint (`ruff-check --fix`) + format Python; pyupgrade via `UP` selector.
  - **mypy:** Strict type checks (local hook, runs `make type`; skipped in CI).
  - **markdownlint-cli + markdown-link-check:** Markdown lint + link validation (markdown-link-check skipped in CI — no
    network).
  - **yamllint:** YAML lint (strict — warnings fail).
  - **actionlint:** GitHub Actions workflow lint.
  - **rstfmt:** Format `docs/source/*.rst`.
  - **prettier:** Format JSON/YAML/Markdown per `.prettierrc.json`.
  - **gitleaks:** Detect secrets in commits.
  - **cspell:** Spell-check files + commit message body.
  - **pytest-pre-commit:** Test suite on every commit.
  - **validate-pyproject:** Schema-validate `pyproject.toml`.
  - **poetry-lock-check:** Validate `pyproject.toml` ↔ `poetry.lock` consistency.
  - **conventional-pre-commit:** Validate commit messages against Conventional Commits.

## Documentation

### Inline Documentation

See [Comments and Documentation][COMMENTS-AND-DOCUMENTATION].

### External Documentation

- **Repository docs:** Root-level `README.md`, `CONTRIBUTING.md`, `STYLEGUIDE.md`, `SECURITY.md`, `LICENSE`. Use
  backticks for file/directory names in Markdown (e.g. `` `.editorconfig` ``).
- **Project docs:** Built with Sphinx. Source in `docs/source/` (`index.rst`, `api/*.rst`); config in
  `docs/source/conf.py`. Output to `docs/build/`. Auto-deploys to GitHub Pages on release.
  - `autoapi` extension for API reference
  - `napoleon` for Google/NumPy docstrings
  - `viewcode` for source links

### Markdown References

- **Reference-style** for descriptive/labeled links:

  ```markdown
  [info][link]

  [link]: https://example.com
  ```

- **Autolinks** for bare URLs and emails:

  ```markdown
  Contact <user@example.com> or visit <https://example.com>.
  ```

- **Local references** use **SCREAMING_SNAKE_CASE** for repo docs (omit extension) and section anchors:

  ```markdown
  [CODE_OF_CONDUCT]: CODE_OF_CONDUCT.md
  [FILE_NAMING_CONVENTIONS]: #file-naming-conventions
  ```

- **External references** use **kebab-case**:

  ```markdown
  [external-link]: https://example.com
  ```

Sort link refs alphabetically. Local refs first, then external.

### Documentation Tools

- **sphinx:** Builds external docs (`make docs-build`, `make docs-serve`). Auto-deploys to GitHub Pages.
- **rstfmt:** Formats `docs/source/*.rst` (pre-commit hook + `make format`).
- **cspell:** Spell-checks code + Markdown.
- **markdown-link-check:** Validates Markdown links.
- **markdownlint:** Enforces Markdown style.

[COMMENTS-AND-DOCUMENTATION]: #comments-and-documentation
[FILE_NAMING_CONVENTIONS]: #file-naming-conventions
