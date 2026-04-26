# Contributing Guidelines

Bug fixes, features, and documentation improvements welcome.

## Getting Started

1. Fork the repo on GitHub.
2. Clone the fork:

   ```bash
   git clone https://github.com/<YOUR_USERNAME>/python-workspace.git
   cd python-workspace
   ```

3. Add upstream remote:

   ```bash
   git remote add upstream https://github.com/Jekwwer/python-workspace.git
   ```

4. Install dependencies per [`README.md`][README].

## Branching and Versioning

This project employs a trunk-based strategy with **Semantic Release** for automated versioning and changelog generation.

### Branching Strategy

Branch names should follow these conventions (examples only; adapt as needed):

- **Feature branches:** `feature/<short-description>` (e.g., `feature/add-login`)
- **Bugfix branches:** `bugfix/<short-description>` (e.g., `bugfix/fix-auth-error`)
- **Pre-release branches:** Use `next`, `beta`, or `alpha` (optional)
- **Main branch:** `main`

### Versioning Strategy

This project adheres to **Semantic Versioning (SemVer)** in the format **`MAJOR.MINOR.PATCH`**:

- **MAJOR:** For large breaking changes that significantly alter the project's behavior or structure.
- **MINOR:** For new, backward-compatible features.
- **PATCH:** For backward-compatible bug fixes.

Semantic Release automatically manages versioning based on commit messages.

### Merging Guidelines

- **Squash (Preferred):** Use GitHub’s **Squash and Merge** to keep the commit history clean and focused. Ensure the
  pull request title follows the Conventional Commits format.

- **Rebase (Optional):** Use **Rebase and Merge** if commit history is already clean and well-structured.

- **Merge (Exceptions):** Use the regular merge option for larger branches with multiple contributors when preserving
  individual commits is necessary.

## Commit Message Conventions

Use Conventional Commits with the project's extended template (custom `[SECTION]` blocks for files, dependencies,
purpose, impact, references). Format enforced by `conventional-pre-commit`; body spell-checked by `cspell`. The
devcontainer auto-runs `pre-commit install`.

### Template

```plaintext
<type>(<scope>): <description>

<detailed description>

[FILES ADDED]
 - <list of newly added files>

[FILES REMOVED]
 - <list of removed files>

[DEPENDENCIES ADDED]
 - <list of newly added dependencies>

[DEPENDENCIES UPDATED]
 - <list of updated dependencies>

[DEPENDENCIES REMOVED]
 - <list of removed dependencies>

[CHANGES]
 - <list of changes>

[PURPOSE]
 - <reason for the change>

[IMPACT]
 - <observable effects>

[REFERENCES]
 - <links to docs, reviews, external issues>

Closes #<issue-number>
Refs #<issue-number>
```

Fill only sections that apply; omit empty headers entirely.

Subject: type, optional scope, ≤72 char description, no trailing period. Allowed types (per `conventional-pre-commit`
config): `build`, `chore`, `ci`, `deps`, `docs`, `feat`, `fix`, `perf`, `refactor`, `revert`, `security`, `style`,
`test`. Breaking change: append `!` to type/scope (`feat!:` or `feat(api)!:`) and add a `BREAKING CHANGE:` footer line
in the body.

### Example

```plaintext
deps(python): bump pytest, pytest-cov, sphinx, autobuild

[DEPENDENCIES UPDATED]
 - pytest: ^8.4.0 → ^9
 - pytest-cov: ^6.2.1 → ^7
 - sphinx: ^8.2.3 → ^9
 - sphinx-autobuild: ^2024.10.3 → ^2025.8
```

## Dependency and Build Management

### Dependency Handling

- **NPM Dependencies:** Managed via `package.json` and `package-lock.json`.

- **Python Dependencies:** Managed via `pyproject.toml` and `poetry.lock`.

- **Dependabot:** The `.github/dependabot.yml` file monitors and updates dependencies for NPM packages, Python packages
  and GitHub Actions.

### Environment Configuration

- **Container Setup:** `.devcontainer/devcontainer.json` defines the base image, features, ports, and post-create
  script, and auto-installs VS Code extensions inside the container.
- **Editor Config:** `.vscode/settings.json`, `.vscode/extensions.json`, and `.vscode/launch.json` are workspace-scoped
  and apply in every context — Codespaces, local devcontainer, and local clone without a container.

## Testing and Quality Assurance

Lint, format, type-check, spell-check, and tests run automatically via editor integrations, pre-commit hooks, and CI.
The same tools are exposed as `make` targets — run `make help` for the full list. Common ones:

- `make check` — format + lint + type + spell
- `make test` — pytest with coverage
- `make pre-commit` — all pre-commit hooks against all files

Documentation builds run manually (`make docs-build`, `make docs-serve`).

## Proposing Changes

1. Check [Issues][issues] / [Discussions][discussions] for prior context.
2. Branch from `main` (`feature/...`, `bugfix/...`, etc.).
3. Make changes; keep them consistent with [`STYLEGUIDE.md`][STYLEGUIDE].
4. Commit per the conventions above.
5. Push and open a pull request, filling the PR template.

## Code of Conduct

By contributing, you agree to the [Code of Conduct][CODE_OF_CONDUCT].

[CODE_OF_CONDUCT]: CODE_OF_CONDUCT.md
[README]: README.md
[STYLEGUIDE]: STYLEGUIDE.md
[discussions]: https://github.com/Jekwwer/python-workspace/discussions
[issues]: https://github.com/Jekwwer/python-workspace/issues
