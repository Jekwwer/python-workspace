"""Placeholder package — rename and replace with your own code.

This is scaffolding shipped by the python-workspace template. The ``cli`` and
``utils`` modules exist only to exercise the toolchain (pytest, ruff, mypy,
Sphinx). Rename the ``my_package`` directory, update imports in ``tests/``,
and adjust ``pyproject.toml`` entries (``[project.scripts]``,
``[tool.coverage]``, ``[tool.ruff.lint.isort]``) accordingly.
"""

from importlib.metadata import PackageNotFoundError, version

__all__ = ["__version__"]

try:
    __version__ = version("python-workspace")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0+unknown"
