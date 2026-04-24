"""Tests for utility functions in my_package.utils."""

import pytest

from my_package.utils import greet


def test_greet_basic() -> None:
    """Greet returns correct greeting for a standard name."""
    assert greet("Alice") == "Hello, Alice!"


@pytest.mark.parametrize(
    "name, expected",
    [
        ("", "Hello, !"),
        ("Bob", "Hello, Bob!"),
    ],
)
def test_greet_parametrized(name: str, expected: str) -> None:
    """Greet returns expected message for empty and typical names."""
    assert greet(name) == expected
