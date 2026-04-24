"""Enable ``python -m my_package`` invocation."""

from my_package.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
