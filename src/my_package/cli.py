"""Command-line interface for greeting users.

Provides a main function to parse user input and display a greeting message.
"""

import argparse

from my_package.utils import greet


def main() -> int:
    """Entry point for the CLI.

    Parses command-line arguments to obtain a name and prints a greeting.

    Args:
        None

    Returns:
        Process exit code.

    """
    parser = argparse.ArgumentParser(prog="cli", description="Greet someone.")
    parser.add_argument("-n", "--name", type=str, default="World", help="Name to greet")
    args = parser.parse_args()
    print(greet(args.name))
    return 0
