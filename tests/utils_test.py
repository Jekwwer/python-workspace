"""Tests for utility functions in my_package.utils."""

import pytest
from hypothesis import given
from hypothesis import strategies as st

from my_package.utils import greet


@pytest.mark.parametrize(
    "name, expected",
    [
        ("", "Hello, !"),
        ("Alice", "Hello, Alice!"),
        ("Bob", "Hello, Bob!"),
    ],
)
def test_greet(name: str, expected: str) -> None:
    assert greet(name) == expected


@given(st.text())
def test_greet_property(name: str) -> None:
    """Property: greet returns ``Hello, <name>!`` for any input string."""
    result = greet(name)
    assert result == f"Hello, {name}!"
    assert name in result
