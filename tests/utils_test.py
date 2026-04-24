"""Tests for utility functions in my_package.utils."""

import pytest

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
