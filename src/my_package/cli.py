"""Command-line interface entry point."""

import argparse

from my_package.utils import greet


def main() -> int:
    """Parse command-line arguments and print a greeting.

    Returns:
        Process exit code.

    """
    parser = argparse.ArgumentParser(prog="cli", description="Greet someone.")
    parser.add_argument("-n", "--name", type=str, default="World", help="Name to greet")
    args = parser.parse_args()
    print(greet(args.name))
    return 0
