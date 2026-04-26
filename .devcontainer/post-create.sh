#!/usr/bin/env bash

set -euo pipefail

pipx install 'poetry>=2.3,<3'
make install
