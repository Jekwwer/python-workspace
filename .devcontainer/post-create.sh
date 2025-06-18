#!/usr/bin/env bash
# .devcontainer/post-create.sh: Installs dependencies for the devcontainer.

set -euo pipefail

npm install

pipx install poetry
poetry config virtualenvs.in-project true
poetry install --with test,lint,mypy,docs

poetry run pre-commit install
