# -*- coding: utf-8 -*-
extensions = [
    'myst_parser',
    'sphinxcontrib.video',
]

myst_enable_extensions = [
    "linkify",
]

html_static_path = [
    "../_output",
]


master_doc = 'index'
source_suffix = '.md'

# General information about the project.
project = 'PyConDE & PyData Berlin 2023 - JupyterLite Tutorial'
author = 'Jeremy Tuloup'

exclude_patterns = ["01-intro.md"]
highlight_language = 'python'
pygments_style = 'sphinx'

html_theme = "pydata_sphinx_theme"
