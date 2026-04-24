"""Tests for the command-line interface in my_package.cli."""

import sys

import pytest
from pytest import CaptureFixture, MonkeyPatch

from my_package.cli import main


@pytest.mark.parametrize(
    "argv, expected",
    [
        (["prog"], "Hello, World!"),
        (["prog", "--name", "Alice"], "Hello, Alice!"),
        (["prog", "-n", "Bob"], "Hello, Bob!"),
    ],
)
def test_main_outputs_correct_greeting(
    capsys: CaptureFixture[str],
    monkeypatch: MonkeyPatch,
    argv: list[str],
    expected: str,
) -> None:
    """CLI main function prints correct greeting for given argv."""
    # Monkey-patch sys.argv for the parser
    monkeypatch.setattr(sys, "argv", argv)
    assert main() == 0
    captured = capsys.readouterr()
    # strip newline for exact match
    assert captured.out.strip() == expected
