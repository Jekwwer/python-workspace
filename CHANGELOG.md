# Changelog

## 3.4.0 - 2026-05-04
### 🚀 New Features

* **gitattributes:** add normalization, generated, and merge rules ([ce5bbf0](https://github.com/Jekwwer/python-workspace/commit/ce5bbf08d3c4a3086f1d909b6585a06ff8c49510))
* **release:** tighten checkout creds, add bot identity and PR perms ([0cb5ef1](https://github.com/Jekwwer/python-workspace/commit/0cb5ef1bdd0058c3699012e354cdfdfb2d9662b9))

### 📦 Dependency Updates

* **actions:** bump actions/attest-build-provenance ([#29](https://github.com/Jekwwer/python-workspace/issues/29)) [skip ci] ([3745f66](https://github.com/Jekwwer/python-workspace/commit/3745f6606c12b5b2ae391abe230757a99c581bb0))
* **devcontainers:** bump ghcr.io/devcontainers/features/node ([#27](https://github.com/Jekwwer/python-workspace/issues/27)) [skip ci] ([fae1878](https://github.com/Jekwwer/python-workspace/commit/fae18787b751d4dccbed5802397cee5390071f32))
* **pre-commit:** bump hypothesis in the pre-commit-deps group ([#28](https://github.com/Jekwwer/python-workspace/issues/28)) [skip ci] ([088f2a1](https://github.com/Jekwwer/python-workspace/commit/088f2a1697dd6665455129470ee8b66e4ecbc2cc))

### 📖 Documentation

* **readme:** add OpenSSF Best Practices badge ([c8d347e](https://github.com/Jekwwer/python-workspace/commit/c8d347ee78f1df254c694f4a5c434d193ff93dae))

## 3.3.0 - 2026-04-30
### 🚀 New Features

* **release:** attach attestation bundle as release asset ([9c082f3](https://github.com/Jekwwer/python-workspace/commit/9c082f32eff44d6d64c34858981aecdcf4936d68))

### 🔒 Security Updates

* **deps:** bump transitive deps to clear 11 GHSAs ([b86620b](https://github.com/Jekwwer/python-workspace/commit/b86620b1535b3fa23ebcf29c98e224aef3f416fe))

## 3.2.0 - 2026-04-29
### 🚀 New Features

* **release:** publish wheel + sdist as GitHub Release assets ([c68506c](https://github.com/Jekwwer/python-workspace/commit/c68506c6adceb555457ff70950466fe868b2cf37))
* **release:** sign artifacts with sigstore keyless attestation ([59bcfeb](https://github.com/Jekwwer/python-workspace/commit/59bcfeb4530c05f9de2849a91ef991cade0c9558))
* **test:** add hypothesis property-based testing ([ea4fb21](https://github.com/Jekwwer/python-workspace/commit/ea4fb21b2c5737589da6a9f3ddbd0cde7ce8d44d))

### 🔒 Security Updates

* **ci:** move workflow write perms to job-level scope ([4ff2bdd](https://github.com/Jekwwer/python-workspace/commit/4ff2bddcbee03f2542e68d0d55e4a1c26768ffbd))

### 🐞 Bug Fixes

* **ci:** add quality-pass aggregator for matrix branch protection ([3ce4ab5](https://github.com/Jekwwer/python-workspace/commit/3ce4ab541dc7b8064a61b66ce9815963ac36d80c))
* **ci:** make branch protection compat with matrix CI + release bot ([e55bfac](https://github.com/Jekwwer/python-workspace/commit/e55bfac6bf196282b6f99acd80394f55c17c107a))
* **ci:** swap deprecated codecov/test-results-action for codecov-action ([7f0870e](https://github.com/Jekwwer/python-workspace/commit/7f0870e138e201b2239f8ec2099e6267420b8fae))
* **ci:** use SCORECARD_TOKEN PAT for branch-protection read ([6d2b66a](https://github.com/Jekwwer/python-workspace/commit/6d2b66ace38d4de08c1033107a43f39fb93ae617))

### 📦 Dependency Updates

* **pip:** bump ruff to 0.15.12 ([#26](https://github.com/Jekwwer/python-workspace/issues/26)) ([bd5f4f9](https://github.com/Jekwwer/python-workspace/commit/bd5f4f93e6f45851373998151efa9fe9bc18fd1d))

### 🔧 Chores

* **ci:** drop dead branch-protection-bypass scaffolding ([0d6bdac](https://github.com/Jekwwer/python-workspace/commit/0d6bdac1cd6fc337596a6cba9121eb0352c737ee))

## 3.1.1 - 2026-04-28
### 🐞 Bug Fixes

* **changelog:** force emoji presentation on BREAKING CHANGES heading ([daf19f5](https://github.com/Jekwwer/python-workspace/commit/daf19f5d942fb2d9d75b016528a0410b5a922958))

### 📦 Dependency Updates

* **actions:** bump github/codeql-action v3.35.2 → v4.35.2 ([e1f154c](https://github.com/Jekwwer/python-workspace/commit/e1f154cf2684f07cdccd187221716b209a25d200))
* **npm:** bump semantic-release ecosystem ([6aec384](https://github.com/Jekwwer/python-workspace/commit/6aec384964eab45b16ff6ccbfdc17bdd0f5907ad))
* **pip:** bump pre-commit, pytest-xdist, sphinx-autoapi ([01f45ba](https://github.com/Jekwwer/python-workspace/commit/01f45ba666bb0c12f8495cb66d553f8cece6f4f0))
* **pre-commit:** bump pytest hook test deps ([ada2691](https://github.com/Jekwwer/python-workspace/commit/ada2691d8548d4193c3b9596ff50ee68e5995c8a))

### 🔧 Chores

* **changelog:** align history with current releaserc + commit rules ([2888e9a](https://github.com/Jekwwer/python-workspace/commit/2888e9a59eeedd8c559499138516a9aee2651a78))

## 3.1.0 - 2026-04-27
### 🚀 New Features

* **ci:** add Codecov Test Analytics upload (OIDC tokenless) ([38a9c9e](https://github.com/Jekwwer/python-workspace/commit/38a9c9e58c5c718ff36337969cd2df12eacc9c47))
* **ci:** add CodeQL SAST workflow (weekly schedule) ([a5171ca](https://github.com/Jekwwer/python-workspace/commit/a5171ca6ae3d2fec8cca5c4c78135207035e3827))
* **ci:** add dependency-review workflow on PRs ([1fddfd6](https://github.com/Jekwwer/python-workspace/commit/1fddfd65f634238618f1811693b3c1c9ac8c2ddd))
* **ci:** add OpenSSF Scorecard workflow ([f60b990](https://github.com/Jekwwer/python-workspace/commit/f60b990233128d12cab1b9eaa2744e4395dc6315))

### 🐞 Bug Fixes

* **ci:** satisfy Dependabot + pre-commit.ci config validation ([3673e57](https://github.com/Jekwwer/python-workspace/commit/3673e5766361718c6d0d8a03f7144023b458a858))
* **cspell:** exclude CHANGELOG.md from scan (auto-generated) ([aecfbcd](https://github.com/Jekwwer/python-workspace/commit/aecfbcd0cdd30923678dcc77ba02122bad10c043))

### 📖 Documentation

* **changelog:** fix v3.0.0 breaking-changes rendering ([82c0b8a](https://github.com/Jekwwer/python-workspace/commit/82c0b8ab9cc932db67410e51f724caff452f123e))
* **readme:** add v3.0.0 Python 3.14 migration note ([bfae0e1](https://github.com/Jekwwer/python-workspace/commit/bfae0e15281663ac9cb5aa43f32c47fcb3bedad6))
* **readme:** refresh badges + auto-upgrade all ([27b9b6f](https://github.com/Jekwwer/python-workspace/commit/27b9b6fa477bbbcea36aece7ed4e4162871e3310))

### 🔧 Chores

* **ci:** rename docs workflow name to match filename ([a35a834](https://github.com/Jekwwer/python-workspace/commit/a35a83423922a2a351ee279c82b576867ef75f3e))

## 3.0.0 - 2026-04-26
### ⚠️ BREAKING CHANGES

* **python_workspace:** import path moved from `python_workspace` to `my_package`.
* **python:** Python 3.14 required. Users on 3.12 must upgrade interpreter and rebuild devcontainer.

### 🚀 New Features

* **ci:** add lint/format/type/spell quality matrix ([f7b94e3](https://github.com/Jekwwer/python-workspace/commit/f7b94e3b3ada13f380504589e01f9e86f64eaf32))
* **ci:** add workflow_dispatch trigger to release and docs ([92363b2](https://github.com/Jekwwer/python-workspace/commit/92363b299dc7ff9b7b8def315dcb75aa4024cac8))
* **ci:** harden workflows with concurrency, timeouts, permissions ([44f3fe4](https://github.com/Jekwwer/python-workspace/commit/44f3fe462e74abb8a5f4dd2bed926766354f28c8))
* **dependabot:** add devcontainers ecosystem ([7ccdb2b](https://github.com/Jekwwer/python-workspace/commit/7ccdb2bf483bb12610382cfdab59587b7a1904b3))
* **dependabot:** tighten update policy ([09469d6](https://github.com/Jekwwer/python-workspace/commit/09469d6aa65f0d0c5ea671c78082a02de27718d9))
* **devcontainer:** add gh-cli, ports, env, and lifecycle config ([d2a2039](https://github.com/Jekwwer/python-workspace/commit/d2a20394121d8d2547fdfa8ef19ef35814a39f5b))
* **docs:** enforce Sphinx warnings as errors ([90cad96](https://github.com/Jekwwer/python-workspace/commit/90cad9680f6fe3e8a58409adf8c250c942324321))
* **github:** add CODEOWNERS ([2619311](https://github.com/Jekwwer/python-workspace/commit/2619311ed205788a1c472cca035824bf3eee6330))
* **github:** add discussion templates ([dc8113c](https://github.com/Jekwwer/python-workspace/commit/dc8113c289f5f58ad1c6ae1cb22130fc38e2aa76))
* **github:** add SUPPORT.md community health file ([c18f0fb](https://github.com/Jekwwer/python-workspace/commit/c18f0fb809cd795c16c3f655676307660a12efbc))
* **gitignore:** prune cruft, add secrets, restructure ([77a8c76](https://github.com/Jekwwer/python-workspace/commit/77a8c76af7ef1b79e4346d38055439a6c3ce9cfc))
* **issue-templates:** convert core templates to YAML forms ([0136975](https://github.com/Jekwwer/python-workspace/commit/013697508f603adfa55fe25718ba267f147808a1))
* **make:** add install/clean/check/pre-commit + sync docs ([d5a8aa7](https://github.com/Jekwwer/python-workspace/commit/d5a8aa7d2397ead7c1f0fdae3f668e01e6b778e7))
* **make:** include pre-commit install in setup target ([0101a94](https://github.com/Jekwwer/python-workspace/commit/0101a945ca141779f2a0e8664bf8809bb8b85e48))
* **mlc:** add markdown-link-check config ([cdd4f94](https://github.com/Jekwwer/python-workspace/commit/cdd4f945dd82e01445c737b3631851245ea88f55))
* **pre-commit:** add gitleaks, reorder, rename, sync docs ([28cbd1c](https://github.com/Jekwwer/python-workspace/commit/28cbd1cd6fc38bd1e3bbe40907cbff350dea29b4))
* **pre-commit:** bumps, drop redundant args, add hooks ([f1362cb](https://github.com/Jekwwer/python-workspace/commit/f1362cb42ef3b2e791a32f4b32c6028573fb75c8))
* **pre-commit:** extend commit-msg type allowlist ([e4687d9](https://github.com/Jekwwer/python-workspace/commit/e4687d98c09bc1c938b7f778438dcba2724d0198))
* **prettier:** add ignore file for CHANGELOG and lockfiles ([e38c3f0](https://github.com/Jekwwer/python-workspace/commit/e38c3f08827378d174087341a7f80153112727fb))
* **pyproject:** add publish guard against PyPI upload ([9511fa6](https://github.com/Jekwwer/python-workspace/commit/9511fa60d2cfeb9482a2b64b7083fa7274e56ba9))
* **python_workspace:** add __main__, py.typed, runtime __version__ ([fd1f52d](https://github.com/Jekwwer/python-workspace/commit/fd1f52d17d3021c4361ab4fef8f432f9e3fdf8a1))
* **release:** add build type, enable pre-release branches ([84ce745](https://github.com/Jekwwer/python-workspace/commit/84ce745def93cbf5bb879d95dc253215e34ab596))
* **release:** auto-update LICENSE year on release ([baa090b](https://github.com/Jekwwer/python-workspace/commit/baa090b1b557009e25a58d311238e6f412edfa8c))
* **yamllint:** enable --strict, tune rules ([6208454](https://github.com/Jekwwer/python-workspace/commit/62084543c20438f1932bbe75d3e852b68eb69dbe))

### 🔒 Security Updates

* **ci:** migrate Codecov to OIDC, drop unused NPM_TOKEN ([b5102b5](https://github.com/Jekwwer/python-workspace/commit/b5102b51ab2b38e10c5019b6ab159b6f1e5fe5f8))
* **ci:** SHA-pin actions with version comments ([55a0bba](https://github.com/Jekwwer/python-workspace/commit/55a0bbac98f56e26937b1e2ddbca3f76346201e0))
* **npm:** patch 11 vulnerabilities via npm audit fix ([c726aea](https://github.com/Jekwwer/python-workspace/commit/c726aea04aae37b8db0e7b32e67341a8410cf824))

### 🐞 Bug Fixes

* **ci:** gate workflow chain and fix Pages path ([cb72609](https://github.com/Jekwwer/python-workspace/commit/cb72609aed530785f01a3a601f030f9a3671b34a))
* **make:** correct run help backticks, docs-clean backslash ([b6d80bc](https://github.com/Jekwwer/python-workspace/commit/b6d80bcf10928a945be1b665c60f1f7bc0ce53cf))

### 📦 Dependency Updates

* bump actions to latest majors and Node 22 ([c4379d4](https://github.com/Jekwwer/python-workspace/commit/c4379d4f5d732058fb6b6e71e38687e965f681d8))
* **devcontainer:** bump node feature 1.6.3 → 1.7.1 and node 20 → 22 ([cffeb11](https://github.com/Jekwwer/python-workspace/commit/cffeb11ac24cf5b91d8982545192ca129f48ee9d))
* **npm:** bump cspell to 10.0.0 ([58ae202](https://github.com/Jekwwer/python-workspace/commit/58ae2022c6ba0b9a68adc88fcf71b02d708f68a0))
* **npm:** bump prettier to 3.8.3 ([68fa9ee](https://github.com/Jekwwer/python-workspace/commit/68fa9eea227747924257504bda7a4b44f8e495e2))
* **python:** bump pytest, pytest-cov, sphinx, autobuild ([e85505d](https://github.com/Jekwwer/python-workspace/commit/e85505db7a2438e19389da4cad8331d4357f2d9b))

### 📖 Documentation

* **coc:** trim bureaucracy + simplify attribution ([8c95cbf](https://github.com/Jekwwer/python-workspace/commit/8c95cbf83c4c134c694ae568f9c370b7526ddc9b))
* **contributing:** split container setup from editor config ([4ec9c74](https://github.com/Jekwwer/python-workspace/commit/4ec9c74927b9f8f5374c7cb75f47abf03d83ddc6))
* **contributing:** trim bureaucracy + sync commit template ([2910e7a](https://github.com/Jekwwer/python-workspace/commit/2910e7ad4e3e9dd84b660318a2d047c3b0733543))
* **my_package:** tighten scaffold docstrings and annotate __version__ ([176b80a](https://github.com/Jekwwer/python-workspace/commit/176b80aba486c0b6749715626daf078a27b34bba))
* **readme:** add fork-time LICENSE guidance ([431677d](https://github.com/Jekwwer/python-workspace/commit/431677d3850d91e41e25a7dff0af93d0395f1ba0))
* **readme:** drop stale pyupgrade ref, fix duplicate phrase ([893c5a0](https://github.com/Jekwwer/python-workspace/commit/893c5a0bfb8f0ed9ff581a9e83ca19dd888795e9))
* **readme:** trim bureaucracy + document local setup ([d6905ac](https://github.com/Jekwwer/python-workspace/commit/d6905ac46d6ace44c1b721e933e606a96b5d00cc))
* **refs:** drop markdown-docs-kit self-attribution from all docs ([f7ef44f](https://github.com/Jekwwer/python-workspace/commit/f7ef44fa9d1cb95feb345aad46b3ca4548f41efd))
* **refs:** switch mailto links to autolink form ([8598060](https://github.com/Jekwwer/python-workspace/commit/8598060d4ce2da97b087a5bca296e66577e495da))
* **security:** trim bureaucracy ([6208d84](https://github.com/Jekwwer/python-workspace/commit/6208d84696feba7314a7074745a68609efc94edf))
* **styleguide:** clarify .github file naming rules ([d7f2c47](https://github.com/Jekwwer/python-workspace/commit/d7f2c472ec43dcd70ce3364ff544a14af0c5705a))
* **styleguide:** document .vscode/ split from devcontainer.json ([b0c5658](https://github.com/Jekwwer/python-workspace/commit/b0c56587a292f46e39c27abe3aab8e22815c68a6))
* **styleguide:** sync package name to my_package ([3347f4b](https://github.com/Jekwwer/python-workspace/commit/3347f4b4d644a6080e9ff64dd328a8fe163b75d9))
* **styleguide:** trim bureaucracy + normalize style ([7de8aee](https://github.com/Jekwwer/python-workspace/commit/7de8aee31b75df915938ccb5a105bf4ecde71dca))

### 🔧 Chores

* **commits:** reorder allowed types to match releaserc ([4e59e78](https://github.com/Jekwwer/python-workspace/commit/4e59e78c878ba8723fbba7c54b1fe45461944096))
* **config:** drop entries handled by auto-discovery ([617aabf](https://github.com/Jekwwer/python-workspace/commit/617aabf6fdc7447a9c0e090fac384d25ea5c9189))
* **config:** standardize filenames to dotted+ext form ([77cc6e4](https://github.com/Jekwwer/python-workspace/commit/77cc6e456189c79012a43c08a1b89ba70c8eae2b))
* **coverage:** silence subprocess module-not-measured warning ([c5b8cd1](https://github.com/Jekwwer/python-workspace/commit/c5b8cd19abbde7a06652d215f4201fa59f6abf86))
* **cspell:** trim words via dictionaries, refine ignore paths ([2600950](https://github.com/Jekwwer/python-workspace/commit/26009508280abb7da5f1002d9d7070f86be20467))
* **dependabot:** normalize fields and naming across ecosystems ([a940895](https://github.com/Jekwwer/python-workspace/commit/a940895a90c7514ea4754ad93d999cd189262d81))
* **devcontainer:** drop personal extensions and stale comment ([9ea6247](https://github.com/Jekwwer/python-workspace/commit/9ea62478e3cbbf8c8eed073ce15c9084907cd9d0))
* **docs:** drop inert config and tighten landing ([fc26cac](https://github.com/Jekwwer/python-workspace/commit/fc26cacde28fee4d821a7d9e2948212e63476aea))
* **editorconfig:** simplify, fix lockfile glob, set Makefile width ([cc3a9df](https://github.com/Jekwwer/python-workspace/commit/cc3a9df43325bfaa3ba75cd0e8179d1c8e10eb45))
* **github:** trim FUNDING.yml ([81ef8a6](https://github.com/Jekwwer/python-workspace/commit/81ef8a6f73b9778eee9eabd99c8aca76ac93b7b3))
* **make:** drop top comment, terse help text, sync CONTRIBUTING ([89f2c84](https://github.com/Jekwwer/python-workspace/commit/89f2c8409d2abd1739bc09ad8078f42063d9cc33))
* **markdownlint:** migrate to YAML, dash style, split ignores ([c758a55](https://github.com/Jekwwer/python-workspace/commit/c758a55730ec3f21f803e11c8a548f5c95e50ac1))
* **metadata:** refresh description, keywords, classifiers, urls ([df84af7](https://github.com/Jekwwer/python-workspace/commit/df84af78d6ed94bc394558893b465e6f737cfd44))
* **mlc:** drop unused aliveStatusCodes override ([25371c7](https://github.com/Jekwwer/python-workspace/commit/25371c721a1939c87ef58f6ba2a520edf4fa60cf))
* **npm:** align metadata, prune redundant flags + unused dep ([14ebcb4](https://github.com/Jekwwer/python-workspace/commit/14ebcb49aa9dfc24eec84ba573c735103fbcd442))
* **pre-commit:** exclude PR template from md-link-check ([e4943e7](https://github.com/Jekwwer/python-workspace/commit/e4943e717d1155b23a3086833e815ea22f5798fe))
* **prettier:** trim default-value pins and redundant override ([19ccfee](https://github.com/Jekwwer/python-workspace/commit/19ccfeefaac2242e1ff0ce430e65455f7ffad88b))
* **pytest:** drop redundant --cov-config flag ([9f400be](https://github.com/Jekwwer/python-workspace/commit/9f400be1956594307a7be7477f37b5ff4f8d5c5e))
* **release:** cleanup, restructure, reading flow ([0d87263](https://github.com/Jekwwer/python-workspace/commit/0d872631ba90fa6decaf67bb77c23fbc625e93cb))

## 2.0.3 - 2025-06-23
### 📦 Dependency Updates

* **npm:** bump prettier to v3.6.0 ([96a602d](https://github.com/Jekwwer/python-workspace/commit/96a602d185056879f35f2477b0e8f3b81d61daf5))

### 📖 Documentation

* **README.md:** update feature section for accuracy ([d481c0b](https://github.com/Jekwwer/python-workspace/commit/d481c0bccd3f6dfe7669cbdced78c62be4125291))

## 2.0.2 - 2025-06-18
### 🐞 Bug Fixes

* **ci:** update Python version to align with project standards ([6aeb1d1](https://github.com/Jekwwer/python-workspace/commit/6aeb1d19a03dd244a1e02fb5cf70a4d2107887d2))

### 📦 Dependency Updates

* **npm:** bump conventional-changelog and cspell to latest versions ([581c638](https://github.com/Jekwwer/python-workspace/commit/581c638c42d051f1075ea9877826473428026126))
* **poetry:** bump pytest-cov, coverage, mypy to latest versions ([b7bb4ff](https://github.com/Jekwwer/python-workspace/commit/b7bb4ff8aae4b661f9950085f788bd0f39227025))

## 2.0.1 - 2025-06-15
### 🐞 Bug Fixes

* **Makefile:** add missing targets to phony list ([1ccffb4](https://github.com/Jekwwer/python-workspace/commit/1ccffb4101024b5954f088e8d5516476856311d4))
* **pre-commit:** update file pattern for format hook ([d7a7638](https://github.com/Jekwwer/python-workspace/commit/d7a76382b1cb51f4bcfb0e57b5c2bd033a7b4b43))

### 📖 Documentation

* **README.md:** add note about migration to Poetry ([90a521d](https://github.com/Jekwwer/python-workspace/commit/90a521d26fae9f3902ec754e9d849b581995e10a))
* **STYLEGUIDE.md:** update style guide for clarity and accuracy ([64cf419](https://github.com/Jekwwer/python-workspace/commit/64cf419e2f3355fb5c8130beb2d35ae39bedaced))

### 🔧 Chores

* **metadata:** add report email to package metadata ([c13f43f](https://github.com/Jekwwer/python-workspace/commit/c13f43fc7e37d2738c96f8d8b3648d10f6d808c0))
* **metadata:** update keywords in package.json and pyproject.toml ([05fa191](https://github.com/Jekwwer/python-workspace/commit/05fa191b3aded8614ccc16e11d903a59fb734dd4))

## 2.0.0 - 2025-06-08
### ⚠️ BREAKING CHANGES

* **build:** Poetry replaces PDM. Adopt Makefile tasks and `poetry` commands; remove PDM scripts and `pdm.lock`.

### 🚀 New Features

* **build:** migrate from PDM to Poetry ([934c82a](https://github.com/Jekwwer/python-workspace/commit/934c82a92eacd9c3fec501bc5f4dea9d6a61fc25))

## 1.0.1 - 2025-06-08
### 🐞 Bug Fixes

* **config:** add and correct restructuredtext format settings ([384f50a](https://github.com/Jekwwer/python-workspace/commit/384f50aad1583722f909b5a29155078fe37aa995))

### 📦 Dependency Updates

* bump mypy 1.16.0 and @semantic-release/github 11.0.3 versions ([488f4ac](https://github.com/Jekwwer/python-workspace/commit/488f4ac78844da5d9307ee13acb6791b8b53f979)), closes [#3](https://github.com/Jekwwer/python-workspace/issues/3)

### 🔧 Chores

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
