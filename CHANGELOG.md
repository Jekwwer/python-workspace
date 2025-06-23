# Changelog

## 2.0.3 - 2025-06-23
### 📦 Dependency Updates

* **npm:** bump prettier to v3.6.0 ([96a602d](https://github.com/Jekwwer/python-workspace/commit/96a602d185056879f35f2477b0e8f3b81d61daf5))

### 📖 Documentation

* **README.md:** update feature section for accuracy ([d481c0b](https://github.com/Jekwwer/python-workspace/commit/d481c0bccd3f6dfe7669cbdced78c62be4125291))

### 🛠️ Refactoring

* **prettierrc:** remove redundant overwrite for printWidth ([639e1ac](https://github.com/Jekwwer/python-workspace/commit/639e1ac831b2a7a06dbfdaa16f52e5c0fe136643))

## 2.0.2 - 2025-06-18
### 🐞 Bug Fixes

* **ci:** update Python version to align with project standards ([6aeb1d1](https://github.com/Jekwwer/python-workspace/commit/6aeb1d19a03dd244a1e02fb5cf70a4d2107887d2))

### 📦 Dependency Updates

* **npm:** bump conventional-changelog and cspell to latest versions ([581c638](https://github.com/Jekwwer/python-workspace/commit/581c638c42d051f1075ea9877826473428026126))
* **poetry:** bump pytest-cov, coverage, mypy to latest versions ([b7bb4ff](https://github.com/Jekwwer/python-workspace/commit/b7bb4ff8aae4b661f9950085f788bd0f39227025))

### 📦 Chores

* **release:** 2.0.2 [skip ci] ([469af53](https://github.com/Jekwwer/python-workspace/commit/469af538b7e9a166fc35c043898169c1a82d9dad))

### 🛠️ Refactoring

* **devcontainer:** optimize devcontainer settings and extensions ([d72f548](https://github.com/Jekwwer/python-workspace/commit/d72f5485535b383fcc94bafb464e2ab35c530eb0))

## 2.0.2 - 2025-06-18
### 📦 Dependency Updates

* **npm:** bump conventional-changelog and cspell to latest versions ([581c638](https://github.com/Jekwwer/python-workspace/commit/581c638c42d051f1075ea9877826473428026126))
* **poetry:** bump pytest-cov, coverage, mypy to latest versions ([b7bb4ff](https://github.com/Jekwwer/python-workspace/commit/b7bb4ff8aae4b661f9950085f788bd0f39227025))

### 🛠️ Refactoring

* **devcontainer:** optimize devcontainer settings and extensions ([d72f548](https://github.com/Jekwwer/python-workspace/commit/d72f5485535b383fcc94bafb464e2ab35c530eb0))

## 2.0.1 - 2025-06-15
### 🐞 Bug Fixes

* **Makefile:** add missing targets to phony list ([1ccffb4](https://github.com/Jekwwer/python-workspace/commit/1ccffb4101024b5954f088e8d5516476856311d4))
* **pre-commit:** update file pattern for format hook ([d7a7638](https://github.com/Jekwwer/python-workspace/commit/d7a76382b1cb51f4bcfb0e57b5c2bd033a7b4b43))

### 📖 Documentation

* **README.md:** add note about migration to Poetry ([90a521d](https://github.com/Jekwwer/python-workspace/commit/90a521d26fae9f3902ec754e9d849b581995e10a))
* **STYLEGUIDE.md:** update style guide for clarity and accuracy ([64cf419](https://github.com/Jekwwer/python-workspace/commit/64cf419e2f3355fb5c8130beb2d35ae39bedaced))

### 📦 Chores

* **metadata:** add report email to package metadata ([c13f43f](https://github.com/Jekwwer/python-workspace/commit/c13f43fc7e37d2738c96f8d8b3648d10f6d808c0))
* **metadata:** update keywords in package.json and pyproject.toml ([05fa191](https://github.com/Jekwwer/python-workspace/commit/05fa191b3aded8614ccc16e11d903a59fb734dd4))

## 2.0.0 - 2025-06-08
### ⚠ BREAKING CHANGES

* The project now uses Poetry instead of PDM for dependency management and build tasks. Workflows and scripts relying on PDM have been removed or replaced. Users must adopt the 'Makefile' tasks and 'poetry' commands for their workflows.

[FILES ADDED]
 - Makefile
 - poetry.lock

[FILES MODIFIED]
 - .devcontainer/devcontainer.json
 - .devcontainer/post-create.sh
 - .editorconfig
 - .github/dependabot.yml
 - .github/workflows/ci.yml
 - .github/workflows/docs.yml
 - .github/workflows/release.yml
 - .pre-commit-config.yaml
 - CONTRIBUTING.md
 - README.md
 - STYLEGUIDE.md
 - cspell.json
 - pyproject.toml

[FILES REMOVED]
 - pdm.lock

[DEPENDENCIES ADDED]
 - poetry

[DEPENDENCIES REMOVED]
 - pdm

[FEATURES/CHANGES]
 - Adapted project to use Poetry for dependency management.
 - Introduced Makefile to standardize development tasks.
 - Updated CI/CD workflows to use Poetry.
 - Updated documentation to reflect changes in tasks and dependencies.

[TECHNIQUES]
 - Replaced PDM scripts with Makefile targets.

[PURPOSE]
 - Simplify task execution and unify development workflow under Poetry and Makefile tooling.

[IMPACT]
 - Users must adapt to using Poetry and Makefile commands for development and CI/CD tasks.

* feat!(build): migrate from PDM to Poetry ([934c82a](https://github.com/Jekwwer/python-workspace/commit/934c82a92eacd9c3fec501bc5f4dea9d6a61fc25))

## 1.0.1 - 2025-06-08
### 🐞 Bug Fixes

* **config:** add and correct restructuredtext format settings ([384f50a](https://github.com/Jekwwer/python-workspace/commit/384f50aad1583722f909b5a29155078fe37aa995))

### 📦 Dependency Updates

* bump mypy 1.16.0 and @semantic-release/github 11.0.3 versions ([488f4ac](https://github.com/Jekwwer/python-workspace/commit/488f4ac78844da5d9307ee13acb6791b8b53f979)), closes [#3](https://github.com/Jekwwer/python-workspace/issues/3)

### 📦 Chores

* **config:** remove redundant ignore pattern for cspell ([ba837ca](https://github.com/Jekwwer/python-workspace/commit/ba837ca57541c810948046ce8d9a03210cc50cf6))
* **docs:** remove redundant settings from Sphinx configuration ([45ba501](https://github.com/Jekwwer/python-workspace/commit/45ba501a0696fd5fef245e9ee3e0553c4827ca97))
* **gitignore:** align comments style in custom section ([2f053ca](https://github.com/Jekwwer/python-workspace/commit/2f053ca6510900c51412eb0c78d956b9ff198a1c))

## 1.0.0 - 2025-05-26
### 🚀 New Features

* **ci:** add CI workflow configuration ([a76383f](https://github.com/Jekwwer/python-workspace/commit/a76383f2b269651b9531960565baecbb5da8ab2d))
* **ci:** add documentation deployment workflow ([039c2cf](https://github.com/Jekwwer/python-workspace/commit/039c2cf535ca7f7917d5a5319418624872b4bccb))
* **ci:** add release workflow ([504e36c](https://github.com/Jekwwer/python-workspace/commit/504e36c46094fc2a9c6e36ae24325d31b0ce884a))
* **ci:** automate dependency updates ([f3ab340](https://github.com/Jekwwer/python-workspace/commit/f3ab3408958d79b7aa9eb4d922833b2e9f4a65ec))
* **config:** add cspell configuration ([d55c6c7](https://github.com/Jekwwer/python-workspace/commit/d55c6c70fd7d25cfdab1712e8a5c875233e6ca30))
* **config:** add devcontainer configuration for development environment ([0aa6166](https://github.com/Jekwwer/python-workspace/commit/0aa6166438c3f6d2e6187c018aeed5976e5e9e93))
* **config:** add EditorConfig for consistent code style ([18f29d1](https://github.com/Jekwwer/python-workspace/commit/18f29d1cf3c33e76aa4da7a4a8fb752f2507de52))
* **config:** add gitignore for Node.js, Python and Visual Studio ([e558b63](https://github.com/Jekwwer/python-workspace/commit/e558b638773015b30a74fd30977f7c53c59a86ea))
* **config:** add markdownlint configuration for pre-commit hook ([a55419c](https://github.com/Jekwwer/python-workspace/commit/a55419c0f4dda79a2155d0e66c440048b8cbda5d))
* **config:** add package files for project metadata and scripts ([f70a0e0](https://github.com/Jekwwer/python-workspace/commit/f70a0e0114104f6ca65539b8e6b6e25a5961b8e2))
* **config:** add pre-commit configuration for code quality checks ([9590b1a](https://github.com/Jekwwer/python-workspace/commit/9590b1a7a8027d7dd2b493288438ab5ce1f0e891))
* **config:** add Prettier configuration file ([bd5c6c8](https://github.com/Jekwwer/python-workspace/commit/bd5c6c86a3eb6bf82e0d9423bb1901ef842e8743))
* **config:** add semantic-release configuration ([16c576c](https://github.com/Jekwwer/python-workspace/commit/16c576cf10b7f334d419e6cf9acf81515bb11139))
* **config:** add yamllint configuration for pre-commit hook ([78d0551](https://github.com/Jekwwer/python-workspace/commit/78d0551ba62ffd2d88ddaa3215fb0c1a190ee834))
* **docs:** add Sphinx for project documentation ([797c853](https://github.com/Jekwwer/python-workspace/commit/797c85340efef7f5eb492a130dfe66f6c92da5ae))
* **src:** add example code ([ae777f7](https://github.com/Jekwwer/python-workspace/commit/ae777f70a249ec99d69eeeb8a7ca3aeaef24a106))
* **tests:** add tests for the example code ([ef976ec](https://github.com/Jekwwer/python-workspace/commit/ef976ec49fd4a01faa7a16f3cc12e493a2c2dff1))

### 📖 Documentation

* **CODE_OF_CONDUCT.md:** Add Contributor Covenant Code of Conduct ([32a019d](https://github.com/Jekwwer/python-workspace/commit/32a019db2c42871f1de57b95ce5a6b412cb8385d))
* **CONTRIBUTING.md:** add contributing guidelines ([0bf9e61](https://github.com/Jekwwer/python-workspace/commit/0bf9e610f6ae3a9444c44b3ad75448b19ca2ffff))
* **github-templates:** add GitHub templates for funding, issues, and pull requests ([eea2354](https://github.com/Jekwwer/python-workspace/commit/eea2354503541e7856c21c83179e2cd581b9ea61))
* **README.md:** expand README with detailed project information ([5585d5a](https://github.com/Jekwwer/python-workspace/commit/5585d5a2ea404292317c7dded35776da905a267a))
* **SECURITY.md:** add security information policy document ([6e71836](https://github.com/Jekwwer/python-workspace/commit/6e7183611651bb94b880d0ef9a40b2456526f31f))
* **STYLEGUIDE.md:** add comprehensive style guide for project consistency ([e507b02](https://github.com/Jekwwer/python-workspace/commit/e507b021cc635225f4990d6ae593e99fdb5a4893))
