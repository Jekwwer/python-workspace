"""Sphinx configuration for the project documentation."""

from importlib.metadata import metadata as _package_metadata

_meta = _package_metadata("python-workspace")

project = "Python Workspace"
author = _meta["Author"]
copyright = f"2025–%Y, {author}"
release = _meta["Version"]

rst_prolog = f"""
.. |project| replace:: {project}
.. |description| replace:: {_meta["Summary"]}
"""

extensions = [
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

autoapi_dirs = ["../../src"]
autoapi_root = "api"
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
]

napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True

add_module_names = False

html_theme = "sphinx_rtd_theme"
