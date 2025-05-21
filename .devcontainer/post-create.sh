#!/usr/bin/env bash
# .devcontainer/post-create.sh: Installs dependencies for the devcontainer.

set -euo pipefail

npm install
pipx install pdm

# Ensuring PEP-582 layout
mkdir -p __pypackages__

pdm install --group :all
pdm run pre-commit install
