# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "dipcoatimage-finitedepth-gui"
copyright = "2023, Jisoo Song"
author = "Jisoo Song"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

autodoc_mock_imports = [
    "PySide6",
    "dawiq.qt_compat",
    "dipcoatimage.finitedepth_gui.datarole",
]

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "numpydoc",
]

autodoc_member_order = "bysource"

autodoc_default_options = {
    "show-inheritance": True,
}

templates_path = []  # type: ignore
exclude_patterns = []  # type: ignore

numpydoc_show_class_members = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = []  # type: ignore
