"""Sphinx configuration for the project documentation."""

project = "Python Workspace"
copyright = "%Y, Evgenii Shiliaev"
author = "Evgenii Shiliaev"
release = "2.0.3"

extensions = [
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

autoapi_type = "python"
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

html_theme = "sphinx_rtd_theme"
