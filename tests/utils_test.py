"""
Tests for utility functions in python_workspace.utils.

Verifies that greeting messages are generated correctly for various inputs.
"""
import pytest

from python_workspace.utils import greet


def test_greet_basic() -> None:
    """
    Test the basic functionality of greet.

    Ensures that greet returns the correct greeting for a standard name.

    Args:
        None

    Returns:
        None
    """
    assert greet("Alice") == "Hello, Alice!"


@pytest.mark.parametrize(
    "name, expected",
    [
        ("", "Hello, !"),
        ("Bob", "Hello, Bob!"),
    ],
)
def test_greet_parametrized(name: str, expected: str) -> None:
    """
    Test greet under multiple scenarios via parametrization.

    Checks that greet returns expected messages for empty and typical names.

    Args:
        name: Input name string for greeting.
        expected: Expected greeting output.

    Returns:
        None
    """
    assert greet(name) == expected
