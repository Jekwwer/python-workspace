"""
Tests for the command-line interface in python_workspace.cli.

Verifies that the main function outputs the correct greeting message
based on provided command-line arguments.
"""
import sys
import pytest
from pathlib import Path
from pytest import CaptureFixture, MonkeyPatch

from python_workspace.cli import main


@pytest.mark.parametrize(
    "argv, expected",
    [
        (["prog"], "Hello, World!"),
        (["prog", "--name", "Alice"], "Hello, Alice!"),
        (["prog", "-n", "Bob"], "Hello, Bob!"),
    ],
)
def test_main_outputs_correct_greeting(
    tmp_path: Path,
    capsys: CaptureFixture[str],
    monkeypatch: MonkeyPatch,
    argv: list[str],
    expected: str,
) -> None:
    """
    Ensure that the CLI main function prints the correct greeting.

    This test monkey-patches sys.argv to simulate CLI input,
    runs the main function, and captures stdout to verify
    the output matches the expected greeting.

    Args:
        tmp_path: pathlib.Path for temporary filesystem operations (unused here).
        capsys: pytest fixture to capture stdout and stderr.
        monkeypatch: pytest fixture to modify objects for testing.
        argv: List of command-line arguments to simulate.
        expected: The expected output string after running main().

    Returns:
        None
    """
    # Monkey-patch sys.argv for the parser
    monkeypatch.setattr(sys, "argv", argv)
    main()
    captured = capsys.readouterr()
    # strip newline for exact match
    assert captured.out.strip() == expected
