"""Integration tests: real entry-point invocation via subprocess."""

import subprocess
import sys
from importlib.metadata import PackageNotFoundError, distribution, entry_points

import pytest

try:
    distribution("python-workspace")
except PackageNotFoundError:  # pragma: no cover
    pytest.skip(
        "python-workspace not installed; integration suite needs an editable install",
        allow_module_level=True,
    )


def _console_scripts() -> list[str]:
    """Return console_scripts registered for python_workspace."""
    return [
        ep.name
        for ep in entry_points(group="console_scripts")
        if ep.value.startswith("python_workspace")
    ]


@pytest.mark.parametrize(
    "invocation",
    [
        *([script] for script in _console_scripts()),
        [sys.executable, "-m", "python_workspace"],
    ],
)
def test_cli_greets(invocation: list[str]) -> None:
    result = subprocess.run(
        [*invocation, "--name", "Alice"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == "Hello, Alice!"
