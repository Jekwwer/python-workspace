"""Placeholder package — rename and replace with your own code.

This is scaffolding shipped by the python-workspace template. The ``cli`` and
``utils`` modules exist only to exercise the toolchain (pytest, ruff, mypy,
Sphinx). To adopt: grep for ``my_package`` (import name) and
``python-workspace`` (distribution name) across the repo and replace as
needed. Import-name rename is cheap and always worthwhile; distribution-name
rename additionally requires repo/PyPI/URL updates and is optional.
"""

from importlib.metadata import PackageNotFoundError, version

__all__ = ["__version__"]

__version__: str
try:
    __version__ = version("python-workspace")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0+unknown"
