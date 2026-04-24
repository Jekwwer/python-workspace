#!/usr/bin/env bash

set -euo pipefail

npm install

pipx install 'poetry>=2.3,<3'
poetry install --with test,lint,mypy,docs

poetry run pre-commit install --hook-type pre-commit --hook-type commit-msg
