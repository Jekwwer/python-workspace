"""Utility functions for greetings.

This module contains helper functions to create greeting messages.
"""


def greet(name: str) -> str:
    """Generate a personalized greeting message.

    Args:
        name: The name of the person to greet.

    Returns:
        A greeting string addressed to the provided name.

    """
    return f"Hello, {name}!"
