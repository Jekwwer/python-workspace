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
    monkeypatch.setattr(sys, "argv", argv)
    assert main() == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
